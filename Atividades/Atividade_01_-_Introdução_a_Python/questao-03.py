"""
Questão 3 - Soma de Dígitos ao Quadrado.

Escreva um programa Python que calcule a soma dos quadrados dos dígitos de um número inteiro fornecido pelo usuário.
"""

num = int(input("Digite um número inteiro: "))

soma = 0

while num > 0:
    digito = num % 10
    soma += digito ** 2
    num = num // 10

print(f"A soma dos quadrados dos dígitos do número é: {soma}")