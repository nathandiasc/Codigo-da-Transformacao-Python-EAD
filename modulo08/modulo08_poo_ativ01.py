# Representa um veículo no sistema.
# Agrupa as características essenciais (marca e modelo)
# e fornece ações para manipular e exibir esses dados.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_info()