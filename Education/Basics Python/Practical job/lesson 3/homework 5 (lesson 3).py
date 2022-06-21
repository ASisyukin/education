# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

sum_number = float()
while True:
    my_str = str(input('Введите числа через пробел, для выхода из программы введите символ №: '))
    my_list = (my_str.split(' '))
    try:
        if my_list.count('№') == 0:
            for i in range(0, len(my_list)):
                my_list[i] = float(my_list[i])
            sum_number = sum_number + sum(my_list)
            print(f' Промежуточная сумма: {sum_number}')
            continue
        else:
            k = my_list.index('№')
            for i in range(k, len(my_list)):
                my_list.pop(k)
            for i in range(0, len(my_list)):
                my_list[i] = float(my_list[i])
            sum_number = sum_number + sum(my_list)
            print(f' Итоговая сумма: {sum_number}')
            break
    except (ValueError, TypeError):
        print('Ошибка! Числа введены неверно')
