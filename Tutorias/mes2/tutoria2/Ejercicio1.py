# 1. Definir una clase básica con encapsulamiento

#  - Ejercicio: Crea una clase `CuentaBancaria` con un atributo privado `_saldo`. Agrega métodos para depositar y retirar dinero, asegurándote de que no se permita un saldo negativo.  

# ? __estadoPrivado
#  _protegido

class CuentaBancaria:
    def __init__(self, saldo, saldo2):
        self.__saldo = saldo
        self.saldo2 = saldo2
        
    def depositar(self, cantidad ):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Deposito de {cantidad} exitoso. Saldo actual es de : {self.__saldo}")
        else:
            print("la cantidad no es valida")    
            
    def consultar_saldo(self):
        print(f"El saldo actual es de : {self.__saldo}" )
            
CuentaSan = CuentaBancaria(100)
CuentaSan.depositar(50)
CuentaSan.consultar_saldo()

