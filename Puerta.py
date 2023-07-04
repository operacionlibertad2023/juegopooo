import pygame, sys

# FPS
fps = 30

# Tamaño_Pantalla
Ancho = 600
Alto = 600

# Colores
Blanco = (255,255,255)
Negro= (0,0,0)
Azul = (108, 124, 230)


# El boton que aparece ariba de los objetos E
Letra_E = pygame.image.load("E.png")
Letra_E = pygame.transform.scale(Letra_E,(50,50)) # Tamaño de la imagen
#____________________________________________


# Jugador de prueva para probar la colicion (A) (Despues cambiad  wrlo por el verdadero)
class jugador_prueba(pygame.sprite.Sprite):
    # Datos a introducir
    def __init__ (self):
        
        # Creacion de el personaje
        super().__init__()
        self.Angulo = 0
        self.image = pygame.image.load("persona.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) # Tamaño
        self.rect = self.image.get_rect()
        self.rect.center=(200,200) # Posicion
    
    # El jugador sigue el maus (me dio fiaca usar flechas (borrar lo del final del xd por si acaso)xddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd puto el que lee (borrar esto xd))
    def update(self):
        self.x,self.y =pygame.mouse.get_pos()
        self.rect.center = (self.x,self.y)
# _________________________________________ (A)


# Clase Llave  (B)                                                                   
class Llave(pygame.sprite.Sprite):                                                
                                                                                       
    # Datos a introducir
    def __init__(self, Llave_X,Llave_Y):
        
        self.Llave_X = Llave_X
        self.Llave_Y = Llave_Y
        self.Agarado = False

        # Creacion de la llave
        super().__init__()
        
        self.image = pygame.image.load("puertas/4.png")
        self.image = pygame.transform.scale(self.image, (37.5, 21)) # Tamaño
        
        self.rect = self.image.get_rect()
        self.rect.center=(100,100) # Posicion
        
    
    # El update 
    def update(self):
     
     self.Colicion_llave = pygame.sprite.spritecollide(Jugador,Llaves,False) # Colicion
     
     if self.Colicion_llave: 
        # Aparece la E
        pantalla.blit(Letra_E, (self.rect.left, self.rect.top - 70)) # La letra aparecera en la posicion de X de la llave y Y de esta menos 70 (despues cambilo por un balor que quede mejor)
        # ____________
        
        # Si se toca la tecla E lo agarra y se elimina
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_e]:
           self.Agarado = True
           self.kill()
        # ____________________________________________

# ____________ (B)


# La clase Escaner (C)
class Escaner(pygame.sprite.Sprite):
   def __init__(self, nombre_Llave, Angulo_Escaner, Escaner_X, Escaner_Y):
      
      self.nombre_Llave = nombre_Llave
      
      self.Angulo_Escaner = Angulo_Escaner
      self.Escaner_X = Escaner_X
      self.Escaner_Y = Escaner_Y
      
      self.Abierto = False

      super().__init__()
      
      
      # Creacion del Escaner ______________________________________________
      self.image = pygame.image.load("puertas/1.png")
      self.image = pygame.transform.scale(self.image, (10,10)) # Tamaño
      self.image = pygame.transform.rotate(self.image,self.Angulo_Escaner)
      
      self.rect = self.image.get_rect()
      self.rect.center = (self.Escaner_X, self.Escaner_Y)
      # ___________________________________________________________________
       
   # El update (Mandarle el mensaje a la puerta que se abra)    
   def update(self):
       
       if self.nombre_Llave.Agarado == True: # Si se agaro la llave
          
          
          self.Colicion_Escaner = pygame.sprite.spritecollide(Jugador,Escaners,False) # Colicion

          # Que aparesca la letra E si se tiene la llave y si ya se abrio que no aparesca _________
          if self.Colicion_Escaner and self.Abierto == False:
             pantalla.blit(Letra_E, (self.rect.left - 20, self.rect.top - 70))
          # _______________________________________________________________________________________    
             
             # Si se preciona la tecla E manda el mensaje _____
             self.tecla = pygame.key.get_pressed()
             if self.tecla[pygame.K_e]:
                self.Abierto = True
                print(self.Abierto)
             # _________________________________________________
# ________________ (C)


# Clase de puertas (D)

class Puerta(pygame.sprite.Sprite):
   def __init__(self, Nombre_Escaner,Angulo_Puerta, Puerta_X,Puerta_Y):
      
      self.Nombre_Escaner = Nombre_Escaner
      
      self.Angulo_Puerta = Angulo_Puerta
      self.Puerta_X = Puerta_X
      self.Puerta_Y = Puerta_Y
      
      # Creacion de la puerta ___________________________________________
      super().__init__()

      self.image = pygame.image.load ("puertas/0.png")
      self.image = pygame.transform.scale(self.image, (50, 50)) # Tamaño
      self.image = pygame.transform.rotate(self.image,self.Angulo_Puerta)
      
      self.rect = self.image.get_rect()
      self.rect.center = (self.Puerta_X,self.Puerta_Y)
      # _________________________________________________________________

   # El update   
   def update(self):
      # Si presionaste E en el escaner con la llave combia de imagen a abierto ___
      if self.Nombre_Escaner.Abierto == True:
         self.image = pygame.image.load ("puertas/2.png")
         self.image = pygame.transform.scale(self.image, (50, 50)) # Tamaño
         self.image = pygame.transform.rotate(self.image,self.Angulo_Puerta)
      # ___________________________________________________________________________
# ________________ (D)



# Jugador
Jugador = jugador_prueba()

# __________________________ Grupos:

# Grupo de las llaves
Llaves = pygame.sprite.Group()
llave1 = Llave(100,100)
Llaves.add(llave1)

# Grupo escaners
Escaners = pygame.sprite.Group()
Escaner1 = Escaner(llave1,0,300,300)
Escaners.add(Escaner1)

# Grupo de puertas
Puertas = pygame.sprite.Group()
Puerta1 = Puerta(Escaner1,0,500,100)
Puertas.add(Puerta1)

#___________________________________


# Pantalla
pygame.init()
pantalla = pygame.display.set_mode((Ancho,Alto))
pygame.display.set_caption("Llave")
# Reloj
clock =pygame.time.Clock()



# ___________________Bucle_______________
Ejecutando = True
while Ejecutando:
     clock.tick(fps)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             Ejecutando = False

   
     # Movimiento jugador de prueba
     Jugador.update()


     # color de fondo 
     pantalla.fill (Blanco)
     
     # ______________ Updates:
     # Llaves
     Llaves.update()
     Llaves.draw(pantalla)
     
     # Escaners 
     Escaners.update()
     Escaners.draw(pantalla)

     #Puertas
     Puertas.update()
     Puertas.draw(pantalla)
     # _______________________

     # Posicion del juegador de prueba (no prestar atencion)
     pantalla.blit(Jugador.image,(Jugador.rect.center))
    
     pygame.display.flip()

    
#_________________Fin_____________________
pygame.quit