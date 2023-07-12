import pygame
from configuraciones import*
from plataformas_enemigos import *



class Nivel():
    def __init__(self,pantalla,fondo,personaje,lista_plataformas,piso_caida,lista_de_copos,lista_enemigos,lista_enemigos_caida,lista_mejoras,boss) -> None:
        #Pantalla y fondo
        self._slave = pantalla
        self.fondo = fondo
        #Personaje
        self.jugador = personaje
        #Plataformas
        self.plataformas = lista_plataformas
        self.plataforma_caida = piso_caida
        #Enemigos
        self.copos = lista_de_copos
        self.enemigos = lista_enemigos
        self.enemigos_caida = lista_enemigos_caida
        self.boss = boss
        #Mejoras
        self.mejoras = lista_mejoras
        self.game_over = False
        
    def update(self,lista_eventos):
        
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: 
                pygame.quit()
                sys.exit(0)
            elif evento.type == caida_nieve:
                update_copos(lista_de_nieve)
            
        self.leer_inputs()
        self.actualizar_pantalla()
        
    def actualizar_pantalla(self):
        self._slave.blit(self.fondo,(0,0))
    
        for piso in self.plataformas:
            self._slave.blit(piso.imagen,piso.rectangulo)
            
        for mejora in self.mejoras:
            self._slave.blit(mejora.imagen,mejora.rectangulo)
            
        for enemigo in self.enemigos:
            self._slave.blit(enemigo.imagen,enemigo.rectangulo)
            enemigo.pendulo_x(self.plataformas,self._slave)
            if enemigo.especie == "pajaro":
                pass
            else:
                enemigo.aplicar_gravedad(self.plataformas)

        self.jugador.update(self._slave,self.plataformas,self.plataforma_caida,self.enemigos,self.copos,self.enemigos_caida,self.mejoras,self.boss)
        
    
    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_a]:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_SPACE]:
            self.jugador.que_hace = "saltar"    
        else:
            if self.jugador.derecha:
                self.jugador.que_hace = "quieto_derecha"
            else:
                self.jugador.que_hace = "quieto_izquierda"
        
