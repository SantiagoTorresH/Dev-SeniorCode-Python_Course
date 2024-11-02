# 3. Ejercicio: Cálculo de Potencias 💥
# Escribe un programa que solicite al usuario dos números: la base y el exponente. El programa debe calcular la potencia utilizando la fórmula:

# [ a^{n} = aaa*a \ (n\ veces)]

# Instrucciones:
# Solicita la base y el exponente al usuario.
# Calcula la potencia utilizando el operador ** en Python.
# Muestra el resultado en pantalla.
# Hazlo ahora sin usar el operador **

# Solicitar la base y el exponente al usuario
base = int(input("Ingresa la base: "))
expo = int(input("Ingresa el exponente: "))

# Calcular la potencia usando el operador **
potencia_con_operador = base ** expo
print(f"{base} elevado a {expo} es: {potencia_con_operador}")

# Calcular la potencia sin usar el operador **
potencia_sin_operador = 1
for _ in range(expo):
    potencia_sin_operador *= base  # Multiplicamos la base, 'expo' veces

print(f"{base} elevado a {expo} es: {potencia_sin_operador} (sin usar el operador **)")
