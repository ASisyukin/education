from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_cloth = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_cloth += self.expence

    def __str__(self):
        return f'Расход ткани на пальто: {self.expence}, общий расход ткани {Coat.expence_cloth}'

    @property
    def expence(self):
        return round((self.size / 6.5 + 0.5), 3)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Coat.expence_cloth += self.expence

    def __str__(self):
        return f'Расход ткани на костюм: {self.expence}, общий расход ткани {Coat.expence_cloth}'

    @property
    def expence(self):
        return round((self.height * 2 + 0.3), 3)


clothes_1 = Coat(49)
print(clothes_1)
clothes_2 = Coat(52)
print(clothes_2)
clothes_3 = Coat(55)
print(clothes_3)
clothes_4 = Costume(1.82)
print(clothes_4)
clothes_5 = Costume(1.93)
print(clothes_5)
