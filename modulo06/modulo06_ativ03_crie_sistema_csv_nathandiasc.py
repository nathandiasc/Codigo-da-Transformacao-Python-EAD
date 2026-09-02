# 1. Importa o módulo 'csv' para manipulação de arquivos de dados tabulares.
# 2. Define o nome do arquivo CSV e uma lista contendo o cabeçalho e os dados dos alunos.
# 3. Cria e grava os dados no arquivo 'notas_alunos.csv' usando 'csv.writer' e 'writerows'.
# 4. Reabre o arquivo em modo de leitura com 'csv.reader' para percorrer cada linha.
# 5. Exibe os dados formatados em colunas alinhadas no terminal.

import csv

nome_arquivo = "notas_alunos.csv"

dados_alunos = [
    ["Nome", "Disciplina", "Nota"],
    ["João Silva", "Matemática", 8.5],
    ["Maria Oliveira", "História", 9.0],
    ["Pedro Santos", "Física", 7.2]
]

with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados_alunos)

print("Notas salvas com sucesso em 'notas_alunos.csv'.")

print("\n--- Relatório de Notas do CSV ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(f"{linha[0]:<15} | {linha[1]:<12} | {linha[2]}")