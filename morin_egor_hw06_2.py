'''

* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.

'''

# открываем файл для чтения и читаем построчно, создаем генератор.
with open('nginx_logs.txt', 'r') as file_nginx_logs:
    data_file = (l.split(" ") for l in file_nginx_logs.readlines())

# с помощью генератор создаем список ip
list_result = list(((next_value[0]) for next_value in data_file))
# создаем словарь, сорт. по значениям
dict_ip_count = sorted({i:list_result.count(i) for i in set(list_result)}.items(), key=lambda kv: kv[1])

print(dict_ip_count)
print(dict_ip_count[-1])