from abc import ABC, abstractmethod


class Warehouse:
    devices_in_warehouse = {}
    full_price_devise = 0

    def __str__(self):
        return f'Устройства на складе:\n{self.devices_in_warehouse}\nПолная стоимость продукции на складе:' \
               f'\n{self.full_price_devise}'


class Device(ABC):
    def __init__(self, model, amount, price):
        self.model = model
        self.amount = amount
        self.price = price

    def to_warehouse(self):
        Warehouse.full_price_devise += (int(self.amount) * int(self.price))
        if Warehouse.devices_in_warehouse.setdefault(self.model) is None:
            Warehouse.devices_in_warehouse[self.model] = int(self.amount)
        else:
            Warehouse.devices_in_warehouse[self.model] = int(self.amount) + \
                                                         Warehouse.devices_in_warehouse.setdefault(self.model)

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
    printer_1 = Printer('Canon 1', 13, 12369)
    print(printer_1)
    printer_1.work()
    printer_1.to_warehouse()
    print(Warehouse())
    print('_________________________')
    scanner_1 = Scanner('HP 1', 7, 14005)
    print(scanner_1)
    scanner_1.work()
    scanner_1.to_warehouse()
    print(Warehouse())
    print('_________________________')
    copier_1 = Copier('Xerox 1', 11, 9452)
    print(copier_1)
    copier_1.work()
    copier_1.to_warehouse()
    print(Warehouse())
    print('_________________________')
    printer_2 = Printer('Canon 1', 7, 12369)
    print(printer_2)
    printer_2.to_warehouse()
    print(Warehouse())


if __name__ == '__main__':
    main()
