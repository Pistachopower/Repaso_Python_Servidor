"""
Crea una clase base llamada FiguraGeometrica con atributos ancho
y altura, y un método area que calcule el área de la figura. 
Luego, crea clases derivadas como Rectangulo y Triangulo que 
hereden de FiguraGeometrica y sobrescriban el método area para 
calcular el área específica de cada figura.

Área= base * altura / 2

AreaRectangulo= base * altura

AreaTriangulo= base * altura / 2

"""

#definimos clase padre FiguraGeometrica
class FiguraGeometrica():
   #creamos el constructor con sus atributos
    def __init__(self, ancho, altura):
       self.ancho= ancho
       self.altura= altura
         
    #usamos el metodo str de Python para mostrar los atributos de los objetos
    def __str__(self):
         return f"Ancho: {self.ancho}, Altura: {self.altura}"
     
     
     
    #método area que calcule el área de la figura
    def calculaArea(self):
        resultado= (self.ancho * self.altura)  / 2
        return resultado
        
        

class Rectangulo( FiguraGeometrica):
    def __init__(self, ancho, altura):
       super().__init__(ancho, altura) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
         

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
       return f"Ancho: {self.ancho}, Altura: {self.altura}"


    def calculaRectangulo(self):
        resultado= (self.ancho * self.altura)  / 2
        return resultado
    

class Triangulo( FiguraGeometrica):
    def __init__(self, ancho, altura):
       super().__init__(ancho, altura) #con la palabra reservada super obtenemos los atributos y métodos de la clase padre
         

    #sobreescribimos el método str de la clase padre animal por el propio de la clase
    def __str__(self):
       return f"Ancho: {self.ancho}, Altura: {self.altura}"


    def calculaTriangulo(self):
        resultado= (self.ancho * self.altura)  / 2
        return resultado
     
    

     
#instanciamos al objeto pasando por parametro los valores
figuraG= FiguraGeometrica(1.5, 6.5)
rectangulo= Rectangulo(5.6,6)
triangulo= Triangulo(5,5)

print(figuraG.calculaArea())

print(rectangulo.calculaRectangulo())

print(triangulo.calculaTriangulo())