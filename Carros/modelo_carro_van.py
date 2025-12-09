from modelo_carro import Carro  # Ajusta según tu estructura de archivos

class Carro_van(Carro):
    def __init__(self, marca, modelo, año, cantidad_acientos, puerta_corrediza, altura_interior):
        super().__init__(marca, modelo, año)
        self.cantidad_acientos = cantidad_acientos
        self.puerta_corrediza = puerta_corrediza
        self.altura_interior = altura_interior

    def imprimir_info(self):
        print(f"La cantidad de acientos es: {self.cantidad_acientos}")
        print(f"La puerta corrediza es: {self.puerta_corrediza}")
        print(f"La altura interior es: {self.altura_interior}")