import json
from pprint import pprint
from uuid import uuid4


def display_student_data(d):
    """
    Читабельно та репрезентативно формує рядок для виведення повних даних про одного працівника
    :param d: повні дані про одного працівника
    :return: повертає сформований рядок про працівника
    """
    return f'{d["name"]} working {d["category"]} with rating {d["rating"]}/10'


def view_index(index_name, index_to_view, source_uid_data):
    '''
    Функція виводить на екран у читальному репрезентативному вигляді
    працівників, розділених за ознакою index_name (index_to_view)
    :param index_name: назва індексу для вводу
    :param index_to_view:сам індекс, словник списком.
        Ключі словника – унікальні значення в індексі
        значення словника - списки унікальних айдішників працівників (посилання на повні дані)
    :param source_uid_data: повні дані студентів промарковані своїм унікальним айдішником
    :return: нічого не повертає
    '''
    print(f'Workers by {index_name.capitalize()}')
    for key, values in index_to_view.items():
        print(f'Displaying {key} workers:')
        for uid in values:
            print(f'  {display_student_data(source_uid_data[uid])}')


def read_file(data_workers, uid_workers):
    '''
    Функція читає json, додає кожному працівнику унікальний індекс
    :param data_workers: дані з json
    :param uid_workers: унікальний індекс кожного студента
    :return: повертає індексований файл
    '''
    for employee_data in data_workers:
        # присвоєння унікального індекса для кожного працівника
        employee_data['uid'] = str(uuid4())
        # додавання силки на повні дані працівника в індекс айдішників
        uid_workers[employee_data['uid']] = employee_data
    print(uid_workers)
    return data_workers


def category_sort(category, data_work):
    '''
    Функція добавляє індекси працівників до відповідної групи, а також зюерігає дані
    :param category: група 'категорія'
    :param data_work: дані  з json
    :return: нічого не повертає
    '''
    for employee_data in data_work:
        if employee_data['category'] in category:
            category[employee_data['category']].append(employee_data['uid'])
            # якщо факультету немає в переліку покажчика (індексу), створюємо поле під працівників
            # додаємо першого працівника туди
        else:
            category[employee_data['category']] = list()
            category[employee_data['category']].append(employee_data['uid'])
    pprint(category)
    # зберігаємо дані про працівників у форматі списку
    json.dump(category_index, open('category_index.json', 'w'), indent=4)


def rating_sort(rating, data_work_copy):
    '''
    Функція добавляє індекси працівників до відповідної групи, а також збергіє дані
    :param rating: група 'рейтинг'
    :param data_work_copy: дані з json
    :return: нічого не повертає
    '''
    for employee_data in data_work_copy:
        if employee_data['rating'] in rating:
            rating[employee_data['rating']].append(employee_data['uid'])
            # якщо факультету немає в переліку покажчика (індексу), створюємо поле під працівників
            # додаємо першого працівника туди
        else:
            rating[employee_data['rating']] = list()
            rating[employee_data['rating']].append(employee_data['uid'])
    pprint(rating)
    # зберігаємо дані про працівників у форматі списку
    json.dump(rating_index, open('rating_index.json', 'w'), indent=4)


data = json.load(open('workers.json', mode='r'))
category_index = dict()
uid_index = dict()
rating_index = dict()
pprint(read_file(data, uid_index))
# групування індексів за категорією
category_sort(category_index, data)
# групування індексів за рейтингом
rating_sort(rating_index, data)
# перегляд у розрізі катогорії
view_index('category', category_index, uid_index)
print('#' * 10)
# перегляд у розрізі рейтинг
view_index('rating', rating_index, uid_index)


