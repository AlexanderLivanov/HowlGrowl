

# Увеличение максимального размера, если Ren'Py выдает ошибку Fixed.
define config.max_fit_size = 10000

default tv_on = False

image tvchannel = Movie(play="ETK.ogv")

screen tvchannel1:
    fixed:
        xysize (2247, 1080)
        fit_first None
        add Fixed(
            HBox("tvchannel", xfill=True),
            xysize=(1920, 1080)
        ) at Transform(xpos=1070, ypos=493, xsize=190, ysize=155)


screen tv_screen():
    # Если телевизор включён, показываем видео
    if tv_on:
        use tvchannel1  # Ваше видео


################################################################################
## Экран параллакса с плавной прокруткой
################################################################################

################################################################################
##Экран постоянного фильтра
init python:
    def swap_images(st, at):
        """
        Функция меняет изображения каждые 0.1 секунды.
        Параметры:
        - st: время с начала показа DynamicDisplayable
        - at: время с начала последней трансформации (можно не использовать здесь)
        """
        if int(st * 10) % 2 == 0:
            return "FilterImage1.png", 0.1  # Показывает "image1.png"
        else:
            return "FilterImage2.png", 0.1  # Показывает "image2.png"

screen infinite_swap():
    # Используем DynamicDisplayable с исправленной функцией
    add DynamicDisplayable(swap_images)

    # Чтобы экран не закрывался, добавляем пустое действие
    timer 0.1 action NullAction()




screen rooms_parallax_screen():


    fixed:
        align (0.5, 0.5)

        # Параллакс-видоискатель
        parallax_viewport id "parallax_vp":
            mousewheel False
            draggable False
            edgescroll (500, 350)
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
                use tv_screen


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

            fixed:
                use infinite_swap

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
        hotspot (1928, 33, 324, 1097) action [Hide("imagemap_komnataS"), Jump("koridorS")]
        alpha False

    imagemap:
        ground "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        idle "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/groundes.png"
        hover "./images/kvartira serogo/komnata serogo morning/kvartira blur hover/tv blur morning.png"


        hotspot (1051, 471, 217, 156):  # Координаты кнопки
            action [
                ToggleVariable("tv_on"),

                Function(renpy.sound.play, "switch_komnataSON.ogg" if tv_on else "switch_komnataSOFF.ogg")
            ]
label roomStart: #версия комнаты открываемая исключительно один раз при старте

    python:
        renpy.music.queue("fon_room_morning.mp3", channel = "music", fadein = 3.0)

    $ show_managed_screen("rooms_parallax_screen")
    with Fade(1.0, 1.0, 2.0) #показываем комнату Серого
    hide scene black

$renpy.pause(hard=True)


label roomS1: #обычная версия комнаты Серого
    $ show_managed_screen("rooms_parallax_screen")
    with Fade(0.4, 0.4, 0.4) #показываем комнату Серого

$renpy.pause(hard=True)

return

