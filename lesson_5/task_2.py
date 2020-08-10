# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

w_count = 0
with open("text_2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    print("*" * 40, " FILE ", "*" * 40)
    print("".join(lines))
    print("*" * 88)

    print(f"Всего строк: {len(lines)}")
    for idx, i in enumerate(lines, 1):
        c = len(i.split())
        w_count += c
        print(f"{idx}: {c} слов")
    print(f"Всего слов: {w_count}")
