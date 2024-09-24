"""
Crea una lista de números y calcula su promedio. 
"""

listaPromedio= [1,2,3,4]
variableContador= 0
variableSumaPromedio=0

for i in listaPromedio:
    
    #contamos la cantidad de números para el promedio
    variableContador= variableContador + 1
    
    #sumamos los elementos
    variableSumaPromedio= variableSumaPromedio + i
    
print("El promedio es " + str(variableSumaPromedio / variableContador ))
    