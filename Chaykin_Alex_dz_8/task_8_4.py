# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps

def val_checker(validate_arg):
    def type_logger(func):
        @wraps(func)
        def type_wrapper(*args, **kwargs):
            if(validate_arg(*args)):
                result = func(*args, **kwargs)
                return result
            else:
                msg = f'Невалидное значение {args[0]}'
                raise ValueError(msg)
        return type_wrapper
    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    '''
    Функция принимает строго один аргумент и возводит его в куб
    :param x:
    :return:
    '''
    return x ** 3

a = calc_cube(5)

# b = calc_cube(-5)

print(help(calc_cube))