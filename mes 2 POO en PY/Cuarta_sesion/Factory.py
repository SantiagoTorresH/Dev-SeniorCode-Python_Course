from abc import ABC, abstractmethod
# Patron de diseno factory. 

# clase abstracta = duperclase" clases
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass
    
# creacion de subclase    
class ClaseA(Clases):  
    def operacion(self):
        return "Esta es la clase A"  
    
class ClaseB(Clases):  
    def operacion(self):
        return "Esta es la clase B"     
    
    def impresion(self):
        pass
    def consulta(self):
        pass 
    def retiro(self):
        pass
    
# clase Factory: FActoriia, rfabrica
class FabricaClases:
    
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == "A":
            return ClaseA()    
        elif tipoObjeto == "B":
            return ClaseB()
        else:
            raise ValueError(f" La clase {tipoObjeto} no existe") # raise , manejo de excepciones 
        
# objeto1 = FabricaClases.creacionObjetos("A")
objeto2 = FabricaClases.creacionObjetos("B")    

# print(objeto1.operacion())
print(objeto2.operacion())
# print(objeto2.impresion())
        
    