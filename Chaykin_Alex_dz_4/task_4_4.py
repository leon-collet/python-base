# Задание 4. Модуль utils
# Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
# Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
# функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:
#
# если используется функция из 2-го задания:
# USD 75.18
# EUR 80.35
# либо, если используется функция из 3-го задания
# USD 75.18, 2020-09-05
# EUR 80.35, 2020-09-05

import utils

response_valute = utils.get_currency_rate('USD')
print(f'Курс USD {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')
response_valute = utils.get_currency_rate('EUR')
print(f'Курс EUR {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')
