'''
Параметри:
	ціле число (секунди)
Повертає: повідомлення кожної секунди скільки часу залишилось та повідомлення коли час вийшов
Наприклад:
	function(6):
		6
		5
		4
		3
		2
		1
		Тум-тум, 6 секунд вже пройшло!
Підказка: метод sleep з модулю time
'''
from time import sleep


def timer(sec):
    '''

    :param sec: кільксть секунд
    :return: нічого не повертає
    '''
    count = sec + 1
    while count != 1:
        sleep(1)
        count -= 1
        print(count)
    print(f'Тум-тум,{sec} секунд вже пройшло!')


timer(3)
'''
13. Нумерологія)
Складність: 1/5
Параметри:
	ціле число
Повертає: суму цифр числа
Наприклад:
	function(252) -> 9
	function(2022) -> 6
'''


def sum_of_digits(number):
    """Обчислює суму цифр числа."""
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

print(sum_of_digits(2022))