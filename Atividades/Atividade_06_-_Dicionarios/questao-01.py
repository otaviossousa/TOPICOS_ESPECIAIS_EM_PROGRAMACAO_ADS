"""

Questão 1 - Escreva um programa que conte a frequência de palavras em uma frase e armazene o resultado em um dicionário.

"""


def contar_frequencia(frase):
    palavras = frase.split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia


def main():
    frase = input("Digite uma frase: ")
    frequencia = contar_frequencia(frase)
    print(frequencia)


main()
