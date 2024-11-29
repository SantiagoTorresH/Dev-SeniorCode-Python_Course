# ## 5. **Ejercicio: Verificación de Año Bisiesto** 📅

# Escribe un programa que solicite un año al usuario y determine si es un año bisiesto. Un año es bisiesto si es divisible por 4 pero no por 100, a menos que también sea divisible por 400.

year = int(input("ingrese the year to verificate : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    print(f" El amo {year} es bisiesto ")
    
else:
    print(f"el amo {year} no es bisiesto. ") 
    