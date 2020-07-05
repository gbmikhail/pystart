# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.


def my_sum(s):
    exit_flag = False
    my_list = input("Введите строку чисел, разделенных пробелом. q - выход: ").split()
    for i in my_list:
        if i.isdigit():
            s += int(i)
        elif i[:1].lower() == "q":
            exit_flag = True
            break

    print(f"sum = {s}")
    if not exit_flag:
        my_sum(s)


# Реализация через рекурсию
my_sum(0)
