from sys import argv

name, time, salary, bonus, tax = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    tax = int(tax)
    res = time * salary + bonus - tax
    print(f'Заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
