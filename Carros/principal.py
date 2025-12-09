#from NOMBRE DEL ARCHIVO import NOMBRE DE CLASE

from modelo_carro import Carro
from modelo_carro_deportivo import Carro_deportivo
from modelo_carro_van import Carro_van
from modelo_carro_camion import Carro_camion

#Codigo principal
#Aquí va la logica del negocio
#Instancia del padre

objCarro = Carro("Mazda", "3Sport", "2008")
objCarro.imprimir_info()

#Instancia de la hija carro deportivo

objCarro_deportivo = Carro_deportivo("Porsche", "911 GT3 RS", "2022","Alerón trasero deportivo fijo","Volante deportivo en cuero, multifunción","LED de alto rendimiento")
objCarro_deportivo.imprimir_info()

#Instancia de la hija carro van

objCarro_van = Carro_van(
    "Toyota", "Hiace", "2021","15","Puerta lateral corrediza","1.60m")
objCarro_van.imprimir_info()

#Instancia de la hija carro camión

objCarro_camion = Carro_camion(
    "Volvo", "FH 460", "2020","Plataforma","2","ligera")
objCarro_camion.imprimir_info()
