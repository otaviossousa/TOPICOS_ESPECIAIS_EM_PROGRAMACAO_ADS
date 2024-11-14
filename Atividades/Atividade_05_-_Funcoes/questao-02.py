"""

Questão 2 - Escreva uma função chamada contar_pares que receba um número n como parâmetro e retorne a quantidade de números pares de 0 até n

"""

def contar_pares(n):
    count = 0
    for i in range(n+1):
        if i % 2 == 0:
            count += 1
    return count

print(contar_pares(10)) # 6