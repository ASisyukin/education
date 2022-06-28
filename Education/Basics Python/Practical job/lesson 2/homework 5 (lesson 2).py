my_list = [7, 5, 3, 3, 2]
while len(my_list) < 10:
    my_list.append(int(input('Введите натуральное число: ')))
    print(sorted(my_list, reverse=True))
