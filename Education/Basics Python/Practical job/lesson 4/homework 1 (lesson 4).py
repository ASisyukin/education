from sys import argv


def salary():
    try:
        time = float(argv[1])
        rate = float(argv[2])
        bonus = float(argv[3])
        print(f'Зарплата: {time * rate + bonus}')
    except ValueError:
        print('Введите все три числа')

salary()
