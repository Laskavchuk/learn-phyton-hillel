def name_(name):
    while True:
        x = input(f"Введіть {name} (повністю): ")
        if len(x) <= 1:
            print("Ви не ввели данні ")
        elif x.isalpha():
            return x
        else:
            print('Приймаються лише літери, не використовуйте числа, пробіли та знаки!')


def print_text():
    x = (f'''
{'-' * 102}
  Dear {name_recipient.title()} {last_name_recipient.title()},                                             

We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa. 
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a. 
   
  ________________
  {name_sender.title()} {last_name_sender.title()}
  {position_of_sender.title()}
{'-' * 102} ''')
    return x

print('*' * 27)
print('Створення офіційного листа!')
print('*' * 27)
name_recipient = name_("Ім'я одержувача")
last_name_recipient = name_('Прізвище одержувача')
name_sender = name_("Ім'я відправика")
last_name_sender = name_('Прізвище відправника')
position_of_sender = name_('Посада відправника')
print(print_text())
