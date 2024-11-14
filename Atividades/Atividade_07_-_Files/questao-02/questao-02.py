"""
questao 2 - Usando JSON, crie um arquivo 'inventario.json' que armazene produtos e quantidades de uma loja.
Crie funcoes para adicionar um produto, remover um produto e listar todos os produtos.

"""

import json


def add_product(inventory, product, quantity):
    inventory[product] = quantity


def remove_product(inventory, product):
    del inventory[product]


def list_products(inventory):
    for product, quantity in inventory.items():
        print(f'{product}: {quantity}')


def main():
    inventory = {}

    add_product(inventory, 'Arroz', 10)
    add_product(inventory, 'Feijao', 8)
    add_product(inventory, 'Macarrao', 5)
    add_product(inventory, 'Carne', 20)
    add_product(inventory, 'Frango', 15)

    with open('inventario.json', 'w') as file:
        json.dump(inventory, file)

    with open('inventario.json', 'r') as file:
        inventory = json.load(file)

    list_products(inventory)

    remove_product(inventory, 'Macarrao')

    with open('inventario.json', 'w') as file:
        json.dump(inventory, file)

    with open('inventario.json', 'r') as file:
        inventory = json.load(file)

    list_products(inventory)


main()
