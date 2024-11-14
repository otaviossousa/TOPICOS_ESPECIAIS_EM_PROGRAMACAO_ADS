"""

Questão 3 - Crie uma lista de objetos Pessoa, representando uma família,
e implemente uma função que percorre essa lista e chama o método falar de cada pessoa.

"""


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} está falando")


def percorrer_lista(lista):

    for pessoa in lista:
        pessoa.falar()


familia = [Pessoa("João"), Pessoa("Maria"), Pessoa("José")]

percorrer_lista(familia)