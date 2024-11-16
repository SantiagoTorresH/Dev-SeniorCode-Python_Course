from datetime import datetime
import statistics
# los parametros reciben el literal de informacion 


class Tarea:
    #funcion de inicializacion = metodo constructor
    def __init__(self, nombre, fechaLimite, categoria,horasDedicadas): # estos son los  parametros que reciben argumentos que son la informacion que viaja . 
        # todo lo que vadespues del self es para decir que lo que va despues son parametros. 
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas
        
#funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre de la tarea")
    fechaLimite_str = input("Ingrese la fecha limite de la terea (DD/MM/YYYY)")      
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y") # si lo hace bien es un try, si no except
        #asifna lo de str a fechalimite 
    except ValueError:
        print("Fecha no valida.")
        return # vuelve y lo retorna para que ingrese 
    
    categoria = input("Ingrese la categoria de la tarea (Estudio, preonal, trabajo, otras. ) ")    
    
    horasDedicadas_str = input("Ingrese las horas dedicadas, separadas en comas ej 3,4,5: ")  # 5, 4,3 
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(","))) # separa con comas los numeros que ingreso, se le pasa que es float, el map sefara lo que aparentemente era flotante y lo convierte en una lista separadas por comas. 
    # antes del map todo era un solo numero, el map los coge y separa cada numero y los agrega a la lista. 
    except ValueError:
        print("fecha no valida.")    
        return
        
# crear un objeto y lo agrega a la lista de tareas # el objeto es tarea 
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas )     
    listaTareas.append(tarea)
    print("Tarea agregada con exito. ")
    
def VisualizarTareas(listaTareas):
    if not listaTareas:    
        print("NO hay tareas para mostrar")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print("f\n Tarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}")
        print(f"categoria: {tarea.categoria}")
        print(f"Horas dedicadas: {tarea.horasDedicadas}")
        
def analizarHoras(listaTareas):
    if not listaTareas:
        print("no hay tareas registradas")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)        # staticstic halla el promedio
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\n Analisis de {tarea.nombre}')
        print(f' Promedio {promedio}')
        print(f' Maximo de horas {maximo}')
        print(f' minimo de horas {minimo}')
        
def generarInforme(listaTareas):  
    if not listaTareas:
        print("no hay tareas registradas")
        return      
    # abrir un archivo tct par esribir tareas
    with open ("informe_tareas.txt", "w") as archivo:
        #escribir los detalled de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f"Nombre: {tarea.nombre}\n")
            archivo.write(f"Fecha limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}")
            archivo.write(f"categoria: {tarea.categoria}\n")
            archivo.write(f"Horas dedicadas: {tarea.horasDedicadas}\n")
            archivo.write("\n")
    print("informe generado como 'inform_taread.txt' ")        
    
def menu():
    listaTareas = []
    while True:
        print("\nmenu de opciones: ")    
        print("1. Agregar Tarea: ")    
        print("2. visualizar tareas: ")    
        print("3. analizar horas dedicadas: ")    
        print("4. generar Informe: ")    
        print("5. Salir: ")    
        
        opcion  = input("Seleccione una opcion: ")
        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            VisualizarTareas(listaTareas) 
        elif opcion == "3":
            analizarHoras(listaTareas)          
        elif opcion == "4":
            generarInforme(listaTareas)
        elif opcion == "5":
            print("Saliendo del programa")  
            break         
        else:
            print("Ingrese una opcion valida")    
            