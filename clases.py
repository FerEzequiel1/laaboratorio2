from configuraciones import *
import pygame


class personaje:
    def __init__(self,tamaño,animaciones,posicion,velocidad):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #Animaciones
        self.contador_pasos = 0
        self.contador_pasos_drop = 0
        self.propulsion = False
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
        #Vidas
        self.vidas = 3
        #Armamento
        self.balas = 0
        #Sonido de golpes
        self.golpe = pygame.mixer.Sound("audios/golpe.wav")
        self.golpe.set_volume(0.1)
        #Golpes
        self.tiempo_retraso = 1000
        self.ultimo_daño = pygame.time.get_ticks()
        
       
     
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
            
      
            
    def update(self,pantalla,lista_de_plataformas,piso_caida,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,lista_de_mejoras,boss):
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
        self.aplicar_gravedad(pantalla,lista_de_plataformas,piso_caida)
        self.detectar_nieve(lista_de_enemigos,lista_de_copos,lista_enemgios_caida,boss)
        self.detectar_colision(lista_de_plataformas,lista_de_mejoras)
        self.vida_personaje(pantalla)
        
                
    def aplicar_gravedad(self,pantalla,lista_de_plataformas,piso_caida):
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
            elif(self.lados["top"].colliderect(plataforma.lados["bottom"])):    
                self.esta_saltado = True
                self.desplazamiento_y = 1
                break
            else:
                self.esta_saltado = True
         
        for piso_falso in piso_caida:       
            if  self.lados["bottom"].colliderect(piso_falso.lados["top"]):
                self.esta_saltado = True
                self.desplazamiento_y += self.gravedad
         
    def detectar_nieve(self,lista_de_enemigos,lista_de_copos,lista_enemgios_caida,boss):
        
        tiempo_actual = pygame.time.get_ticks()
        for copo in lista_de_copos:
            if self.lados["main"].colliderect(copo["rectangulo"]):
                if tiempo_actual - self.ultimo_daño >= self.tiempo_retraso:
                    self.vidas -= 1
                    self.ultimo_daño = tiempo_actual    
                break
                
            if copo["rectangulo"].y > 1200:
                copo["rectangulo"].x = random.randrange(0,1800,60)
                copo["rectangulo"].y = random.randrange(-2000,0,60) 
        
        for acaro in lista_de_enemigos :
            if self.lados["bottom"].colliderect(acaro.lados["top"]):
                self.puntos += 3
                acaro.pendulum = "asd"
                lista_de_enemigos.remove(acaro)
                self.golpe.play()
                
            if self.lados["right"].colliderect(acaro.lados["left"]) or self.lados["left"].colliderect(acaro.lados["right"]):
                if self.propulsion:
                    self.propulsion =False 
                if tiempo_actual - self.ultimo_daño >= self.tiempo_retraso:
                    self.vidas -= 1
                    self.ultimo_daño = tiempo_actual    
                break
        for bosito in boss :
            if self.lados["bottom"].colliderect(bosito.lados["top"]):
                self.puntos += 3
                bosito.pendulum = "asd"
                boss.remove(bosito)
                self.golpe.play()
                
            if self.lados["right"].colliderect(bosito.lados["left"]) or self.lados["left"].colliderect(bosito.lados["right"]):
                if self.propulsion:
                    self.propulsion =False 
                if tiempo_actual - self.ultimo_daño >= self.tiempo_retraso:
                    self.vidas -= 1
                    self.ultimo_daño = tiempo_actual    
                break
                    
        for acaro in lista_enemgios_caida :
            if self.lados["bottom"].colliderect(acaro.lados["top"]):
                self.puntos += 3
                acaro.pendulum = "asd"
                acaro.muerto = "si"
                self.golpe.play()
                lista_enemgios_caida.remove(acaro)
        
                
                
                
    def detectar_colision(self,lista_de_plataformas,lista_de_mejoras):
        for superficie in lista_de_plataformas:
            if self.rectangulo.colliderect(superficie.lados["right"]):
                self.mover(self.velocidad)
            elif (self.rectangulo.colliderect(superficie.lados["left"])):
                  self.mover(self.velocidad*-1)    
                
            
        for drop in lista_de_mejoras:
            tipo = drop.tipo
            if self.rectangulo.colliderect(drop.rectangulo):
                match tipo:
                    case "moneda":
                        drop.rectangulo.y = 3000
                        self.puntos += 60
                    case "propulsion":
                        self.propulsion = True
                    case "balas":
                        self.balas += 5
                    case "vida":
                        if self.vidas<3:
                            self.vidas +=1
                            lista_de_mejoras.remove(drop)
                        else:
                            if self.vidas >=3 and self.puntos >=50:
                                self.vidas +=1
                                drop.rectangulo.y = 3000
                                break
        if self.lados["left"].x  <= 0:
            self.mover(self.velocidad)
        elif self.lados["right"].x >= 1750:
            self.mover(self.velocidad*-1)
           
        if self.propulsion:
            self.velocidad = 8
        else:
            self.velocidad = 5 
                        
    def vida_personaje(self,pantalla):
        separacion = 300
        imagen_vida = pygame.image.load("imagenes/drops/vida.png")
        rectangulo = imagen_vida.get_rect()
        for cuadrado in range(self.vidas):
            pantalla.blit(imagen_vida,(separacion,0))
            separacion += 50             
                        
                        
                        
                        
                    
          
                
       
            
    
    