class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return [self.name, self.surname]

    def get_total_income(self):
        return sum(self._income.values())


engineer = Position('Ivan', 'Ivanov', 'metrologist', 100000, 50000)
print(engineer.get_full_name())
print(engineer.position)
print(engineer.get_total_income())
