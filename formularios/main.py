import pygame,sys
from pygame.locals import *
from GUI_form_prueba import FromPrueba
from configuraciones import *
from nievel_uno import*
from nievel_dos import*
from nievel_tres import*

nivel_1 = NivelUno(PANTALLA)
nivel_2 = NivelDos(PANTALLA)
nivel_3 = NivelTres(PANTALLA)

pygame.init()

width = 1800    
height = 1000
FPS = 50

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((width,height))

# Puntuacion

form_prueba = FromPrueba(pantalla, 400, 200, 1000, 600, "Black", "White", 5,True)
menu =True
nivel2_flag = True
while True:
    if not nivel_1.game_over:
        reloj.tick(FPS)  
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
    
        pantalla.fill("gray")
        form_prueba.update(eventos)        
        print_copos(lista_de_nieve,PANTALLA)
       
    pygame.display.flip()