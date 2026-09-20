# Crie uma lista com algumas cidades.

# Verifique se a cidade "São Paulo" está na lista.

# Se estiver, adicione "Campinas" na posição 1 usando insert() e mostre:
# "São Paulo encontrada!"

# Caso contrário, mostre:
# "Cidade não encontrada!"

# No final, mostre a lista atualizada.
# Lista de cidades
cidades = ["Rio de Janeiro", "São Paulo", "Santos", "Jundiaí"]

# Verifica se São Paulo existe na lista
if cidades.count("São Paulo") > 0:
    cidades.insert(1, "Campinas")
    print("São Paulo encontrada!")
else:
    print("Cidade não encontrada!")

# Mostra a lista atualizada
print("Cidades:", cidades)
