def convert_dollar_to_uah():
    if 'Долар' in user.title() or '1' in user or '$' in user:
        dollar = float(input("Введіть кількість доларів, яку будемо конвертувати: "))
        return round(course_dollar * dollar, 2)


def convert_uah_to_dollar():
    if 'Гривня' in user.title() or '2' in user or 'UAH' in user.upper() or 'Гривню' in user.title():
        uah = float(input("Введіть кількість гривень, яку будемо конвертувати: "))
        return round(uah / course_dollar, 2)


print('''
Меню:
1. Долар, $
2. Гривня, UAH
''')

user = input('Виберіть, що будемо коневертувати?: ')
print('Ціна 1 долара (курс) за замовчуванням = 36.92 UAH')
user_choice = input('Бажаєте змінити курс?:  ')
if 'Так' in user_choice.title():
    course_dollar = float(input('Введіть ціну 1 долара (курс): '))
else:
    course_dollar = 36.92

if 'Гривня' in user.title() or '2' in user or 'UAH' in user.upper() or 'Гривню' in user.title():
    print(convert_uah_to_dollar(), '$')
else:
    print(convert_dollar_to_uah(), 'UAH')





