el_count = int(input("Пользователь вводит количество элементов списка: "))
my_list = []
a = 0
el = 0
while a < el_count:
    my_list.append(input("Пользователь вводит следующее значение списка: "))
    a += 1

for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
