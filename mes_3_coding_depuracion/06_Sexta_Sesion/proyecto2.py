import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG )

@dataclass
class Vendedor:
    nombre: str
    ventas_totales: float 
    
    def calculo_comision(self) -> float:
        if self.ventas_totales > 10000: 
            comision = self.ventas_totales * 0.1 
            logging.debug(f"{self.nombre} ha alcanzado el umbral de ventas. La comision calculda es de : {comision }")
            
        else:
            comision = self.ventas_totales * 0.05
            logging.debug(f"{self.nombre} no ha alcanzado el umbral de ventas. La comision calculada ed de: {comision }")
        return comision         
    
if __name__ == "__main__":
    vendedor = Vendedor("SAnti", 12434)
    print(f"La comision de {vendedor.nombre}: {vendedor.calculo_comision() }")    

