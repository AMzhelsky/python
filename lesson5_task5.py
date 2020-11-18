def summary():
    try:
        with open('text_5.txt', 'w+') as file_obj:
            line = input('Пользователь вводит числа через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка. Введенный символ не является числом')
summary()
