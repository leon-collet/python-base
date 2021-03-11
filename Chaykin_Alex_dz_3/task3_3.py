# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Сможете ли вы вернуть отсортированный по ключам словарь?

name_dict = {}


def thesaurus(*args):
    for one_name in args:
        any_names = filter(lambda el: el.startswith(one_name[0]), args)
        name_dict[one_name[0]] = [*any_names]
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# вернуть сам словарь отсортированный по значениям у меня не вышло, он превращается в список
# отсортированных ключей, но из них можно сделать новый словарь

sort_list = sorted(thesaurus("Алексей"))
print(name_dict)

new_name_dict = {}
for sort_name in sort_list:
    new_name_dict[sort_name] = name_dict[sort_name]

print(new_name_dict)



