class Vehiculo:
    def __init__(self, tipo):
        self.tipe = tipo
    
    def descripcion(self):
        return f"Este vehiculo es de tipo {self.tipo}"
    
class Moto(Vehiculo): # Moto es HIja de vehiculo y me puedo traer lo de veihiculo
    
    def __init__(self, tipo, marca):
        super().__init__(tipo) # Atributo de la clase madre
        self.marca = marca
        
moto1 = Moto("Motocicleta", "Hero")
print(moto1.descripcion())                