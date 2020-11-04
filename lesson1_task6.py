a = int(input("Спортсмен вводит результат пробежки за первый день (в км): "))
b = int(input("Спортсмен вводит целевой показатель пробежки (в км): "))
result_days = 1
result_km = a
while b - a > 0:
    a = a + (0.1 * a)
    result_days += 1
    result_km = result_km + a
print(f"Спортсмен достигнет целевого показателя пробежки на %.d день:" % result_days)