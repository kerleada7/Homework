'''

* (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

'''

import os
from pathlib import Path

# текущий католог
main_catalog = os.getcwd()

# словарь для записи статистики
dict_size = {
    1000: 0,
    10000: 0,
    100000: 0,
}


# цикл по файлам в иерархии
for key_size in dict_size.keys():
    list_size = []
    list_suffix = []
    for path, catalog, files in os.walk(main_catalog):
        list_size += [os.stat(fr'{path}\{file}').st_size for file in files if os.stat(fr'{path}\{file}').st_size < key_size]
        list_suffix += [Path(file).suffix for file in files]

    dict_size[key_size] = (len(list_size), list(set(list_suffix)))

# результат
print(dict_size)