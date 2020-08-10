# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        p = "+"
        if self.im < 0:
            p = "-"
        return f"({self.re}{p}{self.im}j)"

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)


a = ComplexNum(3, 2)
b = ComplexNum(4, 5)
print(f"a = {a}")
print(f"a = {b}")
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
