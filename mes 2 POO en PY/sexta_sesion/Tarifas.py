from abc import ABC, abstractmethod

class EstrategiaTarifa(ABC):
    @abstractmethod
    def calcularTarifa(self, distancia, tiempo):
        raise NotImplementedError("Se debe implementar este metodo")
    
    
class Tarifafija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 300
    
class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return tiempo * 25
    
class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia * 2       
    
class CalculadoraTarifa:
    def __init__(self, estrategia):
        self.estrategia  = estrategia
        
    def cambiarEstrategia(self, estrategia):
        self.estrategia = estrategia
        
    def calcular(self, distancia, tiempo):
        return self.estrategia.calcularTarifa(distancia, tiempo) 
    
    
arriendo1 = Tarifafija()    
calculadora = CalculadoraTarifa(arriendo1)            
print("la tarifa fija:  ", calculadora.calcular(10, 4 ))

calculadora.cambiarEstrategia(TarifaHora())
print("Tarifa por hora: ", calculadora.calcular(100, 2 ))

calculadora.cambiarEstrategia(TarifaKilometro())
print("Tarifa por Kilometro: ", calculadora.calcular(100, 3))