# Implementar un sistema de monitoreo para facturacion de manejo de excepiones por consola y .log file

import logging
from dataclasses import dataclass

logging.basicConfig(
    level= logging.DEBUG, 
    format= '%(asctime)s - %(level)s - %(mensaje)s', 
    filename="ejercicio2.log", 
    filemode = 'w' # w guarda el ultimo , a me guarda el historico. 
    
    
)

# crea un nuevo manejador hadler para gestionar mensajes de auditoria  por .log y por consola

console_handler = logging.StreamHandler() # crear una instacia, es decir, un nuevo manejador
console_handler.setLevel(logging.DEBUG)   # configurar e nivel del logging, en eset caso, el nivel mas lev
console_handler.setFormatter(logging.Formatter('%(asctime)s -%(levelname)s - %(message)s ',)) # Dando formato de salida al logging
logging.getLogger().addHandler(console_handler) # Agregando la instacia console_handler al manejador principal

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precio_unitario: float
    
    
    def procesar(self):
        try:
            logging.info(f"Iniciando el proceso de facturacion para el cliente {self.cliente}")
            
            if self.cantidad <= 0:
                raise ValueError(f"La cantidad del producto debe ser mayor  a cero")
            if self.precio_unitario <= 0:
                raise ValueError(f"El precio deve ser mayor a cero")
            
            total = self.cantidad * self.precio_unitario
            logging.info(f"Factura fue Procesada con exito. Toral de la compra ${total} - cliente: {self.cliente}")
            
        except ValueError as e:
            logging.error(f"Error de validacion del cliente {self.cliente}: {e}")
        except Exception as e:
            logging.critical(f"Error inesperado al momento de procesar la factura de {self.cliente}: {e}")
        finally:
            logging.info(f" El proceso de facturacion para {self.cliente} finalizo ")        
            
if __name__ == "__main__":
    
    factura1 = Factura("Carlos", 10, 1500.25)       
    factura1.procesar()  
    
    # factura2 = Factura("pedro", 10, 1500.25)       
    # factura2 = Procesar()      


