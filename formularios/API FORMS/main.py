import pygame,sys
from pygame.locals import *
from GUI_form_prueba import FromPrueba


pygame.init()

width = 1200    
height = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((width,height))

form_prueba = FromPrueba(pantalla, 200, 100, 900, 350, "Gold", "Magenta", 5,True)

while True:
    reloj.tick(FPS)
    
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pantalla.fill("Black")

    form_prueba.update(eventos)
    
    pygame.display.flip()