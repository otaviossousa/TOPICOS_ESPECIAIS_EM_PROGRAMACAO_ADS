"""

Questão 4 - Desenvolva um código que utilize um loop for para imprimir a tabuada de
multiplicação de 1 a 10.

"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()