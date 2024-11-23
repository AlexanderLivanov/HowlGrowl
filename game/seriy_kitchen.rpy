#############################################################################################################
##############################################     КУХНЯ    #################################################
#############################################################################################################

screen kitchens_parallax_screen():

    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (600, 400)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"


######################################## ЗА ОКНОМ #######################################################


            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/fon room s morning.jpg", xfill=True),
                     xysize=(1920+70, 1080)
                ) ypos -50

            fixed:
                xysize (2000, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/cloud_fons.png", xfill=True),
                    xysize=(2040, 1080)
                ) at moving_cloud2:
                    ypos -100


            fixed:
                xysize (1980, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/panelki_fon_rooms.png", xfill=True),
                    xysize=(1920, 1080)
                ) ypos -30


            fixed:
                xysize (2000, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/derevya_fon.png", xfill=True),
                    xysize=(1920, 1080)
                ) xpos 300 ypos 40


######################################## КОМНАТА #######################################################



            fixed:
                fit_first True
                add "bg_b_kitch"

            fixed:
                fit_first True

                imagebutton:
                    idle "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbutton.png"
                    hover "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbuttonS.png"
                    action Jump("kitchsoflight")
                    xpos 0
                    ypos 0
                    focus_mask True


            fixed:
                xysize (2020, 1080)
                fit_first None
                use kitchenS


            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lights_night.png", xfill=True),
                     xysize=(1920+130, 1080)
               )


            fixed:
                xysize (1920+100, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_fon.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move


            fixed:
                xysize (1920+200, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_middle.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move





            fixed:
                xysize (1920+300, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_front.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move




screen kitchenS():

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/kuhnya serogo morning/hover_kitchenS.png"

        hotspot (318, 557, 132, 119) action Jump("hah")
        hotspot (452, 575, 105, 103) action Jump("hah")
        hotspot (493, 110, 427, 461) action Jump("koridorS")
        hotspot (1471, 271, 516, 818) action Jump("koridorS")
        alpha False


label kitchs:
    hide screen kitchens_parallax_oflight
    hide screen rooms_parallax_screen
    show screen kitchens_parallax_screen

    pause



#############################################################################################################
######################################   КУХНЯ CО СВЕТОМ   ##################################################
#############################################################################################################

image bg_b_kitchl = "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_night_lamp.png"

screen kitchens_parallax_oflight():

    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (600, 200)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"


#############################################     ЗА ОКНОМ     #######################################################


            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/fon room s morning.jpg", xfill=True),
                     xysize=(1920+70, 1080)
                ) ypos -50

            fixed:
                xysize (2000, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/cloud_fons.png", xfill=True),
                    xysize=(2040, 1080)
                ) at moving_cloud2:
                    ypos -100


            fixed:
                xysize (1980, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/panelki_fon_rooms.png", xfill=True),
                    xysize=(1920, 1080)
                ) ypos -30


            fixed:
                xysize (2000, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/derevya_fon.png", xfill=True),
                    xysize=(1920, 1080)
                ) xpos 300 ypos 40



######################################## КОМНАТА #######################################################


            fixed:
                fit_first True
                add "bg_b_kitchl"

            fixed:
                fit_first True

                imagebutton:
                    idle "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbuttonS.png"
                    #hover "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbutton.png"
                    action Jump("kitchs")
                    xpos 0
                    ypos 0
                    focus_mask True

            fixed:
                xysize (2020, 1080)
                fit_first None
                use kitchenS2


            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lights_nightONt.png", xfill=True),
                     xysize=(1920+130, 1080)
               )



screen kitchenS2():

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/kuhnya serogo morning/hover_kitchenS.png"

        hotspot (318, 557, 132, 119) action Jump("hah")
        hotspot (452, 575, 105, 103) action Jump("hah")
        hotspot (493, 110, 427, 461) action Jump("koridorS")
        hotspot (1471, 271, 516, 818) action Jump("koridorS")
        alpha False

label kitchsoflight:
    hide screen kitchens_parallax_screen
    show screen kitchens_parallax_oflight


    pause