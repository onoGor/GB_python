"""Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


def division(num1, num2):
    try:
        if num2 == 0:
            raise DivisionByZero("Ошибка деления на 0")
    except DivisionByZero as e:
        print(e)
    else:
        print(f"Результат деления: {num1} / {num2} = {num1 / num2}")


inp_data = input("Введите два числа через пробел \n")
num1, num2 = map(int, inp_data.split())
division(num1, num2)

