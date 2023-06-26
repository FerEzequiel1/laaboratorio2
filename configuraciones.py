import pygame,random,sys
from clase_nieve import nieve

##### colores  ####
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (200,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

### Cronometro ### 

# minutos_iniciales = 3
# segundos_totales = minutos_iniciales * 60 

def actualizar_cronometro(segundos_totales,pantalla):
    fuente_cronometro = pygame.font.SysFont("Arial",30)
    
    if segundos_totales > 0:
        segundos_totales -= 1

    # Calcular los minutos y segundos actuales
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    # Renderizar el texto del reloj
    time_text = "{:02d}:{:02d}".format(minutos, segundos)
    text_surface = fuente_cronometro.render(time_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (200, 150))
    
    pantalla.blit(text_surface, text_rect)


## Reescalado de imagenes,posicion y diccionarios #####

def resscalar_imagne(lista_imagenes,tamaño):
    
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)

def girar_imagenes(lista_imagenes, flip_x,flip_y):
    lista_girada = []
    
    for imagen in lista_imagenes:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
        
    return lista_girada


personaje_quieto_derecha = [
    pygame.image.load("imagenes/juan-salvo/quieto/quieto1.png"),
    pygame.image.load("imagenes/juan-salvo/quieto/quieto2.png")

]
personaje_saltando_derecha = [
    pygame.image.load("Imagenes/juan-salvo/saltando/quieto1.png"),
    
]

personaje_caminando = [
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo1.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo2.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo3.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo4.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo5.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo6.png"),
    pygame.image.load("imagenes/juan-salvo/corriendo/corriendo7.png")
]

personaje_caminando_izquierda = girar_imagenes(personaje_caminando,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha,True,False)
personaje_saltando_izquierda = girar_imagenes(personaje_saltando_derecha,True,False)

diccionario_animaciones = {}
diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecha
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["camina_derecha"] = personaje_caminando
diccionario_animaciones["camina_izquierda"] = personaje_caminando_izquierda
diccionario_animaciones["salta_derecha"] = personaje_saltando_derecha
diccionario_animaciones["salta_izquierda"] = personaje_saltando_izquierda



## obtencion de rectangulos ###

def obtener_rectangulos(principal)->dict:
        diccionario ={}
        diccionario["main"] = principal
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width,10)
        diccionario["right"] = pygame.Rect(principal.right-2, principal.top,2, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top,2, principal.height)
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom-6, principal.width, 6)
        return diccionario
    
#### PLATAFORMAS #####




##### copos de nieve #####   
def crear_bolas_nieve(cantidad):
    lista = []
    
    for i in range(cantidad):
        x = random.randrange(0,1800,60)
        y = random.randrange(-2000,0,60)
        diccionario = nieve((30,30),(x,y),"imagenes/nieve/nieve.png")
        diccionario_copos = diccionario.lista_de_nieve()
        lista.append(diccionario_copos)
    
    return lista   
                
def update_copos(lista_de_copos):
    for copo in lista_de_copos:
        
        rectangulo = copo["rectangulo"]
        rectangulo.y += copo["velocidad"]
        
 
## Enemigos ####
       
def update_bicho(bicho,velocidad):
    
        lados = bicho.lados
        
        bicho.lados += velocidad
        
        
            
       