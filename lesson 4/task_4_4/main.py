from datetime import date
from utils import currency_rates

print(date.today(), 'Евро = ', str(currency_rates('EUR')), 'рублей')
print(date.today(), 'доллара США =', str(currency_rates('USD')), 'рублей')
print(date.today(), 'Фунт стерлингов =', str(currency_rates('GBP')), 'рублей')

