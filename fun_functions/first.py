def side_spisok(user_input=input('left or right: ')):
    if user_input.lower() == 'left':
        return True
    elif user_input.lower() == 'right':
        return False


def sort_spisok(step, my_list):
    if len(my_list) < step:
        return list()
    if side_spisok() is True:
        return my_list[:step]
    elif side_spisok() is False:
        return my_list[-step:]


spisok = [5, 6, 3, 2, 1]
print(sort_spisok(int(input()), spisok))
