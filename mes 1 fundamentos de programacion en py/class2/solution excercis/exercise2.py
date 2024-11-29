# ### **Ejercicio 2: Conversión de Unidades**

# Crea un programa que convierta una medida en metros a centímetros y milímetros. El programa debe pedir al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.

LongMeters = int(input("ingrese una longitiud en metros: "))

print(f"Esa longitiud en centimetros son: {LongMeters * 100} centimetros")
print(f"Esa longitiud en milimetros son: {LongMeters * 1000} milimetros")