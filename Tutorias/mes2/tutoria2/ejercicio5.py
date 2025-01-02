# 1. Definir una clase básica con encapsulamiento

#  - Ejercicio: Modifica la clase `CuentaBancaria` para usar decoradores `@property` y `@setter` en el atributo `_saldo`.  


# ? __estadoPrivado
#  _protegido

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    @property  # el property accede a la funcion inicial. 
    def saldo(self):
        return self.__saldo # el property permite modificar el privado 
    
    @saldo.setter
    def saldo(self, cantidad):
        if cantidad > 0:
            self.__saldo = cantidad
        else:
            print("La cantidad no es valida")
            
    def depositar(self, cantidad):
        
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de {cantidad} exitoso. Saldo actual es de : {self.__saldo}")
        else:
            print("La cantidad no es valida")
            
    def consultar_saldo(self):
        print(f"El saldo actual es de : {self.__saldo}")

CuentaJuanDavid = CuentaBancaria(1000)
CuentaJuanDavid.consultar_saldo()
CuentaJuanDavid.depositar(500)
CuentaJuanDavid.saldo = 500
print(CuentaJuanDavid.saldo)
CuentaJuanDavid.saldo = -100

