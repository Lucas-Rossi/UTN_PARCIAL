import pygame
from biblioteca_pygame import *
from preguntas import *

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego Serpientes y Escaleras")

imagen_puntaje = pygame.image.load("imagen_puntaje.png")
imagen_puntaje = pygame.transform.scale(imagen_puntaje,(200,60))

imagen_jugar= pygame.image.load("imagen_jugar.png")
imagen_jugar = pygame.transform.scale(imagen_jugar,(200,60))

imagen_salir = pygame.image.load("imagen_salir.png")
imagen_salir = pygame.transform.scale(imagen_salir,(200,60))

imagen_tablero = pygame.image.load("imagen_tablero.png")
imagen_tablero = pygame.transform.scale(imagen_tablero,(1450,150))

posicion_puntaje = (650, 150)
posicion_jugar = (650, 250)
posicion_salir = (650, 350)

boton_puntaje = pygame.Rect(650, 150, 200, 60)
boton_jugar = pygame.Rect(650, 250, 200, 60)
boton_salir = pygame.Rect(650, 350, 200, 60)

lista_contador = [0] * len(preguntas)
posicion = 15  
tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]

pygame.mixer.music.load("musica_pygame.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

modo = "menu"
dijo_nombre = False
mostrando_pregunta = False
flag_correr = True
puntaje_guardado = False
while flag_correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            if puntaje_guardado == False:
                guardar_puntaje(nombre_jugador, posicion)
                puntaje_guardado = True
            flag_correr = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                modo = "menu"

        if modo == "menu":
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = evento.pos

                if boton_puntaje.collidepoint(posicion_click):
                    print("Hiciste clic en Puntaje", posicion_click)
                    modo = "puntaje"

                if boton_jugar.collidepoint(posicion_click):
                    posicion = 15
                    lista_contador = [0] * len(preguntas)
                    dijo_nombre = False
                    nombre_jugador = ""
                    nombre_jugador = pedir_nombre(pantalla)
                    dijo_nombre = True
                    print("Nombre ingresado:", nombre_jugador)
                    modo = "juego"

                if boton_salir.collidepoint(posicion_click):
                    print("Hiciste clic en Salir", posicion_click)
                    if puntaje_guardado == False:
                        guardar_puntaje(nombre_jugador, posicion)
                        puntaje_guardado = True
                    flag_correr = False

        elif modo == "juego":
            gano_perdio = verificar_posicion(posicion,nombre_jugador)

            if gano_perdio == True:
                print("llego al final del tablero")
                modo = "puntaje"
                
            existen_preguntas = revisar_preguntas(lista_contador)
            if existen_preguntas == True:
                numero_pregunta = generar_numero_aleatorio(lista_contador)
                modo = "pregunta"
                
            else: 
                print("no hay mas preguntas")
                if puntaje_guardado == False:
                    guardar_puntaje(nombre_jugador, posicion)
                    puntaje_guardado = True
                modo = "puntaje"

        elif modo == "pregunta":
            resultado_pregunta = mostrar_pregunta_verificar(pantalla, preguntas, numero_pregunta, imagen_tablero, coordenadas_casillas, posicion)

            if resultado_pregunta == True:
                posicion = avanzar_ubicacion(posicion, tablero)
                print("¡Respuesta correcta! Avanzás a la posición", posicion)
            else:
                posicion = retoceder_ubicacion(posicion, tablero)
                print("Respuesta incorrecta. Retrocedés a la posición", posicion)

            if posicion == 0:
                print("Llegaste a la posición 0, perdiste!")
                if puntaje_guardado == False:
                    guardar_puntaje(nombre_jugador, posicion)
                    puntaje_guardado = True
                modo = "puntaje"
            elif posicion == 30:
                print("Llegaste a la posición 30, ganaste!")
                if puntaje_guardado == False:
                    guardar_puntaje(nombre_jugador, posicion)
                    puntaje_guardado = True
                modo = "puntaje"
            else:
                modo = "juego"

    pantalla.fill(WHITE)

    if modo == "menu":
        pantalla.blit(imagen_puntaje, posicion_puntaje)
        pantalla.blit(imagen_jugar, posicion_jugar)
        pantalla.blit(imagen_salir, posicion_salir)

    if modo == "juego" or modo == "pregunta":
        pantalla.blit(imagen_tablero, (25, 420))
        x = coordenadas_casillas[posicion][0]
        y = coordenadas_casillas[posicion][1]
        pygame.draw.circle(pantalla, GREEN, (x, y), 10)

    if modo == "puntaje":
        mostrar_puntajes(pantalla)
        
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()