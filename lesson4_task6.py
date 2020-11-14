from itertools import count

for el in count(int(input('Введите стартовое число от 1 до 100: '))):
    if el > 1000:
        break
    else:
        print(el)
from itertools import cycle

my_list = ['очень', 'трудная', 'задача', '-', 'сломал', 'всю', 'голову']
c = 0
for el in cycle(my_list):
    if c > 21:
        break
    print(el)
    c += 1
