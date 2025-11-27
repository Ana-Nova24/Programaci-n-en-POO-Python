class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"El carro {self.marca} {self.modelo} está arrancando.")

    def apagar(self):
        print(f"El carro {self.marca} {self.modelo} se ha apagado.")

    def imprimir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

