# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))
n2 = int(str(n) + str(n))
n3 = int(str(n) + str(n) + str(n))
result = n + n2 + n3
print(f"{n} + {n2} + {n3} = {result}")
