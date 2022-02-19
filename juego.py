import pygame
import sys
from pygame.locals import *

# Iniciar pygame
pygame.init()

# configuracion ventana
PANTALLA = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Naves Espaciales')

# montar el icono
icono = pygame.image.load('imagenes/icono.png')
pygame.display.set_icon(icono)

# fondo del juego
fondo1 = pygame.image.load('imagenes/fondo.jpg')
PANTALLA.blit(fondo1, [0,0])



# ---------VARIABLES GLOBALES ----------

# Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

HC74255 = (199,66,37)
H61CD35 = (97,205,53)

#PANTALLA.fill(BLANCO) # para colocar un fondo blanco

# Formas a Dibujar
#rectangulo1 = pygame.draw.rect(PANTALLA, ROJO, (100,50,100,50))
#pygame.draw.line(PANTALLA,VERDE, (100,104), (199,104), 5)
#pygame.draw.circle(PANTALLA, NEGRO,(122,250), 20, 5)
#pygame.draw.ellipse(PANTALLA,VERDE,(200, 200, 40, 80), 10)

#puntos = [(100, 300),(100, 100), (150,100)] # un triangulo, + tuplas = mas lados
#pygame.draw.polygon(PANTALLA, (0, 100, 255), puntos, 8) # 8 es el grosor




# bucle para que la ventana permanezca abierta
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit
    pygame.display.update() # para ir actualizando la pantalla