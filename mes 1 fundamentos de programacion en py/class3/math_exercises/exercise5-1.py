# 5. Ejercicio: Calcular la Hipotenusa de un Triángulo Rectángulo 📐
# Usa el Teorema de Pitágoras para calcular la hipotenusa de un triángulo rectángulo. La fórmula es:

# [ c = \sqrt{a^2 + b^2} ]

# donde ( a ) y ( b ) son los catetos del triángulo, y ( c ) es la hipotenusa.

# Instrucciones:
# Solicita al usuario los valores de los catetos.
# Calcula la hipotenusa usando la fórmula.
# Muestra el resultado en pantalla.
# Usa la funcion sqrt de la libreria math de python como en el ejemplo para importar librerias.

import math

firstCateto = int(input("Ingresa el valor del primer cateto. "))
secondCateto = int(input("Ingresa el valor del segundo cateto. "))

hipo =  math.sqrt(firstCateto ** 2 + secondCateto ** 2 )


print("La hipotenusa del triangulo es " + str(hipo))










