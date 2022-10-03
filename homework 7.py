def ask_of_user():
    '''
    Функція запитує, чи бажає користувач ввести, яку кількість нотаток показати.
    А також виконує перевірку на некоректе введеня.
    :return: повертає відповідь користувача
    '''
    while True:
        ask = input('Бажаєте ввести, яку кількісьт покзати? ')
        if len(ask) <= 0:
            print('Ви не ввели значення!')
        elif ask.lower() == 'так':
            return ask
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
        :return: повертає, як сортувати список
    '''
    if len(choice) <= 0:
        print('Ви не ввели значення!')
    elif choice.lower() == 'add' or choice == '1':
        return add_note()
    elif choice.lower() == 'earliest' or choice == '2':
        return earliest_func(earliest='\n''Від найранішої до найпізнішої:')
    elif choice.lower() == 'latest' or choice == '3':
        return latest_func(latest='\n''Від найпізнішої до найранішої:')
    elif choice.lower() == 'shortest' or choice == '4':
        return shortest_func(shortest='\n''Від найкоротшої до найдовшої:')
    elif choice.lower() == 'longest' or choice == '5':
        return longest_func(longest='\n''Від найдовшої до найкоротшоЇ:')
    else:
        print('Введіть щось з переліченого!')


def elements_list(element):
    '''
    Функція додає елементи в список і виконує перевірку на некоректне введення.
    :param element: нотаток
    :return: нічого не повернтає
    '''
    while True:
        if len(element) <= 0:
            print('Ви не ввели нотатку')
            element = input('Введіть нотатку:')
        else:
            list_of_notes.append(element)
            break


def add_note():
    '''
    Функція слугує для зчитування елементу
    :return: повертає введений елемент
    '''
    return elements_list(element=input('Введіть нотатку:'))


def earliest_func(earliest):
    '''
    Функція виконує сортування списка.
    :param earliest: назва сортування
    :return: повертає сортування
    '''
    if ask_of_user():
        list_of_notes_sorted = list_of_notes[:change_list()]
        print(earliest)
        for elem in list_of_notes_sorted:
            print(elem)
        return earliest
    else:
        print(earliest)
        for elem in list_of_notes:
            print(elem)
        return earliest


def latest_func(latest):
    '''
    Функція виконує сортування списка.
    :param latest: назва сортування
    :return: повертає сортування
    '''
    if ask_of_user():
        list_of_notes_sorted = list_of_notes[::-1]
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(latest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return latest
    else:
        print(latest)
        for elem in list_of_notes[::-1]:
            print(elem)
        return latest


def shortest_func(shortest):
    '''
    Функція виконує сортування списка.
    :param shortest: назва сортування
    :return: повертає сортування
    '''
    if ask_of_user():
        list_of_notes_sorted = sorted(list_of_notes, key=len)
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(shortest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return shortest
    else:
        print(shortest)
        for elem in sorted(list_of_notes, key=len):
            print(elem)
        return shortest


def longest_func(longest):
    '''
    Функція виконує сортування списка.
    :param longest: назва сортування
    :return: повертає сортування
    '''
    if ask_of_user():
        list_of_notes_sorted = sorted(list_of_notes, key=len, reverse=True)
        list_of_notes_sorted_2 = list_of_notes_sorted[:change_list()]
        print(longest)
        for elem in list_of_notes_sorted_2:
            print(elem)
        return longest
    else:
        print(longest)
        for i in sorted(list_of_notes, key=len, reverse=True):
            print(i)
        return longest


list_of_notes = []
while True:
    menu =print( '''
Введіть щось з перелічуваного: 
1.add  
2.earliest 
3.latest 
4.shortest 
5.longest
''')
    user_choice(choice=input('Ваш вибір: '))