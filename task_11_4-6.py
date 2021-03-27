from abc import ABC, abstractmethod
"""11.4
Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
11.5
Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру (например, словарь).
11.6
Реализовать механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


class Warehouse:
    def __init__(self):
        self.org_count = {
            'printer': {},
            'scanner': {},
            'copier': {}
        }

    def add_to_warehouse(self, eq_type, eq_name, count):
        try:
            count = int(count)
            if count > 0:
                if eq_name not in self.org_count[eq_type]:
                    self.org_count[eq_type].update({eq_name: count})
                else:
                    self.org_count[eq_type][eq_name] += count
        except ValueError:
            print("Некорректный ввод")

    def sold_to(self, eq_type, eq_name, count):
        try:
            count = int(count)
            if count > 0 and count < self.org_count[eq_type][eq_name]:
                self.org_count[eq_type][eq_name] -= count
                print(f"{eq_name} в количестве {count} шт проданы")
        except ValueError:
            print("Некорректный ввод")


class Office_equipment(ABC):
    @abstractmethod
    def __init__(self, type:str, model, price=0):
        self.type = type
        self.model = model
        self.price = price


class Printer(Office_equipment):
    def __init__(self, type:str, model, price, color=False):
        super().__init__(type, model, price)
        self.color = color

    def __str__(self):
        if self.color:
            c = 'цветной'
        else:
            c = 'черно-белый'
        return f"{self.type.capitalize()} {self.model} {c}, цена - {self.price}"


class Scanner(Office_equipment):
    def __init__(self, type:str, model, price):
        super().__init__(type, model, price)

    def __str__(self):
        return f"{self.type.capitalize()} {self.model}, цена - {self.price}"


class Copier(Office_equipment):
    def __init__(self, type:str, model, price, fax=False):
        super().__init__(type, model, price)
        self.fax = fax

    def __str__(self):
        if self.fax:
            c = 'есть факс'
        else:
            c = 'без факса'
        return f"{self.type.capitalize()} {self.model} {c}, цена - {self.price}"


wh = Warehouse()
tech1 = Printer('printer', 'Epson L120', 4500)
print(tech1)
wh.add_to_warehouse(tech1.type, tech1.model, 5)
tech2 = Printer('printer', 'Canon Pixma G1411', 6000, True)
print(tech2)
wh.add_to_warehouse(tech2.type, tech2.model, 5)
tech3 = Scanner('scanner', 'XEROX MobileScanner', 25000)
wh.add_to_warehouse(tech3.type, tech3.model, 15)
print(tech3)
tech4 = Copier('copier', 'CANON imageRUNNER C1225iF', 40000, True)
wh.add_to_warehouse(tech4.type, tech4.model, 10)
print(f"Состояние склада на текущий момент:\n {wh.org_count}")
wh.sold_to('scanner',tech3.model, 5)
print(f"Состояние склада на текущий момент:\n {wh.org_count}")

