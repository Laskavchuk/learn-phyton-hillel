class Shop:

    def __init__(self, category_object, category, name, price, quantity):
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity
        self.Category_object = category_object

    def check(self):
        if self.quantity == '0':
            s = 'not available'
            return s
        else:
            s = 'is available'
            return s

    def __str__(self):
        s = f'{self.Category_object}\n{self.name}\nPrice:{self.price} UAH\n{self.check()}\n'
        return s



















