import shutil
import os
pasta = os.path.dirname(__file__)
origem = os.path.join(pasta, "documento.txt")
destino = os.path.join(pasta, "backup")
if not os.path.exists(origem):
    with open(origem, "w", encoding="utf-8") as arquivo:
        arquivo.write("Este é um arquivo de teste para o backup.")
os.makedirs(destino, exist_ok=True)
shutil.copy(origem, destino)
print("Backup realizado com sucesso!")