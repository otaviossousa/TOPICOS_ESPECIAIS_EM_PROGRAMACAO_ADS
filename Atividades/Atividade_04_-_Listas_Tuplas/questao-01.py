"""

Questão 1 - Dada uma lista de números, retorne os números que aparecem mais de uma vez sem repetir o resultado.

# Entrada: [1, 2, 3, 4, 5, 3, 2, 6, 1] # Saída: [1, 2, 3]

"""

numeros = [1, 2, 3, 4, 5, 3, 2, 6, 1]
repetidos = []

for numero in numeros:
    if numeros.count(numero) > 1 and numero not in repetidos:
        repetidos.append(numero)

print(f' Os numeros repedidos são: {repetidos}')