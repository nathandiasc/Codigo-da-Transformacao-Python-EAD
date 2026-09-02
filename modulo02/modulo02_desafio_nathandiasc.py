from datetime import datetime

nome = input("Digite o seu nome: ")

agora = datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

print(f"Olá, {nome}! Seja bem-vindo(a). Agora são {hora_formatada}.")