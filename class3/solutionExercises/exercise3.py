# Ejercicio 3: Números Pares e Impares
# Escribe un programa que recorra los números del 1 al 20 e imprima si cada número es par o impar. Usa un bucle for para recorrer los números y condicionales para determinar si un número es par o impar.

for numero in range(1, 21):
    if numero % 2 == 0: 
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")        