"""Реализуйте базовый класс Car:
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
- Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, color, name, is_police, speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return "Это полицейская машина"
        else:
            return "Это гражданская машина"

    def go(self):
        return f"Автомобиль {self.name} начал движение"

    def stop(self):
        self.speed = 0
        return f"Автомобиль {self.name} остановился"

    def turn(self, direction):
        return f"Автомобиль {self.name} движется {direction}"

    def show_speed(self):
        if self.speed > 0:
            return f"Скорость автомобиля {self.name} - {self.speed}км/ч"
        else:
            return f"Автомобиль {self.name} неисправен"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Автомобиь {self.name} превысил скорость на {self.speed - 60} км/ч"
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Автомобиь {self.name} превысил скорость на {self.speed - 40} км/ч"
        else:
            return super().show_speed()


class PoliceCar(Car):
    pass


def test(auto, direction='прямо'):
    print(auto.go())
    print(f"Цвет автомобиля: {auto.color}")
    print(auto.show_speed())
    print(auto.police())
    print(auto.turn(direction))
    print(auto.stop())
    print('##########################################')


town_car = TownCar("красный", "BMW", False, 80)
test(town_car, 'налево')

sport_car = SportCar("красный", "Ferrari", False, 120)
test(sport_car, "направо")

work_car = WorkCar("оранжевый", "Камаз", False, 50)
test(work_car, "назад")

police_car = PoliceCar("синий", "УАЗ Patriot", True, 90)
test(police_car)
