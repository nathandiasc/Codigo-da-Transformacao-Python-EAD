# 1. Define o nome do arquivo de texto a ser manipulado.
# 2. Utiliza o gerenciador 'with' e o modo 'w' para criar e gravar linhas no arquivo.
# 3. Informa no terminal que a gravação foi concluída.
# 4. Reabre o arquivo no modo 'r' para ler todo o conteúdo salvo.
# 5. Exibe o conteúdo lido no terminal.

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