# Entrada de dados básicos
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Processamento computacional
imc = peso / (altura * altura)

# Saída de informações
print(f"Seu IMC é: {imc:.1f}")