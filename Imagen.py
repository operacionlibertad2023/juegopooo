import pygame, sys

# Colores
Blanco = (255,255,255)
Negro= (0,0,0)
Azul = (108, 124, 230)

pygame.init()

# El boton que aparece ariba de los objetos E
Letra_E = pygame.image.load("E.png")
Letra_E = pygame.transform.scale(Letra_E,(50,50)) # Tamaño de la imagen

eje_x = 0
posicion_x = 0


pantalla = pygame.display.set_mode((500, 400))
pygame.display.set_caption("xddd")

Perdiste = False

Ejecutando = True
while Ejecutando:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             Ejecutando = False
		
     pantalla.fill(Azul)

     if Perdiste == False:
         
         tecla = pygame.key.get_pressed()
         if tecla[pygame.K_e]:
           Perdiste = True
     else:
         pygame.draw.rect(pantalla, Blanco, (200,200,200,200))
        

     pygame.display.update()