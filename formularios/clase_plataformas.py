import pygame
from configuraciones import*
class plataforma:
    def __init__(self,dimenciones,posicion,panth):
        self.dimencio = dimenciones
        self.imagen = pygame.image.load(panth) 
        self.imagen = pygame.transform.scale(self.imagen,dimenciones)
        
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        
   
           