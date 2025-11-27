from modelo_carro import Carro  # Ajusta según tu estructura de archivos

class Carro_deportivo(Carro):
    def __init__(self, marca, modelo, año, aleron, volante, faroles):
        super().__init__(marca, modelo, año)
        self.aleron = aleron
        self.volante = volante
        self.faroles = faroles

    def derrapar_carro(self):
        print(f"El carro {self.marca} {self.modelo} derrapa")

    def imprimir_info(self):
        print(f"El alerón es: {self.aleron}")
        print(f"El volante es: {self.volante}")
        print(f"Los faroles son: {self.faroles}")
