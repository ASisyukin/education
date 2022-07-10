class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        print(f'Maшина {self.name} поехала.')

    def stop(self):
        self.speed = 0
        print(f'Maшина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Maшина {self.name} повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} равна {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение ограничения скорости в 60. Скорость машины {self.name} равна {self.speed}.')
        else:
            print(f'Текущая скорость машины {self.name} равна {self.speed}.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение ограничения скорости в 40. Скорость машины {self.name} равна {self.speed}.')
        else:
            print(f'Текущая скорость машины {self.name} равна {self.speed}.')


class PoliceCar(Car):
    is_police = True


town_car = TownCar('Матиз', 'зеленый', 65)
town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.stop()

print()

sport_car = SportCar('Ferrari', 'красный', 125)
sport_car.go()
sport_car.turn('направо')
sport_car.show_speed()
sport_car.stop()

print()

work_car = WorkCar('Газель', 'грязный', 45)
work_car.go()
work_car.turn('направо')
work_car.show_speed()
work_car.stop()
print(f'Разыскивается машина {work_car.name}, цвет {work_car.color}.')

print()

police_car = PoliceCar('Жигули', 'белый', 65)
police_car.go()
police_car.turn('направо')
police_car.show_speed()
police_car.stop()
