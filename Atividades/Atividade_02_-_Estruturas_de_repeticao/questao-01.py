"""

Questão 1 - Crie um programa que utilize um loop for para imprimir os primeiros 10
números da sequência de Fibonacci.

"""

numeros = {}

for i in range(10):
    if i == 0 or i == 1:
        numeros[i] = i
    else:
        numeros[i] = numeros[i-1] + numeros[i-2]

print(numeros)