# iNTERFACES EN PYTHON
# una interfaz define un conjunto de metodos

from abc import ABC, abstractmethod # me apoyo en las abstracatas para definir la interfaz. 

# en la interfaz no se define constructroes
# en la interfaz no se puede definir atributos, van directamente sobre los comportamientos . 


class ProcesoPago(ABC):
    
    @abstractmethod  # en python no existe las interfaces, se implementa a traves de las abstractas. 
    def procesoPago(self, cantidad: float) -> None: # none define que el metodo no va a retornar nada. 
        
        pass
    
    @abstractmethod
    def reembolsoPago(self, transaccionId: str) -> None:
        pass
        
class Paypal(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f"Proceso pafo ${cantidad} por paypal")
        
    def reembolsoPago(self, transaccionesId: str) ->None:
        print (f" REembolsando: Id transaccione numero {transaccionesId} por paypal ")    
        
class Stripe(ProcesoPago):     
    def procesoPago(self, cantidad: float) -> None:
        print(f"Proceso pago ${cantidad} por Stripe")   
        
    def reembolsoPago(self, transaccionesId: str) ->None:    
        print (f" REembolsando: Id transaccione numero {transaccionesId} por Stripe")       
        
        
        
        
if __name__ == "__name__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()
    
    
    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembolsoPago("gfefhdfh")
    
    procesoStripe.procesoPago(1000.0)
    procesoStripe.reembolsoPago("fdfhdfdjf")
        