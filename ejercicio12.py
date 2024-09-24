"""
Crea una clase llamada Rectangulo con atributos ancho y altura. 
Agrega un método para calcular el área del rectángulo y otro para 
calcular su perímetro. 
"""

class Rectangulo:
   #creamos el constructor
    def __init__(self, ancho, altura):
       #definimos los atributos del constructor
       self.ancho= ancho
       self.altura= altura
       
    def calcula_Area_Rectangulo(self):
         #creamos la variable que muestra resultado
        r_Area_Rectangulo= self.ancho * self.altura
           
        print("El área del rectángulo es " + str(r_Area_Rectangulo))
        
        
    def  calcula_Perimetro_Rectangulo(self):
        r_Perimetro_Rectangulo= 2 * (self.ancho + self.altura)
        print("El perimetro del rectángulo es " + str(r_Perimetro_Rectangulo))
     


rectangulo= Rectangulo(6,4)

rectangulo.calcula_Area_Rectangulo()
rectangulo.calcula_Perimetro_Rectangulo()

