from sys import argv
from decimal import Decimal, InvalidOperation
from os.path import getsize

from config import db_file, record_size

if __name__ == '__main__':
   try:
        if not len(argv) >= 3:
            raise Exception('Передано слишком мало аргументов.')

        try:
            element_id = int(argv[1])
        except ValueError:
            raise Exception('Параметр ID должен быть целым числом!')

        try:
            new_price = Decimal(argv[2].replace(',', '.'))
        except InvalidOperation:
            raise Exception('Параметр NEW_PRICE должен быть числом!')

        all_elements = getsize(db_file) // record_size
        if element_id > all_elements:
            raise Exception(f'Параметр ID превышает максимальное число элементов! Всего элементов: {all_elements}!')

        with open(db_file, 'r+') as db:
            db.seek((element_id - 1) * record_size)
            db.write(f'{str(new_price)[:record_size - 1]:9}\n'.replace('.', ','))

    except Exception as e:
        print(e, '\n')
        print(helps)