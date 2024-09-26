"""
Crea una clase llamada Estudiante con atributos nombre, edad y curso. 
Crea varios objetos de tipo Estudiante y almacénalos en una lista. 
Luego, itera sobre la lista e imprime la información de cada estudiante.  
"""
class Estudiante():
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad= edad
        self.curso= curso

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}"


#creamos los objetos
estudiante1= Estudiante("Nelson", 31, "daw")
estudiante2= Estudiante("Pedro", 28, "daw")
estudiante3= Estudiante("Margarito", 25, "daw")

#almacenamos los los estudiantes en una lista
cursoDaw= [estudiante1, estudiante2, estudiante3]

#imprimimos la informacion de los estudiante
for estudiante in cursoDaw:
    print(estudiante) 