import pygame,sys
# FPS
fps = 60

# Tamaño_Pantalla
Ancho = 600
Alto = 600

# Colores
Blanco = (255,255,255)
Negro= (0,0,0)
Azul = (108, 124, 230)
#Permite que los enemigos se muevan
Recorido_X= True 
Recorido_Y= True 
CambiarEje = False

# Clase enemigo
class enemigo(pygame.sprite.Sprite):   
    # Datos a introducir
    def __init__ (self, PosGuard_X, PosGuard_Y, Desde_X, Hasta_X, Desde_Y, Hasta_Y, A):
        
        # De donde (A) hasta donde (B) se movera en x
        self.Desde_X = Desde_X
        self.Hasta_X = Hasta_X
        self.Desde_Y = Desde_Y
        self.Hasta_Y = Hasta_Y
        self.A = A


        # Creacion del enemigo
        super().__init__()
        self.image = pygame.image.load("\imagenes\personajes\guardias\Guardia.png").convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        
        # Posicion inicial del guardia (La cual sera la introducida en la parte de arriba donde estan los datos a introducir)
        self.PosGuard_X = PosGuard_X
        self.PosGuard_Y = PosGuard_Y
        self.rect.center = (PosGuard_X,PosGuard_Y)
    
    # Movimiento del enemigo 
    def update(self):
        global Recorido_X
        global Recorido_Y
        global CambiarEje  
        
        if self.A == 1:
         # Ir
         if CambiarEje == False:
          if Recorido_X == False:
           self.rect.x += 1
           if self.rect.x >= self.Hasta_X:
             Recorido_X = True
        
          # Volver
          if Recorido_X == True:
           self.rect.x -= 1
           if self.rect.x <= self.Desde_X:
             Recorido_X = False 
        

        if self.A == 2:

        # Ir
         if Recorido_Y == False:
          self.rect.y += 1
          if self.rect.y >= self.Hasta_Y:
            Recorido_Y = True
       
        # Volver
         if Recorido_Y == True:
          self.rect.y -= 1
          if self.rect.y <= self.Desde_Y:
            Recorido_Y = False   

          

# Pantalla
pygame.init()
pantalla = pygame.display.set_mode((Ancho,Alto))
pygame.display.set_caption("Codigo Guardia")
# Reloj
clock =pygame.time.Clock()

# Se crea el grupo Guardias donde irian todos los guardias, se crea Guardia1, y se lo agrega a el grupo Guardias)
Guardias = pygame.sprite.Group()
Guardias1 = enemigo (200,200,50,80,40,300,1)
self = enemigo(300,300, 100, 500, 10,200, 2)
Guardias.add(self,Guardias1)


# ___________________Bucle_______________
Ejecutando = True
while Ejecutando:
     clock.tick(fps)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             Ejecutando = False
     
     # color de fondo 
     pantalla.fill ("white")     
     # Ejecuta el movimiento de el grupo guardias
     Guardias.update()
      

     # Colocar todo lo que este en el grupo guardias a la pantalla
     Guardias.draw(pantalla)
     

     pygame.display.update()

 
#_________________Fin_____________________
pygame.quit