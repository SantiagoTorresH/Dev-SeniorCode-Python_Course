for numero in range(1, 6):
    if numero == 3:
        print("Número 3 encontrado, saliendo del bucle.")
        break  # Sale del bucle cuando encuentra el número 3
    print(numero)

for numero in range(1, 6):
    if numero == 3:
        print("Saltando el número 3.")
        continue  # Salta a la siguiente iteración cuando encuentra el número 3
    print(numero)