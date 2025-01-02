from abc import ABC, abstractmethod

# una clase abstracta es una plantilla general 
#Clase abstracta
class Empleado(ABC):
    def __init__(self, nombre, id, salario_base):
        self._nombre = nombre
        self._id = id
        self._salario_base = salario_base
        
    @property    
    def nombre(self):
        return self._nombre    
    
    @property
    def id(self):
        return self._id
    @property
    def salario_base(self):
        return self._salario_base   
    
    @salario_base.setter
    def salario_base(self, nuevo_salario):
        if nuevo_salario > 0:
            self._salario_base = nuevo_salario
        else: 
            raise ValueError("El salario debe ser mayor a cero ")    
        
    @abstractmethod  # esta obligado a moficar esa funcion , usar polimofrismo para ambiar la funcion 
    def calcular_bono(self):
        pass 
    
    
    def __str__(self):
        return f"Empleado: {self._nombre}, id: {self.id}, salario: {self.salario_base }"
    


class Desarrollador(Empleado):
    def calcular_bono(self):
        return self._salario_base * 0.10
    

class Disenador(Empleado):
    def calcular_bono(self):
        return super()._salario_base * 0.05

class Gerente(Empleado):
    def calcular_bono(self):
        return 50000

if __name__ == "__main__":
    dev = Desarrollador("Santiago", 103, 34345)
    designer = Disenador("Santiagorrd", 102, 5945)
    manager = Gerente("Jong", 104, 2343)
    
    empleados = [dev, designer, manager]
    for empleado in empleados:
        print(empleado)
    





