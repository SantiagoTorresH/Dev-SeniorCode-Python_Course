class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad
            
class Tienda:
    def __init__(self):   
        self.productos = {}
        self.historia_ventas = []
        
    def agregar_producto(self, id_producto, nombre, precio, stock):
        self.productos[id_producto] = Producto(id_producto, nombre, precio, stock)
        
    def obtener_productos(self, id_producto):
        return self.productos.get(id_producto)
    
    def registrar_venta(self, id_producto, cantidad):
        producto = self.obtener_productos(id_producto)
    
        if producto:
            producto.reducir_stock(cantidad)
            total = producto.precio * cantidad
            self.lista_productos.append({
                "producto": producto["nombre"], 
                "cantidad": cantidad, 
                "precio_total": total
            
        })
        else:
            raise ValueError(f"Productos de ID {id_producto}, no encontrado ")    
                
        
        