#listas  ## 
nombres = ['Ana', 'Sebastian', 'Santiago','Linda']
# el punto de partida es 0 
# el punto de finalizacion es uno antes. 
# el literal de informacion es el valor de la variable. 

print(nombres)
print(nombres[1])
print(nombres[-1]) # me muestra el ultimo 
print(nombres[0: 2]) # va de el 0 a el que esta en la posicion uno 
print(len(nombres))
nombres.append('Jeniffer') # el .append lo agrega al final . 
print(nombres)
nombres.insert(1, 'Maria') # me lo inserta el la posicion 1. 
print(nombres)
nombres.remove('Linda') # elimina 
print(nombres)
nombres.insert(1, 'Linda')
print(nombres)

nombres.pop()  # 3l pop elimina el ultimo elemento de la lista
print(nombres)
del nombres[3] # Elimian el indice que se le ingresa. 
print(nombres) 

nombres.append('Linda') # el .append lo agrega al final . 
print(nombres)

nombres.remove('Linda') # el .append lo agrega al final . 
print(nombres)

nombres.pop(1) #elimina segun el indice especificado 
print(nombres)
nombres.clear() # limpia la lista borra todo 
print(nombres)
nombres.append("Elizabeth")
print(nombres)
del nombres




