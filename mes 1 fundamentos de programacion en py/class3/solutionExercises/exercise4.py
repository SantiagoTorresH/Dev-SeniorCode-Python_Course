# Ejercicio 4: Menú de Opciones
# Crea un programa que muestre un menú de opciones simples (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y permita al usuario seleccionar una opción. Dependiendo de la opción, el programa debe ejecutar una acción específica o salir del bucle si el usuario elige "Salir". Usa un bucle while para mostrar el menú hasta que el usuario decida salir.

print("Esta en el menu de opciones, tienes la opcion de:\n 1.Saludar\n 2.Despedirse \n 3.Salir")


while  True:
    option = int(input("ingresa 1, 2 o 3 dependiendo de la opcion que quieras. "))
    
    if option == 1:
        print("hola amiguitos")
    elif option == 2:
        print("Bye Bye amiguitos")    
    elif option == 3:
        print("Saliedo del programa... ")
        break
    else:
        print("opcion no valida, por favor digita 1, 2 o 3..")     
    
