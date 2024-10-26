# ## 1. **Ejercicio: Calculadora Avanzada** 📐

# Crea una calculadora que tome dos números y un operador del usuario (`+`, `-`, `*`, `/`, `%`, `**`). El programa debe realizar la operación correspondiente y mostrar el resultado. Si el operador ingresado no es válido, el programa debe mostrar un mensaje de error.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operator = input("Ingresa un operador (+, -, *, /, %, **): ")

result = None  # Inicializa result

# Verifica el operador y realiza la operación correspondiente
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:  # Verifica división por cero
        result = num1 / num2
    else:
        print("Error: No se puede dividir por cero.")
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    print("Error: Operador no válido.")

# Solo imprimir el resultado si es válido
if result is not None:
    print(f"El resultado de {num1} {operator} {num2} es: {result}")
