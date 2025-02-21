import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Empleado(ABC):
    nombre: str
    salario_base: float
    
    @abstractmethod
    def calcular_salario(self):
        pass

@dataclass    
class Manager(Empleado):    
    def calcular_salario(self):
        return self.salario_base + 5000
    
class Developer(Empleado):
    def calcular_salario(self):
        return self.salario_base + 2000
    
def calcular_total_salario(empleado: Empleado) -> float:       
    
    """_summary_

    n = avance de linea en linea
    s = para saltar de funcion (metodo) en funcion(metodo)
    c = para saltar hacia la siguiente pausa
    p variable = muestra el valor de una variable en algun momento de la ajecucion 
    
        
    """
    
    pdb.set_trace() #* activacion debuger  
    return empleado.calcular_salario()

if __name__ == '__main__':
    manager = Manager("pascual", 30000)
    developer = Developer("Jacinta", 25000)
    
    
    print(calcular_total_salario(manager))
    print(calcular_total_salario(developer))
    
    
    




