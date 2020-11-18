import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r') as file:
    for line in file:
        name, firm, income, cost = line.split()
        profit[name] = int(income) - int(cost)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль компаний, работающих с прибылью - {prof_aver:.2f}')
    else:
        print(f'Компания работает в убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)

