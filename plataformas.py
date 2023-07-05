import pygame,sys
from configuraciones import *
from clase_plataformas import*
from clase_enemigo import*
from clase_drops import*

####### PLATAFORMAS LV1 ################
piso = plataforma((width,70),(0,950),"imagenes/plataforma/plataformal2/piso.png")
plataforma001 = plataforma((100,100),(150,900),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma002 = plataforma((400,100),(300,700.9),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma003 = plataforma((300,200),(1150,770),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma004 = plataforma((300,100),(700,600),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma005 = plataforma((300,100),(1000,400),"imagenes/plataforma/plataformal2/plataforma1.png")
piedra1 = plataforma((30,30),(350,680),"imagenes/plataforma/plataformalv1/piedra.png")
piedra2 = plataforma((30,30),(700,580),"imagenes/plataforma/plataformalv1/piedra.png")
piedra3 = plataforma((30,30),(980,580),"imagenes/plataforma/plataformalv1/piedra.png")

lista_de_plataformas_l1 = [piso,plataforma001,plataforma002,plataforma003,plataforma004,plataforma005,piedra1,piedra2,piedra3]
piso_caida_lv1 =[]

############## ENEMIGOS LV1 ######################

cascarudo = enemigo((50,50),(550,650),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo2 = enemigo((50,50),(400,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo3 = enemigo((50,50),(500,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo4 = enemigo((50,50),(450,650),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo5 = enemigo((50,50),(700,750),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo6 = enemigo((50,50),(800,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo7 = enemigo((50,50),(400,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo8 = enemigo((50,50),(600,750),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo9 = enemigo((50,50),(800,900),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo10 = enemigo((50,50),(750,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo11 = enemigo((50,50),(900,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo12 = enemigo((50,50),(800,550),"imagenes/enemigos/cascarudo/cascarudo1.png",diccionario_animaciones_cascarudos,"cascarudo")


lista_de_enemigos_l1 =[cascarudo,cascarudo2,cascarudo3,cascarudo4,cascarudo5,cascarudo6,cascarudo7,cascarudo8,cascarudo9,cascarudo10,cascarudo11,cascarudo12]
lista_enemgios_caida_l1 = []
boss_lv1 = []


####################  MEJORAS LV1  ################
moneda_l1 = drops((50,50),(1065,200),"imagenes/drops/premio.png","moneda")
moneda1_l1 = drops((50,50),(700,910),"imagenes/drops/premio.png","moneda")
moneda2_l1 = drops((50,50),(1500,910),"imagenes/drops/premio.png","moneda")
vida_l1= drops((50,50),(1200,350),"imagenes/drops/vida.png","vida")

lista_de_mejoras_l1 = [moneda_l1,moneda1_l1,moneda2_l1,vida_l1]






################### PLATAFORMAS LV2 ##########
piso_l2_1= plataforma((300,70),(0,950),"imagenes/plataforma/plataformal2/piso.png")
piso_l2_2= plataforma((1100,70),(300,950),"imagenes/plataforma/plataformal2/piso2.png")
piso_l2_3= plataforma((400,70),(1400,950),"imagenes/plataforma/plataformal2/piso.png")
plataforma1_1_lv2= plataforma((200,70),(300,750),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_2_lv2= plataforma((50,50),(650,650),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_3_lv2= plataforma((50,50),(850,550),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_4_lv2= plataforma((200,50),(1000,850),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_5_lv2= plataforma((50,50),(400,550),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_6_lv2= plataforma((400,50),(0,350),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_7_lv2= plataforma((400,50),(1000,350),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_8_lv2= plataforma((50,50),(1300,750),"imagenes/plataforma/plataformal2/plataforma1.png")
plataforma1_9_lv2= plataforma((50,50),(950,650),"imagenes/plataforma/plataformal2/plataforma1.png")
piedra1_lv2 = plataforma((30,30),(1100,322),"imagenes/plataforma/plataformalv1/piedra.png")
piedra2_lv2 = plataforma((30,30),(1370,322),"imagenes/plataforma/plataformalv1/piedra.png")


lista_de_plataformas_l2 = [piso_l2_1,piso_l2_2,piso_l2_3,plataforma1_1_lv2,plataforma1_2_lv2,plataforma1_3_lv2,plataforma1_4_lv2,plataforma1_5_lv2,plataforma1_6_lv2,plataforma1_7_lv2,plataforma1_8_lv2,plataforma1_9_lv2,piedra1_lv2,piedra2_lv2]
piso_caida_lv2 = [piso_l2_2]


################## ENEMIGOS LV2 #############
cascarudo1_lv2= enemigo((50,50),(1111,300),"imagenes/enemigos/prueba.png",diccionario_animaciones_cascarudos,"cascarudo")
pajaro1_lv2 = enemigo((50,50),(550,750),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro2_lv2 = enemigo((50,50),(550,350),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro3_lv2 = enemigo((50,50),(1750,750),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro4_lv2 = enemigo((50,50),(900,450),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro5_lv2 = enemigo((50,50),(0,150),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")


lista_de_enemigos_l2 = [cascarudo1_lv2,pajaro1_lv2,pajaro2_lv2,pajaro3_lv2,pajaro4_lv2,pajaro5_lv2]
lista_enemgios_caida_l2 = []
boss_lv2 = []


####################  MEJORAS LV2  ################

moneda1_l2 = drops((50,50),(1600,930),"imagenes/drops/premio.png","moneda")
moneda2_l2 = drops((50,50),(1000,322),"imagenes/drops/premio.png","moneda")
moneda3_l2 = drops((50,50),(1050,800),"imagenes/drops/premio.png","moneda")
velocidad1_l2 = drops((50,50),(100,300),"imagenes/drops/propulsion.png","propulsion")
vida1_l2= drops((50,50),(0,300),"imagenes/drops/vida.png","vida")
vida2_l2= drops((50,50),(1000,800),"imagenes/drops/vida.png","vida")


lista_de_mejoras_l2 = [vida1_l2,vida2_l2,moneda1_l2,moneda2_l2,moneda3_l2,velocidad1_l2]






######### NIVEL 3 #############


###### PLATAFORMAS NIVEL 3 #############

piso_l3= plataforma((1800,70),(0,950),"imagenes/plataforma/plataformal2/piso.png")
plataforma1_lv3 = plataforma((200,70),(300,750),"imagenes/plataforma/plataformal3/plataforma100.png")
plataforma2_lv3 = plataforma((100,70),(0,750),"imagenes/plataforma/plataformal3/plataforma100.png")
plataforma3_lv3 = plataforma((50,50),(100,550),"imagenes/plataforma/plataformal3/plataforma50.png")
plataforma4_lv3 = plataforma((50,50),(0,350),"imagenes/plataforma/plataformal3/plataforma50.png")
plataforma5_lv3 = plataforma((600,70),(600,650),"imagenes/plataforma/plataformal3/plataforma.png")
plataforma6_lv3 = plataforma((200,70),(1300,750),"imagenes/plataforma/plataformal3/plataforma100.png")
plataforma7_lv3 = plataforma((180,70),(1600,550),"imagenes/plataforma/plataformal3/plataforma100.png")
plataforma8_lv3 = plataforma((50,50),(1300,450),"imagenes/plataforma/plataformal3/plataforma100.png")
plataforma9_lv3 = plataforma((50,50),(700,450),"imagenes/plataforma/plataformal3/plataforma50.png")
plataforma10_lv3 = plataforma((50,50),(900,350),"imagenes/plataforma/plataformal3/plataforma50.png")
piedra1_lv3 = plataforma((30,30),(610,620),"imagenes/plataforma/plataformalv1/piedra.png")
piedra2_lv3 = plataforma((30,30),(1150,620),"imagenes/plataforma/plataformalv1/piedra.png")


lista_de_plataformas_l3 =[piso_l3,plataforma1_lv3,plataforma2_lv3,plataforma3_lv3,plataforma4_lv3,
                          plataforma5_lv3,plataforma6_lv3,plataforma7_lv3,plataforma8_lv3,plataforma9_lv3,
                          plataforma10_lv3,piedra1_lv3,piedra2_lv3]
piso_caida_lv3 = []



###### ENEMIGOS NIVEL 3 ########

cascarudo1_lv3= enemigo((50,50),(1000,600),"imagenes/enemigos/prueba.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo2_lv3= enemigo((50,50),(800,600),"imagenes/enemigos/prueba.png",diccionario_animaciones_cascarudos,"cascarudo")
cascarudo3_lv3= enemigo((50,50),(300,800),"imagenes/enemigos/prueba.png",diccionario_animaciones_cascarudos,"cascarudo")
pajaro1_lv3 = enemigo((50,50),(550,650),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro2_lv3 = enemigo((50,50),(550,350),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro3_lv3 = enemigo((50,50),(1750,650),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro4_lv3 = enemigo((50,50),(850,450),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")
pajaro5_lv3 = enemigo((50,50),(1100,850),"imagenes/enemigos/prueba.png",diccionario_animaciones_pajaro,"pajaro")

boss= enemigo((100,100),(200,0),"imagenes/enemigos/prueba.png",diccionario_animaciones_burgo,"burgo")

lista_de_enemigos_l3 = [cascarudo1_lv3,cascarudo2_lv3,cascarudo3_lv3,pajaro1_lv3,pajaro2_lv3,pajaro3_lv3,pajaro4_lv3,pajaro5_lv3]
boss_lv3 = [boss]

enemigo_caida = enemigo((50,50),(0,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")
enemigo_caida1 = enemigo((50,50),(200,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")
enemigo_caida2 = enemigo((50,50),(800,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")
enemigo_caida3 = enemigo((50,50),(1000,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")
enemigo_caida4 = enemigo((50,50),(1600,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")
enemigo_caida5 = enemigo((50,50),(1450,0),"imagenes/juan-salvo/quieto/quieto1.png",diccionario_animaciones_cascarudos,"cascarudo")

lista_enemgios_caida_l3 = [enemigo_caida,enemigo_caida1,enemigo_caida2,enemigo_caida3,enemigo_caida4,enemigo_caida5]
##### MEJORAS NIVEL 3 ######
vida1_l3 = drops((50,50),(1300,400),"imagenes/drops/vida.png","vida")
moneda1_l3 = drops((50,50),(700,400),"imagenes/drops/premio.png","moneda")
bala1 = drops((50,50),(0,300),"imagenes/drops/bala.png","vida")
bala2 = drops((50,50),(900,300),"imagenes/drops/bala.png","vida")
bala3 = drops((50,50),(1700,500),"imagenes/drops/bala.png","vida")




lista_de_mejoras_l3 = [bala1,vida1_l3,bala2,bala3,moneda1_l3]


