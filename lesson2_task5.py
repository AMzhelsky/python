my_list = [9, 8, 8, 6, 5, 4, 2, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Пользователь вводит натуральное число: "))
for el in range(len(my_list)):
    if my_list[el] == digit:
        my_list.insert(el + 1, digit)
        break
    elif my_list[0] < digit:
        my_list.insert(0, digit)
    elif my_list[-1] > digit:
        my_list.append(digit)
    elif my_list[el] > digit and my_list[el + 1] < digit:
        my_list.insert(el + 1, digit)
        break
print(f"текущий список - {my_list}")
