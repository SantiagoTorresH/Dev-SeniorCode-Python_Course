
class Animal:
    
    def __init__(self):
        pass
        
    def hablar(self):
        pass
    
class Perro(Animal): 
    
    def __init__(self):
        pass
    
    def hablar(self):
        return f"El perro hace gua guag"
        pass
    
class Gato(Animal): 
    
    def __init__(self):
        pass
    
    def hablar(self):
        return f" El gato hace miaumiau "    
    
animales = [Perro(),  # instancias 
            Gato(),
            Perro(),
            Gato()
    
]    
        
for animal in animales:
    print(animal.hablar())     
    
    # las classes abastractas funconan como plantillas 
    # python no usa interfaces, las interfaces no tienen estado 
    
    
    