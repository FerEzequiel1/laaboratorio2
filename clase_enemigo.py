import pygame,random
from configuraciones import*


class enemigo:
    def __init__(self,dimenciones,posicion,panth,animacion):
        self.dimencio = dimenciones
        self.imagen = pygame.image.load(panth) 
        self.imagen = pygame.transform.scale(self.imagen,dimenciones)
        #Rectangulo
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        #Animaciones
        self.animaciones = animacion
        self.velocidad = 3
        self.contador_pasos = 0
        #Lados
        self.lados = obtener_rectangulos(self.rectangulo)
        #Pendulo
        self.pendulum = "derecha"
        #Gravedad
        self.desplazamiento_y = 0
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 10
        self.esta_saltado = False
        #Estado
        self.muerto = "no"
        
        
    def mover(self,velocidad):
         for lado in self.lados:
            self.lados[lado].x += velocidad
            
    def pendulo_x(self,lista_de_plataformas,pantalla):
        
         
         for plataforma in lista_de_plataformas:
            
            if self.rectangulo.colliderect(plataforma.lados["right"]):
                self.mover(self.velocidad)
                self.pendulum = "derecha"
            elif (self.rectangulo.colliderect(plataforma.lados["left"])):
                self.mover(self.velocidad*-1)
                self.pendulum = "izquierda"
            
         if self.pendulum == "derecha":
               self.animar(pantalla,"derecha")
               self.mover(self.velocidad)
         else:
            if (self.pendulum == "izquierda"):
                self.animar(pantalla,"izquierda")
                self.mover(self.velocidad*-1)
            else:
                pass 
           
    def aplicar_gravedad(self,lista_de_plataformas):
        if self.esta_saltado:
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida :
                self.desplazamiento_y += self.gravedad
                
        for plataforma in lista_de_plataformas:   
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.lados["main"].bottom = plataforma.lados["main"].top - 5
                self.esta_saltado = False
                self.desplazamiento_y = 0
                break 
            else:
                self.esta_saltado = True  
                
    def animar(self,pantalla,que_hace):
        animacion = self.animaciones[que_hace]
        
        if self.contador_pasos >= len(animacion):
            self.contador_pasos = 0
         
        pantalla.blit(animacion[self.contador_pasos],self.lados["main"])   
        self.contador_pasos += 1
                  
         
         

         
         
         
         
         
         
         
         
         
         

