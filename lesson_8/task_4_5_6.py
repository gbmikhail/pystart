# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Stock:
    depot = []

    @staticmethod
    def show():
        print('Наличие товара на складе: ')
        for el in Stock.depot:
            print(el)

    @staticmethod
    def move(name, count, name_dep):
        if Stock.valid(name, count, name_dep):
            for el in Stock.depot:
                for key, val in el.items():
                    if name == val:
                        if count <= el['кол-во']:
                            el['кол-во'] -= count
                            if el['кол-во'] == 0:
                                Stock.depot.remove(el)
                            return print(f'Позиция: {name}, кол-во: {count} перемещена в подзразделение: {name_dep}')
                        else:
                            return print('Такого количества нет на складе')
            return print('Такого товара нет на складе')

    @staticmethod
    def valid(name, count, name_dep):
        if not(isinstance(name, str)):
            print('Данные введены некорректно. Наименование должно быть строчным')
            return False
        elif not(isinstance(count, int)):
            print('Данные введены некорректно. Количество должно быть числом')
            return False
        elif not(isinstance(name_dep, str)):
            print('Данные введены некорректно. Название подразделения должно быть строчным')
            return False
        return True


class OfficeEq:
    _office_eq = []

    @staticmethod
    def show_office_eq():
        for el in OfficeEq._office_eq:
            print(el)

    @staticmethod
    def move_depot():
        Stock.depot.extend(OfficeEq._office_eq)
        print('Оргтехника перемещена на склад')

    def __init__(self, name, model, price, count):
        self.name = name
        self.model = model
        self.price = price
        self.count = count


class Printer(OfficeEq):
    def __init__(self, name, model, price, count, tech_print):
        super().__init__(name, model, price, count)
        self.tech_print = tech_print
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.tech_print
        })


class Scanner(OfficeEq):
    def __init__(self, name, model, price, count, sc_type):
        super().__init__(name, model, price, count)
        self.sc_type = sc_type
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.sc_type
        })


class Xerox(OfficeEq):
    def __init__(self, name, model, price, count, x_type):
        super().__init__(name, model, price, count)
        self.x_type = x_type
        OfficeEq._office_eq.append({
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'кол-во': self.count,
            'тип': self.x_type
        })


x1 = Xerox('Xerox XX1', 'CC23456', 45000, 2, 'планшетный')
x2 = Xerox('Xerox XX2', 'CC23446', 45000, 1, 'портативный')
s1 = Scanner('HP Z1', 'XC6565', 13000, 3, 'цветной')
p1 = Printer('HP LJ125', 'MFP123', 45000, 4, 'лазерный')
OfficeEq.show_office_eq()
OfficeEq.move_depot()
Stock.show()
Stock.move('HP LJ125', 4, 'Отдел сбыта')
Stock.show()
Stock.move('Xerox XX1', 3, 'Бухгалтерия')
Stock.show()
Stock.move('HP LJ125i', 5, 'Отдел сбыта')
Stock.show()
Stock.move('HP LJ125i', '5', 'Отдел сбыта')
Stock.move(123, 5, 'Отдел сбыта')
Stock.move('HP LJ125i', 5, 123)
