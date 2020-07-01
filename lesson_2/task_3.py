# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

season_list = ["зима", "весна", "лето", "осень"]
month_dict = {
    12: season_list[0],
    1: season_list[0],
    2: season_list[0],

    3: season_list[1],
    4: season_list[1],
    5: season_list[1],

    6: season_list[2],
    7: season_list[2],
    8: season_list[2],

    9: season_list[3],
    10: season_list[3],
    11: season_list[3],
}

month = int(input("Введите номер месяца: "))
if month in range(1, 13):
    print(f"Это {month_dict[month]}")
else:
    print("Это не номер месяца")
