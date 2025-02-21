
# uso de Breakpoint Simples


class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
        
    def calculo_comision(self):
        
        if self.ventas > 5000:
            print(f"*****Empleado: {self.nombre}. Ventas: {self.ventas} del 10% ")
            return self.ventas * 0.10
        
        print(f"Empleado: {self.nombre}. Ventas: {self.ventas} del 5% ")
        return self.ventas * 0.05
    
empleados = [
    Empleado("lleny", 6000),
    Empleado("Santi", 3000)
]

for emp in empleados:
    print(f"Empleado: {emp.nombre}. comision: {emp.calculo_comision()}")


# Break point condicional



