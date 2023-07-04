import pygame
import Mapa_Zelda
from Tile_Zelda import Tile 
from Tile_Zelda import tile_abajo
from Tile_Zelda import tile_izquierda
from Tile_Zelda import tile_arriba
from Tile_Zelda import tile_esquinaa
from Tile_Zelda import tile_esquina2
from Tile_Zelda import tile_esquina3
from Tile_Zelda import tile_esquinab
from Tile_Zelda import tile_puerta
from Tile_Zelda import tile_puerta2
from Tile_Zelda import puerta
from Tile_Zelda import puerta2
from Tile_Zelda import puerta3
from Link import Link
from Tile_Zelda import piso
from Tile_Zelda import piso1
from Tile_Zelda import piso_1
from Tile_Zelda import piso_1f
from Tile_Zelda import piso_2
from Tile_Zelda import piso_3
from Tile_Zelda import piso_4
from Tile_Zelda import piso_5
from Tile_Zelda import piso_6
from Tile_Zelda import piso_7
from Tile_Zelda import piso_8
from Tile_Zelda import esquinas_1
from Tile_Zelda import esquinas_2
from Tile_Zelda import esquinas_3
from Tile_Zelda import esquinas_4
from Tile_Zelda import esquinas_5
from Tile_Zelda import esquinas_6
from Tile_Zelda import esquinas_7
from Tile_Zelda import pared_1
from Tile_Zelda import pared_2
from Tile_Zelda import pared_3
from Tile_Zelda import pared_4
from Tile_Zelda import pared_5
from Tile_Zelda import pared_6
from Tile_Zelda import pared_7
from Tile_Zelda import pared_8
from Tile_Zelda import cama
class Nivel:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.Sprites_deFondo = YGrupoCamara()
        self.Obstaculos = pygame.sprite.Group()
        self.piso = YGrupoCamara()
        
        self.crearMapa()
        
    def crearMapa(self):
        for row_index, row in enumerate (Mapa_Zelda.mapa):
            for col_index, col in enumerate(row):
                x = col_index * 32
                y = row_index * 32
                if col == "x":
                    Tile((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "L":
                    self.Link = Link((x,y), [self.Sprites_deFondo], self.Obstaculos)
                if col == "p":
                    piso((x,y), [self.piso])
                if col == "z":
                    tile_izquierda((x,y), [self.Sprites_deFondo, self.Obstaculos])  
                if col == "a":
                    tile_arriba((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "j":
                    tile_abajo((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "e":
                    tile_esquinaa((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "l":
                    tile_esquinab((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t":
                    tile_puerta((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t2":
                    tile_puerta2((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t3":
                    tile_esquina2((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t4":
                    tile_esquina3((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t5":
                    puerta((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t6":
                    puerta2((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "t7":
                    puerta3((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "p12":
                    piso1((x,y), [self.piso])
                if col == "p1":
                    piso_1((x,y), [self.piso])
                if col == "pf1":
                    piso_1f((x,y), [self.piso])
                if col == "p2":
                    piso_2((x,y), [self.piso])
                if col == "p3":
                    piso_3((x,y), [self.piso])
                if col == "p4":
                    piso_4((x,y), [self.piso])
                if col == "p5":
                    piso_5((x,y), [self.piso])
                if col == "p6":
                    piso_6((x,y), [self.piso])
                if col == "p7":
                    piso_7((x,y), [self.piso])
                if col == "p8":
                    piso_8((x,y), [self.piso])
                if col == "e1":
                    esquinas_1((x,y), [self.piso])
                if col == "e2":
                    esquinas_2((x,y), [self.piso])
                if col == "e3":
                    esquinas_3((x,y), [self.piso])
                if col == "e4":
                    esquinas_4((x,y), [self.piso])
                if col == "e5":
                    esquinas_5((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "e6":
                    esquinas_6((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "e7":
                    esquinas_7((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa1":
                    pared_1((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa2":
                    pared_2((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa3":
                    pared_3((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa4":
                    pared_4((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa5":
                    pared_5((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa6":
                    pared_6((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa7":
                    pared_7((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "pa8":
                    pared_8((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "c":
                    cama((x,y), [self.Sprites_deFondo, self.Obstaculos])
                    
                    
                    
        
    def corre(self):
        self.piso.dibuja(self.Link)
        self.piso.update()
        
        self.Sprites_deFondo.dibuja(self.Link)
        self.Sprites_deFondo.update()
        
class YGrupoCamara(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
    def dibuja(self, Link):
        self.offset.x = Link.rect.centerx - self.half_width
        self.offset.y = Link.rect.centery - self.half_height
        
        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_rect)
            
            