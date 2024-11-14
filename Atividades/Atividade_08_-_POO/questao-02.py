"""

Questão 2 - Crie uma classe Carro com atributos como marca, modelo e um método ligar.
Em seguida, crie uma subclasse Eletrico que redefina o método ligar para indicar que o carro elétrico está ligado.

"""


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("Carro ligado")


class Eletrico(Carro):
    def ligar(self):
        print("Carro elétrico ligado")


carro = Carro("Fiat", "Uno")
print(f'Marca: {carro.marca} - Modelo: {carro.modelo}')
carro.ligar()

carro_eletrico = Eletrico("Tesla", "Model S")
carro_eletrico.ligar()
