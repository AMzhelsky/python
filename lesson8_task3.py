class Error(Exception):
    def __init__(self, my_list):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значение и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Введенное значение не является числом. Введите число")
                y_or_n = input(f'Продолжить выполнение? Y/N ')

                if y_or_n == 'Y':
                    print(try_except.my_input())
                elif y_or_n == 'N':
                    return f'Выполнение программы завершено'
                else:
                    return f'Выполнение программы завершено'

try_except = Error(1)
print(try_except.my_input())