# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(val_1, val_2, val_3):
    try:
        my_list = [int(val_1), int(val_2), int(val_3)]
        my_list.sort()
        my_list.pop(0)
        return sum(my_list)
    except ValueError:
        print("Вводить нужно числа")


while True:
    vList = input("Введите 3 числа через пробел: ").split()
    if len(vList) == 3:
        value = my_func(vList[0], vList[1], vList[2])
        if value is not None:
            print(value)
            break
