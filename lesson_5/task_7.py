# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

average_profit = 0
count_profit = 0
firm_dict = dict()

with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        firm_list = line.split()
        s = int(firm_list[2]) - int(firm_list[3])
        firm_dict[firm_list[0]] = s
        if s >= 0:
            average_profit += s
            count_profit += 1

        print(firm_list)
    print("*" * 100)
    average_profit_dict = {"average_profit": average_profit / count_profit}

print(firm_dict)
print(average_profit_dict)

with open("text_7.json", "w", encoding="utf-8") as file:
    json.dump([firm_dict, average_profit_dict], file, indent=4, ensure_ascii=False)
