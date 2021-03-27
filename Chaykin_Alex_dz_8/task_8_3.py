# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    message = []
    def type_wrapper(*args, **kwargs):
        for num in args:
            message.append(f'{num}: {type(num)}')
        for key, val in kwargs.items():
            message.append(f'{key}: {val}')
        print(f'{func.__name__}({", ".join(message)})')
        result = func(*args, **kwargs)
        return result
    return type_wrapper


@type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def calc_sum(x, y):
    return x + y

@type_logger
def calc_str(owner, **pets):
    string = f'Owner - {owner}'
    for pet, name in pets.items():
        string += f', {pet} names {name}'
    return string


a = calc_cube(5)
b = calc_sum(5, 6)
c = calc_str('Alex', dog='Mark', cat='Mya')
