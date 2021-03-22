# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# . просто запуск скрипта — выводить все записи;
# . запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# . запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Код записи:
import struct


def save_sum(argv):
    program, *args = argv
    with open('bakery.csv', 'ab') as f:
        for bak_sum in args:
            num_float = str(bak_sum).replace(",",".")
            f.write(struct.pack("d", float(num_float)))
    return 0


if __name__ == '__main__':
    import sys
    exit(save_sum(sys.argv))