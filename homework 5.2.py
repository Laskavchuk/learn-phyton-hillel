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
    y = (f'''
{'-' * 102}
  Dear {name_("Ім'я одержувача").title()} {name_('Прізвище одержувача').title()},                                             

We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa. 
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a. 
   
  ________________
  {name_("Ім'я відправика").title()} {name_('Прізвище відправника').title()}
  {name_('Посаду відправника').title()}
{'-' * 102} ''')
    return y

print('*' * 27)
print('Створення офіційного листа!')
print('*' * 27)
print(print_text())