"""
Вывести простые числа 0 до заданного .
"""


def convert():
    i = 1
    x = int(input('Введите число: '))
    while i < x:
        print(i)
        i = i + 2


convert()
while True:
    flag = input('Ещё раз? [y/n]: ')
    if flag == 'y':
        convert()
    else:
        print('Good bay')
        break
