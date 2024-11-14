"""

Questão 4 - Faça um programa que receba o nome de vários convidados para uma festa
e armazene a quantidade de vezes que cada nome aparece em um dicionário.


"""


def main():
    convidados = {}
    while True:
        nome = input("Digite o nome do convidado ou sair para encerrar: ")
        if nome.lower() == "sair":
            break
        if nome in convidados:
            convidados[nome] += 1
        else:
            convidados[nome] = 1
    print(convidados)


main()
