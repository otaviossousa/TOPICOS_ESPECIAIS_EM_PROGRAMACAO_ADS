"""
Questão 1 - Faça um programa que peça 2 números e um real.
Calcule e mostre:
# O produto do dobro do primeiro com a metade do segundo
# A soma do triplo do primeiro com o terceiro
# O terceiro elevado ao cubo
"""

# Recebendo os valores
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Recebendo o valor real
num3 = float(input('Digite um número real: '))

# Calculando e mostrando o produto do dobro do primeiro com a metade do segundo
print(f'O produto do dobro do primeiro com a metade do segundo é: {(num1 * 2) * (num2 / 2)}')

# Calculando e mostrando a soma do triplo do primeiro com o terceiro
print(f'A soma do triplo do primeiro com o terceiro é: {(num1 * 3) + num3}')

# Calculando e mostrando o terceiro elevado ao cubo
print(f'O terceiro elevado ao cubo é: {num3 ** 3}')
