# 1. Importa funções específicas (multiplicar, dividir e em_moeda)
# do pacote 'meu_pacote'.
# 2. Executa e exibe no terminal os resultados dessas
# funções formatados como moeda.

from meu_pacote import multiplicar, dividir, em_moeda

resultado_mult = multiplicar(25, 4)
resultado_div = dividir(100, 3)

print("--- DESAFIO EXTRA: ESTRUTURA DE PACOTES ---")
print(f"Multiplicação Formatada: {em_moeda(resultado_mult)}")
print(f"Divisão Formatada: {em_moeda(resultado_div)}")