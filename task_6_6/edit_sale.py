from os.path import getsize
file_sale = 'bakery.csv'
max_line = getsize(file_sale)
    # sum(1 for line in open(file_sale, 'r'))

def main(argv):
    program, *args = argv
    try:
        if args[0] == '0':
            raise Exception('Нумерация записей с 1')
        if int(args[1]) > max_line:
            raise Exception(f'Максимальное число записей:{max_line}')
        if len(args) > 2:
            raise Exception('Неверные параметры')
        start = int(args[0])-1 if len(args) >= 1 else 0
        stop = int(args[1]) if len(args) == 2 else max_line
        with open(file_sale) as f:
            lines = f.readlines()
            lines = lines[start:stop]
            for li in lines:
                print(li.strip())
    except Exception as e:
        print(e, '\n')
    # return 0


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))