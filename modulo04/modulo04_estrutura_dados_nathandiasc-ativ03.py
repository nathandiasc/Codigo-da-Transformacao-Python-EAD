numeros = [2, 5, 8, 11, 14, 17, 20, 23]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Números pares:", pares)
print("Números ímpares:", impares)