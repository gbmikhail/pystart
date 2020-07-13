# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

ws_count = 0
ws_salary = 0.0

with open("text_3.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split()
        name, salary = data[0], float(data[1])

        ws_count += 1
        ws_salary += salary

        if salary < 20000:
            print(f"{name:16s} \t {salary:.2f}")

print(f"Средний доход сотрудников: {(ws_salary / ws_count):.2f}")
