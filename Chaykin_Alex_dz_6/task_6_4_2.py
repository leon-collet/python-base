# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

import json

# Прошлый вариант более-менее соответствовал условиям, но если исходные файлы больше ОЗУ, то и файл результата будет
# тоже больше ОЗУ, а значит неправильно создавать в коде словарь, содержащий все результаты парсинга.
# Более правильным решением, по моему мнению, будет считывать исходные файлы построчно, записывать итоговый файл построчно
# и сделать функцию чтения, которая собирает словарь из N строк итогового файла


with open('users.csv', encoding='utf-8') as u, \
        open('hobby.csv', encoding='utf-8') as h, \
        open('users_hobby_6_4_2.txt', 'a', encoding='utf-8') as uh:
    for user in u:
        hobby = h.readline().strip().split(",") if h.readline() != '' else None
        json_list = [user.strip().split(","), hobby]
        uh.write(json.dumps(json_list)+"\n")

def get_dict(start_or_num=None, length=None):
    '''Можно получить три выборки:
    - весь файл - вызываем функцию без аргументов
    - одну строку - указываем 1 аргумент, номер строки считая с 1
    - несколько строк подряд - указываем номер первой и сколько взять'''
    check_dict = {}
    with open('users_hobby_6_4_2.txt', 'r', encoding='utf-8') as uh:
        for i, line in enumerate(uh, start=1):
            list_line = json.loads(line)
            if (length and start_or_num <= i <= start_or_num+length)\
                    or (not length and start_or_num and i == start_or_num)\
                    or (not start_or_num):
                name_tuple = tuple(list_line[0])
                check_dict[name_tuple] = list_line[1]
    return check_dict

new_dict = get_dict(2, 3)
print(new_dict)

