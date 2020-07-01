# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
#
# }

my_list = list()
my_analys = dict()
num = 0
while True:
    num += 1
    new = input(f"Вы хотите ввести новый товар № {num}? (y/n): ").lower()
    if new[:1] == "n" or new[:1] == "q" or new[:1] == "н":
        break

    my_dict = {
        "название": input("Введите название: "),
        "цена": input("Введите цену: "),
        "количество": input("Введите количество: "),
        "eд": input("Введите единицы измерения: ")
    }
    my_list.append((num, my_dict))

if len(my_list) > 0:
    # Берем словарь для анализа из первого элемента. Посто, для того что бы не прописывать еще раз те же ключи
    for key in my_list[:1][0][1].keys():
        my_analys[key] = list()

    for i in my_list:
        item = i[1]
        for key in item.keys():
            if my_analys[key].count(item[key]) == 0:
                my_analys[key].append(item[key])

    print("Аналитика о товарах:")
    print(my_analys)
else:
    print("Товаров нет")
