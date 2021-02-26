# ЗАДАНИЕ 2
#
# Сумма цифр числа
# Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
# Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".

while True:
    user_num = str(input("Введите число:"))
    if user_num == "0":
        print("Конец программы. Cумма: 0")
        exit(0)
    num_sum = int(0)
    while len(user_num) > 0:
        num_sum += int(user_num[0])
        user_num = user_num[1:]
    print("Cумма: " + str(num_sum))
