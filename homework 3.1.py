def choice():   # Функція зчитує значення ведене користуачем
    while True:
        x = input('Виберіть, що будемо коневертувати?: ')
        if '1' in x or '2' in x or 'Долар' in x.title() or 'Долари' in x.title() or 'Гривня' in x.title() or 'Гривню' \
                in x.title() or 'Гривні' in x.title() or 'UAH' in x.upper() or '$' in x:
            return x
        else:
            print('Виберіть те, що є в меню ')


def change_course():    # Функція зчитує значення ведене користуачем
    while True:
        x = input('Бажаєте змінити курс?:  ')
        if 'Так' in x.title() or 'Ні' in x.title():
            return x
        else:
            print('Введіть "Так" або "Ні"')


def course():   # Функція зчитує значення ведене користуачем
    if 'Так' in user_choice.title():
        x = float(input('Введіть ціну 1 долара (курс): '))
    else:
        x = 36.92
    return x


def convert_dollar_to_uah():    # Функція конвертує долар в гривню
    if 'Долар' in user.title() or '1' in user or '$' in user or 'Долари' in user.title():
        dollar = float(input("Введіть кількість доларів, яку будемо конвертувати: "))
        return round(course_dollar * dollar, 2)


def convert_uah_to_dollar():    # Функція конвертує гривню в долар
    if 'Гривня' in user.title() or '2' in user or 'UAH' in user.upper() or 'Гривні' in user.title() \
            or 'Гривню' in user.title():
        uah = float(input("Введіть кількість гривень, яку будемо конвертувати: "))
        return round(uah / course_dollar, 2)


print('''
Меню:
1. Долар, $
2. Гривня, UAH
''')
user = choice()
print('Ціна 1 долара (курс) за замовчуванням = 36.92 UAH')
user_choice = change_course()
course_dollar = course()
if 'Гривня' in user.title() or '2' in user or 'UAH' in user.upper() or 'Гривню' in user.title() \
        or 'Гривні' in user.title():
    print(convert_uah_to_dollar(), '$')
else:
    print(convert_dollar_to_uah(), 'UAH')





