class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} больше разрешенной для данного вида транспорта'
        else:
            return f'Скорость {self.name} допустимая для данного вида транспорта'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} больше разрешенной для данного вида транспорта'
        else:
            return f'Скорость {self.name} допустимая для данного вида транспорта'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это транспорт полицейского департамента'
        else:
            return f'{self.name} этот транспорт не относится к полицейскому департаменту'


kamaz = SportCar(95, 'Белая', 'Камаз', False)
lada = TownCar(25, 'Красная', 'Лада', False)
gazele = WorkCar(110, 'Синяя', 'Газель', True)
volga = PoliceCar(150, 'Черный', 'Волга', True)
print(gazele.turn_left())
print(f'Если {lada.turn_right()}, то {kamaz.stop()}')
print(f'{gazele.name} {gazele.color}')
print(kamaz.show_speed())
print(lada.show_speed())
print(volga.police())
print(volga.show_speed())
