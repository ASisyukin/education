class Road:
    def __init__(self, length=5000, width=20, weight=25, thickness=5):
        self._length = length
        self._width = width
        self.weight = weight
        self.thickness = thickness

    def calc_mass(self):
        return (self._length * self._width * self.weight * self.thickness) / 1000


road_1 = Road(1000, width=30)
print(f'Длина дороги: {road_1._length} м\nШирина дороги: {road_1._width} м\nМасса асфальта на 1 кв. м: {road_1.weight} '
      f'кг\nТолщина асфальта: {road_1.thickness} см\nРасчетная масса асфальта на дорогу: {road_1.calc_mass()} т')
