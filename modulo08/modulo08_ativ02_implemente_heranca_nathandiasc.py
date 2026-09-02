# Representa um veículo genérico no sistema.
# Agrupa características básicas (marca e modelo)
# e fornece ações para exibir esses dados.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")


# Especialização da classe Carro para veículos elétricos.
# Adiciona a autonomia da bateria às características
# e atualiza a exibição de informações para incluir esse dado.
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Autonomia: {self.autonomia_bateria} km")


carro_eletrico = CarroEletrico("BYD", "Dolphin", 400)
carro_eletrico.exibir_info()