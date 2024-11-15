

# Увеличение максимального размера, если Ren'Py выдает ошибку Fixed.
define config.max_fit_size = 10000

################################################################################
## Экран параллакса с плавной прокруткой
################################################################################
screen rooms_parallax_screen():

    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel True
            draggable True
            edgescroll (200, 500)
            xysize (1920, 1080)

            has fixed style "vparallax_fixed"

            # Слои параллакса
            fixed:
                xysize (1920+260, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/fon room s morning.jpg", xfill=True),
                    xysize=(1920, 1080)
                )


            fixed:
                xysize (2190, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/cloud_fons.png", xfill=True),
                    xysize=(1920, 1080)
                ) at moving_cloud2


            fixed:
                xysize (2190, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/panelki_fon_rooms.png", xfill=True),
                    xysize=(1920, 1080)
                )


            fixed:
                xysize (2230, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/derevya_fon.png", xfill=True),
                    xysize=(1920, 1080)
                )


#################################################Комната#######################################################
            fixed:
                fit_first True
                add "bg_d"

            fixed:
                fit_first True
                add "zanaveski_move"

            fixed:
                xysize (2270, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_fon.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move

            fixed:
                fit_first True
                add "bg_s"

            fixed:
                fit_first True
                use imagemap_komnataS

            fixed:
                fit_first True
                add "bg_p"

            fixed:
                xysize (1920, 1080)
                fit_first True
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/seriy_komnata_lights_night3.png", xfill=True),
                     xysize=(1920+350, 1080)
               )

            fixed:
                xysize (2347, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_middle.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move

            fixed:
                xysize (1920+360, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/divan room s morning.png", xfill=True),
                    xysize=(1920, 1080)
                )

            fixed:
                xysize (2427, 1080)
                fit_first None
                add Fixed(
                    HBox("./images/kvartira serogo/komnata serogo morning/kvartira objects/dust_front.png", xfill=True),
                    xysize=(1920, 1080)
                ) at dust_move


################################################################################
## Экран с imagemap
################################################################################

screen imagemap_komnataS():

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/sroom_tv blur morning.png"

        hotspot (142, 458, 386, 450) action Jump("hah")
        hotspot (556, 171, 626, 402) action Jump("hah")
        hotspot (1928, 33, 324, 1097) action Call("koridorS")
        alpha False

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/tv blur morning.png"

        hotspot (1051, 471, 217, 156) action Jump("hah")
        alpha False

return

