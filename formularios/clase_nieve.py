import pygame,random

class nieve:
    def __init__(self,dimenciones,posicion,panth):
        self.dimencio = dimenciones
        self.imagen = pygame.image.load(panth) 
        self.imagen = pygame.transform.scale(self.imagen,dimenciones)
        
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        
        
    def lista_de_nieve(self):
        
        diccionario_nieve = {}
        diccionario_nieve["superficie"] = self.imagen
        diccionario_nieve["rectangulo"] = self.rectangulo
        diccionario_nieve["velocidad"] = random.randrange(3,8,1)
        
        return diccionario_nieve
        