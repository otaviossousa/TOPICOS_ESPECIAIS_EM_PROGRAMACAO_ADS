"""

Questão 1 - Crie uma classe Pessoa com os atributos nome, idade e um método falar que imprime uma saudação com o nome.

"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}")


pessoa = Pessoa("João", 20)
pessoa.falar()
