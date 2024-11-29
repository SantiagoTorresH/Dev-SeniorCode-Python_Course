# ## 2. **Ejercicio: Verificación de Edad y País** 🌏

# Escribe un programa que solicite al usuario su edad y su país de residencia. El programa debe verificar si el usuario tiene al menos 18 años **y** si vive en un país específico (por ejemplo, "España") para determinar si puede votar en las elecciones nacionales.

age = int(input("ingrese su edad mi loco: "))
country = (input("ingrese su country chee: "))

if age >= 18 and country == "Espana":
    print("si podes votar en las elecciones nacioales boludo. ")
    
else:
    print("no puedes votar mi loco ")   