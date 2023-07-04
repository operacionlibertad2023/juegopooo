import pygame
import sys

pygame.init()

# VARIABLES #

# variables de pantalla
W, H = 1900, 1080
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mi juego")
icono = pygame.image.load('D:/pyton/imagenes/principal/icon.png')
pygame.display.set_icon(icono)

# variables bucle while
ejecuta = True

# carga el archivo de sonido de caminar
sonido_caminar = pygame.mixer.Sound('sonido/pasos.mp3')

# sonido principal del juego
bajar_sonido = pygame.image.load('imagenes/principal/icon.png')
subir_sonido = pygame.image.load('imagenes/principal/icon.png')
mute_sonido = pygame.image.load('D:/pyton/imagenes/principal/mute1.png')
max_sonido = pygame.image.load('imagenes/principal/icon.png')

# variables para el jugador
ancho = 50
alto = 50
px = 50
py = 200
velocidad = 5
izquierda = False
derecha = False

# Pone música
pygame.mixer.music.load('sonido/prueba 2.mp3')
pygame.mixer.music.play(-1)

# Carga la imagen del jugador
jugador_img = pygame.image.load("D:/pyton/imagenes/personajes/personaje1.png")

## MENU PRINCIPAL ##
menu_fondo = pygame.image.load("D:/pyton/imagenes/principal/menu_fondo.jpg").convert()
boton_jugar = pygame.image.load("D:/pyton/imagenes/menu-botones/jugar.png").convert()
boton_salir = pygame.image.load("D:/pyton/imagenes/menu-botones/salir.png").convert()


while ejecuta:
    pantalla_activa = 'menu'
    if pantalla_activa == 'menu':
        # dibujar el menú principal
        PANTALLA.blit(menu_fondo, (0, 0))
        PANTALLA.blit(boton_jugar, (600, 400))
        PANTALLA.blit(boton_salir, (600, 500))

        # detectar eventos del menú principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 600 < mouse_pos[0] < 1000 and 400 < mouse_pos[1] < 500:
                    pantalla_activa = 'juego'
                elif 600 < mouse_pos[0] < 1000 and 500 < mouse_pos[1] < 600:
                    ejecuta = False
    elif pantalla_activa == 'juego':
        # Bucle del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecuta = False

            # Opción tecla pulsada
            keys = pygame.key.get_pressed()

            ## CONTROLES SONIDO ##

            # Baja volumen
            if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.0000001)
                PANTALLA.blit(bajar_sonido, (850, 25))
            elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
                PANTALLA.blit(mute_sonido, (850, 25))
        
            # Sube volumen
        if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() +0.01)
            PANTALLA.blit(subir_sonido, (850, 25))
        elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            PANTALLA.blit(max_sonido, (850, 25))

        # Desactivar sonido
        elif keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
            PANTALLA.blit(mute_sonido, (850, 25))
        elif keys[pygame.K_COMMA]:
            pygame.mixer.music.set_volume(1.0)
            PANTALLA.blit(max_sonido, (850, 25))

                ##CONTROLES JUGADOR##

            # mover al jugador hacia la izquierda
        if keys[pygame.K_a] and px > velocidad:
            px -= velocidad
            izquierda = True
            derecha = False
            # reproduce el sonido de caminar hacia la izquierda
            sonido_caminar.play()

        # mover al jugador hacia la derecha
        elif keys[pygame.K_d] and px < 1920 - velocidad - ancho:
            px += velocidad
            izquierda = False
            derecha = True
            # reproduce el sonido de caminar hacia la izquierda
            sonido_caminar.play()

        # jugador quieto
        else:
            izquierda = False
            derecha = False

        # mover al jugador hacia arriba
        if keys[pygame.K_w] and py > 0:
            py -= velocidad
            # reproduce el sonido de caminar hacia la izquierda
            sonido_caminar.play()

        # mover al jugador hacia abajo
        if keys[pygame.K_s] and py < 1030:
            py += velocidad
            # reproduce el sonido de caminar hacia la izquierda
            sonido_caminar.play()

        # dibuja la imagen del jugador en la pantalla
        PANTALLA.fill((255, 255, 255))
        PANTALLA.blit(jugador_img, (px, py))
        
        # actualización de la ventana
pygame.display.update()

    # cierra el programa
pygame.quit()
sys.exit()