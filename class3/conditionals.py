
age = 18
country = 'Col'
userHasDNI = True

if age >= 21 and country =="USA":
    print('you can buy alcohol')
elif age >= 18 and country =="COL":
    print('you can buy alcohol')
else:
    print('you can\ nt  buy alcohol')
    
    # Bucless for for, cuando sabemos cuanto lo vamos a usar. 
    # For each value of the i in the range
    # for i = 0; i < 10; i++
    for i in range(10): # (0, 10, 3) de cero a 10 y que vaya de 3 en 3 . 
        print(i)
        
        # while se usa cuando no se sabe cuantas vexes se va a repetir
# condition
contador = 1
while contador <= 5:
    print(f"Este es el numero {contador}")
    contador += 1
            
        #///
while userHasDNI: 
    
    # block 1 
    print("Hello 1")
    
    # block 2 
    if age >= 21 and country =="USA":
        print('you can buy alcohol')
        break  # el break para el bucle
    elif age >= 18 and country =="COL":
        print('you can buy alcohol')
        break
    else:
        userHasDNI = False
        print('you can\ nt  buy alcohol')
        
        #block 3 
        print (" Ello 2")
        
print("Hello ")        

#continue # sallta a la siguiene iteracion