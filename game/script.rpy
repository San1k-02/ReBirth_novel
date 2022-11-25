define crowd = Character('Толпа', color="#666666")
define speaker = Character('Спикер', color="#ffffff", image = "speaker")
define women_from_the_crowd = Character('Женщина из толпы', color="#666666", image = "women_from_the_crowd") 
define audio.musnormal = "audio/tolpa.mp3"
define audio.likovanie = "audio/likovanie.mp3"
define audio.dictor1_1 = "audio/dictor/1.1.mp3"
define audio.dictor1_2 = "audio/dictor/1.2.mp3"
define audio.gg1 = "audio/gg/1.mp3"
define audio.dictor2 = "audio/dictor/2.mp3"
define audio.gg2 = "audio/gg/2.mp3"
define audio.dictor3 = "audio/dictor/3.mp3"
define audio.dictor4 = "audio/dictor/4.mp3"
define audio.dictor5 = "audio/dictor/5.mp3"
define audio.dictor6 = "audio/dictor/6.mp3"
define audio.dictor7 = "audio/dictor/7.mp3"
define audio.dictor8_1 = "audio/dictor/8.1.mp3"
define audio.dictor8_2 = "audio/dictor/8.2.mp3"
define audio.gg3 = "audio/gg/3.mp3"
define audio.gg4 = "audio/gg/4.mp3"
define audio.gg5 = "audio/gg/5.mp3"
define audio.gg6 = "audio/gg/6.mp3"
define audio.gg7 = "audio/gg/7.mp3"
define audio.shag = "audio/zvuki-shaga.mp3"
define audio.plevok = "audio/plevok.mp3"
define audio.young1 = "audio/young_gg/1.mp3"
define audio.young2 = "audio/young_gg/2.mp3"
define audio.young3 = "audio/young_gg/3.mp3"
define audio.young4 = "audio/young_gg/4.mp3"
define audio.young5 = "audio/young_gg/5.mp3"
define audio.young6 = "audio/young_gg/6.mp3"
define audio.young7 = "audio/young_gg/7.mp3"
define audio.young8 = "audio/young_gg/8.mp3"
define audio.young9 = "audio/young_gg/9.mp3"
define audio.father1 = "audio/father/1.mp3"
define audio.father2 = "audio/father/2.mp3"
define audio.father3 = "audio/father/3.mp3"
define audio.door = "audio/door.mp3"
define gg = Character ('Главный герой', color="#4944d1", image = "gg")
define young_gg = Character ('Главный герой', color="#4944d1", image = "young_gg")
define stranger = Character ('Незнакомец', color="#6b6b6bff", image = "stranger")
define teacher = Character ("Елизавета Андреевна", color="#603d3d", image = "teacher")
define mother = Character ("Мать", color="#996262", image = "mother")
define father = Character ("Отец", color="#3d4b72", image = "father")
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # Устанавливает постепенное появление и исчезновение бара и требуется только один раз в скрипте

init:
    default seen = renpy.count_seen_dialogue_blocks()
    default dialogue = renpy.count_dialogue_blocks()
    default result = seen * 100 / dialogue

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
    play music musnormal volume 0.4

    pause 1.5

    crowd "*Звуки толпы*"

    stop music

    play sound dictor1_1 volume 1.0
    speaker "Дорогие сограждане" 
    stop sound

    play sound dictor1_2 volume 1.0
    speaker "Я рад сообщить, что за прошлый месяц в нашем замечательном городе значительно снизился процент преступности"
    stop sound 

    play music likovanie volume 0.4
    crowd "*Ликование толпы*"
    stop music 

    play music shag volume 1.0
    scene bg second
    with fade
    pause 3.0

    show gg 
    with dissolve
    stop music
    play sound gg1 volume 0.8
    gg "Ага, на одно ограбление бабушки меньше, достойный повод для гордости"
    stop sound

    scene bg first
    with fade
    pause 0.75

    play sound dictor2 volume 0.8
    speaker "Также со дня на день произойдет раздача еды нуждающимся"
    stop sound
    pause 0.4

    play music likovanie volume 0.4
    crowd "*Ликование толпы*"
    stop music

    scene bg second
    show gg
    play sound gg2 volume 0.8
    gg "Опять раздадут свои объедки, какая щедрость"
    stop sound

    scene bg first
    pause 0.75
    play sound dictor3 volume 0.8
    speaker "Но, это еще не все, по причине грядущего праздника будут проведены торжественные мероприятия"
    stop sound

    play sound dictor4 volume 0.8
    speaker "Поэтому мэр города издал указ, согласно которому следующая неделя объявляется нерабочей"
    stop sound

    play music likovanie volume 0.4
    crowd "*Ликование толпы*"
    stop music

    play sound dictor5 volume 0.8
    speaker "И напоследок, я вынужден объявить, что ряд институтов и школ будет закрыт по причине нехватки финансирования и малой рентабельности"
    stop sound 
    
    women_from_the_crowd "Опять вам не хватает денег на образование, лишь бы развлекаться"

    play sound dictor6 volume 0.8
    speaker "Уведите женщину"
    stop sound

    women_from_the_crowd "Да как вы смеете, я заслуженный учитель"

    play sound dictor7 volume 0.8
    speaker "Если вы не способны с благодарностью принимать все, что мы для вас делаем, то, возможно, вы не достойны этого"
    stop sound

    play sound dictor8_1 volume 0.8
    speaker "Наша страна славится уровнем своего образования, исходя из этого я не считаю данное мнение"
    stop sound

    play sound dictor8_2 volume 0.8
    speaker "Ммм...Здравым"
    stop sound

    scene bg second
    show gg

    play sound gg3 volume 0.8
    gg "Замечательно, еще одним недовольным меньше"
    stop sound

    play sound plevok
    gg "*звук плевка*"
    stop sound

    play sound gg4 volume 0.8
    gg "Удивительно, что эта женщина сохранила в себе эту искру"
    
    stop sound
    play sound gg5 volume 0.8
    gg "Обычно она пропадает с окончанием подросткового максимализма"
    stop sound

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

    play sound young1 volume 0.8
    young_gg "Возможно, я не могу ни на что ответить, потому что вы не можете ничего нормально объяснить?"
    stop sound

    play sound young2 volume 0.8
    young_gg "Вы можете бесконечно требовать от меня разные формулы и решения, но с таким подходом вы не добьетесь абсолютно ничего!"
    stop sound

    teacher "Ты совсем совесть потерял? Забыл кто ты, а кто я?"
    teacher "Где уважение к старшим?"
    teacher "Завтра я хочу видеть твоих родителей, хочу обсудить их “чадо”"

    scene black
    with fade
    pause 0.75
    mother "Сын, иди на кухню"

    play sound door volume 0.6
    "*Скрипучий звук открывающийся двери*"
    stop sound

    scene bg fiveth
    with fade
    pause 0.75
    play sound father1 volume 1.6
    father "Сколько можно позорить семью? Я сто раз говорил тебе, забудь про свое эго!"
    stop sound

    play sound father3 volume 1.6
    father "*Сильный кашель*"
    stop sound

    play sound father2 volume 1.3
    father "Но нет, тебе надо спорить, непонятно для чего стоять на своем, тебя вообще не волнует то, что происходит вокруг тебя!"
    stop sound

    play sound young3 volume 0.8
    young_gg "Я не виноват, что Елизавета Андреевна не умеет нормально объяснять"
    stop sound

    play sound young9 volume 0.8
    young_gg "За любую малейшую ошибку она хочет выставить меня перед всеми дураком"
    stop sound

    jump continue_1

label rigth_answer:

    scene bg third

    teacher "Хмм"
    teacher "Правильно"
    teacher "У тебя шпаргалка? В телефон подсмотрел? Может подсказал кто?"

    play sound young5 volume 0.8
    young_gg "Да с чего вы взяли?"
    stop sound

    play sound young6 volume 0.8
    young_gg "Какой смысл мне тогда учить хоть что-то, если что бы я не ответил, я в любом случае виноват?"
    stop sound
    
    teacher "Успокойся и не забывай с кем ты разговариваешь"

    teacher "Нашел ответ где-то и строишь из себя непонятно кого"

    teacher "Завтра я хочу видеть твоих родителей, хочу обсудить их “чадо”"

    scene black
    with fade
    pause 0.75
    mother "Сын, иди на кухню"

    play sound door volume 0.6
    "*Скрипучий звук открывающийся двери*"
    stop sound

    scene bg fiveth
    with fade
    pause 0.75
    play sound father1 volume 1.6
    father "Сколько можно позорить семью? Я сто раз говорил тебе, забудь про свое эго!"
    stop sound

    play sound father3 volume 1.6
    father "*Сильный кашель*"
    stop sound

    play sound father2 volume 1.3
    father "Но нет, тебе надо спорить, непонятно для чего стоять на своем, тебя вообще не волнует то, что происходит вокруг тебя!"
    stop sound

    play sound young7 volume 0.8
    young_gg "Я же был прав, мой ответ был верным"
    stop sound

    play sound young8 volume 0.8
    young_gg "Она просто меня ненавидит"
    stop sound

    jump continue_1


label continue_1:

    play sound father3 volume 1.6
    father "*Сильный кашель*"
    stop sound

    mother "Пожалуйста, не перечь отцу"

    mother "Ты же сам должен понимать, ведь ты уже почти взрослый"

    play sound young4 volume 0.8
    young_gg "А что я должен понимать?"
    stop sound

    mother "Что иногда есть вещи поважнее личного мнения и амбиций"

    scene bg second2
    with fade
    pause 0.75

    play sound gg6 volume 0.8
    gg "Эх, отец, жалко я тогда не понимал"
    stop sound

    play sound gg7 volume 0.8
    gg "Молодой и глупый, пытающийся доказать всем свою правоту"
    stop sound

    gg "Может и хорошо, что ты не видишь меня сейчас, это было бы сплошное разочарование"

    scene bg sixth
    with fade
    pause 0.75

    stranger "Молодой человек, я пару минут наблюдал за вами"

    gg "Что?"

    stranger "Вы очень занятный человек"

    stranger "Безразличие и чувственность в одном ключе"

    gg "Я не совсем понимаю о чем вы"

    stranger "Считаете ли вы себя лучше всех этих людей?"

    gg "(мысли) Он какой-то странный"

    gg "Что вы от меня хотите?"

    stranger "Только ответов на простые вопросы"

    gg "А если я не собираюсь на них отвечать?"

    stranger "Конечно это ваше право"

    stranger "Но вы все-таки попробуйте сделать это"

    gg "Кто ты вообще такой, чтобы требовать что-то от меня?"

    stranger "Я?"

    stranger "Обычный наблюдатель"

    stranger "И если я замечаю интересные экземпляры, то непременно хочу узнать их поближе и оказать услугу"

    gg "(мысли) Экземпляры?"

    gg "(мысли) Видимо это очередной псих"

    gg "(мысли) Но что-то в нем есть, мне как-будто хочется ему отвечать"
    
    gg "Что вы имеете ввиду под словом экземпляры?"

    stranger "Прошу прощения, возможно я неправильно выразился"

    stranger "Никак не могу запомнить, с кем я веду диалоги"

    stranger "Я имел ввиду людей, интересных людей"

    gg "(мысли) Чем же я его мог заинтересовать"

    stranger "Я вижу в вас некий потенциал и я хочу помочь раскрыть его"

    stranger "Для этого вам всего лишь надо ответь на несколько простых вопросов"

    gg "Хорошо, будь по вашему, надеюсь это не займет много времени"

    stranger "*Усмешка*"
    
    stranger "Буквально пару минут"

    stranger "Надеюсь на вашу искренность"

    stranger "Итак, повторюсь. Считаете ли вы себя лучше всех этих людей?"

    gg "(мысли) Лучше этой толпы?"

    menu:
        "Возможно":
            jump maybe

        "Не думаю":
            jump no



label maybe:

    gg "Возможно"

    stranger "И чем же?"

    gg "Вы же сейчас говорите со мной, а не с ними"

    return

label no:

    gg "Не думаю"

    stranger "Хм"

    stranger "Допустим"

    stranger "На всякий случай напомню, отвечайте искренне"

    return