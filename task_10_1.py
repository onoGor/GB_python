"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""
class Matrix:

    def __init__(self, m_list):
        self.elements = m_list

    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.elements])

    def __add__(self, second_m):
        result = []
        if len(self.elements) == len(second_m.elements):
            for row in range(len(self.elements)):
                result.append([self.elements[row][cell] + second_m.elements[row][cell]
                               for cell in range(len(self.elements[row]))])
        else:
            return 'Невозможно сложить матрицы'
        return result


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Матрица 1 \n{m1}')
m2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(f'Матрица 2 \n{m2}')
m3 = Matrix(m1 + m2)
print(f'Результат сложения матриц \n{m3}')