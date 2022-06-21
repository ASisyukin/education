def int_func(word):
    """Выполняет проверку полностью ли состоит слово из маленьких латинских букв.
    Если проверка пройдена успешно => заменяет первую букву на строчную
    """
    if ord('a') > ord(word[0]) or ord(word[0]) > ord('z'):
        print('Слово содержит не полностью состоит из латинских маленьких букв')
    else:
        return word.replace(chr(ord(word[0])), chr(ord(word[0]) - 32), 1)


my_str = input('Введите строку из слов, разделенных пробелом и состоящих из латинских маленьких букв: ')
my_list = my_str.split(' ')
for i in range(0, len(my_list)):
    my_list.insert(i, int_func(my_list[i]))
    my_list.pop(i+1)
my_str = ' '.join(my_list)
print(my_str)
