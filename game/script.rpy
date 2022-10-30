define crowd = Character('Толпа', color="#666666")
define speaker = Character('Спикер', color="#ffffff")
define women_from_the_crowd = Character('Женщина из толпы', color="#666666") 
define audio.musnormal = "audio/tolpa.mp3"
define audio.likovanie = "audio/likovanie.mp3"
define audio.speaker5 = "audio/speaker/5.mp3"
define audio.speaker6 = "audio/speaker/6.mp3"
define audio.speaker7 = "audio/speaker/7.mp3"
define audio.speaker8 = "audio/speaker/8.mp3"
define audio.speaker9 = "audio/speaker/9.mp3"
define audio.speaker10 = "audio/speaker/10.mp3"
define audio.speaker11 = "audio/speaker/11.mp3"
define audio.speaker12 = "audio/speaker/12.mp3"
define audio.shag = "audio/zvuki-shaga.mp3"
define audio.plevok = "audio/plevok.mp3"
define gg =Character('Главный герой', color="#4944d1")
define teacher = Character("Елизавета Андреевна", color="#603d3d")
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # Устанавливает постепенное появление и исчезновение бара и требуется только один раз в скрипте
screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 3:
        text str(time) xpos .5 ypos .6 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xpos .5 ypos .6 at alpha_dissolve
init:
    $ timer_range = 0
    $ timer_jump = 0

label start:

    scene bg prolog
    with fade 
    pause 5.0

    scene bg first
    with fade
    play music musnormal volume 0.2 

    pause 1.5

    crowd "*Звуки толпы*"

    stop music

    play sound speaker5 volume 0.2
    speaker "Дорогие сограждане" 
    stop sound 

    #play sound speaker volume 0.2
    speaker "Я рад сообщить, 
    что за прошлый месяц в нашем замечательном городе значительно снизился процент преступности"
    #stop sound 

    play music likovanie volume 0.2 
    crowd "*Ликование толпы*"
    stop music 

    play music shag volume 1.0
    scene bg second
    with fade
    pause 3.0

    show gg 
    with dissolve
    stop music
    gg "Ага, на одно ограбление бабушки меньше, достойный повод для гордости"

    scene bg first
    with fade
    pause 0.75

    play sound speaker6 volume 0.2
    speaker "Также со дня на день произойдет раздача еды нуждающимся"
    stop music
    pause 0.4

    play music likovanie volume 0.2
    crowd "*Ликование толпы*"
    stop music

    scene bg second
    show gg
    gg "Опять раздадут свои объедки, какая щедрость"

    scene bg first
    pause 0.75
    play sound speaker7 volume 0.2
    speaker "Но это еще не все, по причине грядущего праздника будут проведены торжественные мероприятия объявлены 2 выходных дня"
    stop music

    play music likovanie volume 0.2
    crowd "*Ликование толпы*"
    stop music

    play music speaker8 volume 0.4
    speaker "И напоследок, я вынужден объявить, что ряд институтов и школ будет закрыт по причине нехватки финансирования и малой рентабельности"
    stop music 
    
    women_from_the_crowd "Опять вам не хватает денег на образование, лишь бы развлекаться"

    speaker "Уведите женщину"

    women_from_the_crowd "Да как вы смеете, я заслуженный учитель"

    speaker "Если вы не способны с благодарностью принимать все, что мы для вас делаем, то возможно вы не достойны этого"
    speaker "Наша страна славится уровнем своего образования, исходя из этого я не считаю данные мнения"
    speaker "Ммм...Здравыми"

    scene bg second
    show gg
    gg "Замечательно, еще одним недовольным меньше"
    play sound plevok
    gg "*звук плевка*"
    stop sound
    gg "Удивительно, что эта женщина сохранила в себе эту искру"
    gg "Обычно она пропадает с окончанием подросткового максимализма"

    scene bg third
    with fade
    pause 0.75

    teacher "Держи простую задачу, надеюсь, хотя бы с ней ты сможешь справиться"

    $ time = 15
    $ timer_range = 15
    $ timer_jump = 'wrong_answer'
    show doska 
    with dissolve
    "Как найти длину окружности?"
  
    show screen countdown
    menu:
        "Как найти длину окружности?"

        
        "C = 2r":
            hide screen countdown
            jump wrong_answer

        "C = Пd":
            hide screen countdown
            jump rigth_answer

        
        "С = rпa/180°":
            hide screen countdown
            jump wrong_answer
        
        
        "С = AB/2":
            hide screen countdown
            jump wrong_answer

    return

label wrong_answer:
    
    scene bg third
    with fade
    teacher "Ты вообще хоть что-то учишь?"
    teacher "Что у тебя на уме? Как ты жить дальше будешь? "
    teacher "Третью неделю подряд не можешь ни что ответить"

    gg "Возможно я не могу ни на что ответить потому что вы не можете ничего нормально объяснить?"
    gg "Вы можете бесконечно требовать от меня разные формулы и решения, но с таким подходом вы не добьетесь абсолютно ничего!"

    teacher "Ты совсем совесть потерял? Забыл кто ты, а кто я?"
    teacher "Где уважение к старшим?"
    teacher "Завтра я хочу видеть твоих родителей, хочу обсудить их “чадо”"
    
    return
    
label rigth_answer:

    scene bg third
    with fade

    teacher "Хмм"
    teacher "Правильно"
    teacher " У тебя шпаргалка? В телефон подсмотрел? Может подсказал кто?"

    gg "С чего вы взяли?"
    gg "Какой смысл мне тогда учить хоть что-то, если что бы я не ответил, я в любом случае виноват!"
    
    teacher "Успокойся и не забывай с кем ты разговариваешь"

    return
