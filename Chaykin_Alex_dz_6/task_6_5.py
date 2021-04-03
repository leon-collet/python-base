# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам
# и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

import argparse
import json

parser = argparse.ArgumentParser(description='Сделать словарь имён и хобби')
parser.add_argument('users', type=str, help='Название и путь к файлу со списком людей')
parser.add_argument('hobby', type=str, help='Название и путь к файлу со списком хобби')
parser.add_argument('json', type=str, help='Название и путь к файлу для хранения словаря')
args = parser.parse_args()

users_hobby = {}
write_line = {}

with open(args.users, encoding='utf-8') as u, \
        open(args.hobby, encoding='utf-8') as h, \
        open(args.json, 'a', encoding='utf-8') as uh:
    for user in u:
        hobby = h.readline().strip().split(",") if h.readline() != '' else None
        users_hobby[tuple(user.strip().split(","))] = hobby
        write_line[user.strip()] = hobby
    uh.write(json.dumps(write_line))

print(type(users_hobby), users_hobby, sep='\n')

check_dict = {}

with open(args.json, 'r', encoding='utf-8') as uh:
    check = json.loads(uh.read())
    for people in check:
        check_dict[tuple(people.strip().split(","))] = check[people]

print(type(check_dict), check_dict, sep='\n')
