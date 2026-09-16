from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/somar', methods=['POST'])
def somar():
    data = request.get_json()
    
    # Validação de payload/entradas inválidas
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"erro": "Entrada inválida. 'a' e 'b' são obrigatórios."}), 400

    resultado = data['a'] + data['b']
    return jsonify({"resultado": resultado}), 200

if __name__ == '__main__':
    app.run(debug=True)