try:
    f_obj = open("text_6.txt", 'r', encoding='utf-8')
    content = f_obj.readlines()  # загружаем данные из файла
    dict_subject = {}
    for el in content:
        line_list = el.split(':')  # разбиваем строку по разделителю для поиска названий предметов
        num_list = []
        num = ''
        for i in line_list[1]:  # поиск чисел в оставшейся части строки
            if i.isdigit():
                num = num + i
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
        dict_subject[line_list[0]] = sum(num_list)  # наполнение словаря парами 'Предмет': количество занятий
    print(dict_subject)
    f_obj.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
