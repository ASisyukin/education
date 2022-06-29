try:
    with open("text_1.txt", 'w') as f_obj:
        while True:
            my_str = input('Введите данные для записи, для выхода из цикла записи оставить строку ввода пустой: ')
            if not my_str:
                break
            f_obj.write(my_str + '\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")

f_obj = open("text_1.txt", "r")
print(f'Информация, записанная в файл: \n{f_obj.read()}')
f_obj.close()
