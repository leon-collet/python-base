# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
# вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

RE_LOGS = re.compile(r'^([[\d{1,4}\.]{5,}\d{1,4}).*\[(.*)\].{2}(\w+)\s(\/[a-z,/,_,0-9]*)')

def logs_parse(logs_line):
    raw_result = RE_LOGS.findall(logs_line)
    return raw_result

with open('nginx_logs.txt', encoding='utf-8') as f:
    i = 0
    while i < 10:
        line = f.readline().strip()
        print(line)
        print(logs_parse(line))
        print('-----------')
        i += 1