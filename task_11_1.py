import re
"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""
re_date = re.compile(r'^([0-9]{2}-){2}[0-9]{2,4}$')


class Date:
    def __init__(self, date):
        if re_date.match(date) is not None:
            self.date = self.convert(date)
        else:
            print("Неправильный формат даты")

    @classmethod
    def convert(cls, date):
        d_list = list(map(int, date.split('-')))
        if cls.validation(d_list[0], d_list[1], d_list[2]):
            print(f"день - {d_list[0]}, месяц - {d_list[1]}, год - {d_list[2]}")
            return d_list
        else:
            print("Неправильный формат даты")

    @staticmethod
    def validation(day, month, year):
        if day in range(1, 32) and month in range(1, 13) and year > 0:
            return True
        else:
            return False


d1 = Date('31-01-2021')
d2 = Date('12-13-1425')
d3 = Date('12-12-12')
d4 = Date('32-05-2015')


