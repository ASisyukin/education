my_list = list(input('Введите элементы списка: '))
i = 1
while i < len(my_list):
    if len(my_list) % 2 == 0:
        my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
        i += 2
        continue
    else:
        if i < len(my_list) - 1:
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            i += 2
            continue
        else:
            break
print(my_list)





