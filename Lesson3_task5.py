def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Пользователь вводит число, кроме специального символа x:  ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'x' or number[el] == 'x':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()