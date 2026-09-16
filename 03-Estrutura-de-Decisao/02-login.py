# Solicita o login do usuário
login = input("Digite seu login: ")

# Solicita a senha do usuário
senha = input("Digite sua senha: ")

# Verifica se o login e a senha estão corretos
if login == "admin" and senha == "123456":
    print("Seja bem-vindo, administrador!")
else:
    print("Login ou senha incorretos!")