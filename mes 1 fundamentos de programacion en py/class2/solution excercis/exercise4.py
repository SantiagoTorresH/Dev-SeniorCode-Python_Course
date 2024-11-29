# ### **Ejercicio 4: Verificación de Edad**

# Crea un programa que pida la edad del usuario y verifique si es mayor de edad (18 años o más). Usa operadores lógicos para determinar si la persona puede votar o no.

age = int(input("ingrese su edad: "))
if age >= 18:
    print("usted puede votar")   
    
else:
    print("usted no puede votar, espere a que tenga la edad")   