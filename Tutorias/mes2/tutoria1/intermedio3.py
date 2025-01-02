# 3. Clase `Empleado`: Diseña una clase `Empleado` con atributos: Nombre y Salario. Incluye un método `aumentar_salario`
# que aumente el salario en un porcentaje dado como argumento.
#   Ejemplo:  
#   emp = Empleado("Luis", 2000)
#   emp.aumentar_salario(10)  # Incrementa el salario un 10%
#   print(emp.salario)  # Salida: 2200

class Empleado:
    def __init__(self, nombre, salario):
        # Atributos de instancia
        self.nombre = nombre
        self.salario = salario

    # Método para aumentar el salario
    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento

# Ejemplo de uso
emp = Empleado("Luis", 2000)

# Aumentar el salario en un 10%
emp.aumentar_salario(10)

# Mostrar el salario después del aumento
print(emp.salario)  # Salida: 2200
