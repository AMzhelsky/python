class DivByNull(Exception):
    def __init__(self, txt):
        self.txt = txt
    try:
        res = 100 / 0
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(f"Все хорошо. Результат - {res}")
    finally:
        print("Завершено выполнение программы")


