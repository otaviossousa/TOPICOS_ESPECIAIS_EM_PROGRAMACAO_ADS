'''

Questão 3 - Escreva um programa que receba um texto  e troque todas as vogais por A

'''

# Solicitando a entrada do usuário
string = input("Digite uma frase: ")

# Substituindo vogais minúsculas e maiúsculas por "A"
string = string.replace("a", "A").replace("A", "A")
string = string.replace("e", "A").replace("E", "A")
string = string.replace("i", "A").replace("I", "A")
string = string.replace("o", "A").replace("O", "A")
string = string.replace("u", "A").replace("U", "A")

# Exibindo a string modificada
print(string)

