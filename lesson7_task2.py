class Clothes:
    # Определяем параметры одежды: size (размер) - для пальто, height (рост) - для костюма
    def __init__(self, size, height):
        self.size = size
        self.height = height

    # Определяем метод расхода ткани для пошива пальто
    def expense_coat(self):
        return self.size / 6.5 + 0.5

    # Определяем метод расхода ткани для пошива костюма
    def expense_suit(self):
        return self.height * 2 + 0.3

    # Встраиваем декоратор property c методом определения общего расхода ткани
    @property
    def expense_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}' " м.кв.")

    # Определяем класс "Пальто"
class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.expense_coat = (self.size / 6.5 + 0.5)
    # В окончательном расчете предусматриваем округление значения до двух знаков после запятой
    def __str__(self):
        return f'Площадь ткани на пошив пальто {self.expense_coat:.2f}' " м.кв."

    # Определяем класс "Костюм"
class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.expense_suit = (self.height * 2 + 0.3)
    # В окончательномрасчете предусматриваем округление значения до двух знаков после запятой
    def __str__(self):
        return f'Площадь ткани на пошив костюма {self.expense_suit:.2f}' " м.кв."

    # Определяем параметр "размер" для расчета расхода ткани на пошив пальто. Пусть он равен 50
coat = Coat(50, 0)

    # Определяем параметр "рост" для расчета расхода ткани на пошив костюма. Пусть он равен 180 см (1,8 м)
suit = Suit(0, 1.8)

print(coat)
print(suit)
print(coat.expense_full)

