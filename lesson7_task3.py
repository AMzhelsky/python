class Cell:
    # Определяем параметр quantity, соответствующий количеству ячеек клетки
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "$"}'

    # реализуем метод перегузки арифметических операторов: сложение (__add__)
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    # реализуем метод перегузки арифметических операторов: вычитание (__sub__)
    def __sub__(self, other):
        # ограничиваем выполнение операции условием: "Разность количества ячеек двух клеток должна быть больше 0, иначе выводить предупреждение"
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else print(
            'Невозможно выполнить операцию: отрицательное значение разности!')

    # реализуем метод перегузки арифметических операторов: умножение (__mul__)
    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    # реализуем метод перегузки арифметических операторов: деление (__truediv__)
    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    # Реализуем метод make_order()
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"$" * cells_in_row} \\n'
        row += f'{"$" * (self.quantity % cells_in_row)}'
        return row

# определяем количество ячеек в первой клетке - пусть оно равно 100
cells1 = Cell(100)
# определяем количество ячеек в первой клетке - пусть оно равно 25
cells2 = Cell(25)
print(cells1)
print(cells2)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
# определяем значение для организации ячеек по рядам в первой клетке - пусть оно равно 8
print(cells1.make_order(8))
# определяем значение для организации ячеек по рядам в первой клетке - пусть оно равно 10
print(cells2.make_order(10))
