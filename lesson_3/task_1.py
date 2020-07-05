# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    except ValueError:
        print("Вводить нужно числа")


while True:
    vList = input("Введите 2 числа через пробел: ").split()
    if len(vList) == 2:
        value = division(vList[0], vList[1])
        if value is not None:
            print(value)
            break
