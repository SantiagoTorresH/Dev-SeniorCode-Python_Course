# operaciones.py
from productos import obtener_producto

def calcular_total(lista_productos):
    """calcular el total de la compra"""
    
    total = 0 
    for producto in lista_productos:
        total += producto['precio']    
    # return calcular_total
    return total 

def agregar_producto(id_producto, cantidad, lista_productos):
    """ Agregar un producto a la lista de compra """
    producto = obtener_producto(id_producto)
    if producto:
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio" ] * cantidad })
    else:
        raise ValueError(f"Productos de ID {id_producto}, no encontrado ")    
        
        

    
    

