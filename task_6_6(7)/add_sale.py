from sys import argv

if __name__ == '__main__':
    try:
        if len(argv) == 1:
            raise Exception('Забыли записать покупку')
        for num in argv[1:]:
            if not num.replace('.', '').replace(',', '').isdecimal():
                raise Exception('Неверная запись, нужно численное значение')

        with open('bakery.csv', 'a') as f:
            #нужно ли добавить несколько цен сразу?
            for line in ((ch.replace('.', ',')) for ch in argv[1:]):
                f.write(f'{line}\n')
            print('Записи о продажах успешно добавлены')
    except Exception as e:
        print(e, '\n')
