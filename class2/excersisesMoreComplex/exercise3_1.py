# ## 3. **Ejercicio: Comparador de Números** 🔍

# Escribe un programa que pida al usuario tres números. El programa debe determinar e imprimir cuál de los tres números es el mayor y cuál es el menor usando operadores relacionales.

num1 = float(input("ingrese el first number: "))
num2 = float(input("ingrese el second number: "))
num3 = float(input("ingrese el third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es {num2}")
else:
    print(f"El número mayor es {num3}")    
    
if num1 <= num2 and num1 <= num3:
    print(f"El número menor es {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"El número menor es {num2}")
else:
    print(f"El número menor es {num3}")     
         
