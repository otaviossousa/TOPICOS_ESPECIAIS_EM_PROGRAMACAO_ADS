"""
criar uma atividade em Python simulando o Jogo da Mega-Sena usando a biblioteca random.
O jogo consiste em gerar 6 números aleatórios e o usuário deverá tentar adivinhar quais são esses números.

Passo a Passo:
    Gerar os Números Sorteados: Vamos gerar 6 números aleatórios entre 1 e 60 (como na Mega-Sena).
    Receber os Números do Usuário: O usuário escolherá 6 números para tentar adivinhar os sorteados.
    Comparar os Números: Vamos comparar os números escolhidos pelo usuário com os números sorteados.
    Exibir o Resultado: O programa dirá quantos acertos o usuário teve.

"""
import random


def escolher_numeros(lista):
    global x
    print("Digite seus numeros para o sorteio")
    for i in range(6):
        x = int(input(":"))
        if x not in lista:
            lista.append(x)
    print(lista)
    return lista


def sorteador(lista):
    for i in range(6):
        numero = random.randint(1, 60)
        if numero not in lista:
            lista.append(numero)
    print(lista)
    return lista


def comparar(lista1, lista2):
    count = 0
    for i in range(6):
        for j in range(6):
            if lista1[i] == lista2[j]:
                count += 1
    return print(f"Acertos:{count}")


def __main__():
    numeros_sorteados = []
    numeros_escolhidos = []
    escolher_numeros(numeros_escolhidos)
    sorteador(numeros_sorteados)
    comparar(numeros_escolhidos, numeros_sorteados)

    # numeros_sorteados = random.sample(range(1, 61), 6)


if __name__ == '__main__':
    __main__()
