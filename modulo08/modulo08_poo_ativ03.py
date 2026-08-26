# Representa um veículo agrupando sua marca, modelo e ano.
# Utiliza o método especial __str__ para que, ao usar o print(),
# o carro seja automaticamente formatado em uma frase simples
# e fácil de ler, em vez de mostrar um código interno do Python.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

carro = Carro("Ford", "Mustang", 1969)
print(carro)