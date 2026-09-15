# Objetivo:
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de gols marcados por cada equipa.

# Depois, apresente o placar e calcule o total de gols da partida.

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO
# ================================
# França 3 x 2 Espanha
# Total de gols: 5
# ================================

time_casa = "França"
gols_casa = 3

time_visitante = "Espanha"
gols_visitante = 2

total_gols = gols_casa + gols_visitante

print("================================")
print("        RESULTADO DO JOGO")
print("================================")

print(f"{time_casa} {gols_casa} x {gols_visitante} {time_visitante}")

print(f"Total de gols: {total_gols}")

print("================================")
