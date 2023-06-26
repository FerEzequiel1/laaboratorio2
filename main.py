import pygame,sys
from configuraciones import *
from clases import *
from modo import*
from clase_plataformas import*
from clase_enemigo import*

def actualizar_pantalla(pantalla,personaje:personaje,fondo,lista_de_plataformas,lista_de_nieve,lista_de_acaros):
    pantalla.blit(fondo,(0,0))
    
    
    for piso in lista_de_plataformas:
        pantalla.blit(piso.imagen,piso.rectangulo)

    personaje.update(pantalla,lista_de_plataformas,lista_de_nieve,lista_de_acaros)
    
   
# Datos de la imagen
width = 1800
height = 1000
Tamaño_pantalla = (width,height)
PANTALLA = pygame.display.set_mode(Tamaño_pantalla)
fondo = pygame.image.load("imagenes/fondos/buenos-aires.jpg")
fondo = pygame.transform.scale(fondo,Tamaño_pantalla)

# Datos de tiempo

RELOJ = pygame.time.Clock()
FPS = 50
# Pygame

pygame.init()

#Personaje
posicion_inicial = (height/2,820)
tamaño = (50,100)

juan = personaje(tamaño,diccionario_animaciones,posicion_inicial,5)


#Piso y plataforma
piso = plataforma((width,70),(0,950),"imagenes/plataforma/plataformalv1/pasto")
plataforma001 = plataforma((100,100),(150,900),"imagenes/plataforma/plataformalv1/pasto")
plataforma002 = plataforma((400,100),(350,748.9),"imagenes/plataforma/plataformalv1/pasto")
plataforma003 = plataforma((300,400),(1150,548.9),"imagenes/plataforma/plataformalv1/pasto")

lista_de_plataformas = [piso,plataforma001,plataforma002,plataforma003]

# Evento de nieve y creación
caida_nieve = pygame.USEREVENT + 0
pygame.time.set_timer(caida_nieve,30)

lista_de_nieve = crear_bolas_nieve(50)

# Puntuacion
fuente = pygame.font.SysFont("Arial",30)


#Enemigo

bichito = enemigo((100,100),(550,850),"imagenes/juan-salvo/quieto/quieto1.png",personaje_caminando)
bichito2 = enemigo((100,100),(950,650),"imagenes/juan-salvo/quieto/quieto1.png",personaje_caminando)

lista_de_acaros =[bichito,bichito2]

total_minutes = 3

total_seconds = total_minutes * 60
font = pygame.font.SysFont(None, 48)

while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
            cambiar_modo()
        elif evento.type == caida_nieve:
            update_copos(lista_de_nieve)
            
    bichito.pendulo_x(lista_de_plataformas)
    bichito2.pendulo_x(lista_de_plataformas)
    bichito2.aplicar_gravedad(PANTALLA,lista_de_plataformas)
            
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
    
    actualizar_pantalla(PANTALLA,juan,fondo,lista_de_plataformas,lista_de_nieve,lista_de_acaros)
    
    
    
    PANTALLA.blit(bichito.imagen,bichito.rectangulo)
    PANTALLA.blit(bichito2.imagen,bichito2.rectangulo)
    
    
    for copo in lista_de_nieve:
        PANTALLA.blit(copo["superficie"],copo["rectangulo"])
        
    texto = fuente.render(f"Puntos:{juan.puntos}",False,VERDE,AZUL)
    PANTALLA.blit(texto,(0,0))
        
    
    if get_modo():
        for lados in piso.lados:
            pygame.draw.rect(PANTALLA,"blue",piso.lados[lados],3)
           
        for lado in juan.lados:
            pygame.draw.rect(PANTALLA,"orange",juan.lados[lado],3)
        pygame.draw.rect(PANTALLA,"blue",juan.lados["main"],3)
            
        for plataformas in lista_de_plataformas:
            pygame.draw.rect(PANTALLA,"orange",plataformas.lados["top"],3)
            pygame.draw.rect(PANTALLA,"blue",plataformas.lados["main"],3)
            
        for copo in lista_de_nieve:
            pygame.draw.rect(PANTALLA,"blue",copo["rectangulo"],3)
            
        for bicho in bichito.lados:
            pygame.draw.rect(PANTALLA,"orange",bichito.lados["main"],3)
            
        for papa in bichito2.lados:
            pygame.draw.rect(PANTALLA,"orange",bichito2.lados["main"],3)
            
    milliseconds = RELOJ.tick(FPS)  # Obtener la cantidad de milisegundos transcurridos desde la última actualización
    seconds_elapsed = milliseconds / 1000  # Convertir los milisegundos a segundos
    total_seconds -= seconds_elapsed

    # Verificar si se ha alcanzado el tiempo límite
    if total_seconds <= 0:
        total_seconds = 0
        running = False

    # Calcular los minutos y segundos actuales
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Renderizar el texto del cronómetro
    time_text = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    text_surface = font.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(200, 150))

    
    PANTALLA.blit(text_surface, text_rect)
    pygame.display.update()
    
