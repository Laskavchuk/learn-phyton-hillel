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
    if user_text.capitalize() == 'Привіт' or user_text.capitalize() == 'Хай' or user_text.capitalize() == 'Доброго дня':
        print('Доброго вечора, я бот з України!')
    elif user_text.capitalize() == 'Як справи?' or user_text.capitalize() == 'Що робиш?' or user_text.capitalize() == 'Чим займаєшся?':
        print('Вчусь програмувати на Python!')
    elif user_text.capitalize() == 'Фільм' or user_text.capitalize() == 'Кінотеатр' or user_text.capitalize() == 'Серіал':
        print('Соррі що втручаюсь, не знаю про що йдеться мова, але подивіться серіал *Гострі козирьки*, він просто бомба!')
    elif user_text.capitalize() == 'Бувай' or user_text.capitalize() == 'Надобраніч' or user_text.capitalize() == 'Гудбай' or user_text.capitalize() == 'До зустрічі':
        print(" Побачимось у мережі, I'll be back.")
        break
    else:
        print('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :( ')
