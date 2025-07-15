from biblioteca import *
from preguntas import *

tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
lista_contador =[0]*len(preguntas)
posicion = 15

nombre = preguntar_nombre()
jugar = preguntar_si_quiere_jugar(nombre)

while jugar == "s":

    numero = generar_numero_aleatorio()
    
    while lista_contador[numero] == 1:
        numero = generar_numero_aleatorio()
        if revisar_preguntas(lista_contador) == False:
            jugar = "n"
            print("No quedan más preguntas.")
            break
    lista_contador[numero] = 1

    hacer_pregunta_motrar_respuestas(numero)

    opcion = validar_opcion()
    respuesta = verificar_respuesta(numero,opcion)
    if respuesta == True:
        posicion = avanzar_ubicacion(posicion, tablero)
    elif respuesta == False:
        posicion = retoceder_ubicacion(posicion, tablero)
    print("posicion actual: ",posicion)
    
    fin_del_tablero = verificar_posicion(posicion,nombre)
    if  fin_del_tablero == True:
        jugar = "n"
    elif fin_del_tablero == False:
        jugar = preguntar_si_quiere_jugar(nombre)

guardar_puntaje(nombre,posicion)