import pygame
from pygame.locals import*

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import * 
from GUI_form_menu_score import *
from GUI_form_menu_play import*
from configuraciones import*


class FromPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.volumen = 0.4
        self.flag_play = True
        
        pygame.mixer.init()
        ########## CONTROLES ##########
        self.txtbox = TextBox(self._slave,x,y,50,50,150,30,"Gray","White","Red","Blue",2,font="Comic Sans",font_size=15,font_color="Black")
        self.btn_play = Button(self._slave,x,y,100,100,100,50,"Red","Blue",self.btn_play_click,"Nombre","Pause",font="Verdana",font_size=15,font_color="White")
        self.label_volumen = Label(self._slave,650,190,100,50,"20%","Comic Sans",15,"White","formularios/Table.png")
        self.slider_volumen = Slider(self._slave,x,y,100,200,500,15,self.volumen,"Blue","White")
        self.btn_tabla = Button_Image(self._slave,x,y,255,110,50,50,"formularios/Menu_BTN.png",self.btn_tabla_click,"asd")
        self.btn_jugar = Button_Image(self._slave,x,y,320,110,50,50,"formularios/niveles.png",self.btn_jugar_click,"a")
        self.btn_agregar_nombre = Button(self._slave,x,y,210,50,150,50,"Red","Blue",self.btn_juardar_nombre,"as","Guardar nombre",font="Verdana",font_size=15,font_color="White")

        
        ####################
        
        # Agrego a la lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_agregar_nombre)
        
        
        pygame.mixer.music.load("audios/juego.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
        
    def render(self):
        self._slave.fill(self._color_background)
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
     
    def btn_jugar_click(self,param):
        form_jugar = FormMenuPlay(screen=self._master,
                    x=self._master.get_width()/2 -250,
                    y=self._master.get_height()/2 -250,
                    w = 500,
                    h = 500,
                    color_background=(220,0,220),
                    color_border= (255,255,255),
                    active=True,
                    path_image="formularios/Window.png")
        self.show_dialog(form_jugar)
    def btn_play_click(self,texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
            
        self.flag_play = not self.flag_play
        
    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{int(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
    def btn_tabla_click(self,texto):
        dic_mejores_jugadores = obtener_mejores_jugadores()
        
        form_puntaje = FormMenuScore(self._master,650,250,500,550,(220,0,220),"White",True,"formularios/Window.png",dic_mejores_jugadores,100,10,10)
        
        self.show_dialog(form_puntaje)
        
    def btn_juardar_nombre(self,param):
        nombre = self.txtbox.get_text()
        agregar_nombre_jugador(nombre)