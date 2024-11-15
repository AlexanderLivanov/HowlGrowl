
screen bathroom_parallax_screen():
    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (300, 400)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"

            # Слои параллакса
            fixed:
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/vannaya serogo/Vannaya_Serogo_svet.png", xfill=True),
                     xysize=(1920+19, 1080)
                )
                
            fixed:
                fit_first True
                use imagemap_bathroom
                
label bathroom:
    hide screen koridors_parallax_screen
    hide screen imagemap_koridorS
    hide screen imagemap_koridorS2
    show screen bathroom_parallax_screen
    show screen imagemap_bathroom

$renpy.pause(hard=True)

return

screen imagemap_bathroom():


    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes1.png"
        hover "./images/kvartira serogo/koridor serogo morning/seriy_koridor_fon_hover.png"

        hotspot (1370, 74, 1690, 1080) action Call("koridorS")
        alpha False