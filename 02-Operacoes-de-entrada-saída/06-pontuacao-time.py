"""
Faça um programa que peça o nome de um time de futebol,
a quantidade de vitórias e empates.
Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto,
calcule e mostre a pontuação total do time.
"""
# Entrada de dados básicos.
time = input("Digite o nome do time: ")
vitorias = int(input("Digite a quantidade de vitórias: "))
empates = int(input("Digite a quantidade de empates: "))

# Processamento computacional
pontos = (vitorias * 3) + (empates * 1)

# Saída de informações
print(f"Time: {time}")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Pontuação total: {pontos} pontos")