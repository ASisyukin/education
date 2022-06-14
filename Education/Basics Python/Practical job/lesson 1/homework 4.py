number = int(input('Введите целое положительное число: '))
max_number = 0
number_calculation = number
while True:
    if number_calculation // 10 == 0:
        if max_number < number_calculation % 10:
            max_number = number_calculation % 10
            break
        else:
            break
    else:
        if max_number < number_calculation % 10:
            max_number = number_calculation % 10
            number_calculation = number_calculation // 10
            continue
        else:
            number_calculation = number_calculation // 10
            continue
print(f'В числе {number} максимальная цифра равна: {max_number}')


