# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# src_res = src[1:]
# result = []
#
# for num_min, num_max in zip(src, src_res):
#     if num_min < num_max:
#         result.append(num_max)

# src_res = src[1:]
# result = [num_max for num_min, num_max in zip(src, src_res) if num_min < num_max]

result = [num_max for i, num_max in enumerate(src[1:]) if num_max > src[i]]
print(result)
