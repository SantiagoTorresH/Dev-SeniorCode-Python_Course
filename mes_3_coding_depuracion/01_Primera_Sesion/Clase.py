"""sumary"""


# try:
#     #codigo
    
# except AlgunasExcepcion as e:
#     # codigo
    
# else:
#     # codigo
# finally:
#     # codigo

"""_sumary_  # los docstring son para documentar el codigo
    
    Args:
        numero1
    """

"""
    
    def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(resultado)
    except ZeroDivisionError as e:
        print("la division por cer no se puede lograr")
        return None
division_cero(3, 0)      

# sin captura de excepciones
def division_cero(numero1, numero2):
    resultado = numero1 / numero2
    print(resultado)  
division_cero(3, 0)   
    
    """
    
# mismo ejercicio explicando las excepciones multiples
"""  
def division_segura():
    try:
        numerador = int(input("Ingree el numerador de la division"))    
        denominador = int(input("Ingree el denumerador de la division"))   
        resultado = numerador / denominador
        print(f" El resultado de la division de {numerador} entre el {denominador} es iguala:{resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error {e}")
        
division_segura()   

"""      
# manejo de excepciones especificas "Exception" << No es recomendable SIEMPRE ya que puede esconder errores >>


"""
def abrir_archivo():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
        
            print(numero)
        
    except Exception as e:
        print(f"Se produjo un error{e}")
    
    abrir_archivo()   
    
"""

# uso del else y finally
# ejercicio de la division por Cero

"""
def division_completa():
    try:
        numero = int(input("Ingresa un numero: "))
        resultado = 10 / numero
        print(f" el resultado de la division es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        
    else:
        print(f"El resultdo de la division es { resultado}")    
    finally: # el finally siempre se va a ejecutar
        print("La operacion finalizo ....")   
        
division_completa()

"""

# App que permite procesar pedidos
# validar jque el codigo de producto sea alfanumerico
# validar que la cantidad sea mayor a cero

"""

def procesar_pedido(codigo_producto, cantidad):
    try:
        codigo_producto = input(" Ingrese el codifo del producto")
        cantidad = input(" Ingrese el cantidad del producto")
        
        if not codigo_producto.isalnum():
            raise ValueError("el codigo del procudto debe ser alfanumerico ")
        
        # validar cantidad mayor a cero
        if not cantidad >= 0 :
            raise ValueError(" la cantidad del producto deve ser mayo r a cero")
        
        precio_unitario = 50
        total = precio_unitario * cantidad
        
    except ValueError as e:
        print(f" Error al procedsar el pedido: {e}")
        
    else:
        print(f"Total a pagar: {total}")    
        
    finally:    
        print(" Operacion filalizada")
        
procesar_pedido()         
"""

# class excepciones personalizadas

# class ErrorProductoNoDisponile(Exception):
#     def __init__(ofjeto, message = "El producto no esta disponible en ztock"):
#         objeto.message = message
        

class ErrorDePago(Exception):
    """Gestion de excepciones"""
    pass

class PasarelaDePago():
    """Simulacion de una estrategia tecnologica de pago"""

    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
        
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("El numero de l a tarjeta no es valido")
    
        if monto <= 0:
            raise ErrorDePago(" El monto debe ser mayor a cero")
    
        return f"pago de ${monto} fue procesafo con exito"
    
    def procesar_pago_cliente(nombre_cliente, numero_tarjeta, monto):
        
        try: 
            print(f"Iniciando el proceso de pago para {nombre_cliente}")
            resultado = PasarelaDePago.procesar_pago(numero_tarjeta, monto)
        except ErrorDePago as e:
            print(f" Error al procesar el pago. {e}")
            
        except Exception as e:
            print(f" se produjo un error inesperado. {e}")    
            
        else:
            print(resultado)
        finally: # el finally siempre se va a ejecutar. 
            print("Registro finalizado")        
        
if __name__ == "__main__":
    
    # procesar_pago_cliente = ("Jose", "45454", 99.04)        
    procesar_pago_cliente = ("luis", "12345", 100)        
    # procesar_pago_cliente = ("carolina", "45454", 0)        
    
    
    