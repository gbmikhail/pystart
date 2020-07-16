# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, color):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

        self.DIRECTION_FORWARD = "forward"
        self.DIRECTION_BACK = "back"
        self.direction = self.DIRECTION_FORWARD

    def go(self, speed):
        self.speed = speed
        self.show_speed()

    def stop(self):
        self.speed = 0
        print("STOP ! ! !")

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(f"Speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        print(f"Speed: {self.speed}")
        if self.speed > max_speed:
            print('\33[31m' + f"Over speed! Limitation {max_speed} km/h" + '\33[0m')


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        print(f"Speed: {self.speed}")
        if self.speed > max_speed:
            print('\33[31m' + f"Over speed! Limitation {max_speed} km/h" + '\33[0m')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color):
        super(PoliceCar, self).__init__(name, color)
        self.is_police = True


car_list = [
    TownCar("Tesla Model S", "red"),
    WorkCar("Nissan Titan", "black"),
    SportCar("Bugatti Veyron", "yellow"),
    PoliceCar("BMW i8", "white")
]

for i in car_list:
    print(f"{'*' * 40} {type(i).__name__} {'*' * 40}")
    print(f"Name: {i.name}\nColor: {i.color}\nPolice: {i.is_police}\nDirection: {i.direction}")
    if type(i).__name__ == "TownCar":
        i.go(62)
    elif type(i).__name__ == "WorkCar":
        i.go(50)
    else:
        i.go(90)
