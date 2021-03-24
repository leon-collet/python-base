# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import json
import os
from collections import defaultdict

# Папку some_data скачал из списка файлов к уроку, так как в my_project все файлы создавал практически пустыми
files_dir = 'some_data'
# files_dir = 'my_project'
file_ext = defaultdict(set)
file_sizes = defaultdict(int)
file_info = {}

for root, dirs, files in os.walk(files_dir):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        order = 10**len(str(size))
        extension = file.split('.')[1]
        file_sizes[order] += 1
        file_ext[order].add(extension)


for ext, size in zip(sorted(file_ext), sorted(file_sizes)):

    file_info[ext]=[file_sizes[size], list(file_ext[ext])]

for key in sorted(file_info):
    print(f'{key} : {file_info[key]}')

print(type(file_info))

with open('task_7_5_summary.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(file_info))

with open('task_7_5_summary.json', 'r', encoding='utf-8') as f:
    print(json.loads(f.read()))