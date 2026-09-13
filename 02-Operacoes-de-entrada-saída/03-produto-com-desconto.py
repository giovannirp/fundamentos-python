# Entrada de dados básicos.
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))

# Processamento computacional
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Saída de informações
print(f"Preço digitado: R$ {preco:.2f}")
print(f"Desconto digitado: {desconto:.1f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# Por exemplo, no terminal:

# Digite o preço do produto: 100
# Digite o desconto (%): 10

# Preço digitado: R$ 100.00
# Desconto digitado: 10.0%
# Valor do desconto: R$ 10.00
# Preço final: R$ 90.00