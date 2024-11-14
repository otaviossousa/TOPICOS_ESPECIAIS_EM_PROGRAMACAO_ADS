"""

Questão 4 -  Dada uma lista de tuplas, converta-a em uma lista de listas e, em seguida, aplique uma modificação:
adicione 10 ao segundo elemento de cada sub-lista.

# Entrada: [(1, 2), (3, 4), (5, 6)]     # Saída: [[1, 12], [3, 14], [5, 16]]

"""

# Lista de tuplas
lista_tuplas = [(1, 2), (3, 4), (5, 6)]

# Lista de listas
lista_listas = []

# Conversão de tuplas em listas
for tupla in lista_tuplas:
    lista = list(tupla)
    lista[1] += 10
    lista_listas.append(lista)

print(lista_listas)
