# primero va el ID: luego el value . 
# se diferencia del set por los : puntos .
conceptosProgramacion = {
    'POO': 'Programacion Orientada a objetos',
    'IDE': 'Entorni de desarrollo de datos',
    'DBMS': 'Sistema de Gestion de bases de Datos'
}
print(conceptosProgramacion)
print(len(conceptosProgramacion))

print(conceptosProgramacion['IDE'])

# get obtener
# set establecer. 
print(conceptosProgramacion.get('POO'))

#modificacion
conceptosProgramacion['DBMS'] = 'Database managements System'
print(conceptosProgramacion)

# imprimir solo los Id
for Key, value in conceptosProgramacion.items():
    print(Key, value)