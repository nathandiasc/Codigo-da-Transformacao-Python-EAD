class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

carro = Carro("Ford", "Mustang", 1969)
print(carro)