

define crowd = Character('Толпа', color="#666666")
define speaker = Character('Спикер', color="#ffffff")
define audio.musnormal = "audio/tolpa.mp3"
define audio.speaker1 = "audio/1.mp3"
define audio.speaker2 = "audio/2.mp3"
define gg =Character('Главный перс', color="#666666")

label start:

    scene bg first
    
    play music musnormal volume 0.2 

    pause 1.5

    crowd "*Звуки толпы*"

    stop music

    play sound speaker1 volume 0.2
    speaker "Дорогие сограждане" 
    stop sound 

    play sound speaker2 volume 0.2
    speaker "Я рад сообщить, 
    что за прошлый месяц в нашем замечательном городе значительно снизился процент преступности"
    stop sound 

    play music musnormal volume 0.2 
    crowd "*Ликование толпы*"
    stop music 

    scene bg second
    with fade
    
    gg "Ага, на одно ограбление бабушки меньше, достойный повод для гордости"

    gg "Почему я оказался здесь?"

    scene bg first
    with fade
    pause 0.75

    speaker "Также со дня на день произойдет раздача еды нуждающимся"

    crowd "*Ликование толпы*"
    scene bg three
    with fade 

    gg "Что такое?" 

    gg "Где я?"
    return

