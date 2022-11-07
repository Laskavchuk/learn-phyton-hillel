from shop import Shop


class Processor(Shop):
    def __init__(self, category, name, price, quantity, additional_fields):
        super(Processor, self).__init__('Processor',category, name, price, quantity)
        self.additional_fields = additional_fields

    def __str__(self):
        s = super(Processor, self).__str__()
        s += f'Brand: {self.additional_fields["Brand"]}\nProcessor family: {self.additional_fields["Processor family"]}\n'\
             f'Type socket: {self.additional_fields["Type socket"]}\n'\
             f'Number of cores {self.additional_fields["Number of cores"]}\n...'
        return s
