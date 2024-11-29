# ### **Ejercicio 3: Comparador de Números**

# Escribe un programa que solicite dos números al usuario y determine si el primer número es mayor, menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.

num1 = int(input('ingrese el primer numero'))
num2 = int(input('ingrese el segundo numero'))

if num1 > num2:
    print(f"El {num1} es mayor que el {num2}.")
elif num1 < num2:
    print(f"El {num1} es menor que el {num2}.")
else:
    print(f"El {num1} es igual que el {num2}.")
