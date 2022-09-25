my_list = []
while True:
    user = input('Введіть число: ')
    if user.lower() == 'sum':
        print(sum(my_list))
        break
    try:
        user = float(user)
        my_list.append(user)
    except:
        print('Введіть число або sum будь-ласка!')
        continue















