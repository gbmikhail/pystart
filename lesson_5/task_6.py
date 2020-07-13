# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def only_digit(value):
    new = ''
    for i in value:
        if ord(i) in range(ord('0'), ord('9') + 1):
            new += i
    if len(new) == 0:
        new = "0"
    return int(new)


my_dict = dict()
with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        data_list = line.split(":")

        subject = data_list[0]                  # учебный предмет
        lesson_data = data_list[1].split()      # занятия
        for idx, i in enumerate(lesson_data):
            lesson_data[idx] = only_digit(i)

        my_dict[subject] = sum(lesson_data)

print(my_dict)
