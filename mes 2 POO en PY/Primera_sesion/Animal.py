# el metodo de instancia usa la palabra self
# el metodo de clase, trae la clase

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def saludar(self): # el self trae los atributos
            return f"MI animalito se llama{self.name} y tiene {self.age} anos"    
        
# Crear objetos 
# El objeto va en minuscula para diferenciarlo de la clase. 

animal1 = Animal("Ginebra", 3)        # ya cree el objeto

print(animal1.name)
print(animal1.age)
print(animal1.saludar())