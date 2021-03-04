from requests import get, utils


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
