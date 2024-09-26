"""
Crea una clase base llamada Vehiculo con atributos marca y modelo,
y un método informacion que imprima la información del vehículo. 
Luego, crea clases derivadas como Coche y Bicicleta que hereden de
Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.
"""
#clase padre
class Vehiculo :
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo= modelo
        

    def __str__(self):
       return f"Marca: {self.marca}, Modelo: {self.modelo}" 
   
#clase hija de vehiculo       
class Coche(Vehiculo):
    def __init__(self, marca, modelo, matricula):
       super().__init__(marca, modelo) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
       self.matricula= matricula

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
       return f"Marca: {self.marca}, Modelo: {self.modelo}, Matricula: {self.matricula}" 
   
   
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color):
       super().__init__(marca, modelo) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
       self.color= color

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
       return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}" 


#instanciamos en los atributos
general= Vehiculo("coche 5 plaza", "sin definición")
honda= Coche("honda", "picanto", "54sdad")
biciNegra= Bicicleta("calip", "A432", "negro")

print(general)
print(honda)
print(biciNegra)