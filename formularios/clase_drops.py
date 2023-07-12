from configuraciones import *
from clase_nieve import nieve
import pygame

class drops(nieve):
    def __init__(self, dimenciones, posicion, panth,tipo):
        super().__init__(dimenciones, posicion, panth)
        self.tipo = tipo