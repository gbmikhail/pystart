# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, str_data):
        self.str_data = str_data

    # @staticmethod
    # def convert(str_data):

    @classmethod
    def get_date(cls, str_data):
        ls_date = str_data.split("-")
        if len(ls_date) != 3:
            return False, False, False
        try:
            d, m, y = map(int, ls_date)
            if cls.validation(d, m, y):
                return d, m, y
        except Exception:
            pass
        return False, False, False


    @staticmethod
    def validation(d, m, y):
        if y not in range(1900, 2200):
            return False
        if m not in range(1, 13):
            return False

        md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y % 4 == 0:
            md[1] = 29

        if d < 1:
            return False
        elif d > md[m - 1]:
            return False

        return True


s = input("Введите число в формате день-месяц-год: ")
date = Data(s)
d, m, y = date.get_date(date.str_data)
if d != False:
    print(f"Дата введена корректно: {d:02}-{m:02}-{y}")
else:
    print("Не верно введена дата")
