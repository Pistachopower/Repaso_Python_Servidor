"""
Crea una clase base llamada InstrumentoMusical con un método 
tocar que imprima un mensaje genérico. Luego, crea clases derivadas 
como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban
el método tocar para imprimir mensajes diferentes.

"""
class Instrumento():
    def __init__(self, medida):
        self.medida= medida
        
    def __str__(self):
       return f"Medida: {self.medida}" 

    
class Piano(Instrumento):
    def __init__(self, medida, teclado):
       super().__init__(medida) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
       self.teclado= teclado

    def __str__(self):
       return f"Medida: {self.medida}, Teclado: {self.teclado} " 

class Guitarra(Instrumento):
    def __init__(self, medida, cuerdas):
       super().__init__(medida) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
       self.cuerdas= cuerdas

    def __str__(self):
       return f"Medida: {self.medida}, Cuerdas: {self.cuerdas} " 


general= Instrumento(5.5)
piano= Piano(6, True)
guitarra= Guitarra(5.9, True)

print(general)
print(piano)
print(guitarra)