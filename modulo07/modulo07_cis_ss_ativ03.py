# 🎯 Jogo de Adivinhação — 24 Números

import random
import math

# 🎯 Lista com os 24 números possíveis
numeros = list(range(1, 25))

# 🔐 Escolhe um número secreto aleatoriamente
numero_secreto = random.choice(numeros)

# ❤️ Número máximo de tentativas
max_tentativas = 6
tentativas = 0

print("🎮 ===============================")
print("🎯   JOGO DO NÚMERO SECRETO")
print("🎮 ===============================")
print("🔢 Existem 24 números possíveis!")
print("❤️ Você tem 6 chances para acertar!")
print("🍀 Boa sorte!\n")

while tentativas < max_tentativas:

    # ⏳ Mostra quantas chances ainda existem
    print(f"❤️ Chances restantes: {max_tentativas - tentativas}")

    # 🔢 Recebe o palpite do jogador
    palpite = int(input("👉 Digite seu palpite (1 a 24): "))

    # 🚫 Verifica se o número está dentro do intervalo
    if palpite < 1 or palpite > 24:
        print("⚠️ Digite um número entre 1 e 24!\n")
        continue

    # ➕ Conta a tentativa
    tentativas += 1

    # 📏 Calcula a distância entre o palpite e o número secreto
    diferenca = math.fabs(numero_secreto - palpite)

    # 🏆 Verifica se acertou
    if palpite == numero_secreto:
        print("\n🎉 PARABÉNS!")
        print(f"🏆 Você acertou o número secreto: {numero_secreto}")
        print(f"🎯 Você precisou de {tentativas} tentativa(s)!")
        break

    # 📈 Dá dica se o número secreto for maior
    elif palpite < numero_secreto:
        print("📈 Tente um número MAIOR!")

    # 📉 Dá dica se o número secreto for menor
    else:
        print("📉 Tente um número MENOR!")

    # 🔥 Dica de proximidade
    if diferenca <= 3:
        print("🔥 Você está MUITO perto!")

    elif diferenca <= 6:
        print("🙂 Você está perto!")

    else:
        print("🥶 Você está longe!")

    print()

# 💀 Verifica se o jogador perdeu todas as chances
if tentativas == max_tentativas and palpite != numero_secreto:
    print("💀 FIM DE JOGO!")
    print(f"😢 Você utilizou todas as {max_tentativas} chances.")
    print(f"🔐 O número secreto era: {numero_secreto}")
    print("🎮 Tente novamente!")