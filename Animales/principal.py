from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_escarabajo import Escarabajo
from modelo_animal_pescado import Pescado
from modelo_animal_pato import Pato

# Instancia de la hija caballo
caballo = Caballo("Alfred", 2, "campo", "hierba", "pequeño", "blanco", "mustang", 60)
caballo.mostrar_info()
caballo.galopar()
print()

# Instancia de la hija cocodrilo
cocodrilo = Cocodrilo("Drilo", 6, "pantano", "carnívoro", "mediano", "verde", 2000)
cocodrilo.mostrar_info()
cocodrilo.atacar()
print()

# Instancia de la hija escarabajo
escarabajo = Escarabajo("Escar", 2, "selva", "hojas", "pequeño", "marrón", True, "Hércules")
escarabajo.mostrar_info()
escarabajo.volar()
print()

# Instancia de la hija pescado
pescado = Pescado("Frito", 1, "océano", "algas", "mediano", "gris", "salada")
pescado.mostrar_info()
pescado.nadar()
print()

# Instancia de la hija pato
pato = Pato("Cuack", 3, "lago", "omnívoro", "grande", "negro", "ancho")
pato.mostrar_info()
pato.graznar()
print()
