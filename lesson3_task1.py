def div(*args):
    try:
        arg1 = int(input("Пользователь вводит первое число: "))
        arg2 = int(input("Пользователь вводит второе число "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Вы не можете использовать ноль в качестве второго числа"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'result  {div()}')
