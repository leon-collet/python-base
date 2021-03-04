# ЗАДАНИЕ 3
#
# Сумма чисел из списка *
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):
#
# 1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
#
# 2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.
#
# 3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков

kub_list = list()
i = 1

while i < 1000:
    kub_list.append(i**3)
    i += 2

print("Список кубов нечётных чисел: ")
print(kub_list)

# Список кубов нечётных чисел создан.
# Использовал функцию, чтобы не повторять код для второго вычисления
# Первое вычисление:

def krat_seven_check(kub_list):
    global sum_krat_seven
    sum_krat_seven = 0

    for num_ins in kub_list:
        a = 0
        krat_seven = 0

        while a < len(str(num_ins)):
            krat_seven += int(str(num_ins)[a])
            a += 1

        if krat_seven % 7 == 0:
            sum_krat_seven += num_ins

krat_seven_check(kub_list)

print("1. Сумма элементов, сумма чисел которых делится на 7 без остатка: ")
print(sum_krat_seven)

# Второе вычисление:
plus_kub_list = list()

for inst_num in kub_list:
    plus_kub_list.append(inst_num + 17)

krat_seven_check(plus_kub_list)

print("2. Та же сумма, но после увеличения массива на 17: ")
print(sum_krat_seven)

# Третие вычисление:
j = 0
while j < len(kub_list):
    kub_list[j] += 17
    j += 1

krat_seven_check(kub_list)

print("3. Та же сумма, но без создания нового списка: ")
print(sum_krat_seven)