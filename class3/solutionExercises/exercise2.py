# Ejercicio 2: Calculadora de Notas
# Crea un programa que pida al usuario su calificación (entre 0 y 100). Dependiendo del valor ingresado, el programa debe mostrar si el estudiante ha aprobado (60 o más) o ha reprobado (menos de 60). Usa condicionales para determinar el resultado.

yourCalification = int(input("Ingrese su calificacion de un rango de  0 a 100 ==>: "))

if yourCalification >= 60 and yourCalification < 100 :
    print("Usted ha aprobado.")
elif yourCalification > 100 or yourCalification < 1:
    print("es un numero en un rango de 0 a 100. ")  
# return()   
else:
    print("usted ha reprobado,")    
