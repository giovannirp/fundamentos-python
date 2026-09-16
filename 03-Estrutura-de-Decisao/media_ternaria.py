############ Entrada de dados básicos
nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

############ Processamento computacional.
# Cálculo da média.
media = (n1 + n2) / 2

# Classificação binária
resultado = "Aprovado" if (media >= 5) else "Reprovado"

############ Saída de informações
print(f"Aluno: {nome}")
print(f"Média Final: {media}")
print(f"Situação: {resultado}")
