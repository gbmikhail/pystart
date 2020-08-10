# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self):
        self.title = "канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__()
        self.title = "ручка"

    def draw(self):
        print(f"Запуск отрисовки '{self.title}'")


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__()
        self.title = "карандаш"

    def draw(self):
        print(f"Запуск отрисовки '{self.title}'")


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__()
        self.title = "маркер"

    def draw(self):
        print(f"Запуск отрисовки '{self.title}'")


my_list = [
    Stationery(),
    Pen(),
    Pencil(),
    Handle()
]

for i in my_list:
    i.draw()
