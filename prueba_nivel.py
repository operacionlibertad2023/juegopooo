import pygame
import sys
from nivel import Nivel
pygame.init()
W, H = 800,800
PANTALLA = pygame.display.set_mode((W, H))
icono = pygame.image.load('imagenes\principal\icon.png')
pygame.display.set_caption("Operacion")
BG = (50, 50, 50)
nivel = Nivel()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        nivel.corre()
        pygame.display.update()