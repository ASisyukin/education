def my_func(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших аргументов.

    Именованные параметры:
    num_1 -- первый аргумент
    num_2 -- второй аргумент
    num_2 -- третий аргумент

    """
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        num_3 = int(num_3)
        my_list = [num_1, num_2, num_3]
        my_list.sort()
        return my_list[1] + my_list[2]
    except (ValueError, TypeError):
        print('Ошибка! Число введено неверно')


val_1 = input('Введите число 1: ')
val_2 = input('Введите число 2: ')
val_3 = input('Введите число 3: ')
print(f' Сумма двух наибольших аргументов равна: {my_func(val_1, val_2, val_3)}')
