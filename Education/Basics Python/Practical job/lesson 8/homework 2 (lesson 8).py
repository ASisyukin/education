class MyZeroDivisionError(Exception):
    text = "Деление на ноль запрещено"

    def __str__(self):
        return self.text


try:
    num_1 = float(input("Введите делимое: "))
    num_2 = float(input("Введите делитель: "))
    if num_2 == 0:
        raise MyZeroDivisionError
    result = num_1 / num_2
except ValueError:
    print('Ошибка, необходимо ввести оба числа.')
except MyZeroDivisionError as err:
    print(err)
else:
    print(f"result = {result}")
