class Cell:

    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        print('Cложение')
        return Cell(self.numbers + other.numbers)

    def __sub__(self, other):
        print('Вычитание')
        if self.numbers < other.numbers:
            raise ValueError('В первой клетке ячеек меньше чем во второй')
        return Cell(self.numbers - other.numbers)

    def __mul__(self, other):
        print('Умножение')
        return Cell(self.numbers * other.numbers)

    def __floordiv__(self, other):
        print('Целочисленное деление')
        return Cell(self.numbers // other.numbers)

    def make_order(self, len_cell):
        result = ['*' * len_cell] * (self.numbers // len_cell)
        if self.numbers % len_cell:
            result.append('*' * (self.numbers % len_cell))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.numbers}'


cell_1 = Cell(17)
cell_2 = Cell(8)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
