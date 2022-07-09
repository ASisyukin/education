try:
    with open("text_3.txt", 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        sum_salary = 0
        for el in content:
            my_list = el.split(' ')
            if float(my_list[1]) < 20000:
                print(f'ЗП сотрудника {my_list[0]} меньше 20000 и равна {float(my_list[1])}')
            sum_salary += float(my_list[1])
        print(f'Средняя заплата всех сотрудников: {sum_salary / len(content)}')
except IOError:
    print("Произошла ошибка ввода-вывода!")
