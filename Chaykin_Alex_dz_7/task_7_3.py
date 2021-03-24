# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os, shutil

root_folder = os.path.abspath('my_project')
folder = os.path.join(root_folder, 'templates')
os.chdir('my_project')
if not os.path.exists('templates'):
    os.mkdir('templates')

for root, dirs, files in os.walk('.'):
    if root.__contains__('templates') and not root.startswith('./templates'):
        new_dir = root.split('templates')[1].strip('/')
        copy_folder = os.path.join(folder, new_dir) if new_dir != '' else folder
        os.chdir(root)
        try:
            for copy_file in files:
                if not os.path.exists(os.path.join(copy_folder, copy_file)):
                    shutil.copy2(copy_file, copy_folder)
            for copy_dir in dirs:
                if not os.path.exists(os.path.join(copy_folder, copy_dir)):
                    os.mkdir(os.path.join(copy_folder, copy_dir))
        except ValueError as e:
            print(f'Ошибка со значением пути или именем файла/директории: {e}')
        os.chdir(root_folder)
