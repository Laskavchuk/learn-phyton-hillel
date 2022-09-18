number = float(input('Введіть число: '))
if number <= -500:
    print(f'Число {number} дорівнює або менше ніж -500')
elif -100 >= number > -500:
    print(f'число {number}, дорівнює або менше ніж -100, але більше -500')
elif 0 > number > -100:
    print(f'число {number}, менше ніж 0, але більше -100')
elif 0 <= number < 100:
    print(f'число {number},дорівнює або більше ніж 0, але менше 100')
elif 100 <= number < 500:
    print(f'число {number},дорівнює або більше ніж 100, але менше 500')
elif number >= 500:
    print(f'число {number},дорівнює або більше ніж 500')