nome_arquivo = "dados.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha de texto armazenada.\n")
    arquivo.write("Aprendendo a manipular arquivos em Python.\n")
    arquivo.write("Linha final registrada com sucesso.\n")

print("Dados gravados no arquivo .txt!")

print("\n--- Conteúdo do Arquivo .txt ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)