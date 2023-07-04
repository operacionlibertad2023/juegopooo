import pygame
import sys
from Button import Button


pygame.init()

W, H = 1920, 1080
PANTALLA = pygame.display.set_mode((W, H))
icono = pygame.image.load('imagenes\principal\icon.png')
pygame.display.set_caption("Operacion")
BG = (50, 50, 50)
    #Permite que los enemigos se muevan
    
Recorido_X= True 
Recorido_Y= True 
CambiarEje = False

def fuentes(size):
    return pygame.font.Font("imagenes\menu-botones\principal-fuente.ttf", size)

def juego():
    # carga el archivo de sonido de caminar
    sonido_caminar = pygame.mixer.Sound('sonido/pasos2.mp3')

    #sonido principal juego
    bajar_sonido = pygame.image.load('imagenes\principal\icon.png')
    subir_sonido = pygame.image.load('imagenes\principal\icon.png')
    mute_sonido = pygame.image.load('imagenes\principal\mute1.png')
    max_sonido = pygame.image.load('imagenes\principal\icon.png')

    # variables para el jugador
    ancho = 50
    alto = 50
    px = 50
    py = 200
    velocidad = 5
    izquierda = False
    derecha = False
    juego_pausado = False
    juego_reanudado = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            ##CONTROLES SONIDO##

        # Carga la imagen del jugador
        jugador_img = pygame.image.load("imagenes\personajes\personaje1.png")
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        # Baja volumen
        if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -0.0000001)
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
        pygame.display.update()