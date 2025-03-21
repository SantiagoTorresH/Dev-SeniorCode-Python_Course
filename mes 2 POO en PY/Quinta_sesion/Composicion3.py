# Tercer ejercicio composicion
class CalcularImpuesto:
    def ejecutar(self, monto):
        return monto * 0.19
    
class AplicarDescuento:
    def ejecutar(self, monto, descuento ):
        return  monto - (monto * descuento / 100)
    
    
class GenerardRecibo:   
    def ejecutar(self, monto):
        return f"Recibo generado por ${monto:.2f}"
        

class Facturacion:
    def __init__(self):
        self.pasos = []
        
    def agregar_paso(self, paso):
        self.pasos.append(paso)
        
    def procesar_factura(self, monto, descuento=0):
        print("Procesar factura")
        for paso in self.pasos:
            if isinstance(paso, CalcularImpuesto): # is instance es codigo , si ve que no esta no lo ejecuta
                impuesto = paso.ejecutar(monto)
                print(f"Impuesto calculado: ${impuesto:.2f}")
                monto += impuesto     
                
            elif isinstance(paso, AplicarDescuento):
                monto = paso.ejecutar(monto, descuento)
                print(f"Descuento aplicado: ${monto:.2f}")
                
            elif isinstance(paso, GenerardRecibo):
                print(paso.ejecutar(monto))
                
facturacion = Facturacion()
impuesto = CalcularImpuesto()
descuento = AplicarDescuento()
recibo = GenerardRecibo()

facturacion.agregar_paso(impuesto)                
facturacion.agregar_paso(descuento)
facturacion.agregar_paso(recibo)

facturacion.procesar_factura(500, descuento=10)
                
                    
                       