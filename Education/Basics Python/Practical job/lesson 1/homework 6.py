revenue = float(input('Введите сумму выручки: '))
costs = float(input('Введите сумму издержек: '))
profit = (revenue - costs)
if profit > 0:
    profitability = profit / costs
    numbers_workers = int(input('Введите количество сотрудников предприятия: '))
    profit_worker = profit / numbers_workers
    print(f'Прибыль предприятия равна: {profit:.2f} (округлена до двух знаков после запятой)')
    print(f'Рентабельность предприятия равна: {profitability:.2f} (округлена до двух знаков после запятой)')
    print(f'Прибыль фирмы в расчете на одного сотрудника равна: {profit_worker:.2f} (округлена до двух знаков после запятой)')

elif profit == 0:
    print(f'Прибыль предприятия равна: {profit:.2f}')
else:
    print(f'Убыток предприятия равен: {profit:.2f}')