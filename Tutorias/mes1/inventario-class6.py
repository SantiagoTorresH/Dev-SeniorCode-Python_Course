## los diccionarios pueden ser mutables o inmutables 
# El valor del diccionario es mutables
# la clave del diccionario no se puede modificar. 

inventario = { # un diccionario que almacena diccionarios. 
    "2323jff": {
        "nombre_producto" : "Kit arrastre",
        "modelo" : "124",
        "cantidad" : 5,
        "fecha de ingreso": "2023-05-23",
        "fecha de ultima venta" : "3042-45-5"
        },
    "2323j566ff": {
        "nombre_producto" : "Kit arrastre",
        "modelo" : "124",
        "cantidad" : 5,
        "fecha de ingreso": "2023-05-23",
        "fecha de ultima venta" : "3042-45-5"
        },
}

def crear_producto():
    pass

def mostrar_inventario():
    if inventario:
        print("======Inventario======")
        for producto in inventario:
            print(f"serial: {producto}")
            print(f"Nombre: {inventario[producto] ['nombre_producto']}")
            print(f"modelo: {inventario[producto] ['cantidad']}")
            print(f"modelo: {inventario[producto] ['modelo']}")
            print(f"modelo: {inventario[producto] ['fecha de ingreso']}")
            print(f"modelo: {inventario[producto] ['fecha de ultima venta']}")
    else:
        print("El inventario esta vacio")

def actualizar_inventario():
    pass

def eliminar_producto():
    pass

def main():
    while True:     
        print("bienvenido al inventario ")
        print("1. Mostrar inventario ")
        print("2. crear Producto")
        print("3. actualizar inventario")
        print("4. eliminr producto")
        print("5. salir")
    
        opcion = input("Seleccione una opcion :") # sin int hace que acepte cualquier cosa 
    
        if opcion == 1:
            pass
        if opcion == 2:
            pass
        if opcion == 3:
            pass
        if opcion == 4:
            pass
        if opcion == 5:
            pass
    
    
    
# if __name__ == "__main__"    

main()