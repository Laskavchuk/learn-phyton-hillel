class Shop:

    def __init__(self, category_object, category, name, price, quantity):
        '''
        Атрибути
        :param category_object: Категорія товару
        :param category: Категорія товару
        :param name: Назва
        :param price: Ціна
        :param quantity: Кількість
        '''
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity
        self.Category_object = category_object

    def check(self):
        '''
        Перевіряє чи є товар чи ні
        :return: результат перевірки
        '''
        if self.quantity == '0':
            s = 'not available'
            return s
        else:
            s = 'is available'
            return s

    def __str__(self):
        '''
        Виводить дані
        :return: дані
        '''
        s = f'{self.Category_object}\n{self.name}\nPrice:{self.price} UAH\n{self.check()}\n'
        return s



















