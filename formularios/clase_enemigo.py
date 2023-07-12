import pygame,random
from configuraciones import*


class enemigo:
    def __init__(self,dimenciones,posicion,panth,animacion,especie):
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
        #Especie
        self.especie = especie
        self.vidas = 3
        
    def mover(self,velocidad):
         for lado in self.lados:
            self.lados[lado].x += velocidad
            
    def pendulo_x(self,lista_de_plataformas,pantalla):
        
         
         for plataforma in lista_de_plataformas:
            
            if self.rectangulo.colliderect(plataforma.lados["right"]) or self.rectangulo.x<=0:
                self.mover(self.velocidad)
                self.pendulum = "derecha"
            elif (self.rectangulo.colliderect(plataforma.lados["left"]) or self.rectangulo.x >1750):
                self.mover(self.velocidad*-1)
                self.pendulum = "izquierda"
                
            
         if self.pendulum == "derecha":
               self.mover(self.velocidad)
               self.animar(pantalla,"derecha")
         else:
            if (self.pendulum == "izquierda"):
                self.mover(self.velocidad*-1)
                self.animar(pantalla,"izquierda")
                
             
           
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
        
    def vida(self,pantalla):
        separacion = 1650
        imagen_vida = pygame.image.load("imagenes/drops/vida.png")
        rectangulo = imagen_vida.get_rect()
        for cuadrado in range(self.vidas):
            pantalla.blit(imagen_vida,(separacion,0))
            separacion += 50  
            
        fuente = pygame.font.SysFont("Arial",30)    
        vidas = fuente.render(f"Vidas Boss:",False,BLANCO,None)
        pantalla.blit(vidas,(1450,0))  
                  
         
         

         
         
         
         
         
         
         
         
         
         

