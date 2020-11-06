my_list = [404, "строка", [100, "список", None], (tuple('кортеж')), set('множество'), dict(key1='a', key_2='b'), True]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
