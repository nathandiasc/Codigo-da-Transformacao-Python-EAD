# app_atividade1.py
from flask import Flask, jsonify

app = Flask(__name__)


# 1. Rota GET /saudacao
@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Bem-vindo à API Flask!"}), 200


if __name__ == "__main__":
    app.run(debug=True)