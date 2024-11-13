### Tuplas 
# las tuplas son como una lista pero es inmutable, no se puede modificar. 
# las tuplas van entre ()
paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')
print(type(paises))

print(paises)
print(len(paises))
print(paises[2])
print(paises[-1])
print(paises)
for pais in paises:
    print(pais) # me imprime la lieral de informacion directamente


paisesLista = list(paises) # paises lo convierte al lista y lo asigna a paisesLista
paisesLista[1] ='Argentina'    
paises = tuple(paisesLista)# la lista la convierte a tupla y la asigna a paises 
print(paises)

del paises
print(paises)