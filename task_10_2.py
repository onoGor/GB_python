from abc import ABC, abstractmethod
"""Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property."""


class Clothes(ABC):
    @abstractmethod
    def __init__(self, v):
        self.v = v

    def __add__(self, *args):
        return sum(args)


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculate(self):
        return round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f"Для отшива пальто размером {self.size} потребуется ткани: {self.calculate}"


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calculate(self):
        return round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f"Для отшива костюма размером {self.height} потребуется ткани: {self.calculate}"


s = Suit(128)
c = Coat(44)
print(s)
print(c)
print(f"Суммарный расход ткани на производстве: {s.calculate + c.calculate}")





