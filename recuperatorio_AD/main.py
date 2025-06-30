from biblioteca import *

seguir = "s"
while seguir == "s":
    print("""
    --- MENÚ ---
    1. Mostrar estudiantes y calificaciones
    2. Mostrar estudiantes ordenados por promedio
    3. Buscar calificaciones de un estudiante
    4. Buscar estudiantes por calificación
    5. Salir
    """)
    opcion = int(input("Elija una opción 1-5: "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("vuelva a elejir una opción 1-5: "))

    if opcion == 1:
        mostrar_estudiantes_calificaciones(estudiantes, calificaciones)
    elif opcion == 2:
        ordenar_segun_promedios(estudiantes, promedios, calificaciones)
    elif opcion == 3:
        buscar_estudiante(estudiantes, calificaciones)
    elif opcion == 4:
        buscar_calificacion(estudiantes, calificaciones)
    elif opcion == 5:
        print("Fin del programa")
        seguir= "n"
    