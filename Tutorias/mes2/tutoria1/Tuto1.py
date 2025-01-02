#Los metodos son las acciones, los atributos son las caracteristicas

class Libro:
    # Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def descripcion(self): # referencia a los atributos del objeto
        return f"El libro {self.titulo} fue escrito por {self.autor}."
    
libro1 = Libro("El senor de los anillos", "jrr")            
libro2 = Libro("Harry", "clarrk")         


# print("El senor de los anillos", "JRR tOLKIEN".descripcion())     

print(libro2.descripcion())       
        