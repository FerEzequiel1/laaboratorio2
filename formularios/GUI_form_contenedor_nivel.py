import pygame
from pygame.locals import*

from GUI_form import*
from GUI_button_image import*

class FormContendorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),color_background="Black")
        nivel._slave = self._slave
        self.nivel = nivel
        self._btn_home = Button_Image(screen=self._slave,
                                      master_x=self._x,
                                      master_y=self._y,
                                      x=self._w - 100,
                                      y=self._h - 100,
                                      w=50,
                                      h=50,
                                      color_background=(255,0,0),
                                      color_border=(255,0,255),
                                      onclick=self.btn_home_click,
                                      onclick_param="",
                                      path_image="formularios/home.png")
        self.lista_widgets.append(self._btn_home)
        
    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        
    def btn_home_click(self,param):
        self.end_dialog()