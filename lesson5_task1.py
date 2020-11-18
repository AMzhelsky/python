new_file = open('Test.txt', 'w')
line = input('Пользователь вводит текст: \n')
while line:
    new_file.writelines(line)
    line = input('Пользователь вводит текст: \n')
    if not line:
        break

new_file.close()
new_file = open('test.txt', 'r')
content = new_file.readlines()
print(content)
new_file.close()
