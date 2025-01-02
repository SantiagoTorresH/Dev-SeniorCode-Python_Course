# 5. Sistema de Inventario Simple: Diseña una clase `Producto` con: Nombre y Precio. Luego, implementa una clase `Inventario` que administre una lista de productos. Incluye métodos para: 
#   - Agregar un producto.
#   - Mostrar la lista de productos.
#   - Calcular el valor total del inventario.

class Producto:
    def __init__(self, nombre, precio):
        # Atributos de instancia
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        # Método para representar el producto como una cadena
        return f"{self.nombre} - ${self.precio:.2f}"

class Inventario:
    def __init__(self):
        # Atributo para almacenar los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario
        self.productos.append(producto)

    def mostrar_inventario(self):
        # Método para mostrar la lista de productos
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario de productos:")
            for producto in self.productos:
                print(producto)

    def calcular_valor_total(self):
        # Método para calcular el valor total del inventario
        valor_total = sum(producto.precio for producto in self.productos)
        return valor_total

# Ejemplo de uso
producto1 = Producto("Camiseta", 20.50)
producto2 = Producto("Pantalón", 40.75)
producto3 = Producto("Zapatos", 60.00)

# Crear inventario y agregar productos
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar inventario
inventario.mostrar_inventario()

# Calcular y mostrar valor total del inventario
valor_total = inventario.calcular_valor_total()
print(f"\nValor total del inventario: ${valor_total:.2f}")
