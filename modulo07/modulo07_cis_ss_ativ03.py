import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número secreto entre 1 e 100!")

while True:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1
    
    diferenca = math.fabs(numero_secreto - palpite)
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
        
    if diferenca <= 5:
        print("Dica: Você está muito perto!")