# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

dict_translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
}


def num_translate_adv(number):
    translate = dict_translate.get(number.lower())
    if number[0].isupper():
        print("Заглавная")
        translate = translate.title()
    return translate


number = input('Введите число для перевода: ')
print(f'Перевод "{number}": {num_translate_adv(number)}')