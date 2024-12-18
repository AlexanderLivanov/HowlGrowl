
############################################################################
############################  СНЕГОПАД  ####################################
############################################################################
transform superexitmenu0:
    alpha 0.0
    ease 1.0 alpha 1.0

transform superexitmenu:
    alpha 0.0
    ease 2.0 alpha 1.0

transform superexitmenu1:
    alpha 0.0
    ease 4.0 alpha 1.0

transform superexitmenu2:
    alpha 0.0
    ease 5.0 alpha 1.0

transform moving_cloud3:
    xpos 700
    linear 120 xpos - 1200
    repeat
screen fade_screen():
    add "images/blacks.png" # Плавное затемнение экрана


transform snowfall1: #здесь и ниже «snow1» ваше название
    ypos 0 #привязка изображения по координатам 1.0
    linear 5.0 ypos 1080 #сдвиг изображения за 1.5 секунды на координаты 0.0
    repeat #повторение трансформации

transform snowfall11: #здесь и ниже «snow1» ваше название
    ypos -1440 #привязка изображения по координатам 1.0
    linear 5.0 ypos 0 #сдвиг изображения за 1.5 секунды на координаты 0.0
    repeat #повторение трансформации

transform disolve:
    alpha 1.0
    ease 3.0 alpha 0.0


transform snowfall2:
    ypos 0
    linear 12.0 ypos 1080
    repeat

transform snowfall22:
    ypos -1080
    linear 12.0 ypos 0
    repeat

transform snowfall3:
    ypos 0
    linear 17.0 ypos 1080
    repeat

transform snowfall33:
    ypos -1080
    linear 17.0 yalign 0
    repeat

transform snowfall4:
    ypos 0
    linear 15.0 ypos 10080
    repeat

transform snowfall44:
    ypos -10080
    linear 15.0 yalign 0
    repeat


############################################################################
############################   ОБЛАКО   ####################################
############################################################################
transform moving_cloud:
    xpos 300 alpha 0.0
    linear 1.5 xpos 200 alpha 1.0
    linear 120.0 xpos -2460
    repeat

transform moving_cloud2:
    xpos 300 alpha 0.0
    linear 5.0 xpos 200 alpha 1.0
    linear 180.0 xpos -2460
    repeat


############################################################################
############################   ТУМАН    ####################################
############################################################################
transform moving_tuman:
    xpos 0
    ease 5.0 xpos -100
    ease 5.0 xpos 0
    repeat


############################################################################
############################   ПЫЛЬ    ####################################
############################################################################
transform dust_move:
    xalign 0.0
    linear 35.0 xalign 1.0
    repeat


############################################################################
###########################   МОРГАНИЕ   ###################################
############################################################################
transform semi_blink:
    alpha 0.0
    linear 4 alpha 0.0
    linear 0.3 alpha 1.0
    linear 0.3 alpha 0.0
    repeat

transform closed_blink:
    alpha 0.0
    linear 4 alpha 0.0
    ease 0.3 alpha 1.0
    ease 0.3 alpha 0.0
    repeat


############################################################################
###################   ТЁМНАЯ ФИГУРА В МЕНЮ    ##############################
############################################################################
#transform missed_figure:
#    alpha 0.0
#    linear 1.0 alpha 1.0
#    linear 1.0 alpha 0.0
#    linear 3.0 alpha 1.0
#    linear 0.5 alpha 0.0
#
#    repeat
