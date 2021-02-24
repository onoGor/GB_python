from requests import get, utils
from datetime import date


def currency_rates(code_money):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    idx = content.find(code_money)
    if idx > 0:
        str_result = content[idx:idx+120]
        idx_start = str_result.find('<Value')
        idx_end = str_result.find('</Value')
        str_value = str_result[idx_start+7:idx_end]
        num_res = str_value.replace(',', '.')
        return float(num_res)
    else:
        return None


print(date.today(), 'Евро = ', str(currency_rates('EUR')), 'рублей')
print(date.today(), 'доллара США =', str(currency_rates('USD')), 'рублей')
print(date.today(), 'Фунт стерлингов =', str(currency_rates('GBP')), 'рублей')

