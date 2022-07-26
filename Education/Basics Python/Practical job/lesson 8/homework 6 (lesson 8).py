from abc import ABC, abstractmethod


class Warehouse:
    devices_in_warehouse = {}
    full_price_devise = 0
    devices_in_office = {}

    def __init__(self, model=None, amount=None):
        self.model = model
        self.amount = amount

    def __str__(self):
        return f'Устройства на складе (модель: [количество, цена за единицу]):\n{self.devices_in_warehouse}\nПолная ' \
               f'стоимость продукции на складе:\n{self.full_price_devise}\n'

    @classmethod
    def from_warehouse(cls, model, amount):
        if cls.devices_in_warehouse.setdefault(model) is None:
            print(f'Позиция {model} отсутствует на складе\n')
        else:
            if cls.devices_in_warehouse.setdefault(model)[0] < int(amount):
                print(
                    f'Запрошено {amount} единиц товара {model}.\n'
                    f'На складе {cls.devices_in_warehouse.setdefault(model)[0]} единиц {model}.'
                    f'\nВыполнить запрос на отгрузку невозможно.\n')
            else:
                print(f'На складе {cls.devices_in_warehouse.setdefault(model)[0]} единиц {model}.\n'
                      f'Запрошено {amount} единиц товара {model}')
                cls.devices_in_warehouse[model] = [cls.devices_in_warehouse.setdefault(model)[0] - int(amount),
                                                   cls.devices_in_warehouse.setdefault(model)[1]]
                cls.full_price_devise -= (int(amount) * cls.devices_in_warehouse.setdefault(model)[1])
                print(f'Отгружено {amount} единиц товара {model}.\nОстаток после отгрузки: '
                      f'{cls.devices_in_warehouse.setdefault(model)[0]} единиц {model}\n')


class Device(ABC):
    def __init__(self, model, amount, price):
        self.model = model
        self.amount = amount
        self.price = price

    def to_warehouse(self):
        Warehouse.full_price_devise += (int(self.amount) * int(self.price))
        if Warehouse.devices_in_warehouse.setdefault(self.model) is None:
            Warehouse.devices_in_warehouse[self.model] = [int(self.amount), int(self.price)]
        else:
            Warehouse.devices_in_warehouse[self.model] = \
                [int(self.amount) + Warehouse.devices_in_warehouse.setdefault(self.model)[0], int(self.price)]

    def __str__(self):
        return f'Модель устройства {self.model}, количество {self.amount}, стоимость единицы {self.price}.'

    @abstractmethod
    def work(self):
        pass


class Printer(Device):
    def work(self):
        print(f'Принтер модель {self.model} печатает.')


class Scanner(Device):
    def work(self):
        print(f'Сканер модель {self.model} сканирует.')


class Copier(Device):
    def work(self):
        print(f'Ксерокс модель {self.model} копирует.')


def main():
    # printer_1 = Printer('Canon 1', 13, 12369)
    # print(printer_1)
    # printer_1.work()
    # printer_1.to_warehouse()
    # print(Warehouse())
    # print('_________________________')
    # scanner_1 = Scanner('HP 1', 7, 14005)
    # print(scanner_1)
    # scanner_1.work()
    # scanner_1.to_warehouse()
    # print(Warehouse())
    # print('_________________________')
    # copier_1 = Copier('Xerox 1', 11, 9452)
    # print(copier_1)
    # copier_1.work()
    # copier_1.to_warehouse()
    # print(Warehouse())
    # print('_________________________')
    # printer_2 = Printer('Canon 1', 7, 12369)
    # print(printer_2)
    # printer_2.to_warehouse()
    # print(Warehouse())
    # print('________Вторая часть проекта_________')
    # Warehouse.from_warehouse('Canon 1', 5)
    # Warehouse.from_warehouse('Canon 2', 5)
    # print(Warehouse())
    # Warehouse.from_warehouse('Xerox 1', 12)
    # print(Warehouse())
    print('________Третья часть проекта_________')
    user_model = input('Введите название модели техники: ')
    user_amount = input('Введите количество техники: ')
    user_price = input('Введите стоимость единицы техники: ')
    try:
        user_amount = int(user_amount)
        user_price = int(user_price)
    except ValueError as err:
        print(f'Ошибка ввода ({err})')
    printer_user = Printer(user_model, user_amount, user_price)
    print(printer_user)
    printer_user.work()
    printer_user.to_warehouse()
    print(Warehouse())


if __name__ == '__main__':
    main()
