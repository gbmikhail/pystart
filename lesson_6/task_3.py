# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, wage, bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname} ({self.position})"


    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position_list = [
    Position("Иванов", "Иван", "Менеджер по кадрам", 35000, 4500),
    Position("Петров", "Петр", "Маркетинг менеджер", 35000, 7000),
    Position("Сидоров", "Дмитрий", "Менеджер по логистике", 31000, 3000),
    Position("Иванова", "Дарья", "Менеджер по связи", 30000, 71000),
    Position("Петрова", "Надежда", "Менеджер проекта", 40000, 10000),
    Position("Сидорова", "Марина", "Начальник отдела", 35000, 8000),
    Position("Октябрьский", "Сергей", "PR менеджер", 25000, 50000),
    Position("Петровский", "Олег", "Менеджер по разработкам", 32000, 6000),
    Position("Знаменский", "Василий", "Разнорабочий", 20000, 0)
]

for i in position_list:
    print(f"{i.get_full_name():50s} {i.get_total_income()}")
