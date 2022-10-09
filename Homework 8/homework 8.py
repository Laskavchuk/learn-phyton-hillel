import os


def save_notes(save):
    '''
    Функція зберігає нотатки у файл, виконує перевірку чи є ноатки у списку (щоб не вводити пустоту)
    :param save: Збереження нотаток
    :return: нічого
    '''
    print(save)
    filename = 'Notes.'
    if len(notes(list_of_notes)) == 0:
        print('Ви не ввели нотатки!')
    elif os.path.exists(filename):
        if ask_of_user_save_notes():
            with open(filename, 'a') as fp:
                for element in notes(list_of_notes):
                    fp.write(element)
                    fp.write('\n')
                print('Нотатки збережено!')
                clear_list(list_of_notes)
        else:
            with open(filename, 'w') as fp:
                for element in notes(list_of_notes):
                    fp.write(element)
                    fp.write('\n')
                print('Нотатки збережено!')
            clear_list(list_of_notes)

    else:
        with open(filename, 'w') as fp:
            for element in notes(list_of_notes):
                fp.write(element)
                fp.write('\n')
            print('Нотатки збережено!')
        clear_list(list_of_notes)


def load_notes(load, load_list):
    '''
    Функція завантажує нотатки із файлу і додає їх до списку, а також виконує перевірку чи існує файл
    :param load: Завантаження нотаток
    :param load_list: Список
    :return: Нічого не повертає
    '''
    print(load)
    filename = 'Notes.'
    if os.path.exists(filename) is False:
        print('Файла не знайдено!')
    else:
        with open(filename, 'r') as fp:
            print(fp.read())
        filename = 'Notes.'
        with open(filename) as fp:
            for line in fp:
                load_list.append(line.strip())


def clear_notes(clear):
    '''
    Функція стирає всі нотатки і видаляє файл, а також виконує перевірку чи існує файл
    :param clear: Видалення нотаток
    :return: нічого
    '''
    print(clear)
    filename = 'Notes.'
    if os.path.exists(filename) is False:
        print('Файл не знайдено!')
        print('Нотатки із списку видалено успішно!')
    else:
        os.remove(filename)
        print('Файл і нотатки із списку видалено успішно!')
    clear_list(list_of_notes)


def ask_of_user_save_notes():
    '''
    Функція запитує, чи бажає користувач добавити нотатки стираючи попередні.
    А також виконує перевірку на некоректе введеня.
    :return: правду
    '''
    while True:
        ask = input('Бажаєте добавити нотатки стираючи попередні? ')
        if len(ask) <= 0:
            print('Ви не ввели значення!')
        elif ask.lower() == 'так':
            break
        elif ask.lower() == 'ні':
            return True
        else:
            print('Введіть так або ні')


def ask_of_user():
    '''
    Функція запитує, чи бажає користувач ввести, яку кількість нотаток показати.
    А також виконує перевірку на некоректе введеня.
    :return: правду
    '''
    while True:
        ask = input('Бажаєте ввести, яку кількісьт покзати? ')
        if len(ask) <= 0:
            print('Ви не ввели значення!')
        elif ask.lower() == 'так':
            return True
        elif ask.lower() == 'ні':
            break
        else:
            print('Введіть так або ні')


def change_list():
    '''
    Функція запитує, яку кількість нотаток показати.
    А також виконує перевірку на некоректе введеня.
    :return: повертає, яку кількість нотаток показати
    '''
    while True:
        part = input('Введіть яку кількість показати: ')
        try:
            part = int(part)
        except:
            print('Приймаються лише цифри')
            continue
        if part <= 0:
            print('Ви не ввели значення!')
        else:
            return part


def user_choice(choice):
    '''
    Функція запитує, вибір користувача з меню, вокнує перевірку на некоректне введення.
    :return: вибір користувача
    '''
    if len(choice) <= 0:
        print('Ви не ввели значення!')
    elif choice.lower() == 'add' or choice == '1':
        elements_list(list_of_notes)
    elif choice.lower() == 'earliest' or choice == '2':
        earliest_func(earliest='\n''Від найранішої до найпізнішої:')
    elif choice.lower() == 'latest' or choice == '3':
        latest_func(latest='\n''Від найпізнішої до найранішої:')
    elif choice.lower() == 'shortest' or choice == '4':
        shortest_func(shortest='\n''Від найкоротшої до найдовшої:')
    elif choice.lower() == 'longest' or choice == '5':
        longest_func(longest='\n''Від найдовшої до найкоротшоЇ:')
    elif choice.lower() == 'save' or choice == '6':
        save_notes(save='\n''Збереження нотаток:')
    elif choice.lower() == 'load' or choice == '7':
        load_notes(load='\n''Завантаження нотаток:', load_list=list_of_notes)
    elif choice.lower() == 'clear' or choice == '8':
        clear_notes(clear='\n''Видалення нотаток:')
    elif choice.lower() == 'exit':
        return choice
    else:
        print('Введіть щось з переліченого!')


def elements_list(global_list):
    '''
    Функція додає елементи в список і виконує перевірку на некоректне введення.
    :return: нічого не повернтає
    '''
    while True:
        element = input('Введіть нотатку: ')
        if len(element) <= 0:
            print('Ви не ввели нотатку')
        else:
            global_list.append(element)
            break


def clear_list(list_change):
    '''
    Функція видаляє усі елементи зі списку
    :param list_change: список з global scope
    :return: пустий список
    '''
    return list_change.clear()


def notes(list_overwriting):
    '''
    Функція перезаписуює список з global scope
    :param list_overwriting: список з global scope
    :return: перезаписаний список
    '''
    return list_overwriting


def earliest_func(earliest):
    '''
    Функція виконує сортування списка.
    :param earliest: назва сортування
    :return: нічого не повернтає
    '''
    if ask_of_user():
        list_of_notes_sorted = notes(list_of_notes[:change_list()])
        print(earliest)
        for elem in list_of_notes_sorted:
            print(elem)
        return
    else:
        print(earliest)
        for elem in notes(list_of_notes):
            print(elem)
        return


def latest_func(latest):
    '''
    Функція виконує сортування списка.
    :param latest: назва сортування
    :return: нічого не повернтає
    '''
    if ask_of_user():
        list_of_notes_sorted = notes(list_of_notes[::-1])
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(latest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return
    else:
        print(latest)
        for elem in notes(list_of_notes[::-1]):
            print(elem)
        return


def shortest_func(shortest):
    '''
    Функція виконує сортування списка.
    :param shortest: назва сортування
    :return: нічого не повернтає
    '''
    if ask_of_user():
        list_of_notes_sorted = sorted(notes(list_of_notes), key=len)
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(shortest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return
    else:
        print(shortest)
        for elem in sorted(notes(list_of_notes), key=len):
            print(elem)
        return


def longest_func(longest):
    '''
    Функція виконує сортування списка.
    :param longest: назва сортування
    :return: нічого не повернтає
    '''
    if ask_of_user():
        list_of_notes_sorted = sorted(notes(list_of_notes), key=len, reverse=True)
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(longest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return
    else:
        print(longest)
        for i in sorted(notes(list_of_notes), key=len, reverse=True):
            print(i)
        return


list_of_notes = []


while True:
    print('''
Введіть щось з перелічуваного: 
1.add  
2.earliest 
3.latest 
4.shortest 
5.longest
6.save
7.load
8.clear
EXIT
''')
    if user_choice(choice=input('Ваш вибір: ').lower()) == 'exit':
        break