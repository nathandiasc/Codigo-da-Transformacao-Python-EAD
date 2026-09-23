# app_desafio_extra.py
import datetime
import hashlib
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "blog.db"


# -------------------------------------------------------------------
# Inicialização do Banco de Dados
# -------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Tabela de Usuários
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL,
            token TEXT
        )
    """
    )

    # Tabela de Posts
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER NOT NULL,
            data_criacao TEXT NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES usuarios (id)
        )
    """
    )

    # Tabela de Comentários
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            autor_id INTEGER NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts (id),
            FOREIGN KEY (autor_id) REFERENCES usuarios (id)
        )
    """
    )

    conn.commit()
    conn.close()


init_db()


# Auxiliar: Função simples de hash para senhas
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


# Auxiliar: Validação do token enviado no Header 'Authorization'
def obter_usuario_por_token(headers):
    token = headers.get("Authorization")
    if not token:
        return None

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios WHERE token = ?", (token,))
    user = cursor.fetchone()
    conn.close()
    return user


# -------------------------------------------------------------------
# Rotas de Autenticação
# -------------------------------------------------------------------
@app.route("/auth/registrar", methods=["POST"])
def registrar():
    dados = request.get_json()
    if not dados or "nome" not in dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Campos 'nome', 'email' e 'senha' são obrigatórios."}), 400

    senha_criptografada = hash_senha(dados["senha"])

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            (dados["nome"], dados["email"], senha_criptografada),
        )
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Email já cadastrado."}), 400


@app.route("/auth/login", methods=["POST"])
def login():
    dados = request.get_json()
    if not dados or "email" not in dados or "senha" not in dados:
        return jsonify({"erro": "Campos 'email' e 'senha' são obrigatórios."}), 400

    senha_criptografada = hash_senha(dados["senha"])

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome FROM usuarios WHERE email = ? AND senha_hash = ?",
        (dados["email"], senha_criptografada),
    )
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"erro": "Credenciais inválidas."}), 401

    # Criação de um token simples de acesso
    token = hash_senha(f"{user[0]}-{datetime.datetime.utcnow()}")
    cursor.execute("UPDATE usuarios SET token = ? WHERE id = ?", (token, user[0]))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Login realizado com sucesso!", "token": token}), 200


# -------------------------------------------------------------------
# Rotas do Blog (Posts)
# -------------------------------------------------------------------
@app.route("/posts", methods=["GET"])
def listar_posts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT posts.id, posts.titulo, posts.conteudo, posts.data_criacao, usuarios.nome 
        FROM posts 
        JOIN usuarios ON posts.autor_id = usuarios.id
    """
    )
    posts = cursor.fetchall()
    conn.close()

    resultado = [
        {
            "id": p[0],
            "titulo": p[1],
            "conteudo": p[2],
            "data_criacao": p[3],
            "autor": p[4],
        }
        for p in posts
    ]
    return jsonify({"posts": resultado}), 200


@app.route("/posts", methods=["POST"])
def criar_post():
    usuario = obter_usuario_por_token(request.headers)
    if not usuario:
        return jsonify({"erro": "Não autorizado. Envie um token válido."}), 401

    dados = request.get_json()
    if not dados or "titulo" not in dados or "conteudo" not in dados:
        return jsonify({"erro": "Campos 'titulo' e 'conteudo' são obrigatórios."}), 400

    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (titulo, conteudo, autor_id, data_criacao) VALUES (?, ?, ?, ?)",
        (dados["titulo"], dados["conteudo"], usuario[0], data_atual),
    )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    return jsonify({"mensagem": "Post criado com sucesso!", "post_id": post_id}), 201


# -------------------------------------------------------------------
# Rotas do Blog (Comentários)
# -------------------------------------------------------------------
@app.route("/posts/<int:post_id>/comentarios", methods=["GET"])
def listar_comentarios(post_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT comentarios.id, comentarios.conteudo, comentarios.data_criacao, usuarios.nome 
        FROM comentarios 
        JOIN usuarios ON comentarios.autor_id = usuarios.id
        WHERE comentarios.post_id = ?
    """,
        (post_id,),
    )
    comentarios = cursor.fetchall()
    conn.close()

    resultado = [
        {"id": c[0], "conteudo": c[1], "data_criacao": c[2], "autor": c[3]}
        for c in comentarios
    ]
    return jsonify({"comentarios": resultado}), 200


@app.route("/posts/<int:post_id>/comentarios", methods=["POST"])
def adicionar_comentario(post_id):
    usuario = obter_usuario_por_token(request.headers)
    if not usuario:
        return jsonify({"erro": "Não autorizado. Envie um token válido."}), 401

    dados = request.get_json()
    if not dados or "conteudo" not in dados:
        return jsonify({"erro": "O campo 'conteudo' é obrigatório."}), 400

    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Verifica se o post existe
    cursor.execute("SELECT id FROM posts WHERE id = ?", (post_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Post não encontrado."}), 404

    cursor.execute(
        "INSERT INTO comentarios (post_id, autor_id, conteudo, data_criacao) VALUES (?, ?, ?, ?)",
        (post_id, usuario[0], dados["conteudo"], data_atual),
    )
    conn.commit()
    comentario_id = cursor.lastrowid
    conn.close()

    return jsonify({"mensagem": "Comentário adicionado com sucesso!", "comentario_id": comentario_id}), 201


if __name__ == "__main__":
    app.run(debug=True)