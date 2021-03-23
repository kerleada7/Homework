'''

Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
 (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
 решена, например, во фреймворке django.

'''
import os
from shutil import copy2

# Каталог для копирования
catalog_copy = r'my_project\templates'

# создадим каталог если его нет
if not os.path.exists(catalog_copy):
    os.mkdir(catalog_copy)

# теущий католог
main_catalog = os.getcwd()
for path, catalog, files in os.walk(main_catalog):
    # print(path, catalog, files)
    # цикл по файлам
    for file in files:
        # если нашли искомый файл попробуем его скопировать
        if file.endswith('.html'):
            new_path = catalog_copy + '\\' + path.split("\\")[-1]
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            if not os.path.exists(fr'{new_path}\{file}'):
                copy2(fr'{path}\{file}', f'{new_path}')
            else:
                print(f'Файл {file} уже был скопирован')
