# Crie um programa que permita cadastrar filmes em uma lista.

# O programa deve pedir o nome de um filme.

# Enquanto o usuário não digitar "sair", adicione o filme na lista.

# Se o filme for "Batman", mostre:
# "Você adicionou Batman!"

# Quando o usuário digitar "sair", mostre todos os filmes cadastrados.

# Exemplo:

# Digite um filme: Avatar
# Digite outro filme ou sair: Batman
# Você adicionou Batman!
# Digite outro filme ou sair: Titanic
# Digite outro filme ou sair: sair

# Filmes cadastrados:
# ['Avatar', 'Batman', 'Titanic']

# Vai usar
# append() adiciona um novo item no final da lista.

filmes = []

filme = input("Digite um filme: ")

while filme != "sair":

    filmes.append(filme)

    if filme == "Batman":
        print("Você adicionou Batman!")

    filme = input("Digite outro filme ou sair: ")

print("Filmes cadastrados:")
print(filmes)