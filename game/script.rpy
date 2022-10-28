

define crowd = Character('Толпа', color="#666666")
define speaker = Character('Boss of the gym', color="#ffffff")
define audio.musnormal = "audio/tolpa.mp3"
define gg =Character('Главный перс', color="#666666")

label start:

    scene bg first
    
    play music musnormal volume 0.2

    pause 1.5

    
    crowd "*Звуки толпы*"

    speaker "Дорогие сограждане, я рад сообщить, 
    что за прошлый месяц в нашем замечательном городе значительно снизился процент преступности"
    

    crowd "*Недоумение толпы*"
    
    speaker "эээаэаэаэаэаэаэ"

    scene bg second
    with fade

    gg "Что происходит?"

    gg "Почему я оказался здесь?"

    scene bg three
    with fade 

    gg "Что такое?" 

    gg "Где я?"
    return

