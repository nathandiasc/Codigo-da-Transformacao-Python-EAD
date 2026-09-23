# app_atividade2.py
from flask import Flask, jsonify, request

app = Flask(__name__)


# 2. Rota POST /cadastrar para receber JSON
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    # Validação dos campos recebidos
    if not dados or "nome" not in dados or "email" not in dados:
        return (
            jsonify(
                {"erro": "Os campos 'nome' e 'email' são obrigatórios."}
            ),
            400,
        )

    nome = dados["nome"]
    email = dados["email"]

    # Retorna os dados recebidos para confirmar o recebimento
    return (
        jsonify(
            {
                "mensagem": "Dados de usuário recebidos com sucesso!",
                "usuario": {"nome": nome, "email": email},
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)