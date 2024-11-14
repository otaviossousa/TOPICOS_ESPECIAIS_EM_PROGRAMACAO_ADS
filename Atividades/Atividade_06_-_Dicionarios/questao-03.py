"""

Questão 3 - Desenvolva um programa que receba uma lista de compras (produto e quantidade) e crie um dicionário
representando o carrinho de compras.

"""


def carrinho_compras(lista_compras):
    carrinho = {}
    for item in lista_compras:
        produto, quantidade = item.split()
        carrinho[produto] = quantidade
    return carrinho


lista_compras = ['arroz 2', 'feijao 1', 'macarrao 3', 'carne 2']
print(carrinho_compras(lista_compras))
