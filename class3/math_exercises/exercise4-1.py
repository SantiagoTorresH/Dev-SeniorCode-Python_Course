# 4. Ejercicio: Suma de Números Naturales ➕
# La suma de los primeros ( n ) números naturales se calcula con la fórmula:

# [{\displaystyle \sum _{k=1}^{n}k={\frac {n(n+1)}{2}}}]

# Instrucciones:
# Pide al usuario un número entero positivo.
# Usa la fórmula para calcular la suma de los primeros ( n ) números naturales.
# Muestra el resultado en pantalla.

# Solicitar un número entero positivo al usuario
number = int(input("Ingresa un número entero positivo: "))

# Calcular la suma de los primeros n números naturales usando la fórmula
suma = number * (number + 1) // 2  # Usamos // para obtener un resultado entero

# Mostrar el resultado
print(f"La suma de los primeros {number} números naturales es: {suma}")
