'''

* (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (
не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

'''

import os
import yaml

def create_files(path, name):
    f_path = fr'{path}\{name}'
    if not os.path.exists(f_path):
        with open(f_path, 'w') as f:
            f.write('')
    else:
        print(f'Файл {name} уже существует!')


def create_catalog(path, name):
    catalog_path = fr'{path}\{name}'
    if not os.path.exists(catalog_path):
        os.mkdir(catalog_path)
    else:
        print(f'Каталог {name} уже существует!')

def create_catalog_files(current_path, tree_file):

    # цикл по дереву значений
    for key_tree, value_tree in tree_file.items():
        # если не словарь, т.е. у нас список файлов, тогда создаем файлы
        if type(value_tree) != dict:
            for f_name in value_tree:
                create_files(current_path, f_name)
        else:
            create_catalog(current_path, key_tree)
            create_catalog_files(fr'{current_path}\{key_tree}', value_tree)


# чтение yaml
with open('config_hw2.yaml') as file:
    tree_file = yaml.safe_load(file)

    if len(tree_file) == 0:
        print('Пустой файл шаблона!')
        raise IOError

# текущий путь к каталогу
current_path = os.getcwd()

# Создадим файлф и папки в рекурсии... т.к. дерево легче так обходить
create_catalog_files(current_path, tree_file)