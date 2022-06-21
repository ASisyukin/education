def my_func(x, y):
    """Выполняет возведение числа 'x' в степень 'y'."""
    try:
        x = float(x)
        y = int(y)
        return x ** y
    except (ValueError, TypeError):
        print('Ошибка! Число введено неверно')
    except ZeroDivisionError:
        print('Ошибка! Деление на 0')


def my_func_cycle(x, y):
    """Выполняет возведение числа 'x' в степень 'y' с использованием цикла."""
    try:
        x = float(x)
        y = int(y)
        i = 1
        composition = 1
        while i <= abs(y):
            if y >= 0:
                composition = composition * x
                i += 1
            else:
                composition = composition * (1 / x)
                i += 1
        return composition
    except (ValueError, TypeError):
        print('Ошибка! Число введено неверно')
    except ZeroDivisionError:
        print('Ошибка! Деление на 0')


x = input('Введите число, возводимое в степень: ')
y = input('Введите степень (целое число), в которую будет возводиться число: ')

print(f'Число {x} в степени {y} равно: {my_func(x, y)}')
print(f'Число {x} в степени {y} равно: {my_func_cycle(x, y)}, (метод с циклом)')
