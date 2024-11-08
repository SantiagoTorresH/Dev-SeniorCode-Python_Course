## listas tuplas y diccionarios 

## las listas crecen y disminuyenb en el tiempo 
# los diccionarios tienen un indice o id y un valor que es la variable
# los json estan basados en diccionarios

estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

# funcion para matricular un estudiante
def matricularEstudiante():
    nombre = input('Digite el nombre del estudiante: ') # i para estudiante,, curso para java o py 
    print('Seleccione el curso a matricular: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
        
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {'nombre':nombre, 'curso': curso}  # Estudiante es un diccionario
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso{curso} ')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos ')    
        
# funcion para asignar un docente a un curso
def asignarDocente():
    print(f'Seleccionar el curso al que desea asignar un docente: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')        
        
    cursoSeleccionado = int(input('Ingrese el numero del curso: ')) 
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input('Ingrese el nombre del docente: ')
        docente = {'nombre':nombreDocente, 'curso': curso}  # Estudiante es un diccionario
        docentes.append(docente)
        print(f'Docente: {nombreDocente}, asignado en el curso{curso} ')
    else:
        print(f'OPcion de curso no valida, recuerde que solo hay {len(cursos)} cursos  ')
            
# funcion para asignar horario a un curso 
def asignarHorario():
    print('Seleccionar el curso al que desea asignar el horario: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')   
        
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))    
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        dias = input('Ingrese los dias de clase (ej: martes y jueves): ')
        hora = input('Ingrese la hora de la clase (ej: 6:pm ): ')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'Horario asifnado al curso: {curso}: {dias} a las {hora }')
    else: 
        print(f"opcion de curso no valida, recuerde que solo hay {len(cursos)}")     
        
def mostrarEstudiantes():
    if estudiantes:
        print('lista de estudiantes matriculados')
        for estudiante in estudiantes:    
            print(f"Estudiante: {estudiante['nombre']}, Curso:{estudiante['curso']}")   
    else:
        print('NO hay estudiantes matriculados ')         
        
def mostrarDocentes():
    if docentes:
        print('lista de docentes asignados')
        for docente in docentes:    
            print(f"Docente: {docente['nombre']}, Curso:{docente['curso']}")   
    else:
        print('NO hay docentes asignados ')      
        
def mostrarHorarios():
    if horarios:
        print('\n lista de estudiantes matriculados')
        for horario  in horarios:    
            print(f"Curso: {horario['curso']}, Dias:{horario['dias']}, HOra{horario['hora']}")   
    else:
        print('NO hay horarios asignados ')                      
        
while True:
    print('\n Sistema de matricula de Dev Senior')
    print('1. Matricular estudiante')
    print('2. Asignar docente a un curso')
    print('3. Asignar horario a un curso')
    print('4. MOstrar la lista de estudiantes matriculados')
    print('5. MOstrar la lista de Docentes asignados')
    print('6. Mostrar horarios de los cursos')
    print('7. salir')
    
    opcion = int(input('Digite la opcion: '))
    
    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3: 
        asignarHorario()        
    elif opcion == 4: 
        mostrarEstudiantes()        
    elif opcion == 5: 
        mostrarDocentes()        
    elif opcion == 6: 
        mostrarHorarios()        
    elif opcion == 7: 
        print("Estas abandonando el programa byee. .")
        break
    else:
        print("ha ingresado una opcion no valida papyyy")       
            