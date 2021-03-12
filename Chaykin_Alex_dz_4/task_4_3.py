# Задание 3. * Курс Валюты (расширенный)
# Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
# на которую этот курс действует (взять из того же файла ЦБ РФ).
# Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
# Дата должна быть типа datetime.date.

from requests import get
from xml.dom import minidom
from datetime import date
from decimal import *


def get_currency_rate(code):
    cdr_response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml_parsed = minidom.parseString(cdr_response.text)
    datelist = (xml_parsed.getElementsByTagName("ValCurs")[0].getAttribute("Date")).split('.')
    resp_date = date(int(datelist[2]), int(datelist[1]), int(datelist[0]))
    for valute in xml_parsed.getElementsByTagName("Valute"):
        if valute.getElementsByTagName("CharCode")[0].firstChild.nodeValue == code.upper():
            value = valute.getElementsByTagName("Value")[0].firstChild.nodeValue
            return Decimal(value.replace(",", ".")), resp_date


# code = input("Курс какой валюты вас интересует? ")
# print(get_currency_rate(code))

response_valute = get_currency_rate('USD')
print(f'Курс USD {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')