# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

i = int(input("Введите сумму выручки: "))
o = int(input("Введите сумму издержек: "))

if i < o:
    print("Фирма работает с издержками")
elif i == o:
    print("Деятельность фирмы не приносит результатов. Вы работаете бесплатно.")
else:
    r = i - o
    count = int(input("Введите численность сотрудников: "))
    print(f"Рентабельность: {r}. Прибыль фирмы в расчете на одного сотрудника: {r / count}")
