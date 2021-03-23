'''

 Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

'''

import json
import os


with open('starter_7_1.json') as f:
    list_file = json.load(f)

# текущий путь к каталогу
current_path = os.getcwd()

# цикл по массиву путей
for i in list_file:
    catalog_f = i.get("catalog")
    parent_f = i.get("parent")

    if parent_f == '':
        new_path = fr'{current_path}\{catalog_f}'
    else:
        new_path = fr'{current_path}\{parent_f}\{catalog_f}'

    # создаем каталог
    if not os.path.exists(new_path):
        os.mkdir(new_path)