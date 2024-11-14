"""
Questão 4 - Encontre 0 Número Perfeito.

Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios positivos, excluindo ele mesmo.
Escreva um programa Python que verifique se um número fornecido pelo usuário é um número perfeito ou não.

"""


def numero_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n


n = int(input("Digite um número: "))
if numero_perfeito(n):
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito.")
