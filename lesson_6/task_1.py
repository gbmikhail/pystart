# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
# https://en.wikipedia.org/wiki/ANSI_escape_code
import time


class TrafficLight:
    __color = {
        "red": [7, '\33[31m'],
        "yellow": [2, '\33[33m'],
        "green": [7, '\33[32m']
    }
    __CEND = '\33[0m'

    def running(self):
        while True:
            for key in self.__color:
                self.__print_color(key)
            self.__print_color("yellow")

    def __print_color(self, key):
        print(self.__color[key][1] + key, self.__CEND)
        time.sleep(self.__color[key][0])


traffic_light = TrafficLight()
traffic_light.running()
