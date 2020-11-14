my_list = [27, 14, 14, 45, 108, 11, 2, 55, 55, 1009]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
