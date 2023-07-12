import pygame
from configuraciones import*

class Laser():
    def __init__(self) -> None:
        self.imagen = pygame.image.load("imagenes/drops/misil.png").convert()
        self.imagne_derecha = pygame.transform.flip(self.imagen,True,False)
        self.imagen.set_colorkey(NEGRO)
        self.rectangulo = self.imagen.get_rect()
        
    def update(self,velocidad):
        self.rectangulo.x += 5*velocidad