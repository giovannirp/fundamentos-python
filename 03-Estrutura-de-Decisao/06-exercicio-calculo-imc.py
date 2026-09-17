# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso

# Solicita o peso e a altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

# Verifica a classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")

