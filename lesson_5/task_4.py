# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
# английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translation = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("text_4_new.txt", "w", encoding="utf-8") as new_file:
    with open("text_4.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            t_list = line.split()

            for idx, i in enumerate(t_list):
                if translation.get(i) is not None:
                    t_list[idx] = translation.get(i)

            new_file.write(" ".join(t_list) + "\n")
            print(" ".join(t_list))
