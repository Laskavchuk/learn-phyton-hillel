def read_quadrangle_vertice(name):
    while True:
        x = input(f'{name} = ')
        try:
            x = float(x)
        except Exception:
            print('Це не число!')
            continue
        if x > 0:
            return x
        else:
            print('Це число не може бути в чотирикутнику!')


def does_square_is(a, b, c, d):
    if a == b and a == c and a == d and pow(a**2+b**2, 1/2) == pow(c**2+b**2, 1/2):
        return True


def does_rectangle_is(a, b, c, d):
    if pow(a, 2) + pow(b, 2) == pow(c, 2) + pow(d, 2):
        print("Це є прямокутник ")
        return True
    else:
        print("Це не є прямокутник ")
        return False


def the_area_of_the_rectangle(a, b):
    return a*b
print('*' * 32)
print('Перевірка опуклого чотирикунтка!')
print('*' * 32)

a = read_quadrangle_vertice('a')
b = read_quadrangle_vertice('b')
c = read_quadrangle_vertice('c')
d = read_quadrangle_vertice('d')
if does_square_is(a, b, c, d):
    print('Це квадрат ')
elif does_rectangle_is(a, b, c, d):
    print(f'Площа прямокутника = {the_area_of_the_rectangle(a, b)} ')



