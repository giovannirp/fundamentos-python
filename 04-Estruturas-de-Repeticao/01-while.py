# Define o valor inicial do contador
contador = 1

# 1 <= 5 → True ✅ → continua
# 2 <= 5 → True ✅ → continua
# 3 <= 5 → True ✅ → continua
# 4 <= 5 → True ✅ → continua
# 5 <= 5 → True ✅ → continua

# Enquanto o contador for menor ou igual a 5
while contador <= 5:

    # Mostra o valor atual do contador
    print("Contador agora é:", contador)

    # Aumenta o contador em 1
    contador = contador + 1

# Mostra uma mensagem quando o while termina
print("Contador chegou a 6. O while terminou!")