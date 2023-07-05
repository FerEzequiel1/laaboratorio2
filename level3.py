import pygame,sys
from clases import *
from clase_drops import*
from plataformas import*


# Datos de la imagen

Tamaño_pantalla = (width,height)
PANTALLA = pygame.display.set_mode(Tamaño_pantalla)

fondo_l3 = pygame.image.load("imagenes/fondos/plaza-congreso.jpg")
fondo_l3 = pygame.transform.scale(fondo_l3,Tamaño_pantalla)

# Datos de tiempo
RELOJ = pygame.time.Clock()
FPS = 50
# Pygame

pygame.init()

#Personaje
posicion_inicial = (100,800)
tamaño = (50,100)
juan = personaje(tamaño,diccionario_animaciones,posicion_inicial,5)

# Evento de nieve y creación
caida_nieve = pygame.USEREVENT + 0
pygame.time.set_timer(caida_nieve,30)
lista_de_nieve = crear_bolas_nieve(20)
# Puntuacion
fuente = pygame.font.SysFont("Arial",30)

minutos_totales = 3
segundos_totales = minutos_totales * 60
font = pygame.font.SysFont(None, 48)



while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
        elif evento.type == caida_nieve:
            update_copos(lista_de_nieve)
            borrar_enemigos(lista_de_enemigos_l1)
           
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        juan.que_hace = "derecha"
    elif keys[pygame.K_a]:
        juan.que_hace = "izquierda"
    elif keys[pygame.K_SPACE]:
        juan.que_hace = "saltar"
    else:
        if juan.derecha:
            juan.que_hace = "quieto_derecha"
        else:
            juan.que_hace = "quieto_izquierda"

    actualizar_pantalla(PANTALLA,juan,fondo_l3,lista_de_plataformas_l3,piso_caida_lv3,lista_de_enemigos_l3,lista_de_nieve,lista_enemgios_caida_l3,lista_de_mejoras_l3)

    print_copos(lista_de_nieve,PANTALLA)
    texto = fuente.render(f"Puntos:{juan.puntos}",False,BLANCO,None)
    vidas = fuente.render(f"Vidas:",False,BLANCO,None)
    
    PANTALLA.blit(texto,(20,0))
    PANTALLA.blit(vidas,(200,0))
    
    
            
        
            
    milliseconds = RELOJ.tick(FPS)  # Obtener la cantidad de milisegundos transcurridos desde la última actualización
    seconds_elapsed = milliseconds / 1000  # Convertir los milisegundos a segundos
    segundos_totales -= seconds_elapsed
    
    # if segundos_totales <= 170:
        
    #     for bicho in lista_enemgios_caida:
    #         PANTALLA.blit(bicho.imagen,bicho.rectangulo)
    #         bicho.pendulo_x(lista_de_plataformas,PANTALLA)
    #         bicho.aplicar_gravedad(lista_de_plataformas)
    
    # Calcular los minutos y segundos actuales
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    # Renderizar el texto del cronómetro
    time_text = "{:02d}:{:02d}".format(int(minutos), int(segundos))
    text_surface = font.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (width/2, 50))
    
    PANTALLA.blit(text_surface, text_rect)
    pygame.display.update()
    