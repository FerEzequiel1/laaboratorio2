from configuraciones import *
import pygame


class personaje:
    def __init__(self,tamaño,animaciones,posicion,velocidad):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #Animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto_derecha"
        self.animaciones = animaciones
        self.derecha = True
        self.rescalar_animaciones()
       
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #Gravedad
        self.gravedad = 1
        self.potencia_salto = -20
        self.limite_velocidad_caida = 15
        self.esta_saltado = False
        #Rectangulos
        self.rectangulo = self.animaciones["quieto_derecha"][0].get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        #Puntos
        self.puntos = 0
       
     
    def rescalar_animaciones(self):
        for clave in self.animaciones:
            resscalar_imagne(self.animaciones[clave],[self.ancho,self.alto])
        
    def animar(self,pantalla,que_hace):
        animacion = self.animaciones[que_hace]
        
        if self.contador_pasos >= len(animacion):
            self.contador_pasos = 0
         
        pantalla.blit(animacion[self.contador_pasos],self.lados["main"])   
        self.contador_pasos += 1
    
    def mover(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
            
      
            
    def update(self,pantalla,lista_de_plataformas,lista_de_nieve,lista_de_acaros):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltado:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
                self.derecha = True
            case "izquierda":
                if not self.esta_saltado:
                    self.animar(pantalla,"camina_izquierda")
                self.mover(self.velocidad * -1)
                self.derecha = False
            case "quieto_derecha":
                if not self.esta_saltado:
                     self.animar(pantalla,"quieto_derecha")
            case "quieto_izquierda":
                if not self.esta_saltado:
                     self.animar(pantalla,"quieto_izquierda")
            case "saltar":
                if not self.esta_saltado:
                    self.esta_saltado = True
                    self.desplazamiento_y = self.potencia_salto
        self.aplicar_gravedad(pantalla,lista_de_plataformas)
        self.detectar_nieve(lista_de_nieve,lista_de_acaros)
        self.detectar_colision(lista_de_plataformas)
                
    def aplicar_gravedad(self,pantalla,lista_de_plataformas):
        if self.esta_saltado:
            if self.derecha: 
                self.animar(pantalla,"salta_derecha")
            else:
                self.animar(pantalla,"salta_izquierda")
            
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida :
                self.desplazamiento_y += self.gravedad
                
        for plataforma in lista_de_plataformas:   
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.lados["main"].bottom = plataforma.lados["main"].top 
                self.esta_saltado = False
                self.desplazamiento_y = 0
                break 
            else:
                self.esta_saltado = True
            
         
    def detectar_nieve(self,lista_de_nieve,lista_de_acaros):
        for copo in lista_de_nieve:
            if self.lados["top"].colliderect(copo["rectangulo"]):
                
                copo["rectangulo"].x = random.randrange(0,1800,60)
                copo["rectangulo"].y = random.randrange(-2000,0,60)
                
            if copo["rectangulo"].y > 1200:
                copo["rectangulo"].x = random.randrange(0,1800,60)
                copo["rectangulo"].y = random.randrange(-2000,0,60) 
        
        for acaro in lista_de_acaros:
            if self.lados["bottom"].colliderect(acaro.lados["top"]):
                self.puntos += 1
                for lado in acaro.lados:
                    acaro.lados[lado].y = 3000
                
                
                
    def detectar_colision(self,lista_de_plataformas):
        for superficie in lista_de_plataformas:
            if self.rectangulo.colliderect(superficie.lados["right"]):
                self.mover(self.velocidad)
            elif (self.rectangulo.colliderect(superficie.lados["left"])):
                  self.mover(self.velocidad*-1)
                  
        if self.lados["left"].x  == 0:
            self.mover(self.velocidad)
        elif self.lados["right"].x > 1850:
            self.mover(self.velocidad*-1)
          
                
       
            
    
    