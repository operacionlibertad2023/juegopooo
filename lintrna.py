import pygame,sys
fps = 60
clock = pygame.time.Clock()
ancho = 600
alto = 600

pantalla = pygame.display.set_mode((ancho,alto))
Ejecutando = True
while Ejecutando:
     clock.tick(fps)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             Ejecutando = False
     
     # color de fondo 
     pantalla.fill ("white") 
     
     pygame.display.update()
#_________________Fin_____________________
pygame.quit