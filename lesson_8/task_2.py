# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = input('Введите 2 числа через пробел: ').split()

try:
    a = int(my_list[0])
    b = int(my_list[1])
    if b == 0:
        raise OwnError('На 0 делить нельзя.')
    c = a / b
except ValueError:
    print('Вы ввели не числа.')
except OwnError as ZeroError:
    print(ZeroError)
else:
    print(f'a / b = {c}')
