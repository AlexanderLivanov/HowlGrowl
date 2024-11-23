define n = Character(None, kind=nvl)

define Sergey = Character("Серый", color="#c6c6c6")
define Semen = Character("Сёма", color="#ffcccc")
screen click_blocker():
    key "mouseup_1" action NullAction()

label start_game_transition:
    # Показываем экран затемнения
    show screen fade_screen
    stop music fadeout 1.5

    # Выполняем плавное затемнение
    with Dissolve(1.5)
    # Убираем главное меню
    hide screen main_menu
    # Переход к начальной метке
    return Start()

label start:
    scene black

    $renpy.pause(2.0, hard=True)
    n "\ \ \ \ \ \ \ \ \Я чувствую собственное дыхание." with Dissolve (3.0)
    nvl hide Dissolve (0.5)
    nvl clear


    n "{cps=10}\ \ \ \ \ \ \ \ \Вдох,{w=0.8} выдох.{w=0.8} Вдох,{w=0.8}{cps=5} пауза{w=0.4}.{w=0.4}.{w=0.4}.{w=2.0}{cps=8} выдох.{/cps}" with Dissolve (1.0)
    nvl hide Dissolve (0.5)
    nvl clear

    n '''{cps=26}Неестественный свет бьёт в закрытые глаза, \n \ \ \ \заставляя укутаться в одеяло с головой{/cps}''' with Dissolve (0.5)

    n "\ \ \ \ \ \ \ \ \ \ \ \ \но тело {cps=8}{w}{sc=[2]}{color=971117}не хочет шевелиться.{/color}{/sc}{/cps}" with Dissolve (1.0)
    nvl hide Dissolve (0.5)
    nvl clear

    n "{cps=26}В точности не знаешь, чего ждать если \n \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ откроешь глаза.{/cps}" with Dissolve (0.5)
    n "{cps=26}\ Можно лишь полагаться на ощущения.{/cps}" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "{cps=15}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \Возможно,\n{w=0.6}{cps=26} застанешь комнату, залитую солнечными \n\ \ \ \ \ \ \ \ лучами после полуденного сна...{/cps}" with Dissolve (0.5)

    n "{cps=150} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ {cps=15}А может,{p=0.6}{cps=26} свинцовые тучи на пару с беспощадным ливнем.{/cps}" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "{cps=26}В прочем, в этом году второй вариант для Елинска -{p=0.8} \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ практически константа.{/cps}"
    nvl hide Dissolve (0.5)
    nvl clear

    n "Сквозь дрему я прислушиваюсь к звукам вокруг себя, надеясь не услышать, до жути надоевшую, барабанную партию дожда."with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Что ж, видимо, молитвы были услышанны.{w} Тишина." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Хотя нет!" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Только я обрадовался, как послышался, давящий на голову, низкий шум." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Он как напряжение, бегущее по сосудам моей головы - пытается заполнить каждый её уголок и от того становится всё громче.{w} Всё мощнее." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "И это странно, ведь в моей квартире нечему гудеть." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Даже прислонившись ухом к телевизору, не получился бы такой глубокий и обволакивающий пространство шум." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Его громкость была бы нормой для футбольного матча, собравшего полные трибуны.{w} Или даже для большого завода, но уж точно не для моей маленькой квартиры." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Скорее всего - это проделки моего воспаленного разума, который, будто издеваясь, крутит кошмары на любой вкус и цвет.{w} Однако сегодня любопытство побеждает страх." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Неожиданно яркий, но мягкий свет заливает зрачки, на миг вводя меня в замешательство.{w} На этом аттракцион иллюзий не заканчивается и появляется новая странность..." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Всё мое зрение будто сузилось в одной голубовато-белой точке.{w} Вокруг этой самой точки беспросветная темнота." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Кажется, что в этом месте может воплотиться любая мысль.{w} Даже самая неприятная или пугающая. А круг, как единственная видимая материя, пропустит через себя и материализует эти страхи." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Но было всё также тихо." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Никаких, ползущих ко мне, зомби, или необъятных размеров Ктулху из недавно прочитанной книги Лавкрафта.{w} Нет даже банальной стаи худых и изувеченных голодом волков с их диким оскалом." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Получается, я действительно просто сплю?" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Вдруг гул исчезает, а размытая картинка резко становится четкой." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear
    n "Моё лицо заливает нежным лунным светом.{w} Он проникает внутрь моей головы через глаза, делает несколько оборотов и возвращается наружу.{w} Ощущения странные, но тревога и внутренний хаос быстро рассеялись." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "НА ЕДИНЕ С ЛУНОЙ Я ЧУВСТВУЮ, ЧТО ВИЖУ ЭТО НЕ СПРОСТА. ОНА КАК ЗНАМЕНИЕ ЧЕГО-ТО ДАЛЁКОГО, ШЕПЧЕТ СВОИМ БЛЕДНЫМ, ПРЕКРАСНЫМ БЛЕСКОМ. А Я БУДТО ИЗБРАННЫЙ ЕЙ - ПОНИМАЮ И ЗАСЛУЖИВАЮ ЕЁ ДОВЕРИЯ." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "МОЖЕТ ЛУНА ПРИШЛА МЕНЯ О ЧЁМ-ТО ПРЕДУПРЕДИТЬ?" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "А вдруг вчера я был другим, и только сейчас стал собой.{w} И теперь могу принять вызов, которого так долго ждал." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Сознание потихоньку возвращается, принося с собой один единственный вопрос." with Dissolve (0.5)
    n "~Где я~?"
    nvl hide Dissolve (0.5)
    nvl clear

    n "Недавно забытая тревога возвращается на положеное ей место." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear
    n "Главная загадка последних 10 лет - как быть спокойным, когда за окном...{w} это все." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Отпечаток времени на панельках, неказистый двор в лапах предрассветной темноты, паутина на стыке стены и потолка." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Я разочаровано осознаю, что редкий момент спокойствия - всего лишь сон.{w} Однако, может еще не все потеряно?" with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Я еще не встал, значит есть шанс вернуться туда, где меня наполняет неведомая сила, уносящая объективное восприятие действительности." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Хочу отдаться ей, не боясь быть обманутым.{w} Но кого интересуют мои желания." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Несмотря на неприглядность реального мира..." with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear

    n "Я должен проснуться!"  with Dissolve (0.5)
    nvl hide Dissolve (0.5)
    nvl clear


    jump roomS1









    return
