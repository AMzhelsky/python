class Data:
    def __init__(self, day_month_year):
        # self.day = день
        # self.month = месяц
        # self.year = год
        self.day_month_year = str(day_month_year)

    # Реализуем декоратор @classmetod
    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])
    
    # Реализуем декоратор @staticmetod
    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все правильно'
                else:
                    return f'В дате указан неправильный год'
            else:
                return f'В дате указан неправильный месяц'
        else:
            return f'В дате указан неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('26 - 11 - 2020')
print(today)
print(Data.valid(36, 11, 2020))
print(Data.valid(26, 14, 2020))
print(Data.valid(26, 11, 2030))
print(today.valid(26, 11, 2020))
print(Data.extract('26 - 11 - 2020'))
print(today.extract('26 - 11 - 2020'))


