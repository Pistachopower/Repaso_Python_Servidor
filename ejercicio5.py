"""
Calcula el factorial de un número.
"""
input= 5
variableIncrementadora=1

#usamos el bucle 
for i in range(input, 0, -1):
    variableIncrementadora*= i

print("Factorial de " + str(input) + str(" es ")  + str(variableIncrementadora))
