import pygame
import sys
from Button import Button
from Zelda_Juego import *


pygame.init()

W, H = 1280, 720
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
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1366,768))
        pygame.display.set_caption("Zelda")
        self.nivel = Nivel()
        
    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                        
            self.screen.fill("black")
            self.nivel.corre()
            pygame.display.update()

    if __name__ == "__main__":
        zelda_juego = Zelda()
        zelda_juego.corre_juego()
        # actualización de la ventana
        pygame.display.update()
        
def pausa():
    while True:
        PANTALLA.fill((54, 211, 238))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

                #crea boton para reanudar en el menu de pausa
        REANUDAR_BTN = Button(image=pygame.image.load("imagenes\menu-botones\Options Rect.png"), pos=(960, 119),
                            text_input="REANUDAR", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")
        
                #crea boton para los ajustes en el menu de pausa
        AJUSTES_BTN = Button(image=pygame.image.load("imagenes\menu-botones\Options Rect.png"), pos=(960, 358),
                            text_input="AJUSTES", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")
        
                #crea boton para volver al menu principal
        VOLVER_BTN = Button(image=pygame.image.load("imagenes\menu-botones\Quit Rect.png"), pos=(960, 597),
                            text_input="MENU", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")
        
                #crea boton para salir al escritorio
        DESK_BTN = Button(image=pygame.image.load("imagenes\menu-botones\Options Rect.png"), pos=(960, 836),
                            text_input="SALIR", font=fuentes(70), base_color="#d7fcd4", hovering_color="White")

        for button in [REANUDAR_BTN, AJUSTES_BTN, VOLVER_BTN, DESK_BTN]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # cuando toque el boton reanudar vuelve al juego
                if REANUDAR_BTN.checkForInput(MENU_MOUSE_POS):
                    juego()

                # cuando toque el boton ajuste abre l ventana ajustes
                if AJUSTES_BTN.checkForInput(MENU_MOUSE_POS):
                    pausa_ajustes()

                # cuando toque el boton volver vuelve al menu principal
                if VOLVER_BTN.checkForInput(MENU_MOUSE_POS):
                    main_menu()

                # regresa al escritorio y sale del programa
                if DESK_BTN.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # actualiza pantalla
        pygame.display.update()

def pausa_ajustes():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("white")

        OPTIONS_TEXT = fuentes(45).render("aguamte el lol", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(960, 260))
        PANTALLA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(960, 460),
                            text_input="BACK", font=fuentes(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pausa()

        pygame.display.update()


def ajustes():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        PANTALLA.fill("white")

        OPTIONS_TEXT = fuentes(45).render("aguamte el lol", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(960, 260))
        PANTALLA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(960, 460),
                            text_input="BACK", font=fuentes(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    # Pone música
    pygame.mixer.music.load('sonido\musica-fondo.mp3')
    pygame.mixer.music.play(-1)
    while True:
        PANTALLA.fill(BG)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuentes(70).render("Operacion Libertad", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(560, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("imagenes\menu-botones\Play Rect.png"), pos=(560, 216),
                            text_input="JUGAR", font=fuentes(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("imagenes\menu-botones\Options Rect.png"), pos=(560, 455),
                            text_input="AJUSTES", font=fuentes(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("imagenes\menu-botones\Quit Rect.png"), pos=(560, 694),
                            text_input="SALIR", font=fuentes(60), base_color="#d7fcd4", hovering_color="White")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    juego()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ajustes()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
# cierra el programa
pygame.quit()
sys.exit()
