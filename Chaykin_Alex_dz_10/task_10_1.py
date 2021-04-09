# 1. Реализовать класс Matrix (матрица).
# Конструктор класса __init__() должен принимать список списков чисел для задания превоначального состояния матрицы.
# Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# В методе __init__() надо проверить корректность передаваемых данных - все списки должны быть одинаковой длины.
# В случае расхождения выбрасывать исключение ValueError с соответствующим описанием.
# Добавить метод __add__() сложения двух матриц. Складывать можно матрицы одинаковой размерности.
# В случае, когда пользователь пытается сложить матрицы разных размеров выбросить исключение ValueError.
# В результате сложения двух матриц должна образоваться новая матрица размером N x M, где каждый элемент в ячейке i,j образован сложением значений из соответствующих ячеек исходных матриц.
# Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6", отводя под числа по три разряда, чтобы для небольших чисел матрица выглядела как таблица.
# Создать три матрицы (две одинаковые по размеру и одну с другим размером).
# Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат сложения.