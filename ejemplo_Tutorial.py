

"""
#crea un rango de numeros y ordenalos en una lista de 
# pares e impares
#7 y 10 = [7,8,9,10]

def rango_de_numeros(a,b):
    rango_final=[]
    for numero in range(a,b+1):
        rango_final.append(numero)
    return rango_final


"""

def rango_de_numeros(a,b):
    rango_final=[]
    for numero in range(a,b):
        rango_final.append(numero)
    return rango_final


print(rango_de_numeros(7,10))