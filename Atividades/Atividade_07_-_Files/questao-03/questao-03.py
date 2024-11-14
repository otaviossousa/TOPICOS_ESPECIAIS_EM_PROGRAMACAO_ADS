"""
Questao 3 - Leia um arquivo de texto 'diario.txt' e conte o numero de palavras nele.
Adicione uma funcao que, ao rodar, acrscente a data e o total de palavras em um arquivo.

"""


def contar_palavras():
    with open('diario.txt', 'r') as file:
        texto = file.read()
        palavras = texto.split()
        return len(palavras)


def adicionar_data_e_palavras():
    with open('diario.txt', 'a') as file:
        file.write(f'\nData: 2021-10-12\nTotal de palavras: {contar_palavras()}')


adicionar_data_e_palavras()

# Testando a funcao contar_palavras
print(contar_palavras())
# Testando a funcao adicionar_data_e_palavras
adicionar_data_e_palavras()

# Testando a funcao contar_palavras
print(contar_palavras())

# Testando a funcao adicionar_data_e_palavras
adicionar_data_e_palavras()
