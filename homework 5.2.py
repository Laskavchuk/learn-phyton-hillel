def name_recipient():
    while True:
        name = input("Введіть ім'я одержувача (повністю): ")
        if len(name) <= 1:
            print("Ви не вели ім'я!")
        elif name.isalpha():
            return name
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')


def last_name_recipient():
    while True:
        last_n = input('Введіть прізвище одержувача (повністю): ')
        if len(last_n) <= 1:
            print("Ви не вели прізвище!")
        elif last_n.isalpha():
            return last_n
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')


def name_sender():
    while True:
        name = input("Введіть ім'я відправника (повністю): ")
        if len(name) <= 1:
            print("Ви не вели ім'я!")
        elif name.isalpha():
            return name
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')


def last_name_sender():
    while True:
        last_n = input("Прізвище відправника (повністю): ")
        if len(last_n) <= 1:
            print("Ви не вели прізвище!")
        elif last_n.isalpha():
            return last_n
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')


def position_of_sender():
    while True:
        position = input('Посада відправника: ')
        if len(position) <= 1:
            print("Ви не вели посаду!")
        elif position.isalpha():
            return position
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')

print('*' * 27)
print('Створення офіційного листа!')
print('*' * 27)
name_recipient = name_recipient()
last_name_recipient = last_name_recipient()
name_sender = name_sender()
last_name_sender = last_name_sender()
position_of_sender = position_of_sender()
print('*' * 25)
print('''Зачекайте декілька секунд,
лист генерується!''')
print('*' * 25)
import time
time.sleep(5)

print(f'''
{'-' * 102}
  Dear {name_recipient.title()} {last_name_recipient.title()},                                             

We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa. 
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a. 
   
  ________________
  {name_sender.title()} {last_name_sender.title()}
  {position_of_sender.title()}
{'-' * 102}
''')