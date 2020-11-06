my_str = input("Пользователь вводит предложение из нескольких слов: ")
summ_word = []
num = 0
for el in range(my_str.count(' ') + 1):
    summ_word = my_str.split()
    if len(str(summ_word)) <= 10:
        print(f" {num} {summ_word[el]}")
        num += 1
    else:
        print(f" {num} {summ_word[el][0:10]}")
        num += 1
