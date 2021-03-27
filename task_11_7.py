"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, fake):
        self.real = real
        self.fake = fake

    def __str__(self):
        if self.fake > 0:
            return f"{self.real} + {self.fake}i"
        elif self.real == 0:
            return f"{self.fake}"
        elif self.fake < 0:
            return f"{self.real} - {abs(self.fake)}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.fake + other.fake)

    def __mul__(self, other):
        mul_real = self.real*other.real + -1*self.fake*other.fake
        mul_fake = self.real*other.fake + self.fake*other.real
        return ComplexNumber(mul_real, mul_fake)


cn1 = ComplexNumber(3, 1)
print(cn1)
cn2 = ComplexNumber(2, -3)
print(cn2)
print(f"Результат сложения комплексных чисел {cn1 + cn2}")
print(f"Результат умножения комплексных чисел {cn1 * cn2}")
