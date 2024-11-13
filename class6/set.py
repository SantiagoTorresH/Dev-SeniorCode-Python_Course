# los set no tiene un orden definido, no existe orden 
# se puede agregar y eliminar, mas no modificar datos. 
# no puede buscar por posicion 
# no deja ningun duplicado 
lenguajes = {'Java', 'Python', 'JavasCript '}
print(lenguajes)
print(len(lenguajes))
print('Java' in lenguajes) # busca a go en lenguajes 
lenguajes.add('Go') # m3 lo agrega en cualquier parte. 
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje)
lenguajes.remove('Java')
print(lenguajes)    
lenguajes.discard('Python')
print(lenguajes )


