

"""
return ("La división es: " +  str((a / b)))


"""

def rango_de_numeros(a,b):
    rango_final=[]
    for numero in range(a,b):
        rango_final.append(numero)
    return rango_final


print(rango_de_numeros(7,10))