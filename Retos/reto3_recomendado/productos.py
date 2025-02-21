# diccionarios de productos precargados
productos = {
    1:{"nombre": "manzana", "precio": 500, "stock":100 }, 
    2:{"nombre": "Pera", "precio": 2, "stock":100},
    3:{"nombre": "Sandia", "precio": 3, "stock":100}
    
}

historial_ventas = []

def obtener_producto(id_producto):
    return productos.get(id_producto, None)

def calcular_total(lista_productos):

    total = 0
    for producto in lista_productos:
        total += producto['precio']
    return total        

def agregar_producto_historia_venta(id_producto, cantidad, lista_productos):
    producto = obtener_producto(id_producto)
    if producto:
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio"] * cantidad})
        
# registrar la venta en el historial 
        # historial_ventas.append({
        #     "producto": producto["nombre"], 
        #     "cantidad": cantidad, 
        #     "precio_total":producto["precio"] * cantidad
            
        # })
        
    else:
        raise ValueError(f"Producto con ID {id_producto} no encontrado  ")           
        
