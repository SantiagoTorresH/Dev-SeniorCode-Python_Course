import threading   # thread es hilo de comunicacion, para llamar al lock
from abc import ABC, abstractmethod

# patron de dise;o Singleton, se acegura que la clase tenga una unica instancia
#

class SistemaFacturacion:
    
    _instancia = None  # variables de clase
    _lock = threading.Lock()   # el loock variable proteguida captura el hilo y luego lo bloqueamos
    
    def __new__(cls, *args, **Kwargs):
        
        if not cls._instancia is None:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia          
        
        
            #d opcionL
        """       
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia  
        """
        
    def _inicializacionHistorico(self):
        self.historial = []
        print("Sistema de facturacion inicializado")
            
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)  
        print(f"La operacion fue registrada: {operacion}")  
        
# clase Abstracta = Superclase
class ProcesoNegocio(ABC):
    
    @abstractmethod
    def ejecutar(self):
        pass
    
class ProcesarPedido(ProcesoNegocio):
    def ejecutar(self):
        print("procesando pedido....")
        return "Pedido procesado"
    
class ProcesarFactura(ProcesoNegocio):  
    
    def ejecutar(self):
        print("procesando factura....")
        return "factura procesada"        
    
# crear la fabrica (patron dise;o Factory)  
class FabricaProcesosNegocio:
    
    @staticmethod
    def crearProceso(tipoProceso):
        
        if tipoProceso == "pedido":
            return ProcesarPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"El proceso {tipoProceso} no existe")
    
if __name__ == "__main__":
    
    sistema_facturacion = SistemaFacturacion()
    
    proceso1 = FabricaProcesosNegocio.crearProceso("pedido") # me crea el promer proceso
    proceso2 = FabricaProcesosNegocio.crearProceso("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido1) 
        
    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido2)            

    print(" ***Historico ce procesos de negocio ***")
    for operacion in sistema_facturacion.historial:
        print(f"Transaccioon: {operacion}")
        
        








