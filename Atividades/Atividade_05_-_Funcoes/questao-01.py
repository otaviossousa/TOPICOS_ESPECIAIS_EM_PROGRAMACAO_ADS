"""

Questão 1 - Crie uma função chamada calcular_media que recebe três notas como parâmetros e retorna a média dessas notas.

"""


def calcular_media(x, y, z):
    media: float = (x + y + z) / 3
    return media


notas = [7, 8, 9]

media = calcular_media(notas[0],notas[1],notas[2])
print(f'A media das notas é {media}')