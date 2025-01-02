class CuentaBancaria:
    
    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self._saldo = saldo # protegido
        self.__clave = clave # privado
        
    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f"Deposito exitoso. Saldo actual {self._saldo}"
    
    def retirar(self, cantidadRetiro):
        if cantidadRetiro > self._saldo:
            return "fondos insuficientes"
        self._saldo -= cantidadRetiro
        return f"Retiro exitoso. El saldo actual es { self._saldo}"    
    
    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f"Clave modificada de forma exitoa. la nueva clase es : { self.__clave}"
    
cuentaBancaria1 = CuentaBancaria("Santi", 10000, 1234)
    
print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(5000000))
print(cuentaBancaria1.depositar(5000000))
print(cuentaBancaria1.retirar(1000000))
print(cuentaBancaria1.retirar(1000000))
print(cuentaBancaria1.retirar(1000000))
print(cuentaBancaria1.retirar(1000000))

print(cuentaBancaria1.modificarClave(12345667878))