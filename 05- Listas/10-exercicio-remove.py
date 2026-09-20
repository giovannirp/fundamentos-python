# Crie uma lista com alguns produtos.

# Peça para o usuário digitar o nome de um produto.

# Verifique se o produto está na lista.

# Se estiver, remova o produto usando remove().

# Caso contrário, informe que o produto não está na lista.

# Exemplo quando não encontra:

# Digite o produto que deseja remover: Café
# Produto não encontrado!
# Lista atualizada: ['Arroz', 'Feijão', 'Macarrão', 'Leite']

# Lista de produtos
produtos = ["Arroz", "Feijão", "Macarrão", "Leite"]

# Pede um produto para o usuário
produto = input("Digite o produto que deseja remover: ")

# Verifica se o produto existe na lista
if produtos.count(produto) > 0:

    # Remove o produto
    produtos.remove(produto)

    print("Produto removido!")

else:
    print("Produto não encontrado!")

# Mostra a lista atualizada
print("Lista atualizada:", produtos)