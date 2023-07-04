import pygame
import Mapa_Zelda

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("17.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
class tile_izquierda(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("9.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
class tile_abajo(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("1.png")
        self.rect = self.image.get_rect(topleft = pos)


class piso(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("pisof.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso1(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("pisof-1.png")
        self.rect = self.image.get_rect(topleft = pos)
        

class tile_arriba(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("20.png")
        self.rect = self.image.get_rect(topleft = pos)

class tile_esquinaa(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("7.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class tile_esquinab(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("10.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class tile_puerta(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("targeta_y_puertas.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class tile_puerta2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("puerta.png")
        self.rect = self.image.get_rect(topleft = pos)        
class tile_esquina2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("7 _2.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class tile_esquina3(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load("10 _2.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class puerta(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("puertas/3.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class puerta2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("puertas/3-1.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class puerta3(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("puertas/3-2.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_1(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso1.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_1f(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso1f.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso2.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_3(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso3.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_4(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso4.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_5(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso5.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_6(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso6.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_7(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso7.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class piso_8(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("piso8.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class esquinas_1(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquinas_1.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
class esquinas_2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquinas_4.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
class esquinas_3(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquinas_3.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
class esquinas_4(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquinas_10 .png")
        self.rect = self.image.get_rect(topleft = pos)
        
        
        
class esquinas_5(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquina10.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class esquinas_6(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquina11.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class esquinas_7(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("esquina12.png")
        self.rect = self.image.get_rect(topleft = pos)



        
class pared_1(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("4.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_2(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("5.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_3(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("21.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_4(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("25.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_5(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("26.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_6(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("27.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_7(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("22.png")
        self.rect = self.image.get_rect(topleft = pos)

        
class pared_8(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("28.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class cama(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
            
        self.image = pygame.image.load("cama.png")
        self.rect = self.image.get_rect(topleft = pos)
        