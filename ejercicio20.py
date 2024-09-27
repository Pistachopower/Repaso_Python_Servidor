"""
Crea una clase base llamada Empleado con atributos nombre y salario,
y un método calcular_salario_anual que calcule el salario anual del 
empleado. Luego, crea clases derivadas como Gerente y Programador 
que hereden de Empleado y añadan atributos y métodos específicos de 
cada tipo de empleado.
"""
#clase padre
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario= salario
        
    def __str__(self):
       return f"Nombre:  {self.nombre}, Salario: {self.salario}"
   
   
    def calcular_Salario_Anual(self):
        salarioAnual= self.salario * 12
        return salarioAnual

#clase hija
class Gerente(Empleado):
    def __init__(self, nombre, salario, numEmpleados):
        super().__init__(nombre, salario)
        self.numEmpleados= numEmpleados
        
        
    def __str__(self):
       return f"Nombre:  {self.nombre}, Salario: {self.salario}, Numéro de empleados a cargo: {self.numEmpleados}"  
#clase hija
class Programador(Empleado):
    def __init__(self, nombre, salario, lenguajeProgramacion):
        super().__init__(nombre, salario)
        self.lenguajeProgramacion= lenguajeProgramacion
        
        
    def __str__(self):
       return f"Nombre:  {self.nombre}, Salario: {self.salario}, Lenguaje de programción: {self.lenguajeProgramacion}"  




#instanciamos a las clases  
empleado1= Empleado("Juan", 1500)
gerente= Gerente("Antonio", 2000, 10)
programador= Programador("Jorge", 1900, "Python")

print(empleado1)
print(gerente)
print(programador)

print("El salario de " + programador.nombre + " es " + str(programador.calcular_Salario_Anual()))