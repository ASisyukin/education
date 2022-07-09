try:
    my_list = input('Введите набор чисел разделенных пробелами: ')  # запрашиваем числа и записываем в файл
    f_obj = open("text_5.txt", 'w', encoding='utf-8')
    f_obj.write(my_list)
    f_obj.close()

    f_obj_2 = open("text_5.txt", 'r', encoding='utf-8')  # открываем файл для чтения
    my_list = [float(i) for i in f_obj_2.read().split(' ')]
    print(f'Сумма чисел из файла {f_obj_2.name} равна: {sum(my_list)}')
    f_obj_2.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
except (ValueError, TypeError):
    print('Ошибка! Необходимо ввести только числа')
