class Persona: # el nombre de la clase debe ser el nombre del modulo 
    
    def __init__(self, nombre, edad): # clase con sus atributos, nombre y edad
        # self hace relacion a la instancia, a los metodos
        self.nombre = nombre
        self.edad = edad
        
        def saludar(self): # el self trae los atributos
            return f"Hola, soy{self.nombre} y tengo {self.edad} anos"
        