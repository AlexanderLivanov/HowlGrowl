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
            edgescroll (700, 400)
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
                    action [Hide("kitchsofflight"), Jump("kitchsonlight")]
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


            fixed:
                use infinite_swap


screen kitchenS():

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/kuhnya serogo morning/kvartira blur hover/hover_kitchenS.png.png"


        hotspot (1471, 271, 516, 818) action [Hide("kitchenS"), Hide("kitchenS2"),Jump("koridorS")]
        alpha False


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
            edgescroll (700, 200)
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
                    hover "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbutton.png"
                    action [Hide("kitchsonlight"), Jump("kitchsofflight")]
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

            fixed:
                use infinite_swap

screen kitchenS2():

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/kuhnya serogo morning/kvartira blur hover/hover_kitchenS.png.png"


        hotspot (1471, 271, 516, 818) action [Hide("kitchenS"), Hide("kitchenS2"),Jump("koridorS")]
        alpha False

label kitchsS: #кухня со светом

    $ show_managed_screen("kitchens_parallax_screen")
    with Fade (0.4, 0.4, 0.4)


label kitchsofflight: #кухня со светом

    $ show_managed_screen("kitchens_parallax_screen")


$renpy.pause(hard=True)

return


label kitchsonlight: #кухня без света

    $ show_managed_screen("kitchens_parallax_oflight")

$renpy.pause(hard=True)

return
