'''

Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

'''

import os

# текущий католог
main_catalog = os.getcwd()

# словарь для записи статистики
dict_size = {
    1000: 0,
    10000: 0,
    100000: 0,
}
# цикл по файлам в иерархии
for path, catalog, files in os.walk(main_catalog):
    list_size = [os.stat(fr'{path}\{file}').st_size for file in files]
    dict_size[1000] += len([file_size for file_size in list_size if file_size < 1000])
    dict_size[10000] += len([file_size for file_size in list_size if 1000 <= file_size < 10000])
    dict_size[100000] += len([file_size for file_size in list_size if 10000 <= file_size < 100000])

# результат
print(dict_size)