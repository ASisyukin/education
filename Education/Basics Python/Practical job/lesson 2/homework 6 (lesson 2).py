i = 1
my_list = []

# Запрос данных от пользователя и создание списка кортежей, состоящих из номера товара и словаря с характеристиками
while True:
    name = str(input('Введите название товара: '))
    price = float(input(f'Введите цену товара {name}: '))
    quantity = int(input(f'Введите количество товара {name}: '))
    unit = str(input(f'Введите единицу поставки товара {name}: '))
    my_dict = dict([('Название', name), ('цена', price), ('количество', quantity), ('ед.', unit)])
    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    i += 1
    q = str(input('Для продолжения заполнения данных введите любой символ. Для завершения введите слово <выход>: '))
    if q == 'выход':
        break
    else:
        continue

print('')
print(f'Лист данных: {my_list}')
print('Лист данных построчно:')
for el in my_list:
    print(el)

# Аналитика данных. Словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
list_name = []
list_price = []
list_quantity = []
list_unit = []

for ind, el in my_list:
    list_name.append(my_list[ind - 1][1].get('Название'))
    list_price.append(my_list[ind - 1][1].get('цена'))
    list_quantity.append(my_list[ind - 1][1].get('количество'))
    list_unit.append(my_list[ind - 1][1].get('ед.'))

new_dict = dict([('Название', list_name), ('цена', list_price), ('количество', list_quantity), ('ед.', list_unit)])
print('')
print(f'Словарь для аналитики данных: {new_dict}')
