class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
    def mover(self):
        print("El vehiculo se comenzo a mover ")    
        
class Coche(Vehiculo):
    
    def __init__(self, marca, motor, ruedas):
        super().__init__(marca)
        self.motor = motor
        self.ruedas = ruedas    
        
    def iniciar_viajes(self):
        self.motor.encender()
        for rueda in self.ruedas:
            rueda.girar()
            print("el dcoche se mueve ")     
        self.mover()
            
    def mover(self):
            print("el coche a comenzado a moverse ")    
        

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def encender(self):
        print(f"el motor de tipo {self.tipo} se ha encendido")
        
class Rueda:
    def __init__(self, tamano):
        self.tamano = tamano
    
    def girar(self):
        print(f"la rueda se tamano {self.tamano} esta girando")
        
        

            
motor_deportivo = Motor('v23')

tipo_ruedas = int(input("elija el tipo de ruedas que va a usar (10- 45): "))

# ruedas_pequenas = [Rueda(14), Rueda(14) , Rueda(14) , Rueda(14)   ]                     
ruedas_pequenas = [Rueda(tipo_ruedas), Rueda(tipo_ruedas) , Rueda(tipo_ruedas) , Rueda(tipo_ruedas)   ]                     


# coche_deportivoo = Coche(motor_deportivo, ruedas_pequenas)
coche_deportivoo = Coche("renolth 9",motor_deportivo, ruedas_pequenas)
coche_deportivoo.iniciar_viajes()