# Задание 5. * Вызов с командной строки
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
# а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
# Вывод курсов сделать в том же порядке, что присланные аргументы
# Например:
#
# python task5.py USD EUR
# USD 75.18, 2020-09-05
# EUR 80.35, 2020-09-05

import utils

def main(argv):
    program, *args = argv
    for code in args:
        response_valute = utils.get_currency_rate(code)
        print(f'Курс {code.upper()} {response_valute[0]} руб. на {response_valute[1].strftime("%d.%m.%Y")}')
    return 0


if __name__ == '__main__':
   import sys

   exit(main(sys.argv))
