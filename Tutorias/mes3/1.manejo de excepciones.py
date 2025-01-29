# nombre = input("Ingrese su nombre: ")

# El bloque try se utiliza para envolver el codigo que puede generar excepciones.si ocurre una excepcion, ejecuta el bloque except
try:
    num = int(input("Ingrese un numero: "))

    print(f"el doble es : {num*2}")
    
except ValueError:
    print("Error: No ingresaste un numero valido ")    
    
else: # El bloque ese solo se ejecuta solo si no ocurre ninguna exepcion dentro del bloque try
    print(f"el numero ingresado es: {num}")    
    
# El bloque finally se ejecuta siempre, independientemente de si ocurre o no una excepcion
# es util para liberar recursos, cerrar archivos, conexiones a bases de datos, etc. 

try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print('Error: el archivo no existe')
finally: 
    try:
        archivo.close()
        print("Archivo cerrado")
    except NameError:
        print("El archivo no se abrio, no hay ue cerrar ")    
        
        #? manejo de multiples excepciones
# puedes manejar diferentes tipos de exepciones en el bloque separados por except o agruparlos

'''  
try:
    num = int(input("ingresa un numero: "))
    resultado = 10/num
except ValueError:
    print("Error: no ingresaste un numero valido")
    
except ZeroDivisionError:
    print("Error: no se puede dividir por 0 ")        
    
    '''
    
try:
    num = int(input("ingresa un numero: "))
    resultado = 10/num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
    
    #* creacion de excepciones personalizadas
    
class MiExcepciones(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
try:
    edad = int(input("Ingrese la edad: "))
    if edad < 0:
        raise MiExcepciones("La  edad no puede ser negativa")
    print(f"Tu edad es {edad}")    
except MiExcepciones as e:
    print(f"Error: {e}")        
    
    
#! REcomendacions
#Use de excepciones solo para situaciones exepcionales, no como logica de control
# siempre usar finally para liberar recursos
#se especifica al capturar error
            