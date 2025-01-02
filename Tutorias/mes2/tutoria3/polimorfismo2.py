# polimorfismo con herencias y metodos sobrescritos 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        return "Sonido generico"
    
class Perro(Animal):
    def sonido(self):
        return "gua gua"
    
class Gato(Animal):
    def sonido(self):
        return "mia miau "    
    
    # Se sobrescribe los metodos sonido
    
mi_gato = Gato()
mi_perro = Perro()

print(mi_gato.sonido())        