# ==========================================
# MÉTODOS PARA MANIPULAR LISTAS EM PYTHON
# ==========================================

frutas = ["Maçã", "Banana", "Laranja", "Banana"]


# index()
print("index():", frutas.index("Banana"))


# count()
print("count():", frutas.count("Banana"))


# append()
frutas.append("Uva")
print("append():", frutas)


# insert()
frutas.insert(1, "Morango")
print("insert():", frutas)


# extend()
outras_frutas = ["Abacaxi", "Melancia"]
frutas.extend(outras_frutas)
print("extend():", frutas)


# remove()
frutas.remove("Banana")
print("remove():", frutas)


# pop()
frutas.pop(0)
print("pop():", frutas)


# clear()
frutas.clear()
print("clear():", frutas)


# copy()
frutas = ["Maçã", "Banana", "Laranja"]
outra_lista = frutas.copy()

print("copy():", outra_lista)


# reverse()
frutas.reverse()
print("reverse():", frutas)


# sort()
frutas.sort()
print("sort():", frutas)