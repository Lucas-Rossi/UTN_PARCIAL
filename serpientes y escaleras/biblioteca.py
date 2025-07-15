from preguntas import *
import random

def preguntar_nombre()->str:
    #pregunta el nombre con un input y lo guarda en una variable para luego retornarlo
    nombre = input("ingrese un nombre: ")
    print("bienvenido! ",nombre)
    return nombre

def preguntar_si_quiere_jugar(nombre:str)->str:
    #le da el valor a una variable seguir en "s" luego pregunta si quiere jugar con un input y guarda el valor en la misma variable seguir y lo retorna
    seguir = "s"
    seguir = input("quiere jugar? s/n: ")
    if seguir == "n":
        print("muchas gracias por jugar! ",nombre)
    return seguir

def generar_numero_aleatorio()->int:
    #usa el modulo random y genera un numero entre 0 y 14 y lo retorna
    numero = random.randint(0,14)
    return numero

def hacer_pregunta_motrar_respuestas(numero:int):
    #muestra la pregunt y las opciones para responder
    print(preguntas[numero]["pregunta"])
    print("opcion a: ",preguntas[numero]["respuesta_a"])
    print("opcion b: ",preguntas[numero]["respuesta_b"])
    print("opcion c: ",preguntas[numero]["respuesta_c"])

def validar_opcion()->str:
    #pide ingresar una opcion y la valida, luego la retorna
    opcion = input("respuesta: a / b / c: ")
    while opcion != "a" and opcion != "b" and opcion != "c":
        opcion = input("opcion invalida, seleccione respuesta: a / b / c: ")
    return opcion

def verificar_respuesta(numero:int,opcion:str)->bool:
    #con un condcicional verifica si la respuesta es la misma que la respuesta correcta y si es asi guarda True en una variable , caso contrario guarda False, y lo retorna
    respuesta = False
    
    if opcion == preguntas[numero]["respuesta_correcta"]:
        respuesta = True
        print(" respuesta correcta! ")
    else:
        respuesta = False
        print(" respuesta incorrecta! ")
    return respuesta

def avanzar_ubicacion(posicion:int, tablero:list)->int:
    # se le suma a posicion 1 y el elemento que haya en en esa posicion 
    posicion += 1
    print("avanzaste a la posicion: ", posicion)
    if tablero[posicion] > 0:
        print("escalones extras avanzados: ", tablero[posicion])
        posicion += tablero[posicion]
    return posicion

def retoceder_ubicacion(posicion:int, tablero:list)->int:
    # se le resta a posicion 1 y el elemento que haya en en esa posicion 
    posicion -= 1
    print("retrocediste a la posicion: ", posicion)
    if tablero[posicion] > 0:
        print(" escalones extras retrocedidos: ", tablero[posicion])
        posicion -= tablero[posicion]
    return posicion

def verificar_posicion(posicion:int, nombre:str)->bool:
    # verifica que la posicion sea 0 o 30 y si es asi retorna true
    flag = True
    if posicion == 0:
        print("perdiste! ", nombre)
    elif posicion == 30:
        print("ganaste! ", nombre)
    else:
        flag = False    
    return flag

def revisar_preguntas(lista_contador:list)->bool:
    #recorre la lista de contadores y si son todos 1 devuelve false ya que no hay mas preguntas, si hay algun 0 devuelve true ya que quedan preguntas
    preguntas_existentes = False
    for i in lista_contador:
        if i == 0:
            preguntas_existentes = True
    return preguntas_existentes

def guardar_puntaje(nombre: str, posicion: int):
    #guarda el nombre y posicion en un archivo csv
    with open("score.csv", "a") as archivo:
        archivo.write(f"{nombre},{posicion}\n")