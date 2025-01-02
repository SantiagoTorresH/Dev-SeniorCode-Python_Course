# 2. Herencia: Clase Vehiculo y Moto: Crea una clase base Vehiculo con los atributos: Tipo y Marca. Crea una subclase Moto que herede de Vehiculo y tenga un método hacer_wheelie que imprima:  "¡La moto [Marca] está haciendo un wheelie!"
# Clase base Vehiculo

class Vehiculo:
    def __init__(self, tipo, marca):
        # Atributos de instancia
        self.tipo = tipo
        self.marca = marca

# Subclase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca):
        # Llamar al constructor de la clase base
        super().__init__("Moto", marca)

    # Método específico de la subclase
    def hacer_wheelie(self):
        print(f"¡La moto {self.marca} está haciendo un wheelie!")

# Ejemplo de uso
moto = Moto("Yamaha")

# Llamar al método de la subclase
moto.hacer_wheelie()  # Salida: ¡La moto Yamaha está haciendo un wheelie!
