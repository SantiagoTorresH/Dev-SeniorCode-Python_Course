import tkinter as tk
from tkinter import messagebox

# modelo
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.idProducto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def reducir_stock(self, cantidad):
        if cantidad < self.stock:
            self.stock -= cantidad
            return True
        return False
    
class Modelo:
    def __init__(self):
        self.productos = {
    1: {"productID": 1,"name": "Apple", "price": 1.5, "stock": 100},
    2: {"productID": 2,"name": "Green banana", "price": 1.0, "stock": 150},
    3: {"productID": 3,"name": "Pear", "price": 2.0, "stock": 80},
    4: {"productID": 4,"name": "Grapes", "price": 2.5, "stock": 120},
    5: {"productID": 5,"name": "Watermelon", "price": 3.0, "stock": 50},
    6: {"productID": 6,"name": "Melon", "price": 2.8, "stock": 60},
    7: {"productID": 7,"name": "Orange", "price": 1.2, "stock": 200},
    8: {"productID": 8,"name": "Tangerine", "price": 1.3, "stock": 180},
    9: {"productID": 9,"name": "Kiwi", "price": 3.5, "stock": 70},
    10: {"productID": 10,"name": "Strawberry", "price": 2.8, "stock": 90},
    11: {"productID": 11,"name": "Avocado", "price": 2.2, "stock": 110},
    12: {"productID": 12,"name": "Papaya", "price": 2.6, "stock": 40},
    13: {"productID": 13,"name": "Pomegranate", "price": 3.2, "stock": 75},
    14: {"productID": 14,"name": "Cherry", "price": 4.0, "stock": 85},
    15: {"productID": 15,"name": "Raspberry", "price": 3.7, "stock": 65},
    16: {"productID": 16,"name": "Plantain", "price": 1.8, "stock": 95},
    17: {"productID": 17,"name": "Pinapple", "price": 3.5, "stock": 55},
    18: {"productID": 18,"name": "Mango", "price": 2.5, "stock": 105},
    19: {"productID": 19,"name": "Lime", "price": 1.0, "stock": 130},
    20: {"productID": 20,"name": "Lemon", "price": 1.0, "stock": 140}
        }
        
    def obtener_productos(self):
        return [f"{prod.id_producto} - {prod.nombre} - ${prod.precio}- Stock {prod.stock}" for prod in self.productos.values()]   
    
    def obtener_historia(self):
        return self.historial_ventas
    
    def vender_productos(self, id_producto, cantidad):
        if id_producto in self.productos and self.productos[id_producto].reducir_stock(cantidad):
            total = self.productos[id_producto].precio * cantidad
            self.historial_ventas.append((self.productos[id_producto].nombre, cantidad, total))
            return total
        return None
    
    
        

#controlador
class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        
    def obtener_productos(self):
        return self.model.obtener_productos()
    
    
    def agregar_al_carrito(self, producto_str, cantidad, carrito):
        id_productos = int(producto_str.split(" - "[0]))
        total = self.modelo.vender_producto(id_producto, cantidad)
        if total is not None:
            carrito[id_productos] = carrito.get(id_producto, 0) + total
            
        else: messagebox.showerror("Error", "Stock insuficiente")
        
    def finalizar_compra(self, carrito, total_var):
        if not carrito:
            messagebox.showerror("error", "El carrito esta vacion")
            return
        mensaje = "Compra Finalizada"
        for id_producto, total in carrito.items():
            mensaje += f"{self.modelo.productos[id_producto].nombre}: ${total}"
        messagebox.showinfo("compra REalizada", mensaje)
        carrito.clear()
        
                        
        


#vista

class vista():
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("caja Registradora - Fruber")
        
        self.carrito = {}
        self.total = tk.StringVar(value="Total: $0")
        self.cantidad_var = tk.StringVar()
        
        
        

#Main 

root = tk.Tk()
controlador = Controlador()
app = vista 