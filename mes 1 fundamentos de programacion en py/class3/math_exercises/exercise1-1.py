# 1. Ejercicio: Serie de Fibonacci 🌀
# La serie de Fibonacci es una secuencia de números en la que cada número es la suma de los dos anteriores, comenzando con 0 y 1. La fórmula de Fibonacci es:

# [ F(n) = F(n-1) + F(n-2) ]

# Instrucciones:
# Escribe un programa que solicite al usuario cuántos términos de la serie de Fibonacci desea calcular.
# Usa un bucle for o while para calcular y mostrar los términos de la serie.

# Solicitar al usuario el número de términos
terminos = int(input("¿Cuántos términos de la serie de Fibonacci deseas? "))

# En esta linea declaramos dos variables al tiempo, es lo mismo que usar: 
# a = 0
# b = 1
a, b = 0, 1
for i in range(terminos):
    print(a)
    tempA = a
    a = b
    b = tempA + b