# Metodos Estaticos

class Matematica: 
    
    @staticmethod # el decorador indica que lo que sigue es estatico, va pegado
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b
    
print(Matematica.suma(10, 10))    
print(Matematica.resta(10, 5))    
    