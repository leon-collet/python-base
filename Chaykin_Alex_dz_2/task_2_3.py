# Задание 3
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(main_list):
    if main_list[i].isdigit():
        main_list[i] = f'{int(main_list[i]):02}'
        main_list.insert(i, '"')
        main_list.insert(i + 2, '"')
        i += 1
    elif (main_list[i][1:] if main_list[i][0] in ['+','-'] else '').isdigit():
        main_list[i] = f'{main_list[i][0]}'f'{int(main_list[i]):02}'
        main_list.insert(i, '"')
        main_list.insert(i + 2, '"')
        i += 1
    i += 1

print(main_list)

# После этого примера понял всю прелесть регулярок и стал жалеть что ещё их не знаю и не использую

msg_str = " ".join(main_list)

left_space = True

# Возможно это очень криво, но мне показалось лучшим вариантом: первая найденная табличка всегда открывающая,
# значит мы можем расставлять их по очереди, а цикл будет работать пока не кончатся кавычки с пробелами с двух сторон
# (это косяк, понимаю, кавычка может быть в конце предложения)

while 1 <= msg_str.count(' " '):
    if left_space:
        msg_str = msg_str.replace(' " ', ' "', 1)
    else:
        msg_str = msg_str.replace(' " ', '" ', 1)
    left_space = not left_space

print(msg_str)
