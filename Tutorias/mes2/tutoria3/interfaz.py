from abc import ABC, abstractmethod

class FigurasGeometricas(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
# si quiero heredar figuras geometricas debo usar si o si area y perimetro en una interfaz

class Circulo(FigurasGeometricas):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return 3.1415 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.1415 * self.radio
        
    # def ver_radio(self):
    #     return self.radio      
    
class Cuadrado(FigurasGeometricas):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return  self.lado ** 2
    
    def perimetro(self):
        return self.lado  * 4     
    
def main():     
    figuras = [
    Circulo(5),
    Circulo(4),
    Circulo(2),
    Circulo(1),
    Circulo(7)    
    ]    

    for figura in figuras:
        print(f"Area: {figura.area()}, perimetro: {figura.perimetro()}")
    
if __name__ == "__main__":
    main()

    
# mi_circulo = Circulo(50)

# print(mi_circulo.ver_radio())
    