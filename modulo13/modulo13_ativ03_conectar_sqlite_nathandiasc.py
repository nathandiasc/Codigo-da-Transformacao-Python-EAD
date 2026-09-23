# app_atividade3.py
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DB_NAME = "banco.db"


def init_db():
    """Cria a tabela de usuários se ela não existir no banco SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# Inicializa a tabela no banco de dados
init_db()


# 3. Rota POST /cadastrar com persistência em banco SQLite
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return (
            jsonify(
                {"erro": "Os campos 'nome' e 'email' são obrigatórios."}
            ),
            400,
        )

    nome = dados["nome"]
    email = dados["email"]

    try:
        # Conecta ao banco de dados SQLite e insere o novo registro
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email)
        )
        conn.commit()
        usuario_id = cursor.lastrowid
        conn.close()

        return (
            jsonify(
                {
                    "mensagem": "Usuário gravado com sucesso no SQLite!",
                    "usuario": {"id": usuario_id, "nome": nome, "email": email},
                }
            ),
            201,
        )
    except Exception as e:
        return jsonify({"erro": f"Erro ao salvar no banco: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)