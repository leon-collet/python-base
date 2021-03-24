# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os

with open('config.yaml', 'r+', encoding='utf-8') as f:
    start_level = 0
    for line in f:
        num_level = line.count('|   ') + line.count('|--')
        name = line.replace('|   ', '').replace('|--', '').strip()
        for i in range(start_level - num_level):
            os.chdir('..')
        start_level = num_level
        if not name.count('.'):
            if not os.path.exists(name):
                os.mkdir(name)
            os.chdir(name)
            start_level += 1
        elif not os.path.exists(name):
            with open(name, 'w', encoding='utf-8') as f:
                f.write('empty')