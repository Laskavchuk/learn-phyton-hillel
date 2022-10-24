class Triangle:
    def __init__(self, side_a, side_b, side_c):
        '''
        Передається довжина сторін трикутника та зберігаються у атрібутах класу
        :param side_a: сторона "a"
        :param side_b: сторона "b"
        :param side_c: сторона "c"
        '''
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def exists(self):
        '''
        Перевіряє чи існує трикутник
        :return: правду чи не правду
        '''
        if self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b and self.side_b + \
                self.side_c > self.side_a:
            return True
        else:
            return False

    def print_exists(self):
        '''
        :return: результат існування трикутника
        '''
        if self.exists() is True:
            s = "існує"
            return s
        else:
            s = "не існує"
            return s

    def is_the_triangle_isosceles(self):
        '''
        Перевіряє чи трикутник рівнобедрений
        :return: правду чи не правду
        '''
        if self.side_a == self.side_b and self.exists() is True or self.side_a == self.side_c and self.exists() \
                is True or self.side_b == self.side_c and self.exists() is True:
            return True
        else:
            return False

    def is_the_triangle_equilateral(self):
        '''
        Перевіряє чи трикутник рівносторонній
        :return: правду або не правду
        '''
        if self.side_a == self.side_b == self.side_c and self.exists() is True:
            return True
        else:
            return False

    def triangle_type(self):
        '''
        :return: результат перевірки на вид трикутника
        '''
        if self.is_the_triangle_equilateral() is True:
            s = 'рівносторонній'
            return s
        elif self.is_the_triangle_isosceles() is True:
            s = 'рівнобедрений'
            return s
        elif self.exists() is True:
            s = 'різносторонній'
            return s

    def perimetr(self):
        '''
        Виконує пошук периметра, якщо трикутник існує
        :return: значення периметра
        '''
        if self.exists() is True:
            perimetr = self.side_a + self.side_c + self.side_b
            return perimetr

    def area_of_triangle_equilateral(self):
        '''
        Знаходить площу трикутника, якщо він рівносторонній (можна знаходити і за формулою Герона)
        :return: значення площі, округлене до 2 знаків після коми
        '''
        if self.is_the_triangle_equilateral() is True:
            area = (pow(self.side_a, 2)*pow(3, 0.5))/4
            return round(area, 2)

    def triangle_area(self):
        '''
        Знаходить площу трикутника за формулою Герона
        :return: значення площі, округлене до 2 знаків після коми
        '''
        p = self.perimetr()/2
        area = pow(p * (p - self.side_a) * (p - self.side_b) * (p-self.side_c), 0.5)
        return round(area, 2)

    def __str__(self):
        '''
        :return: результати роботи методів
        '''
        if self.exists() is True and self.is_the_triangle_equilateral() is True:
            s = (f'Трикутник зі сторорнами: {self.side_a}, {self.side_b}, {self.side_c} - {self.print_exists()}, '
                  f'є {self.triangle_type()}, '
                  f'периметр = {self.perimetr()}, площа = {self.area_of_triangle_equilateral()}')
            return s
        elif self.exists() is True:
            s = (f'Трикутник зі сторорнами: {self.side_a}, {self.side_b}, {self.side_c} - {self.print_exists()}, '
                  f'є {self.triangle_type()}, '
                  f'периметр = {self.perimetr()}, площа = {self.triangle_area()}')
            return s
        else:
            s = (f'Трикутник зі сторорнами: {self.side_a}, {self.side_b}, {self.side_c} - {self.print_exists()}')
            return s


if __name__ == '__main__':
    triangle_1 = Triangle(side_a=5, side_b=5, side_c=5)
    print(triangle_1)

    triangle_2 = Triangle(side_a=6, side_b=10, side_c=8)
    print(triangle_2)

    triangle_3 = Triangle(side_a=6, side_b=4, side_c=6)
    print(triangle_3)

    triangle_4 = Triangle(side_a=6, side_b=10, side_c=2)
    print(triangle_4)

    triangle_5 = Triangle(side_a=7.5, side_b=4.8, side_c=5)
    print(triangle_5)
