# ЗАДАНИЕ 4
#
# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

i = 1
words = ["процент", "процента", "процентов"]

while i <= 100:
    i = str(i)
    answer = i + " "
    if int(i[-1]) == 1 and int(i) != 11:
        print(answer + words[0])
    elif 1 < int(i[-1]) < 5 and int(i) != 12 and int(i) != 13 and int(i) != 14:
        print(answer + words[1])
    else:
        print(answer + words[2])
    i = int(i) + 1
