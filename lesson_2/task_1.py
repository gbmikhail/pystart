# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

myList = [None, 1024, 3.14, True, "python", [1, 2, 3], {1, 2, 3}, {1: "1", 2: "2", 3: "3"}, (1, 2, 3)]

for i in myList:
    print(i, " - ", type(i))
