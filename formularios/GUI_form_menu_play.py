import pygame
from pygame.locals import*
from GUI_form import*
from GUI_button_image import*
from GUI_form_contenedor_nivel import *
from manejador_niveles import Manejador_niveles


class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        
        self._btn_level_1 = Button_Image(screen=self._slave,
                                         x=100,
                                         y=100,
                                         master_x=x,
                                         master_y=y,
                                         w=100,
                                         h=150,
                                         onclick = self.entrar_nivel,
                                         onclick_param="nivel_uno",
                                         path_image="imagenes/formulario/nivel_1.png")
        
        self._btn_level_2 = Button_Image(screen=self._slave,
                                         x=250,
                                         y=100,
                                         master_x=x,
                                         master_y=y,
                                         w=100,
                                         h=150,
                                         onclick = self.entrar_nivel,
                                         onclick_param="nivel_dos",
                                         path_image="imagenes/formulario/nivel_2.png")
        self._btn_level_3 = Button_Image(screen=self._slave,
                                         x=100,
                                         y=300,
                                         master_x=x,
                                         master_y=y,
                                         w=100,
                                         h=150,
                                         onclick = self.entrar_nivel,
                                         onclick_param="nivel_tres",
                                         path_image="imagenes/formulario/nivel_3.png")
        
        self._btn_home = Button_Image(screen=self._slave,
                                      master_x=x,
                                      master_y=y,
                                      x=400,
                                      y=400,
                                      w=50,
                                      h=50,
                                      color_background=(255,0,0),
                                      color_border=(255,0,255),
                                      onclick=self.btn_home_click,
                                      onclick_param="",
                                      path_image="formularios/home.png")
        
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        
    def on(self,parametro):
        print("hola",parametro) 
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
            
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContendorNivel(self._master,nivel)
        self.show_dialog(form_contenedor_nivel)
        
    def btn_home_click(self,param):
        self.end_dialog()
    
    
        