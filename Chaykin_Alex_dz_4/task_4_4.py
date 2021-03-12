import utils

response_valute = utils.get_currency_rate('USD')
print(f'Курс USD {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')
response_valute = utils.get_currency_rate('EUR')
print(f'Курс EUR {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')