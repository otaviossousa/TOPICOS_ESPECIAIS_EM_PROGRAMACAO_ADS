"""
Questao 1 -
Crie um arquivo 'produtos.csv' que armazene o nome e preco de produtos. Depois, cire um programa que leia esse arquivo e calcule o preco medio.

"""

import csv

def main():
    with open('produtos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Produto', 'Preço'])
        writer.writerow(['Arroz', 10])
        writer.writerow(['Feijão', 8])
        writer.writerow(['Macarrão', 5])
        writer.writerow(['Carne', 20])
        writer.writerow(['Frango', 15])

    with open('produtos.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        total = 0
        count = 0
        for row in reader:
            total += float(row[1])
            count += 1

    print(f'O preço médio dos produtos é: R${total/count:.2f}')


main()
    