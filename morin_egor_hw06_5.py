'''

**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов
 и имя выходного файла. Проверить работу скрипта.

'''

import os
import general_functions

# запросим пути
files_users = input('Путь к файлу с юзерами: ')
files_hobby = input('Путь к файлу с хобби: ')
files_save = input('Путь к файл, для сохранения данных: ')

# проверка на существование файла
if not os.path.isfile(files_users):
    print(f'Файл не существует: {files_users}')
    raise IOError

# проверка на существование файла
if not os.path.isfile(files_hobby):
    print(f'Файл не существует: {files_hobby}')
    raise IOError

# вызов модуля
general_functions.save_common_file(files_users, files_hobby, files_save)

