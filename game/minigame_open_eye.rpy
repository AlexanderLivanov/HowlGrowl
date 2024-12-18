
# Стиль для реплик
init:
    style frustation_style:
        font "DejaVuSans.ttf"  # Укажите ваш шрифт
        size 30
        color "#FF4444"
        outlines [(2, "#000000")]  # Добавляем чёрный контур текста


default bar_value = 0.0  # Текущее значение (0.0 - глаз закрыт, 1.0 - глаз полностью открыт)
default bar_timer_running = True  # Указывает, активна ли игра
default clicks_during_timeout = False  # Флаг, были ли клики во время 20 секунд ожидания
default darkness_alpha = 0.0  # Уровень затемнения экрана (от 0 до 1)

# Экран мини-игры с анимацией глаза
screen mini_game_eye_animation():
    # Фиксированный слой для интерфейса
    fixed:
        align (0.5, 0.5)

        # Плавное затемнение экрана
        if not clicks_during_timeout:
            add Solid("#000000") alpha darkness_alpha

        # Выбор изображения глаза
        if bar_value < 0.1:
            add "./images/moonstart/loonaeye_open0.0.png" xpos 1050 ypos 200
        elif bar_value < 0.2:
            add "./images/moonstart/loonaeye_open0.1.png" xpos 1050 ypos 200
        elif bar_value < 0.3:
            add "./images/moonstart/loonaeye_open0.2.png" xpos 1050 ypos 200
        elif bar_value < 0.4:
            add "./images/moonstart/loonaeye_open0.3.png" xpos 1050 ypos 200
        elif bar_value < 0.5:
            add "./images/moonstart/loonaeye_open0.4.png" xpos 1050 ypos 200
        elif bar_value < 0.6:
            add "./images/moonstart/loonaeye_open0.5.png" xpos 1050 ypos 200
        elif bar_value < 0.7:
            add "./images/moonstart/loonaeye_open0.6.png" xpos 1050 ypos 200
        elif bar_value < 0.8:
            add "./images/moonstart/loonaeye_open0.7.png" xpos 1050 ypos 200
        elif bar_value < 0.9:
            add "./images/moonstart/loonaeye_open0.8.png" xpos 1050 ypos 200
        elif bar_value < 1.0:
            add "./images/moonstart/loonaeye_open0.9.png" xpos 1050 ypos 200
        else:
            add "./images/moonstart/loonaeye_open1.0.png" xpos 1050 ypos 200

        # Кнопка "Проснуться!"
        textbutton "Проснуться!":
            action [Function(update_bar), SetVariable("clicks_during_timeout", True)]
            xalign 0.5 yalign 0.6

    # Таймер для убывания значения
    if bar_timer_running:
        timer 0.1 action Function(decrease_bar) repeat True

# Экран реплик досады
screen frustration_quotes():
    frame:
        xalign 0.5
        ypos 0.8
        text frustration_quote style "frustration_style"

# Логика мини-игры
init python:
    def update_bar():
        """
        Увеличивает значение глаза при клике.
        """
        global bar_value, bar_timer_running
        if bar_timer_running:
            bar_value = min(1.0, bar_value + 0.066)
            if bar_value >= 1.0:
                bar_timer_running = False
                renpy.call_in_new_context("bar_full_outcome")

    def decrease_bar():
        """
        Уменьшает значение глаза со временем.
        """
        global bar_value, bar_timer_running
        if bar_timer_running:
            bar_value = max(0.0, bar_value - 0.03)
            if bar_value <= 0.0:
                bar_timer_running = False
                renpy.call_in_new_context("bar_empty_outcome")

    def reset_game():
        """
        Сбрасывает значения для новой игры.
        """
        global bar_value, bar_timer_running, clicks_during_timeout, darkness_alpha
        bar_value = 0.4
        bar_timer_running = True
        clicks_during_timeout = False
        darkness_alpha = 0.0  # Начальная прозрачность затемнения

# Исходы мини-игры
label bar_empty_outcome:

    $ frustration_messages = [
        "Я не могу проснуться...",
        "Это какой-то кошмар!",
        "Почему я засыпаю снова?",
        "Мне нужно встать...",
        "Эта темнота давит на меня..."
    ]
    $ frustration_quote = ""
    show screen frustration_quotes


    # Постепенное затемнение экрана с репликами
    $ total_time = 20.0  # Общее время затемнения
    $ steps = len(frustration_messages)  # Количество шагов (реплик)
    $ step_duration = total_time / steps  # Длительность каждого шага
    $ i = 0  # Счётчик реплик

    while i < steps and not clicks_during_timeout:
        # Плавное увеличение затемнения
        $ darkness_alpha = min(0.1, darkness_alpha + (0.1 / steps))
        $ frustration_quote = frustration_messages[i]  # Отображаем текущую реплику
        pause step_duration
        $ frustration_quote = ""  # Убираем реплику
        pause 0.5
        $ i += 1

    # Переход через 20 секунд, если не было кликов
    if not clicks_during_timeout:
        "Темнота поглотила вас."
        window hide
        jump roomStart  # Укажите метку для проигрыша

    # Если были клики, возвращаемся к мини-игре
    return

# Основная мини-игра
label mini_game:
    $ reset_game()
    show screen mini_game_eye_animation
    return





