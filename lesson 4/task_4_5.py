from datetime import date
from requests import get, utils


def main(argv):
    program, *args = argv
    code_money = str(args[0])
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    idx = content.find(code_money)
    if idx > 0:
        str_result = content[idx:idx + 120]
        idx_start = str_result.find('<Value')
        idx_end = str_result.find('</Value')
        str_value = str_result[idx_start + 7:idx_end]
        num_res = str_value.replace(',', '.')
        print(date.today(), args[1], '= ', num_res, 'рублей')
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
