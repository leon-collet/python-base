# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

#dir_list = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp'], 'settings': ['templates', 'config'], 'mainapp': ['restapi']}
dir_list = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def great_dir(new_dir):
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)


for key in dir_list:
    great_dir(key)
    for child in dir_list[key]:
        great_dir(child)
        os.chdir("..")
    if key != 'my_project':
        os.chdir("..")

# Этот вариант решения выглядит более аккуратно и позволяет сделать два уровня вложенности, нужно только расширить словарь.
# Словарь кажется оптимальным, так как не будет повторений папки и ясно видна структура. Создание файлов непредусмотрено
# структурой в задании, по этому и не прописал.
