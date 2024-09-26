"""
Crea una clase base llamada Vehiculo con atributos marca y modelo,
y un método informacion que imprima la información del vehículo. 
Luego, crea clases derivadas como Coche y Bicicleta que hereden de
Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.
"""
class Vehiculo :
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo= modelo
        
    def informacion(self):
        print("Marca: " + self.marca + " Modelo: " + self.modelo)

       
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
       super().__init__(marca, modelo) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
         

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
       return f"Marca: {self.marca}, Modelo: {self.modelo}" 

general= Vehiculo("Honda", "picanto")



#honda.informacion()