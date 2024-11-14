"""

Questão 2 - Dada uma lista de strings, crie uma nova lista contendo apenas as palavras que possuem todas as suas letras em maiúsculo e que têm um comprimento maior que 4.

# Entrada: ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
# Saída: ['PYTHON', 'JAVASCRIPT']

"""


def filter_words(words):
    return [word for word in words if word.isupper() and len(word) > 4]


def main():
    words = ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
    print(filter_words(words))


main()
