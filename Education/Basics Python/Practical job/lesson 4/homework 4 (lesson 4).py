my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11, 1]
unique_num = []
repeated_num = []
for el in my_list:
    if el in repeated_num:
        continue
    if el in unique_num:
        repeated_num.append(el)
        unique_num.remove(el)
        continue
    unique_num.append(el)
print(unique_num)
