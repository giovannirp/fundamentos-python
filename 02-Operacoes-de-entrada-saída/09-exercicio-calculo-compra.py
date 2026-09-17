# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados básicos
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

# Processamento computacional
total = preco * quantidade

# Saída de informações
print("Produto:", produto)
print("Total da compra:", total)