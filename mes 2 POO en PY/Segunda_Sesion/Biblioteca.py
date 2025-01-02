
class Biblioteca:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
        
    
    
    def descripcion(self):
        return f"Libro: {self.titulo} Author: {self.autor}"
    
    
    #opcional
    
    def __str__(self):
        
        return f"Libro: {self.titulo} Autor: {self.autor} STR "
    
    
    # el polimorfismo erescribe un metodo pero le cambia 
class libroDigital(Biblioteca):
    
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor) # traig los atributos de la clase madre.
        self.formato = formato
        
    
    def descripcion(self):
        return f"Libro: {self.titulo} Author:  {self.autor} Formato {self.formato} "
        
        
    
    def __str__(self):
        
        return f"Libro: {self.titulo} Autor: {self.autor} Formato {self.formato} STR "    
    
    
libro1 = Biblioteca("la peste", "Alberto Campo")
libroDigital1 = libroDigital("El conde de Monte Cristo", "Alejandro Dumas", "pdf")

print(libro1.__str__())
print(libro1.descripcion())

print(libroDigital1.__str__())
print(libroDigital1.descripcion())

