# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(s: str):
    return s.title()


def check_word(s: str):
    for ch in s:
        if ord(ch) not in range(ord('a'), ord('z') + 1):
            return None
    return int_func(s)


flag = True
my_list = []
while flag:
    my_list = input("Ввыдите строку из слов в нижнем регистре: ").split()
    for idx, i in enumerate(my_list):
        my_list[idx] = check_word(i)
        if my_list[idx] is not None:
            flag = False
        else:
            print("Error")
            flag = True
            break

print(" ".join(my_list))
