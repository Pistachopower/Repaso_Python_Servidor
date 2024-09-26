"""
Crea una clase base llamada Animal con un método hablar
que imprima un mensaje genérico. Luego, crea dos clases
derivadas, Perro y Gato, que hereden de Animal y sobrescriban
el método hablar para imprimir mensajes diferentes. 
"""
#definimos clase padre animal
class Animal():
   #creamos el constructor con un atributo
    def __init__(self, nombre):
       self.nombre= nombre
         
    #usamos el metodo str de Python para mostrar los atributos de los objetos
    def __str__(self):
        return f"Estoy hablando "
    

#creamos la clase hija que hereda de la clase padre animal
class Perro(Animal):
    def __init__(self, nombrePerro):
       super().__init__(nombrePerro) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
         

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
        return f"Soy el perro "
    
class Gato(Animal):
    def __init__(self, nombreGato):
       super().__init__(nombreGato)
   
    def __str__(self):
        return f"Soy el gato "
    
#instanciamos objeto de la clase padre Animal    
animal= Animal("pepe")
print(animal)

#instanciamos objeto de la clase hija perro
perro= Perro("lacy")
print(perro)

#instanciamos objeto de la clase padre Gato
gato= Gato("mimi")
print(gato)




      

    