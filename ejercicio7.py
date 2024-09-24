"""
Calcula el máximo común divisor (MCD) de dos números. 

Algoritmo MCD
    Entrada: dos números enteros positivos a y b
    Salida: el máximo común divisor de a y b

    Mientras b ≠ 0 hacer
        r ← a mod b
        a ← b
        b ← r
    Fin Mientras

    Retornar a
Fin Algoritmo

"""

a=48   #resultado: 6
b= 18
r= 0 #resultado

while b != 0:
    r= a % b
    a= b
    b= r
    
print("El máximo común divisor es: " + str(a))
