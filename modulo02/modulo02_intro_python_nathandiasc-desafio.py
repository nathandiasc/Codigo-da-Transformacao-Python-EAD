from datetime import datetime

nome = input("Digite seu nome: ")

hora = datetime.now().strftime("%H:%M:%S")

print(f"Olá, {nome}! Seja bem-vindo(a)!")
print(f"Hora atual: {hora}")