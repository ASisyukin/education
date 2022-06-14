revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
profit = (revenue - costs)
if profit >= 0:
    print(f'Прибыль предприятия равна {profit}')
else:
    print(f'Убыток предприятия равен {profit}')