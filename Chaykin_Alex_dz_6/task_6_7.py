# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи
# и новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию,
# когда пользователь вводит номер записи, которой не существует.
import struct


def update_sum(argv):
    program, *args = argv
    with open('bakery.csv', 'rb+') as f:
        f.seek(0, 2)
        line = (int(args[0]) - 1) * 8
        if line <= f.tell():
            f.seek(line)
            num_float = str(args[1]).replace(",",".")
            f.write(struct.pack("d", float(num_float)))
    return 0


if __name__ == '__main__':
    import sys
    exit(update_sum(sys.argv))