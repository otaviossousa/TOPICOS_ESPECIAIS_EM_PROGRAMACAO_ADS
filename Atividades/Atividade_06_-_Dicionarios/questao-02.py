"""

Questão 2 - Crie um programa que calcule a média das notas de alunos e armazene os resultados em um dicionário
onde as chaves são os nomes dos alunos e os valores são suas respectivas médias.

"""

# Dicionário com as notas dos alunos
notas = {
    'João': [8, 7, 6],
    'Maria': [10, 9, 8],
    'José': [7, 6, 5],
    'Ana': [9, 8, 7]
}

# Dicionário para armazenar as médias dos alunos
medias = {}

# Calcula a média das notas de cada aluno
for aluno, notas_aluno in notas.items():
    media = sum(notas_aluno) / len(notas_aluno)
    medias[aluno] = media

print(medias)
