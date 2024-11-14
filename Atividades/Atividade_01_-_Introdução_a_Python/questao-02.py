"""
Questão 2 - Verificação de Números Primos

Escreva um programa Python que verifique se um número fornecido pelo usuário é um número primo ou não.
"""

# Recebendo o número
num = int(input('Digite um número: '))

# Inicializando a variável que contará quantas vezes o número é divisível
count = 0

# Verificando se o número é primo
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
