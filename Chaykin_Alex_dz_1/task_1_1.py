# ЗАДАНИЕ 1
#
# Человеко-ориентированное представление интервала времени
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
#
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
#
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

user_seconds = int(input('Введите число секунд:'))
time_cut_names = [' сек', ' мин', ' час', ' дн']
time_cut_length = [60, 60, 24, 365]
answer = ""
i = 0

while user_seconds > 0 and i <= 3:
    if (user_seconds % time_cut_length[i]) > 0:
        answer = str(user_seconds % time_cut_length[i]) + time_cut_names[i] + " " + answer
    user_seconds = user_seconds // time_cut_length[i]
    i += 1

print(answer)
