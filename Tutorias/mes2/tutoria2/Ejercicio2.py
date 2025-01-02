class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    

Coche1 = Coche("Ford", "Mustanf")

print(Coche1.marca)
print(Coche1.modelo)
        