from keyboards import Keyboard
from processors import Processor
import csv
import json


class Manager:

    def __init__(self,):
        '''
        Атрибути класу
        '''
        self.menu = list()
        self.user_input = input('Choose one\n> ')
        self.filtered_objects = list()
        self.global_menu = 'Would you like to filter or reset?'
        self.menu_2 = list()

    def check_user(self):
        '''
        Перевіряє на коректнісь введення
        :return:правду або неправду
        '''
        if self.user_input.capitalize() == 'Keyboards' or self.user_input.capitalize() == 'Processors':
            return True
        else:
            return False

    def filters_of_processors(self, type_of_sort, value):
        '''
        Фільтрує процесори за критеріями
        :param type_of_sort: вид сортування
        :param value: значення
        '''
        for i in self.menu:
            if type_of_sort.lower() == 'brand':
                if i['additional_fields']['Brand'] == value.capitalize() or \
                        i['additional_fields']['Brand'] == value.upper():
                    obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                    i['additional_fields'])
                    self.filtered_objects.append(obj.category)
                    print(obj)
            elif type_of_sort.lower() == 'processor family':
                if i['additional_fields']['Processor family'] == value:
                    obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                    i['additional_fields'])
                    self.filtered_objects.append(obj.category)
                    print(obj)
            elif type_of_sort.lower() == 'number of cores':
                if i['additional_fields']['Number of cores'] == int(value):
                    obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                    i['additional_fields'])
                    self.filtered_objects.append(obj.category)
                    print(obj)
            elif type_of_sort.lower() == 'type socket':
                if i['additional_fields']['Type socket'] == value.upper():
                    obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                    i['additional_fields'])
                    self.filtered_objects.append(obj.category)
                    print(obj)
            elif type_of_sort.lower() == 'price':
                if i['Price'] == value:
                    obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                    i['additional_fields'])
                    self.filtered_objects.append(obj.category)
                    print(obj)
            elif type_of_sort.lower() == 'quantity':
                if value.capitalize() == 'Available':
                    if i['Quantity'] > '0':
                        obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                        i['additional_fields'])
                        self.filtered_objects.append(obj.category)
                        print(obj)
                elif value.lower() == 'not available':
                    if i['Quantity'] == '0':
                        obj = Processor(i['category'], i['name'], i['Price'], i['Quantity'],
                                        i['additional_fields'])
                        self.filtered_objects.append(obj.category)
                        print(obj)
        print(f'Founded {self.filtered_objects.count("Processors")} {self.obj.category}.')

    def filters_of_keyboards(self, type_of_sort, value):
        '''
        Фільтрує клавіатури за критеріями
        :param type_of_sort: вид сортування
        :param value: значення
        '''
        for i in self.menu:
            if type_of_sort.lower() == 'brand':
                if i['additional_fields']['Brand'] == value:
                    obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'], i['additional_fields'])
                    print(obj)
                    self.filtered_objects.append(obj.category)
            elif type_of_sort.lower() == 'type':
                if i['additional_fields']['Type'] == value.capitalize():
                    obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'], i['additional_fields'])
                    print(obj)
                    self.filtered_objects.append(obj.category)
            elif type_of_sort.lower() == 'connection':
                if i['additional_fields']['Connection'] == value:
                    obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'], i['additional_fields'])
                    print(obj)
                    self.filtered_objects.append(obj.category)

            elif type_of_sort.lower() == 'price':
                if i['Price'] == value:
                    obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'], i['additional_fields'])
                    print(obj)
                    self.filtered_objects.append(obj.category)
            elif type_of_sort.lower() == 'quantity':
                if value.capitalize() == 'Available':
                    if i['Quantity'] > '0':
                        obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'],
                                       i['additional_fields'])
                        print(obj)
                        self.filtered_objects.append(obj.category)
                elif value.lower() == 'not available':
                    if i['Quantity'] == '0':
                        obj = Keyboard(i['category'], i['name'], i['Price'], i['Quantity'],
                                       i['additional_fields'])
                        print(obj)
                        self.filtered_objects.append(obj.category)
        print(f'Founded {self.filtered_objects.count("Keyboards")} {self.obj.category}.')

    def filter(self):
        '''
        Приймає дані від користувача і переходить до потрібного методу сортування
        '''
        while self.check_user() is True:
            print(self.global_menu)
            user_filter = input('Choose one\n>')
            if user_filter.capitalize() == 'Filter':
                self.filtered_objects.clear()
                if self.user_input.capitalize() == 'Keyboards':
                    print(f'Searching for {self.obj.category}, you can filter by: \nPrice \nQuantity \nBrand \nType '
                          f'\nConnection')
                    user_filter_2 = input('Choose one\n>')
                    if user_filter_2.lower() == 'brand':
                        print('Brands:')
                        for i in self.menu:
                            print(i['additional_fields']['Brand'])
                    elif user_filter_2.lower() == 'connection':
                        print('Connection')
                        for i in self.menu:
                            print(i['additional_fields']['Connection'])
                            print('wireless')
                            break
                    elif user_filter_2.lower() == 'quantity':
                        print('Quantity: \navailable\nnot available')
                    elif user_filter_2.lower() == 'type':
                        print('Types:')
                        print('Membrane\nMechanical')
                    elif user_filter_2.lower() == 'price':
                        print('Prices:')
                        for i in self.menu:
                            print(i['Price'],'UAH')
                    user_filter_3 = input('Choose one\n>')
                    self.filters_of_keyboards(user_filter_2, user_filter_3)
                elif self.user_input.capitalize() == 'Processors':
                    print(f'Searching for {self.obj.category}, you can filter by: \nPrice \nQuantity \nBrand'
                          f'\nType socket\nProcessor family\nNumber of cores')
                    user_filter_2 = input('Choose one\n>')
                    if user_filter_2.lower() == 'quantity':
                        print('Quantity: \navailable\nnot available')
                    elif user_filter_2.lower() == 'brand':
                        print('Brands:')
                        print('AMD\nIntel')
                    elif user_filter_2.lower() == 'type socket':
                        print('Sockets:\nAM4\n1200')
                    elif user_filter_2.lower() == 'number of cores':
                        print('Number of cores:')
                        print('6\n4')
                    elif user_filter_2.lower() == 'processor family':
                        print('Processor family:')
                        for i in self.menu:
                            print(i['additional_fields']['Processor family'])
                    elif user_filter_2.lower() == 'price':
                        print('Prices:')
                        for i in self.menu:
                            print(i['Price'],'UAH')
                    else:
                        print('Not correct!')
                        continue

                    user_filter_3 = input('Choose one:\n>')
                    self.filters_of_processors(user_filter_2, user_filter_3)
            elif user_filter.capitalize() == 'Reset':
                del self.menu
                del self.menu_2
                print(f"Internet-shop Tech-stop welcomes you!\nCategories to search in:\n"
                      f"Keyboards\n"
                      f"Processors\n")
                break

    def check_user_print(self):
        '''
        Відповідно до методу <<check_user>> виводить значення прервірки
        '''
        if self.check_user() is False:
            print('Введіть значення з меню')

    def warehouse(self,):
        '''
        Зчитує дані відповідно до обрадного значення користувача і додоає їх до списку для подальшої роботи
        '''
        filename = 'warehouse.csv'
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                json_field = json.loads(row['additional_fields'])
                row['additional_fields'] = json_field
                if row['category'] == self.user_input.capitalize() == 'Keyboards':
                    self.obj = Keyboard(row['category'], row['name'], row['Price'], row['Quantity'], json_field)
                    print(self.obj)
                    self.menu.append(row)
                    self.menu_2.append(self.obj.category)
                elif row['category'] == self.user_input.capitalize() == 'Processors':
                    self.obj = Processor(row['category'], row['name'], row['Price'], row['Quantity'], json_field)
                    print(self.obj)
                    self.menu.append(row)
                    self.menu_2.append(self.obj.category)
            if self.user_input.capitalize() == 'Keyboards':
                print(f'Founded {self.menu_2.count("Keyboards")} {self.obj.category}.')
            elif self.user_input.capitalize() == 'Processors':
                print(f'Founded {self.menu_2.count("Processors")} {self.obj.category}.')

print(f"Internet-shop Tech-stop welcomes you!\nCategories to search in:\n"
      f"Keyboards\n"
      f"Processors")
while True:
    shop_manager = Manager()
    shop_manager.check_user_print()
    shop_manager.warehouse()
    shop_manager.filter()