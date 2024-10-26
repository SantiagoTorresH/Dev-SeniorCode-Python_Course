# funcion def, nombre dela funcion parametros. 

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario = input("Ingresa un first numer0: ")

# isNumeric = inputUsuario.isnumeric() 
isFloat = is_float(inputUsuario)



if not isFloat:
    inputUsuario = input("El numero no es valido, ingrese uno nuevo: ")

numero1 = float(inputUsuario)

numero2 = float(input ("ingresa el second number: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# print("Suma: ", suma)
print(f"REsta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")


