# 1. Importa o módulo 'json' para manipulação e estruturação de arquivos JSON.
# 2. Cria um dicionário com dados de clientes e define o nome do arquivo de destino.
# 3. Salva o dicionário no arquivo 'clientes.json' com formatação legível (indentação e acentos).
# 4. Lê e carrega os dados salvos do arquivo JSON de volta para o programa.
# 5. Percorre o dicionário carregado e exibe as informações formatadas no terminal.

import json

clientes = {
    "1": {"nome": "Ana Souza", "email": "ana@email.com", "ativo": True},
    "2": {"nome": "Carlos Lima", "email": "carlos@email.com", "ativo": False},
    "3": {"nome": "Beatriz Rocha", "email": "beatriz@email.com", "ativo": True}
}

nome_arquivo = "clientes.json"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)

print("Dados dos clientes salvos em 'clientes.json'.")

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

print("\n--- Clientes Carregados do JSON ---")
for id_cliente, info in dados_carregados.items():
    status = "Ativo" if info["ativo"] else "Inativo"
    print(f"ID: {id_cliente} | Nome: {info['nome']} | Email: {info['email']} | Status: {status}")