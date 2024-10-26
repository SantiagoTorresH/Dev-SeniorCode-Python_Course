# ## 4. **Ejercicio: Cálculo de Descuento** 💸

# Crea un programa que calcule el precio final de un producto con descuento. Solicita al usuario el precio original del producto y el porcentaje de descuento. El programa debe calcular y mostrar el precio final utilizando operadores aritméticos.

price = float(input("Ingrese el precio del producto: "))
discount = float(input("ingrese el descuento que tendra ese producto: "))

total_discount = (price * discount / 100)
total = price - total_discount

print(f"el precio que tendra ese producto sin descuento es de {total} " )