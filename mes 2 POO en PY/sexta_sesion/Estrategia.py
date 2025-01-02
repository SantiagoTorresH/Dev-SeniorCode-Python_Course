from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    
    
    @abstractmethod
    def calcular(self, monto):
        pass
    
class SinDescuento(EstrategiaDescuento): # mis estrategias
    
    def calcular(self, monto):
        return monto    
    
class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        # return super().calcular(monto)    
        self.porcentaje = porcentaje
        
    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)
    
class DescuentoFijo(EstrategiaDescuento):
    def __init__(self, montoDescuento ):
        self.montoDescuento = montoDescuento
        
    def calcular(self, monto):
        return monto - self.montoDescuento    
    
class Pedido:
    
    def __init__(self, monto, estrategiaDescuento: EstrategiaDescuento): # ? mi constructor para solicitar el monto y la estrategia
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento
        
        
    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)      

pedido1 = Pedido(1000, SinDescuento()) # ! monto y estrategia 
print(f"Total sin descuennto: ${ pedido1.calcularTotal()}")     

pedido2 = Pedido(1000, DescuentoPorcentaje(50))
print(f" Tortal con 50% de descuennto: ${pedido2.calcularTotal() } " )

pedido3 = Pedido(1000, DescuentoFijo(100))
print(f"Total de descuento fijo de $100: ${pedido3.calcularTotal()} " )





        
        
        
    




