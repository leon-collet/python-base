# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в
# обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную
# задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы
# с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции
# не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get
from xml.dom import minidom


def currency_rates(code):
    cdr_response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml_parsed = minidom.parseString(cdr_response.text)
    for valute in xml_parsed.getElementsByTagName("Valute"):
        if valute.getElementsByTagName("CharCode")[0].firstChild.nodeValue == code:
            value = valute.getElementsByTagName("Value")[0].firstChild.nodeValue
            return round(float(value.replace(",", ".")), 2)

code = input("Курс какой валюты вас интересует? ").upper()

print(currency_rates(code))
