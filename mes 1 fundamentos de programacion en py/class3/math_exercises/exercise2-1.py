# 2. Ejercicio: Cálculo del Factorial 🎯
# El factorial de un número ( n ) (representado como ( n! )) es el producto de todos los enteros positivos hasta ( n ). La fórmula es:

# [ n! = n*(n-1)(n-2) \ldots* 1 ]

# Instrucciones:
# Crea un programa que pida un número al usuario y calcule su factorial usando un bucle.
# Muestra el resultado en pantalla.
# Solicitar un número al usuario

number = int(input("Ingrese un número para calcular su factorial: "))

# Inicializar la variable para almacenar el resultado
factorial = 1

# Calcular el factorial usando un bucle
for i in range(1, number + 1):
    factorial *= i  # Esto es lo mismo que factorial = factorial * i

# Mostrar el resultado
print(f"El factorial de {number} es: {factorial}")