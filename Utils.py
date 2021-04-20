import requests
from decimal import*
from datetime import datetime

getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None

    current_rate = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    current_date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, current_date)
    return f"{(Decimal(current_rate.replace(',', '.')))}, {datetime(day=day, month=month, year=year)}"

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
    print(currency_rates('eur'))
    print(currency_rates('uds'))