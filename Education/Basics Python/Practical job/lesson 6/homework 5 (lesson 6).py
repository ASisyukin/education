class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. {self.title}.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки письма. Используется {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки рисунка. Используется {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки плаката. Использованием {self.title}.')


stationery = Stationery('Канцелярская приналежность')
stationery.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
