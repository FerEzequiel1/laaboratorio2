from configuraciones import *
from plataformas_enemigos import *
from nivele import*
from clases import *

class NivelTres(Nivel):
    def __init__(self, pantalla:pygame.Surface) -> None:
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        #Personaje
        posicion_inicial = (100,800)
        tamaño = (50,100)
        juan = personaje(tamaño,diccionario_animaciones,posicion_inicial,5)
        
        fondo = pygame.image.load("imagenes/fondos/plaza-congreso.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))
        super().__init__(pantalla, fondo, juan, lista_de_plataformas_l3, piso_caida_lv3, lista_de_nieve, lista_de_enemigos_l3, lista_enemgios_caida_l3, lista_de_mejoras_l3, boss_lv3)
