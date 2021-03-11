file_sale = 'bakery.csv'
max_line = sum(1 for line in open(file_sale, 'r'))


def main(argv):
    program, *args = argv
    try:
        if argv[1] == '0':
            raise Exception('Нумерация записей с 1')
        if int(argv[1]) > max_line:
            raise Exception(f'Максимальное число записей:{max_line}')
        if len(args) != 2:
            raise Exception('Введите номер строки для редактирования и новую сумму продажи')
        records = []
        line_edit = int(argv[1])
        new_record = argv[2].strip().replace('.', ',')
        with open(file_sale, 'r', encoding='utf-8') as f:
            for line in f:
                records.append(line.strip())
        records[line_edit - 1] = new_record
        with open(file_sale, 'w', encoding='utf-8') as f:
            f.write("\n".join(records))
            print('Запись успешно отредактирована')
    except Exception as e:
        print(e, '\n')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
