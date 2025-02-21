# los logs, LOG

import logging
from dataclasses import dataclass, field

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s -%(message)s'
)

logging.debug("Este mensaje es del DEBUG")
logging.info("Este mensaje es del INFO")
logging.warning("Este mensaje es del warning")
logging.error("Este mensaje es para el  ERROR")
logging.critical("Este mensaje es   CRITICO")

# aPP que permite llevar seguimiento de compreas/ allos e este tipo de transaccion
# Esta app, egistraada la cantidad de prodctos, conprados,confirmacion de compra y error  en estas transacciones


logging.basicConfig(
    level= logging.DEBUG, 
    format= '%(asctime)s - %(level)s - %(mensaje)s', 
    filename="registro.log", 
    filemode = 'a'
    
)

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad:  int
    
    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"Error: no hay suficiente cantidad del producto {self.nombre}. El stock disponible {self.cantidad}")
            print(f"Error: no hay suficiente cantidad del producto {self.nombre}. El stock disponible {self.cantidad}")
            raise ValueError(f"Error: no hay suficiente cantidad del producto {self.nombre}. El stock disponible {self.cantidad}")


        else:
            self.cantidad -= cantidad
            logging.info(f"la compra fue exitosa.  El stock restante es {self.cantidad}")
            print(f"la compra fue exitosa.  El stock restante es {self.cantidad}")
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto]= field(default_factory=list)
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f"{producto.nombre} fue agregado con exito, el precio es de {producto.precio} - Cantidad: {producto.cantidad} unidades en stock")
        
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto: 
            try: 
                total = producto.comprar(cantidad)
                logging.info(f"compra realizada: { cantidad} unidades de  {nombre_producto} con un total de  {total}")
                return total
            except ValueError as e:
                logging.error(f"Error al efectuar la compra: {e}")  
        else:
            logging.warning(f"El produducto esta fuera de stock")
            
if __name__ == "__main__":
    
    tienda = Tienda()
    
    inventario_portatil = Producto(nombre= "Portatil", precio=1000, cantidad=10 )
    tienda.agregar_producto(inventario_portatil)
    tienda.realizar_compra("portatil", 4)
    
    
    inventario_teclado = Producto(nombre= "teclado", precio=445, cantidad=140 )
    tienda.agregar_producto(inventario_teclado)
    tienda.realizar_compra("teclado", 4)
        
                
        