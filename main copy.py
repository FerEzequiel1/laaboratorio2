import pygame,sys
from clases import *
from clase_drops import*
from plataformas_enemigos import*
from nievel_uno import *
from nievel_dos import *
from nievel_tres import *


bandera_lv1 = True
bandera_lv2 = False
bandera_lv3 = False

bandera_finalizo = False
tiempo_finalizado = 0

# Datos de la imagen

Tamaño_pantalla = (width,height)
PANTALLA = pygame.display.set_mode(Tamaño_pantalla)
# FONDOS DE NIVELES
nivel_1 = NivelUno(PANTALLA)
nivel_2 = NivelDos(PANTALLA)
nivel_3 = NivelTres(PANTALLA)

# Datos de tiempo
RELOJ = pygame.time.Clock()
FPS = 50
# Pygame

pygame.init()

#SONIDO NIVEL 
pygame.mixer.music.load("audios/juego.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

#SONIDO GOLPE
# pygame.mixer.music.load("audios/juego.wav")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.1)


# Puntuacion
fuente = pygame.font.SysFont("Arial",30)

minutos_totales = 3
segundos_totales = minutos_totales * 60
font = pygame.font.SysFont(None, 48)



while True:
    milliseconds = RELOJ.tick(FPS)  # Obtener la cantidad de milisegundos transcurridos desde la última actualización
    seconds_elapsed = milliseconds / 1000  # Convertir los milisegundos a segundos
    segundos_totales -= seconds_elapsed
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
           
    nivel_1.update(lista_eventos)
    print_copos(lista_de_nieve,PANTALLA)
    texto = fuente.render(f"Puntos:{nivel_1.jugador.puntos}",False,"red",None)
    vidas = fuente.render(f"Vidas:",False,BLANCO,None)
    
    PANTALLA.blit(texto,(0,0))
    PANTALLA.blit(vidas,(200,0))
     
    if bandera_lv1:
        if nivel_1.enemigos == []:
            nivel_2.jugador.puntos = nivel_1.jugador.puntos
            nivel_2.jugador.vidas = nivel_1.jugador.vidas
            bandera_lv2 = True
            segundos_totales = 180
            bandera_lv1 = False
        
        
    if bandera_lv2:
        nivel_1 = nivel_2
        if nivel_2.enemigos == []:
            nivel_3.jugador.puntos = nivel_2.jugador.puntos
            nivel_3.jugador.vidas = nivel_2.jugador.vidas
            bandera_lv3 = True
            nivel_2 = nivel_3
            segundos_totales = 180
           
    
    if bandera_lv3:
        if segundos_totales <= 170:
            bandera_lv2 = False
            for bicho in nivel_3.enemigos_caida:
                PANTALLA.blit(bicho.imagen,bicho.rectangulo)    
                bicho.pendulo_x(nivel_3.plataformas,PANTALLA)
                bicho.aplicar_gravedad(nivel_3.plataformas)                     
    
        if nivel_3.enemigos == [] and nivel_3.enemigos_caida == []:
            for bicho in nivel_3.boss:
                PANTALLA.blit(bicho.imagen,bicho.rectangulo)
                bicho.pendulo_x(lista_de_plataformas_l3,PANTALLA)
                bicho.aplicar_gravedad(lista_de_plataformas_l3)
                bandera_lv1 = False
        if nivel_3.boss == []:
            bandera_finalizo = True
            print(f'Finalizo el juego restandoles {texto_finalizo}')
           
            
            
    # Calcular los minutos y segundos actuales
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    # Renderizar el texto del cronómetro
    time_text = "{:02d}:{:02d}".format(int(minutos), int(segundos))
    text_surface = font.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (width/2, 50))
    PANTALLA.blit(text_surface, text_rect)
    if not bandera_finalizo:
        tiempo_finalizado  = (pygame.time.get_ticks()/1000)
        minutos_finalizados = tiempo_finalizado // 60
        segundos_finalizados = segundos_totales % 60
        texto_finalizo = "{:02d}:{:02d}".format(int(minutos_finalizados), int(segundos_finalizados))
        
        
    
    pygame.display.update()
    
