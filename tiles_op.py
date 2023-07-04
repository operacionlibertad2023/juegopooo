import pygame
import mapa_op

class tile(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('imagenes\mapa\paredes.png')
        self.rect = self.image.get_rect(topleft = pos)
class personaje(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('imagenes\personaje\personaje1.png')
        self.rect = self.image.get_rect(topleft = pos)
        