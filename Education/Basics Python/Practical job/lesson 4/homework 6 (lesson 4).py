from itertools import count, cycle
from random import randint

for el in count(1, 3):
    if el > 12:
        break
    else:
        print(f'{el} - модуль count')

my_list = [randint(0, 9) for _ in range(6)]
print(f'{my_list} - список, модуль cycle')
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(f'{el} - модуль cycle')
    c += 1
