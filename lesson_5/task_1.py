# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("text_1.txt", "w", encoding="utf-8") as file:
    while True:
        s = input("Введите текст. Выход - пустая строка: ")
        if len(s) > 0:
            file.write(f"{s}\n")
        else:
            break
