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
        self.animacion = animacion
        self.velocidad = 3
        self.contador_de_pasos = 0
        #Lados
        self.lados = obtener_rectangulos(self.rectangulo)
        #Pendulo
        self.pendulum = "derecha"
        
        self.desplazamiento_y = 0
        
        
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 10
        self.esta_saltado = False
        
      def mover(self,velocidad):
         for lado in self.lados:
            self.lados[lado].x += velocidad
            
      def pendulo_x(self,lista_de_plataformas,):
         
         for plataforma in lista_de_plataformas:
            
            if self.rectangulo.colliderect(plataforma.lados["right"]):
                self.mover(self.velocidad)
                self.pendulum = "derecha"
            elif (self.rectangulo.colliderect(plataforma.lados["left"])):
                self.mover(self.velocidad*-1)
                self.pendulum = "asd"
            
         if self.pendulum == "derecha":
               self.mover(self.velocidad)
         else:
               self.mover(self.velocidad*-1)
               
      def aplicar_gravedad(self,pantalla,lista_de_plataformas):
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
                  
         
         

         
         
         
         
         
         
         
         
         
         

