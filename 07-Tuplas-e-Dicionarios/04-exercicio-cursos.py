# Enunciado:
# Crie uma tupla com 5 cursos. Use for e if para verificar se o curso "Python" está presente.

# Tupla com cursos
cursos = ("Python", "Java", "HTML", "JavaScript", "C++")

# Percorrendo a tupla
for curso in cursos:
    if curso == "Python":
        print("Curso encontrado:", curso)
    else:
        print("Curso:", curso)