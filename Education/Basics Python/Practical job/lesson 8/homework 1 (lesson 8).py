import time


class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_date(cls, date_str):
        date_list = list(map(int, date_str.split('-')))
        return date_list

    @staticmethod
    def validate(date_str):
        try:
            time.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False


print(Date.extract_date('01-01-2001'))
print(Date.validate('01-01-2001'))
print()
print(Date.extract_date('29-02-2020'))
print(Date.validate('29-02-2020'))
print()
print(Date.extract_date('29-02-2021'))
print(Date.validate('29-02-2021'))
