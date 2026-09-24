# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium



# Função que exibe as informações do perfil de um utilizador.
# O parâmetro tipo_conta tem 'Gratuito' como valor padrão.
def exibir_perfil(nome, idade, tipo_conta='Gratuito'):
    print(f"Utilizador: {nome} | Idade: {idade} | Plano: {tipo_conta}")

# Teste 1: Chamada sem especificar o tipo de conta (usa o valor padrão)
exibir_perfil("Ana Silva", 28)

# Teste 2: Chamada especificando um tipo de conta diferente
exibir_perfil("Carlos Souza", 35, "Premium")