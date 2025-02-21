from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass # no usa constructo por la libreria 
class Vendedor(ABC):
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcular_comision(self) -> float: # -> me dice que lo que resulte del metodo va a ser flotante. 
        pass 
    # python no trabaja con interfaces, simula con las clases abstractas. 
    
@dataclass 
class VendedorBase(Vendedor): 
    
    def calcular_comision(self) -> float:
        return self.ventas * 0.10
    
@dataclass
class VendedorPremium(Vendedor):
    
    def calcular_comision(self) -> float :
        return self.ventas * 0.15 
    
    
        