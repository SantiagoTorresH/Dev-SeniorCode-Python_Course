class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
        # polimorfismo reutilizo el metodo. 
    
    def hablar(self): # polimorfismo, aca hace algo, abajo otra cosa
        return "Todo animal habla de alguna forma"
        
    
    def __str__(self):  # str imprime, convierte los atributo sen texto para poderlo imprimir
        return f" El nombre del animal es: {self.nombre}"
        
    
class Perro(Animal): # Hereda
    
    def __init__(self, nombre, raza):
        super().__init__(nombre) # el super trae de la clase madre los atributos que necesite, la trae del constructor de la clase principasl        
        self.raza = raza
            
    def hablar(self):
        return "Gua Guau"
        
    
    def __str__(self):
        return f"El nombre del perro es: {self.nombre} y su raza es: {self.raza}"
        
    
animal1 = Animal("Wisky")
perro1 = Perro("Tequila", "Doberman")

print(animal1.hablar())    
print(animal1.__str__())    

print(perro1.hablar())  # uso el mismo metodo por polimorfismo. 
print(perro1.__str__()) ## reutiliza el metodo str 