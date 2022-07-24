class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.matrix)

    def __add__(self, other):
        return Matrix([map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)])


a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
b = [[3, 5, 8], [3, 6, 3], [7, 1, 11]]
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Матрица 1:\n{matrix_1}\n')
print(f'Матрица 2:\n{matrix_2}\n')
print(f'Сложение матриц:\n{matrix_1 + matrix_2}')
