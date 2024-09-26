"""
Crea una clase llamada Persona con atributos nombre y edad. 
Luego, crea un objeto de tipo Persona e imprime sus atributos.
"""
#definimos clase persona
class Persona():
    #creamos el constructor
    def __init__(self, nombre, edad):
        #definimos los atributos del constructor
        self.nombre= nombre
        self.edad= edad
        
    #creamos el metodo mostrar
    def mostrar_Atributos(self):
        print("Nombre: " + self.nombre + " " + " edad: " + str(self.edad))
        


#creamos una instancia de la clase persona
persona1= Persona("Nelson", 31)

#accedemos a sus atributos 
print(persona1.nombre)



persona1.mostrar_Atributos()
    