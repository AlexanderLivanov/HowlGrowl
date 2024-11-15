
screen koridors_parallax_screen():


    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (550, 80)
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
                    action Jump("koridorSvet")
                    xpos 0
                    ypos 0
                    focus_mask True

            fixed:
                fit_first True
                use imagemap_koridorS

label koridorS:
    hide screen bathroom_parallax_screen
    hide screen rooms_parallax_screen
    hide screen koridors_svet_screen
    show screen koridors_parallax_screen

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
            edgescroll (550, 80)
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
                    action Jump("koridorS")
                    xpos 0
                    ypos 0
                    focus_mask True

            fixed:
                fit_first True
                use imagemap_koridorS2




screen imagemap_koridorS():


    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        hover "./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_hover.png"

        hotspot (239, 54, 281, 1020) action Call("bathroom")
        hotspot (957, 276, 336, 576) action Call("hah")
        hotspot (1547, 0, 260, 1083) action Call("hah")
        hotspot (700, 861, 700, 227) action Call("kitchs")
        alpha False


screen imagemap_koridorS2():


    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        hover "./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_hover2.png"

        hotspot (239, 54, 281, 1020) action Call("bathroom")
        hotspot (957, 276, 336, 576) action Call("hah")
        hotspot (1547, 0, 260, 1083) action Call("hah")
        hotspot (700, 861, 700, 227) action Call("kitchs")
        alpha False
        



label koridorSvet:
    hide screen bathroom_parallax_screen
    hide screen koridors_parallax_screen
    show screen koridors_svet_screen

$renpy.pause(hard=True)

return