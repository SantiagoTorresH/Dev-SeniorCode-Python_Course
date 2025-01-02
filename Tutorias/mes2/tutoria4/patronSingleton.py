import json

class SistemaGuardado:
    
    __instance = None
    
    # El patron singleton puede acceder a los datos en cualquier parte
    
    @staticmethod
    def get_instance():
        if SistemaGuardado.__instance is None:
            SistemaGuardado.__instance = SistemaGuardado()
        return SistemaGuardado.__instance
    
    def __init__(self):
        self.archivo_guardado = "Guardado.bat" # inicializa
        
    def guardar_juego(self, dato_a_guardar):
        with open(self.archivo_guardado, "w") as f: # abre el archivo # w- write
            # f.write(dato_a_guardar)
            json.dump(dato_a_guardar, f, indent= 4)
            
            
    def cargar_juego(self):
        with open(self.archivo_guardado, "r") as f: # r - read
            # return f.read()
            return json.load(f)


        
class Jugador():
    
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel 
    
    # def guardar_progreso(self):
    #     guardo = SistemaGuardado.get_instance()       
    #     datos_a_guardar = self.serializar()
    #     print(datos_a_guardar)
    #     guardo.guardar_juego(datos_a_guardar)
        
    def serializar(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel
                
        }    
    @classmethod    
    def deserializar(self, data):
        return self(data["nombre"], data["nivel"])  
                    
        
def cargar_partida():
        guardo = SistemaGuardado.get_instance()       
        datos_guardados = guardo.cargar_juego()
        jugador = Jugador.deserializar(datos_guardados)
        

            
            
"""
jugador1 = Jugador("Santiago", 24)           
guardado = SistemaGuardado.get_instance()
guardado.guardar_juego(jugador1.serializar())
"""

guardando = SistemaGuardado.get_instance()
datos_cargados = guardando.cargar_juego()
jugador_cargado = Jugador.deserializar(datos_cargados)        
print(jugador_cargado.nombre)    
            