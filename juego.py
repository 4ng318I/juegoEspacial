import pygame
import sys
from pygame.locals import *

pygame.init()

# configuracion ventana
PANTALLA = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Naves Espaciales')


# bucle para que la ventana permanezca abierta
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit