try:
    with open("text_2.txt", 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        print(f'Количество строк в файле {f_obj.name}: {len(content)}')
        i = 1
        for el in content:
            my_list = el.split(' ')
            print(f'Количество слов в строке {i}: {len(my_list)}')
            i += 1
except IOError:
    print("Произошла ошибка ввода-вывода!")
