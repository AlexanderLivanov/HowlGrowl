
screen koridors_parallax_screen():


    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (650, 100)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"



            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/koridor serogo morning/seriy_koridor_stenka_OFF.png", xfill=True),
                     xysize=(1920+15, 1080)
                ) xpos -20

            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_OFF.png", xfill=True),
                     xysize=(1920+19, 1080)
                )

            fixed:
                fit_first True
                imagebutton:
                    idle "./images/kvartira serogo/koridor serogo morning/seriy_koridor_knopka_OFF.png"
                    #hover "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbutton.png"
                    action [Hide("koridorNoSvet"), Hide("koridorS"), Jump("koridorSvet"), Play("sound", ksOFF)]
                    xpos 0
                    ypos 0
                    focus_mask True

            fixed:
                fit_first True
                use imagemap_koridorS

            fixed:
                use infinite_swap

label koridorS:

    $ show_managed_screen("koridors_parallax_screen")
    with Fade(0.4, 0.4, 0.4) #показываем комнату Серого



$renpy.pause(hard=True)

return


label koridorNoSvet:

    $ show_managed_screen("koridors_parallax_screen")


$renpy.pause(hard=True)

return

##############################################################################################
    ###################################################################################
    ###################################################################################

screen koridors_svet_screen():


    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (650, 100)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"


            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/koridor serogo morning/seriy_koridor_stenka_OFF.png", xfill=True),
                     xysize=(1920+15, 1080)
                ) xpos -20

            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_ON.png", xfill=True),
                     xysize=(1920+19, 1080)
                )

            fixed:
                fit_first True
                imagebutton:
                    idle "./images/kvartira serogo/koridor serogo morning/seriy_koridor_knopka_ON.png"
                    #hover "./images/kvartira serogo/kuhnya serogo morning/seriy_kitchen_lightbutton.png"
                    action [Hide("koridorSvet"), Hide("koridorS"), Jump("koridorNoSvet"), Play("sound", "switch_komnataSON.ogg")]
                    xpos 0
                    ypos 0
                    focus_mask True

            fixed:
                fit_first True
                use imagemap_koridorS2

            fixed:
                use infinite_swap


screen imagemap_koridorS():


    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        hover "./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_hover.png"

        hotspot (239, 54, 281, 1020) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("bathroom")]
        hotspot (957, 276, 336, 576) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("roomS1")]
        hotspot (1547, 0, 260, 1083) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("roomS1")]
        hotspot (700, 861, 700, 227) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("kitchsS")]
        alpha False


screen imagemap_koridorS2():


    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        hover "./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_hover2.png"

        hotspot (239, 54, 281, 1020) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("bathroom")]
        hotspot (957, 276, 336, 576) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("roomS1")]
        hotspot (1547, 0, 260, 1083) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("roomS1")]
        hotspot (700, 861, 700, 227) action [Hide("imagemap_koridorS"), Hide("imagemap_koridorS2"), Jump("kitchsS")]
        alpha False




label koridorSvet:

    $ show_managed_screen("koridors_svet_screen")



$renpy.pause(hard=True)

return