def my_func(val_1, val_2):
    """Возвращает частное от деления.

    Именованные параметры:
    val_1 -- делимое
    val_2 -- делитель

    """
    try:
        val_1 = int(val_1)
        val_2 = int(val_2)
        return val_1 / val_2
    except (ValueError, TypeError):
        print('Ошибка! Число введено неверно')
    except ZeroDivisionError:
        print('Ошибка! Деление на 0')


p_1 = input('Введите делиммое: ')
p_2 = input('Введите делитель: ')

print(f'Результат деления {p_1} на {p_2} равен: {my_func(p_1, p_2)}')
