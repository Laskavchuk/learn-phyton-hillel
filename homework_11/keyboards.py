from shop import Shop


class Keyboard(Shop):
    def __init__(self, category, name, price, quantity, additional_fields):
        super(Keyboard, self).__init__('Keyboard', category, name, price, quantity)
        self.additional_fields = additional_fields

    def __str__(self):
        s = super(Keyboard, self).__str__()
        s += f'Brand: {self.additional_fields["Brand"]}\nType: {self.additional_fields["Type"]}\n'\
             f'Connection: {self.additional_fields["Connection"]}\n...'
        return s
    '''
    def __str__(self):
        s = (f'Keyboard\n{self.name}\nPrice:{self.Price} UAH\n{self.check()}\n'
             f'Brand: {self.additional_fields["Brand"]}\nType: {self.additional_fields["Type"]}\n'
             f'Connection: {self.additional_fields["Connection"]}\n...')
        return s '''



