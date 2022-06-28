def fact(num):
    fact_num = 1
    if num == 0:
        i = 0
        yield i, fact_num
    for i in range(1, num + 1):
        fact_num *= i
        yield i, fact_num


try:
    for i, el in fact(int(input('Введите число для вычисления его факториала: '))):
        print(f'Факториал числа {i} равен {el}')
except ValueError:
    print('ValueError')
