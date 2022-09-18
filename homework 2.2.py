while True:
    print('''
    Спілкування з ботом!
    Виберіть слова зі списку:
    Привіт / Хай / Доброго дня
    Як справи? / Що робиш? / Чим займаєшся?
    Фільм / Кінотеатр / Серіал
    Бувай / Надобраніч / Гудбай
    ''')
    user_text = input('Ведіть слово: ')
    if 'привіт' in user_text.lower() or 'хай' in user_text.lower() or 'доброго дня' in user_text.lower():
        print('Доброго вечора, я бот з України!')
    elif 'як справи?' in user_text.lower() or 'що робиш?' in user_text.lower() or 'чим займаєшся?' in user_text.lower():
        print('Вчусь програмувати на Python!')
    elif 'фільм' in user_text.lower() or 'кінотеатр' in user_text.lower() or 'серіал' in user_text.lower():
        print('Соррі що втручаюсь, не знаю про що йдеться мова, але подивіться серіал *Гострі козирьки*, він просто бомба!')
    elif 'бувай' in user_text.lower() or 'надобраніч' in user_text.lower() or 'гудбай' in user_text.lower() or 'до зустрічі' in user_text.lower():
        print(" Побачимось у мережі, I'll be back.")
        break
    else:
        print('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :( ')
