# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

# А
print(f"{'*' * 40} А {'*' * 40}")
begin = int(input('Введите стартовое число '))
wl = count(begin)
i = begin
# Берем 10 значений. И break не используем.
while i < begin + 10:
    i = next(wl)
    print(i)

# Б
print(f"{'*' * 40} Б {'*' * 40}")
index = 0
wl = cycle("ABC")
# Выводим 15 раз
while index < 15:
    index += 1
    i = next(wl)
    print(f"{index:}. {i}")
