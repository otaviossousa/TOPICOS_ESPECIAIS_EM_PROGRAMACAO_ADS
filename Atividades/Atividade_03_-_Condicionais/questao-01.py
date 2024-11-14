"""

Questão 1 - Receber Nomes e Notas de Alunos e Imprimir Maior Nota

"""

# Recebendo a quantidade de alunos
n = int(input("Digite a quantidade de alunos: "))
# Inicializando a variável que armazenará o maior valor
maior_nota = 0
# Inicializando a variável que armazenará o nome do aluno com a maior nota
nome_maior_nota = ""
# Loop para receber os nomes e notas dos alunos
for i in range(n):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    # Verificando se a nota é maior que a maior nota já registrada
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
# Imprimindo o nome do aluno com a maior nota
print(f"O aluno com a maior nota é {nome_maior_nota} com a nota {maior_nota}")
