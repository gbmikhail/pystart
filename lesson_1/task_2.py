# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

s = int(input("Введите время в секундах: "))

hour = s // 3600
min = (s - hour * 3600) // 60
sec = s - hour * 3600 - min * 60

print(f"{hour:02d}:{min:02d}:{sec:02d}")