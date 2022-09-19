# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
# в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile(r'^([^\@]+)\@([^\@]+\.\w{2,10})$')

def email_parse(email):
    result = RE_EMAIL.findall(email)
    if result:
        return {'username': result[0][0], 'domain': result[0][1]}
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)

# print(email_parse(input('Введите email: ')))
# print(email_parse('support@geekbrains.ru'))
# print(email_parse('support@geekbrainsru'))
print(email_parse('павелфролов@москва.онлайн'))