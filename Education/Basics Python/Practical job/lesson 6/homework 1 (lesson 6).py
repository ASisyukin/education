import itertools
import time


class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [2, 33]],
               ['green', [5, 32]]]  # 7, 2, 5 - время "горения" цвета, 31, 32, 33 - выбор цвета текста

    def running(self):
        for el in itertools.cycle(self.__color):
            print(f'\r\033[{el[1][1]}m{el[0]}', end='')  # \033[{el[1][1]}m - код выбора цвета текста
            time.sleep(el[1][0])


a = TrafficLight()
a.running()
