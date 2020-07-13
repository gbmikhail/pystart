# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

gen_list = [str(i) for i in range(0, 1024)]

with open("text_5.txt", "w", encoding="utf-8") as new_file:
    new_file.write(" ".join(gen_list) + "\n")

with open("text_5.txt", "r", encoding="utf-8") as file:
    my_list = map(int, file.read().split())
    print("Сумма чисел:", sum(my_list))
