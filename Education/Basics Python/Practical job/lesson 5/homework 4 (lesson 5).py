try:
    final_list = []  # список из которого будут загружаться данные в новый текстовый файл
    with open("text_4.txt", 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        dict_rus = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
        for el in content:
            my_list = el.split(' - ')  # список, который получаем при разбиении строки на элементы
            for i in dict_rus.keys():
                if int(my_list[1]) == i:
                    final_list.append(' - '.join([dict_rus[i], my_list[1]]))
        print(final_list)
    f_obj_final = open("text_4_2.txt", 'w', encoding='utf-8')
    f_obj_final.writelines(final_list)
    f_obj_final.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
