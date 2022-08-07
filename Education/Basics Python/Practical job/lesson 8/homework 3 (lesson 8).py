class UserNotNumberError(Exception):
    text = "Вы ввели не число!"

    def __str__(self):
        return self.text

    @staticmethod
    def valid_number(number):
        try:
            if float(number):
                return True
        except ValueError:
            return False


def main():
    numbers_list = []
    while True:
        number = input('Введите число или "stop" для выхода: ')
        if number == 'stop':
            break
        try:
            if UserNotNumberError.valid_number(number):
                numbers_list.append(float(number))
            else:
                raise UserNotNumberError
        except UserNotNumberError as err:
            print(err)
    print(numbers_list)


if __name__ == '__main__':
    main()
