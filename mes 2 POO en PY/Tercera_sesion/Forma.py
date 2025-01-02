# CLASES ABSTRACTAS EN PYTHON

from abc import ABC, abstractmethod  # librerias de clases abstractas


# las clases inician en mayuscula, los objetos en minuscula. 

class Forma(ABC): # sabe que con esto es una clase abstracta
    # el la ntefaz no puedo definir constructores, 
    # cada metodo en la claseabstracta debe ener abstrac method
    
    @abstractmethod
    def __init__(self):  #El metodo constructor debe ir para buen codigo, lo dejamos vacion
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class Circulo(Forma):
    
    # si defino constructores es una clase abstracta
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return f"El area de un circulo es {3.14 * self.radio ** 2}"
    
    def perimetro(self): # puedo agregar el metodo sin probl
        return f"El perimetro de un circulo es: {2 * 3.14 * self.radio }"    
    
    
class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return f"El area de un rectangulo es {self.base * self.altura}"
    
    def perimetro(self):     # aca estamos haciendo polilmorfismo
        return f"El perimetro de un rectangulo  es: {2 * (self.base + self.altura)}"
    
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return f"El area de un cuadrado es {self.lado ** 2 }"
    
formas = [Circulo(5),
        Rectangulo(2,10),
        Cuadrado(8),
        Rectangulo(10, 20),
        Circulo(22)
]  


print("Area de las formass")
for forma in formas:
    print(forma.area())

""" 
print("\perimetro de las formas")
for forma in formas:
print(forma.perimetro())      

"""  
circulo1 = Circulo(5)
rectangulo1 = Rectangulo(2, 10)

print(circulo1.perimetro())
print(rectangulo1.perimetro())


