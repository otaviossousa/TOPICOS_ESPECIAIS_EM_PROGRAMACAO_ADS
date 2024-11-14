"""

Questão 3 - Dada uma tupla contendo pares de números, retorne a soma de todos os segundos elementos de cada par.

# Entrada: ((1, 2), (3, 4), (5, 6))
# Saída: 12 (2 + 4 + 6)

"""


def sum_second_elements(tupla):
    return sum([x[1] for x in tupla])


tupla = ((1, 2), (3, 4), (5, 6))
print(sum_second_elements(tupla)) # 12
