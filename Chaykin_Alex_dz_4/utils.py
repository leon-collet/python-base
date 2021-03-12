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
            return round(Decimal(value.replace(",", ".")), 2), resp_date

