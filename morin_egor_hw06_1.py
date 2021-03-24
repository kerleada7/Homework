'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

# функция получения следующего эелемента генератора, пока не закончится
def next_generation(generator):
    try:
        next_value = next(generator)
        print((next_value[0], next_value[5].replace('"',''), next_value[6]))
    except StopIteration:
        print('...StopIteration...')
        return False
    else:
        return True

# открываем файл для чтения и читаем построчно, создаем генератор.
with open('nginx_logs.txt', 'r') as file_nginx_logs:
    data_file = (l.split(" ") for l in file_nginx_logs.readlines())


# fl = True
# # цикл по генератору
# while fl:
#     fl = next_generation(data_file)

# с помощью генератор создаем список кортежей
result = list(((next_value[0], next_value[5].replace('"',''), next_value[6]) for next_value in data_file))
print(result)