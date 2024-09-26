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
        pass
     
#instanciamos al objeto pasando por parametro los valores
figuraG= FiguraGeometrica(1.5, 6.5)

print(figuraG)