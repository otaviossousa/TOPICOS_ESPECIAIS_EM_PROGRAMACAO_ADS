"""

Questão 2 - Escreva um programa em Python que utilize um loop for para imprimir os
primeiros 10 números primos.

"""

# Função para verificar se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Variáveis para controlar a contagem de números primos
contador = 0
num = 2

# Loop para encontrar e imprimir os primeiros 10 números primos
while contador < 10:
    if eh_primo(num):
        print(num)
        contador += 1
    num += 1