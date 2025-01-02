class PublicExample:
    def __init__(self, saldo):
        self.public_atribute = "soy publico"
        self._protectecd_atribute = " soy protegido"
        self.__private_atribute = "soy privado"
        self.__saldo = saldo
        
        
    def public_method(self):
        return " Este metodo es publico"
    
    def _protected_method(self):
        return " Este metodo es protegido"
    
    def __private_method(self):  # no se puede xonsultar igual se necesita con otro  metodo . 
        return " Este metodo es privado"
    
    def consultar_saldo(self):
        return f"saldo actual {self.__saldo}"
    
obj = PublicExample(50000)

print("---publico-----")
print(obj.public_atribute) #  aceso directo
print(obj.public_method) 

print("---protegido-----")
print(obj._protectecd_atribute) #  aceso directo
print(obj._protected_method) 

print("---privado-----")
print(obj.consultar_saldo())

# print(obj.__private_atribute) #  aceso directo
# print(obj.__private_method) 
