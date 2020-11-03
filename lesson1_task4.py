x = abs(int(input("Пользователь ввел целое положительное число: ")))
max = x % 10
while x >= 1:
    x = x // 10
    if x % 10 > max:
        max = x % 10
    if x > 9:
        continue
    else:
        print("Максимальная цифра в введенном пользователе числе: ", max)
        break