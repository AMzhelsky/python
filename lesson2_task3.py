seasons_list = ['ЗИМА', 'ВЕСНА', 'ЛЕТО', 'ОСЕНЬ']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Пользователь вводит номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict.get(4))
