import json

try:
    with open("text_7.txt", 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()  # загружаем данные из файла
        list_final = []  # итоговый список
        list_profit = []  # список для расчета средней прибыли
        dict_company = {}  # словарь для компаний и их прибыли
        for el in content:
            my_list = el.split(' ')  # разбиваем строку по разделителю
            if len(my_list) == 1:  # проверка на пустую строку (т.е. в строке только один элемент \n)
                continue
            else:
                dict_company[my_list[0]] = int(my_list[2]) - int(
                    my_list[3])  # наполнение словаря парами 'Фирма': прибыль
                if dict_company[my_list[0]] > 0:  # условие проверки получения прибыли
                    list_profit.append(dict_company[my_list[0]])  # заполнение списка для расчета средней прибыли
        dict_profit = {'average_profit': sum(list_profit) / len(list_profit)}
        list_final.append(dict_company)
        list_final.append(dict_profit)
        print(list_final)
except IOError:
    print("Произошла ошибка ввода-вывода!")

with open("json_7.json", 'w', encoding='utf-8') as f:
    json.dump(list_final, f, ensure_ascii=False)
