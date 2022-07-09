number_n = input('Введите число от 1 до 9 включительно: ')
number_1 = int(number_n)
number_2 = int(number_n+number_n)
number_3 = int(number_n+number_n+number_n)
sum_numbers = number_1 + number_2 + number_3
print(number_1)
print(number_2)
print(number_3)
print(f'Сумма чисел {number_1} + {number_2} + {number_3} = {sum_numbers}')

