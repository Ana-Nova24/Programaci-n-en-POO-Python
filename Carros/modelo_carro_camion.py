from modelo_carro import Carro  # Ajusta según tu estructura de archivos

class Carro_camion(Carro):
    def __init__(self, marca, modelo, año, tipo_remolques, cantidad_ejes, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.tipo_remolques = tipo_remolques
        self.cantidad_ejes = cantidad_ejes
        self.capacidad_carga = capacidad_carga

    def imprimir_info(self):
        print(f"El tipo remolques es: {self.tipo_remolques}")
        print(f"La cantidad de ejes es: {self.cantidad_ejes}")
        print(f"La capacidad de carga es: {self.capacidad_carga}")