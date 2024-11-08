#codificacion camel case

ventasTotales = 0.0

#solicitar el numero de productoss
numProductos = int(input('ingrese el numero de productos a gestionar: '))

#listas para al macenar la informacion
nombres = []
precios = []
cantidades = [] 

print('Ingreso inicial de productos a la tienda')
for i in range(numProductos):
    print(f'producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ' ).lower()
    nombres.append(nombre) 
    
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    
    cantidad = int(input('Digite la cantidad del producto: '))
    cantidades.append(cantidad)
    
#ciclo principal meni
while True:
    print('\n --- MENU DE GESTION DE DROGUERIA')
    print('1. vender prodcto')
    print('2. mostrar inventario')
    print('3. mostrar ventas totales')
    print('4. Salir')
        
    opcion = int(input('ingrese una opcion: ')) # = asignacion
        
    if opcion == 1:  # == comparacion 
        print(' \nVender producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('ingrese la cantidad a vender: '))
        productoEncontrado = False
            
        for i in range(len(nombres)):
            if nombres[i]  == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    tatalVenta = cantidadVender * precios[i]
                    ventasTotales += tatalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. toal de esta venta ${tatalVenta:.2f}')
                    print(f'Quedan {cantidades[i]}  unidades de {nombre[i]} en el inventario')
                else:
                    print(f'cantidad insuficiente en inventario. ya que en stock solo tenemos {cantidades[i]}')    
                break    
        if not productoEncontrado:
            print('producto no encontrado en el inventario')
                
                
    elif opcion == 2:
        print('\n Inventario de productos')
        for i in range(len(nombres)):
            print(f'producto {i+1}: {nombres[i].capitalize()}, precio: ${precios[i]:.2f},cantidad: {cantidades[i]}')
                
    elif opcion == 3:
        print(f'\n Ventas totales acumuladas: $ {ventasTotales:.2f}')    
            
    elif opcion == 4 :
        print('Gracias por usar el sistema de gestion de drogueria dev seniot')
        break
    else : 
        print('solo ingre opcion entre 1 y 4 . ')   
        
             