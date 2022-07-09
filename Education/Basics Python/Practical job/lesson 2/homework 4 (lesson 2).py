# my_string = "Пример форматирования строк в домашнем задании"
my_string = str(input("Введите строку из нескольких слов, разделённых пробелами: "))
my_list = my_string.split()
print(my_list)
for ind, el in enumerate(my_list):
    print(ind + 1, el[:10:])
