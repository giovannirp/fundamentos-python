# Cria um programa que permita ao utilizador fazer vários pedidos numa lanchonete.

# O programa deve pedir ao utilizador o nome de um produto.

# Enquanto o utilizador não escrever sair, o programa deve continuar a pedir novos produtos.

# Quando o utilizador escrever sair, o programa deve mostrar:

#   .Quantos produtos foram pedidos;
#   .Uma mensagem a indicar que o pedido foi finalizado.

# Digite o produto que deseja pedir: hambúrguer
# Digite o produto que deseja pedir: batata
# Digite o produto que deseja pedir: refrigerante
# Digite o produto que deseja pedir: sair

# Pedido finalizado!
# Você pediu 3 produtos.

quantidade = 0

produto = input("Digite o produto que deseja pedir: ")

while produto != "sair":
    intesAdicionados.append(produto)
    quantidade = quantidade + 1

    produto = input("Digite outro produto: ")

print("Pedido finalizado!")
