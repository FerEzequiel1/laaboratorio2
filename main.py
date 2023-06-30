import pygame,sys
from configuraciones import *
from clases import *
from modo import*
from clase_plataformas import*
from clase_enemigo import*
from clase_drops import*


def actualizar_pantalla(pantalla,personaje:personaje,fondo,lista_de_plataformas,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,lista_de_mejoras):
    pantalla.blit(fondo,(0,0))
   
    
    for piso in lista_de_plataformas:
        pantalla.blit(piso.imagen,piso.rectangulo)
        
    for mejora in lista_de_mejoras:
        pantalla.blit(mejora.imagen,mejora.rectangulo)
        
        
    for enemigo in lista_de_enemigos:
        pantalla.blit(enemigo.imagen,enemigo.rectangulo)
        enemigo.pendulo_x(lista_de_plataformas,pantalla)
        enemigo.aplicar_gravedad(lista_de_plataformas)
        
    if personaje.propulsion:
        personaje.velocidad = 10
    else:
        personaje.velocidad = 5
       
   
        

    personaje.update(pantalla,lista_de_plataformas,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,lista_de_mejoras)
    
   
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
posicion_inicial = (100,800)
tamaño = (50,100)

juan = personaje(tamaño,diccionario_animaciones,posicion_inicial,5)


#Piso y plataforma
piso = plataforma((width,70),(0,950),"imagenes/plataforma/plataformalv1/pasto")
plataforma001 = plataforma((100,100),(150,900),"imagenes/plataforma/plataformalv1/pasto")
plataforma002 = plataforma((400,100),(300,700.9),"imagenes/plataforma/plataformalv1/pasto")
plataforma003 = plataforma((300,200),(1150,770),"imagenes/plataforma/plataformalv1/pasto")
plataforma004 = plataforma((300,100),(700,600),"imagenes/plataforma/plataformalv1/pasto")
plataforma005 = plataforma((300,100),(1000,400),"imagenes/plataforma/plataformalv1/pasto")

piedra1 = plataforma((30,30),(350,680),"imagenes/plataforma/plataformalv1/piedra.png")
piedra2 = plataforma((30,30),(700,580),"imagenes/plataforma/plataformalv1/piedra.png")
piedra3 = plataforma((30,30),(980,580),"imagenes/plataforma/plataformalv1/piedra.png")

lista_de_plataformas = [piso,plataforma001,plataforma002,plataforma003,plataforma004,plataforma005,piedra1,piedra2,piedra3]

# Evento de nieve y creación
caida_nieve = pygame.USEREVENT + 0
pygame.time.set_timer(caida_nieve,30)

lista_de_nieve = crear_bolas_nieve(20)

# Puntuacion
fuente = pygame.font.SysFont("Arial",30)


#Enemigo

cascarudo = enemigo((50,50),(550,650),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo2 = enemigo((50,50),(400,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo3 = enemigo((50,50),(500,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo4 = enemigo((50,50),(450,650),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo5 = enemigo((50,50),(700,750),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo6 = enemigo((50,50),(800,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo7 = enemigo((50,50),(400,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo8 = enemigo((50,50),(600,750),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo9 = enemigo((50,50),(800,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo10 = enemigo((50,50),(750,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo11 = enemigo((50,50),(900,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)
cascarudo12 = enemigo((50,50),(800,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos)


lista_de_enemigos =[cascarudo,cascarudo2,cascarudo3,cascarudo4,cascarudo5,cascarudo6,cascarudo7,cascarudo8,cascarudo9,cascarudo10,cascarudo11,cascarudo12]


enemigo_caida = enemigo((50,50),(150,100),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)
enemigo_caida1 = enemigo((50,50),(200,300),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)
enemigo_caida2 = enemigo((50,50),(800,150),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)
enemigo_caida3 = enemigo((50,50),(1000,250),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)
enemigo_caida4 = enemigo((50,50),(1600,300),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)
enemigo_caida5 = enemigo((50,50),(1450,400),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos)

lista_enemgios_caida = [enemigo_caida,enemigo_caida1,enemigo_caida2,enemigo_caida3,enemigo_caida4,enemigo_caida5]

minutos_totales = 3

segundos_totales = minutos_totales * 60
font = pygame.font.SysFont(None, 48)

##Drops
moneda = drops((50,50),(1065,200),"imagenes/drops/premio.png","moneda")
moneda1 = drops((50,50),(700,910),"imagenes/drops/premio.png","moneda")
moneda2= drops((50,50),(1500,910),"imagenes/drops/premio.png","moneda")
vida= drops((50,50),(1200,380),"imagenes/drops/premio.png","vida")


propulsion = drops((50,50),(1200,380),"imagenes/drops/premio.png","propulsion")


lista_de_mejoras = [moneda,moneda1,moneda2,propulsion,vida]

while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
            cambiar_modo()
        elif evento.type == caida_nieve:
            update_copos(lista_de_nieve)
            borrar_enemigos(lista_de_enemigos)
           
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
    
    
    actualizar_pantalla(PANTALLA,juan,fondo,lista_de_plataformas,lista_de_enemigos,lista_de_nieve,lista_enemgios_caida,lista_de_mejoras)
    
    for copo in lista_de_nieve:
        PANTALLA.blit(copo["superficie"],copo["rectangulo"])
        
    texto = fuente.render(f"Puntos:{juan.puntos}",False,"red",None)
    vidas = fuente.render(f"Vidas:",False,BLANCO,None)
    
    PANTALLA.blit(texto,(0,0))
    PANTALLA.blit(vidas,(150,0))
    # PANTALLA.blit(moneda.imagen,moneda.rectangulo)
    # PANTALLA.blit(moneda1.imagen,moneda1.rectangulo)
    # PANTALLA.blit(moneda2.imagen,moneda2.rectangulo)
    # PANTALLA.blit(propulsion.imagen,propulsion.rectangulo)
        
    
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
            
        for bicho in cascarudo.lados:
            pygame.draw.rect(PANTALLA,"orange",cascarudo.lados["main"],3)
            
        for papa in cascarudo2.lados:
            pygame.draw.rect(PANTALLA,"orange",cascarudo2.lados["main"],3)
            
    milliseconds = RELOJ.tick(FPS)  # Obtener la cantidad de milisegundos transcurridos desde la última actualización
    seconds_elapsed = milliseconds / 1000  # Convertir los milisegundos a segundos
    segundos_totales -= seconds_elapsed
    
            
    # Verificar si se ha alcanzado el tiempo límite
   
        
    start_time = pygame.time.get_ticks()
    pruba = pygame.time.get_ticks()
    tiempo_pasado = int((pygame.time.get_ticks() - start_time) / 1000)


    # if segundos_totales <= 170:
        
    #     for bicho in lista_enemgios_caida:
    #         PANTALLA.blit(bicho.imagen,bicho.rectangulo)
    #         bicho.pendulo_x(lista_de_plataformas,PANTALLA)
    #         bicho.aplicar_gravedad(lista_de_plataformas)
    
    # Calcular los minutos y segundos actuales
    minutes = segundos_totales // 60
    seconds = segundos_totales % 60

    # Renderizar el texto del cronómetro
    time_text = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    text_surface = font.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (width/2, 50))
    
    PANTALLA.blit(text_surface, text_rect)
    pygame.display.update()
    
D