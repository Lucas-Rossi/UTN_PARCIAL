import pygame
import random
from colores import *

ANCHO_VENTANA = 1500
ALTO_VENTANA = 600

coordenadas_casillas = [
    (50, 500), (95, 500), (145, 500), (190, 500), (240, 500), 
    (285, 500), (335, 500), (380, 500), (430, 500), (460, 500),
    (510, 500), (555, 500), (605, 500), (650, 500), (700, 500),
    (745, 500), (790, 500), (840, 500), (885, 500), (935, 500),
    (980, 500), (1025, 500), (1075, 500), (1120, 500), (1170, 500),
    (1215, 500), (1265, 500), (1310, 500), (1360, 500), (1405, 500),
    (1455, 500)
    ]
def pedir_nombre(pantalla):
    #pide el nombre del usuario y lo retorna, muestra una caja para que el usuario ingree el nombre
    font_input = pygame.font.SysFont("Arial", 30)
    ingreso = ""
    ingreso_rect = pygame.Rect(100,200,300,40)

    flag_correr = True
    while flag_correr:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_correr = False
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[:-1]
                elif evento.key == pygame.K_RETURN and ingreso != "":
                    flag_correr = False
                    return ingreso
                else:
                    ingreso += evento.unicode
        
        pantalla.fill(WHITE)
        pygame.draw.rect(pantalla, BLACK, ingreso_rect , 2)
        texto = font_input.render("Ingrese su nombre:", True, BLACK)
        ingreso_surface = font_input.render(ingreso, True, BLACK) 
        pantalla.blit(texto, (100, 150))
        pantalla.blit(ingreso_surface, ( ingreso_rect.x+5 , ingreso_rect.y + 5 ))
        pygame.display.flip()

def generar_numero_aleatorio(lista_contador:list)->int:
    #genera un numero random y se fija en la lista que se pasa como parametro que en laposicion de ese numero se ponga 1 y e retoorna el numero generado
    while True:
        numero = random.randint(0, len(lista_contador) - 1)
        if lista_contador[numero] == 0:
            lista_contador[numero] = 1
            return numero

def mostrar_pregunta_verificar(pantalla, preguntas, numero_pregunta, imagen_tablero, coordenadas_casillas, posicion):
    #pone la preguntas y opciones en la pantalla, tambien pone el tablero y modifica la posicion en el
    fuente = pygame.font.SysFont("Arial", 24)
    pregunta = preguntas[numero_pregunta]

    rect_a = pygame.Rect(100, 200, 1000, 40)
    rect_b = pygame.Rect(100, 260, 1000, 40)
    rect_c = pygame.Rect(100, 320, 1000, 40)
    
    tiempo_limite = 10  
    tiempo_inicial = pygame.time.get_ticks()
    flag_correr = True
    while flag_correr:
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = tiempo_limite - (tiempo_actual - tiempo_inicial) // 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_correr = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_a.collidepoint(evento.pos):
                    return pregunta["respuesta_correcta"] == "a"
                
                elif rect_b.collidepoint(evento.pos):
                    return pregunta["respuesta_correcta"] == "b"
                
                elif rect_c.collidepoint(evento.pos):
                    return pregunta["respuesta_correcta"] == "c"
                
        if tiempo_restante <= 0:
            print("Tiempo agotado.")
            return False
        
        pantalla.fill(WHITE)
        pantalla.blit(imagen_tablero, (25, 420))
        x = coordenadas_casillas[posicion][0]
        y = coordenadas_casillas[posicion][1]
        pygame.draw.circle(pantalla, GREEN, (x, y), 10)

        texto_pregunta = fuente.render(pregunta["pregunta"], True, (0, 0, 0))
        texto_a = fuente.render("A) " + pregunta["respuesta_a"], True, (0, 0, 255))
        texto_b = fuente.render("B) " + pregunta["respuesta_b"], True, (0, 0, 255))
        texto_c = fuente.render("C) " + pregunta["respuesta_c"], True, (0, 0, 255))
        texto_timer = fuente.render(f"Tiempo restante: {tiempo_restante}s", True, (255, 0, 0))

        pantalla.blit(texto_pregunta, (100, 100))
        pantalla.blit(texto_a, (100, 200))
        pantalla.blit(texto_b, (100, 260))
        pantalla.blit(texto_c, (100, 320))
        pantalla.blit(texto_timer, (100, 50))

        pygame.draw.rect(pantalla, BLUE, rect_a, 2)
        pygame.draw.rect(pantalla, BLUE, rect_b, 2)
        pygame.draw.rect(pantalla, BLUE, rect_c, 2)
        pygame.display.flip()
    
def revisar_preguntas(lista_contador:list)->bool:
    #recorre la lista de contadores y si son todos 1 devuelve false ya que no hay mas preguntas, si hay algun 0 devuelve true ya que quedan preguntas
    preguntas_existentes = False
    for i in lista_contador:
        if i == 0:
            preguntas_existentes = True
    return preguntas_existentes


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

def avanzar_ubicacion(posicion:int, tablero:list)->int:
    # se le suma a posicion 1 y el elemento que haya en en esa posicion 
    posicion += 1
    if tablero[posicion] > 0:   
        posicion += tablero[posicion]
    return posicion

def retoceder_ubicacion(posicion:int, tablero:list)->int:
    # se le resta a posicion 1 y el elemento que haya en en esa posicion 
    posicion -= 1
    if tablero[posicion] > 0:
        posicion -= tablero[posicion]
    return posicion

def guardar_puntaje(nombre: str, posicion: int):
    #guarda el nombre y posicion en un archivo csv
    with open("score.csv", "a") as archivo:
        archivo.write(f"{nombre}, {posicion}\n")


def mostrar_puntajes(pantalla):
    #lee el archivo donde estan los puntajes y los ordena ascendentemente
    with open("score.csv", "r") as archivo:
        lineas = archivo.readlines()

    lista_nombres = []
    lista_puntajes = []

    for linea in lineas:
        nombre, puntaje = linea.strip().split(",")
        lista_nombres.append(nombre.strip())
        lista_puntajes.append(int(puntaje.strip()))  

    for i in range(len(lista_puntajes) - 1):
        for j in range(i + 1, len(lista_puntajes)):
            if lista_puntajes[i] > lista_puntajes[j]:
                aux = lista_puntajes[i]
                lista_puntajes[i] = lista_puntajes[j]
                lista_puntajes[j] = aux

                aux = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = aux
    fuente = pygame.font.SysFont("Arial", 28)
    y = 100
    titulo = fuente.render("Ranking de Puntajes", True, BLACK)
    pantalla.blit(titulo, (100, 50))

    for i in range(len(lista_nombres)):
        texto = fuente.render(f"{lista_nombres[i]}: {lista_puntajes[i]}", True, BLACK)
        pantalla.blit(texto, (100, y))
        y += 40

    mensaje = fuente.render("Presioná ESC para volver al menú", True, (100, 100, 100))
    pantalla.blit(mensaje, (100, y + 20))





    