my_list = [48, 52, 11, 8, 104, 1, 300, 17, 66, 182, 183, 180, 200]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
