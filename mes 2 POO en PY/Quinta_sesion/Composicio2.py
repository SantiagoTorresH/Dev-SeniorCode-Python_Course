
            
class Tarea:
    def __init__(self):
        pass     
    def ejecutar(self):
        pass
    
class TrabajoProyecto(Tarea):
    
    def __init__(self):
        pass
    
    def ejecutar(self):
        return("Trabajo en un proyecto")
    
class Capacitacion(Tarea):
    
    def __init__(self):
        pass
    
    def ejecutar(self):
        return " Tomando una capacitacion"
    
class Evaluacion(Tarea):
    def __init__(self):
        pass
    def ejecutar(self):
        return " Desarrollando evaluacion al personal "    
    
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        
    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def realizar_tarea(self):
        print(f"{self.nombre}, esta desarrllo las siguinetee tAREAS")
        for tarea in self.tareas:
            print(f" = {tarea.ejecutar()}")     
    
proyecto = TrabajoProyecto()
capacitacion = Capacitacion()
evaluacion = Evaluacion()
    
    
empleado = Empleado("Santi")
empleado.asignar_tarea(proyecto)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(capacitacion)

empleado.realizar_tarea()