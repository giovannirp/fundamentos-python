# Crie uma lista vazia para armazenar nomes.

# Use um for para pedir 3 nomes ao usuário.

# A cada nome digitado, adicione o nome na lista usando append().

# No final, mostre todos os nomes cadastrados.

# Exemplo:

# Digite um nome: João
# Digite um nome: Maria
# Digite um nome: Pedro

# Nomes cadastrados: ['João', 'Maria', 'Pedro']

# Cria uma lista vazia
nomes = []

# Repete 3 vezes
for i in range(3):

    # Pede um nome
    nome = input("Digite um nome: ")

    # Adiciona o nome na lista
    nomes.append(nome)

# Mostra os nomes cadastrados
print("Nomes cadastrados:", nomes)

for nome in nomes:
    print("-", nome)