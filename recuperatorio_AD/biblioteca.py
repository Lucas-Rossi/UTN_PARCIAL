estudiantes = ["Ana", "Bruno", "Carla", "Diego"]
calificaciones = [
    #matematica #historia #biologia
    [9,8,10], #ana
    [6,7,8],  #bruno
    [10,10,9],#carla
    [7,6,5]   #diego
]

def mostrar_estudiantes_calificaciones(estudiantes:list,calificaciones:list):
    #recorre la lista estudiantes y muestra las calificaciones de cada estudiante
    print("estudiantes y calificaciones: ")
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]} -> {calificaciones[i]}")
        

def sacar_promedio(calificaciones:list)->list:
    #recorre calificiones y saca el promedio de cada estudiante y lo guarda en una lista y la retorna
    promedios=[]
    for i in range(len(calificaciones)):
        numero=0
        for j in range(len(calificaciones[i])):
            numero += calificaciones[i][j]
        total=numero/3
        promedios.append(total)
    return promedios

promedios = sacar_promedio(calificaciones)

def ordenar_segun_promedios(estudiantes:list, promedios:list, calificaciones:list):
    #ordena los estudiantes y sus calificaciones segun los promedios del mas alto al mas bajo, luego muestra como quedo
    for i in range(len(promedios)-1):
        for j in range(i+1,len(promedios)):
            if promedios[i] < promedios[j]:
                aux = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux

                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux

                aux = calificaciones[i]
                calificaciones[i] = calificaciones[j]
                calificaciones[j] = aux
    
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]} -> promedio: {promedios[i]}, calificaciones: {calificaciones[i]}")



def buscar_estudiante(estudiantes: list, calificaciones: list):
    #pide el nombre del estudiante y lo valida, luego recorre la lista de estudiantes para encontar la posicion  y muestra sus calificaciones
    nombre = input("Ingrese nombre del estudiante (Ana, Bruno, Carla, Diego): ").capitalize()
    while nombre != "Ana" and nombre != "Bruno" and nombre != "Carla" and nombre != "Diego":
        nombre = input("Ingrese un estudiante válido Ana, Bruno, Carla, Diego: ").capitalize()

    numero = 0
    for i in range(len(estudiantes)):
        if nombre == estudiantes[i]:
            numero = i

    print(f"Las calificaciones del estudiante {estudiantes[numero]} son: {calificaciones[numero]}")


def buscar_calificacion(estudiantes:list, calificaciones:list):
    #pide la nota que esta buscando y la valida, luego recorre calificaciones y si esta muestra a quien pertenece y a que materia
    nota=int(input("ingrese la calificacion entre 1-10: "))
    while nota < 1 or nota > 10:
        nota=int(input("vuelva a ingresar la calificacion entre 1-10: "))

    materias = ["matematica", "historia", "biologia"]
    encontrado = False

    for i in range(len(calificaciones)):
        for j in range(len(calificaciones[i])):
            if nota == calificaciones[i][j]:
                print(f"Nota encontrada: {nota} -> Estudiante: {estudiantes[i]}, Materia: {materias[j]}")
                encontrado = True

    if encontrado == False:
        print("no hay estudiantes con esa nota...")
