'''

(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно
ли для них уточнить регулярное выражение?

'''
import re

# str = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

# regexp = re.compile('^\d{1,3}(?:[.-]\d{1,3}){3}')
# regexp = re.compile('\d\d[\/]\w+[\/]\w+(?:[:-]\d{2}){3}[ +][+]\d\w+')
regexp = re.compile('^(.*)\s-\s-\s.*\[(.+)]\s\"(\w*)\s(.*?)\"\s(\d{3})\s(\d*)\s')


# print(re.findall(regexp, str))

# Читаем файл
with open('nginx_logs.txt', 'r', encoding='UTF8') as f:
    file_data = (re.findall(regexp, i) for i in f.readlines())

print(*file_data)