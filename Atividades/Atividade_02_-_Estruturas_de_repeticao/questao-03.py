"""

Questão 3 - Escreva um programa em Python que utilize um loop while para calcular a
raiz quadrada de um número fornecido pelo usuário com uma precisão de pelo menos 4 casas decimais.

"""

num = int(input("Digite um número: "))
precisao = 0.0001
raiz = num
while abs(num - raiz**2) > precisao:
    raiz = (raiz + num/raiz)/2
print(f"A raiz quadrada de {num} é aproximadamente {raiz:.4f}")
