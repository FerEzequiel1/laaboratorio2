import pygame,random,sys
from clase_nieve import nieve
import json
import sqlite3
width = 1800
height = 1000
Tamaño_pantalla = (width,height)
PANTALLA = pygame.display.set_mode(Tamaño_pantalla)

##### colores  ####
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (200,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

### actualizar_pantalla ### 
def actualizar_pantalla(pantalla,personaje,fondo,lista_de_plataformas,piso_caida,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,lista_de_mejoras,boss):
    pantalla.blit(fondo,(0,0))
   
    
    for piso in lista_de_plataformas:
        pantalla.blit(piso.imagen,piso.rectangulo)
        
    for mejora in lista_de_mejoras:
        pantalla.blit(mejora.imagen,mejora.rectangulo)
        
        
    for enemigo in lista_de_enemigos:
        pantalla.blit(enemigo.imagen,enemigo.rectangulo)
        enemigo.pendulo_x(lista_de_plataformas,pantalla)
        if enemigo.especie == "pajaro":
            pass
        else:
            enemigo.aplicar_gravedad(lista_de_plataformas)

    personaje.update(pantalla,lista_de_plataformas,piso_caida,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,lista_de_mejoras,boss)

## Reescalado de imagenes,posicion y diccionarios #####

def resscalar_imagne(lista_imagenes,tamaño):
    
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)

def girar_imagenes(lista_imagenes, flip_x,flip_y):
    lista_girada = []
    
    for imagen in lista_imagenes:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
        
    return lista_girada

imagen_de_prueba = pygame.image.load("imagenes/enemigos/prueba.png")
personaje_quieto_derecha = [
    pygame.image.load("imagenes/juan-salvo/quieto/quieto1.png"),
    pygame.image.load("imagenes/juan-salvo/quieto/quieto2.png")

]
personaje_saltando_derecha = [
    pygame.image.load("Imagenes/juan-salvo/saltando/quieto1.png"), 
]
misil_izquierda = [
    pygame.image.load("Imagenes/drops/misil.png"), 
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
misil_derecha = girar_imagenes(misil_izquierda,True,False)

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

def print_copos(lista_de_copos,pantalla):
    for copo in lista_de_copos:
        pantalla.blit(copo["superficie"],copo["rectangulo"])
pygame.init()    
lista_de_nieve = crear_bolas_nieve(20)
caida_nieve = pygame.USEREVENT + 0
pygame.time.set_timer(caida_nieve,30)
## Enemigos ####
       

        
cascarudo_caminando_izquierda= [
    pygame.image.load("imagenes/enemigos/cascarudo/cascarudo1.png"),
    pygame.image.load("imagenes/enemigos/cascarudo/cascarudo2.png"),
    pygame.image.load("imagenes/enemigos/cascarudo/cascarudo3.png"),
    pygame.image.load("imagenes/enemigos/cascarudo/cascarudo4.png"),
    pygame.image.load("imagenes/enemigos/cascarudo/cascarudo5.png")
]    

cascarudo_caminando_derecha = girar_imagenes(cascarudo_caminando_izquierda,True,False)
diccionario_animaciones_cascarudos = {}
diccionario_animaciones_cascarudos["derecha"] = cascarudo_caminando_derecha
diccionario_animaciones_cascarudos["izquierda"] = cascarudo_caminando_izquierda

pajaro_volando_derecha = [
    pygame.image.load("imagenes/enemigos/pajaro/pajaro-1.png"),
    pygame.image.load("imagenes/enemigos/pajaro/pajaro-2.png"),
    pygame.image.load("imagenes/enemigos/pajaro/pajaro-3.png"),
    pygame.image.load("imagenes/enemigos/pajaro/pajaro-4.png")   
]
pajaro_volando_izquierda = girar_imagenes(pajaro_volando_derecha,True,False)

diccionario_animaciones_pajaro = {}
diccionario_animaciones_pajaro["derecha"] = pajaro_volando_derecha
diccionario_animaciones_pajaro["izquierda"] = pajaro_volando_izquierda


burgo_caminando_izquierda = [
    pygame.image.load("imagenes/enemigos/burgo/burgo-camina-1.png"),
    pygame.image.load("imagenes/enemigos/burgo/burgo-camina-2.png"),
    pygame.image.load("imagenes/enemigos/burgo/burgo-camina-3.png"),
    pygame.image.load("imagenes/enemigos/burgo/burgo-camina-4.png")   
]
burgo_caminando_derecha = girar_imagenes(burgo_caminando_izquierda,True,False)

diccionario_animaciones_burgo = {}
diccionario_animaciones_burgo["derecha"] = burgo_caminando_derecha
diccionario_animaciones_burgo["izquierda"] = burgo_caminando_izquierda

def agregar_nombre_jugador(nombre):
    with open('formularios/nombre_jugador.json', 'r') as json_file:
        data = json.load(json_file)
        
    nuevo_diccionario = {"nombre": nombre}

    data.append(nuevo_diccionario)

    with open('formularios/nombre_jugador.json', 'w') as json_file:
        json.dump(data, json_file)
        
def obtener_mejores_jugadores():
    conexion = sqlite3.connect('datos_puntos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre,puntos FROM Puntos ORDER BY puntos DESC LIMIT 3")
    resultados = cursor.fetchall()
    conexion.close()

    lista_mejores_jugadores =[]
    for registro in resultados:
        diccionario = {
            "nombre":registro[0],
            "puntos":registro[1]
        }
        lista_mejores_jugadores.append(diccionario)

    return(lista_mejores_jugadores)

def perder_juego(pantalla,texto,size,x,y):
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(f"{texto}",True,(0,255,0))

        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        pantalla.blit(text_surface, text_rect)
        
def guardar_puntos(puntos,nombre):
    
    with sqlite3.connect("datos_puntos.db") as conexion:
        try:
            sentencia = '''
                        insert into Puntos(nombre,puntos) values (?,?)
                       
                    '''
            conexion.execute(sentencia,(nombre,puntos))
            
        except Exception as e:
            print("Error")

def obtener_ultimo_nombre():
    with open('formularios/nombre_jugador.json', 'r') as json_file:
        data = json.load(json_file)

    ultimo_diccionario = data[-1]
    
    return(ultimo_diccionario["nombre"])
############# PLATAFORMAS lv1 #######################

