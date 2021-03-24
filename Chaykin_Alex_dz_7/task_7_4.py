# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
from collections import defaultdict

# Папку some_data скачал из списка файлов к уроку, так как в my_project все файлы создавал практически пустыми
files_dir = 'some_data'
# files_dir = 'my_project'
file_sizes = defaultdict(int)

for root, dirs, files in os.walk(files_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        order = 10**len(str(size))
        file_sizes[order] += 1

for key in sorted(file_sizes):
    print(f'{key} : {file_sizes[key]}')
