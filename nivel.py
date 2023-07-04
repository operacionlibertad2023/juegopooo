import pygame
from tiles_op import tile
from tiles_op import personaje
import mapa_op
class Nivel: 
 def __init__ (self): 
  self.pantalla = pygame.display.get_surface()
  self.sprits_fondo = pygame.sprite.Group()
  self.obtaculos = pygame.sprite.Group()
  self.muros = pygame.sprite.Group()
  self.creacion_de_mapa()


 def creacion_de_mapa(self):
   
   for row_index, row in enumerate(mapa_op.mapa):
     for col_index, col in enumerate (row):
      x = col_index * 64
      y = row_index * 64
      if col == "x":
       tile((x,y),[self.sprits_fondo, self.obtaculos,])
       if col == "m":
         personaje ((x,y),[self.sprits_fondo])
 def corre (self):
  self.sprits_fondo.draw(self.screen)