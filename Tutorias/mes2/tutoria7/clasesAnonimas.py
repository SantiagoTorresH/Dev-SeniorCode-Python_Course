# la clase anonima es mas facil de trabajar en si no es como una clase

Producto = type("Productos", ( ), {"Nombre": None, "Precio": None})

Producto1 = Producto()
Producto1.Nombre = "Laptop"
Producto1.Precio = 1500

print(f"Producto: {Producto1.Nombre}, Precio: {Producto1.Precio}")

