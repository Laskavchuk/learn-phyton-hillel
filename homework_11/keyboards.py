from shop import Shop


class Keyboard(Shop):
    def __init__(self, category, name, price, quantity, additional_fields):
        '''
        Атрибути класу
        :param category: Категорія
        :param name: Назва
        :param price: Ціна
        :param quantity: Кількість
        :param additional_fields: дадоткова інформація
        '''
        super(Keyboard, self).__init__('Keyboard', category, name, price, quantity)
        self.additional_fields = additional_fields

    def __str__(self):
        '''
        Виводить дані
        :return: дані
        '''
        s = super(Keyboard, self).__str__()
        s += f'Brand: {self.additional_fields["Brand"]}\nType: {self.additional_fields["Type"]}\n'\
             f'Connection: {self.additional_fields["Connection"]}\n...'
        return s



