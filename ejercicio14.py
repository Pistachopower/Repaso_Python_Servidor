"""
Crea una clase llamada CuentaBancaria con atributos titular y saldo. 
Agrega métodos para depositar y retirar dinero de la cuenta. 
"""
#definimos clase CuentaBancaria
class CuentaBancaria():
   #creamos el constructor
    def __init__(self, titular, saldo):
       #definimos los atributos del constructor
       self.titular= titular
       self.saldo= saldo
      
    def __str__(self):
        return f"Titular:  {self.titular}, Saldo: {self.saldo} €"


    def depositar(self, monto):
        self.saldo= self.saldo + monto

    def retiro(self, montoRetiro):
        self.saldo= self.saldo - montoRetiro
        
        
#instanciamos los objetos
cuenta1= CuentaBancaria("Juan Gomez", 150)

print("Saldo inicial")
print(cuenta1)

print("Saldo con depósito")
cuenta1.depositar(50)
print(cuenta1)

print("Saldo con retiro")
cuenta1.retiro(50)
print(cuenta1)