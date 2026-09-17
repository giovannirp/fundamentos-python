# Faça um programa que peça um número inteiro e verifique
# se ele é par ou ímpar.

# O % significa resto da divisão.

# Solicita um número
numero = int(input("Digite um número: "))

# Verifica se o número é par
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
