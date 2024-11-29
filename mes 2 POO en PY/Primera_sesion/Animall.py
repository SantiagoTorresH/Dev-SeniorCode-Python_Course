class Animal1: 
    
    cantidadAnimales = 0
    
    def _init__(self, name):
        self.name = name
        Animal1.cantidadAnimales += 1
        
        
    @classmethod # los decoradores sirve para documentar, sirve para ver que el metodo que viene es de clase
# el argumento ya no el sl objeto si no que se trae tada la clase 
    def totalAnimales(cls): # me trae toda la clase, no solo el self
    
        return f"TEngo {cls.cantidadAnimales} animalitos "
    
        animalitos1 = Animal1("Ron") # creo la primera instancia, el primer objeto luego del igual va la instancia, meejecuta el me
        animalitos2 = Animal1("RAyo")  # nombre del objeto animalitos 2, luego va la instancia
        animalitos10 = Animal1("RAyo")
    
        print(animalitos10.name)
        print(Animal1.cantidadAnimales())

        