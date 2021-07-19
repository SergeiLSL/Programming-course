"""
Как создать игровое поле для своей игры Pygame. Клеточное поле, Поле в клетку

Знакомство с библиотекой pygame

https://www.youtube.com/watch?v=HdretXgMBGg
Артем Егоров
"""
"""
Почти в каждой игре есть игровое поле, которое разделено на квадратики.
И в процессе игры мы должны с ними взаимодействовать.
Рассмотри как можно создать такое игровое поле.
И также научимся при помощи мышки изменять состояние каждого квадратика.
Причем программа сохраняет состояние этих квадратиков. И при 
повторном нажатии делает их вновь беллого цвета.
"""

import pygame
import sys

# pygame.init()
#
# size = (510, 510)  # размер игрового поля
# screen = pygame.display.set_mode(size)  # выводим на экран игровое поля
# pygame.display.set_caption('Game field')  # название игрового поля
#
# # зададим параметры квадратика
# width = height = 40  # ширина и высота квадратика
# red = (255, 0, 0)  # цвет квадратика
# margin = 10  # для того чтобы межу квадратиками был промежуток
#
# while True:
#     for event in pygame.event.get():  # цикл обработки событий
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     # Нарисуем один квадратик. красный, начало 0,0 конец  width, height
#     # pygame.draw.rect(screen, red, (0, 0, width, height))
#     # pygame.display.update()  # обновим экран
#     # Нарисуем еще 10 квадратиков в строке
#     for col in range(10):  # надо заполнить первую строку
#         x = col * width + (col + 1) * margin # меняется только координата x
#         pygame.draw.rect(screen, red, (x, 0, width, height))
#     pygame.display.update()

"""
Теперь надо заполнить ряды создадим еще один цикл и зададим 
переменную игрек
"""
# pygame.init()
#
# size = (510, 510)  # размер игрового поля
# screen = pygame.display.set_mode(size)  # выводим на экран игровое поля
# pygame.display.set_caption('Game field')  # название игрового поля
#
# # зададим параметры квадратика
# width = height = 40  # ширина и высота квадратика
# red = (255, 0, 0)  # цвет квадратика
# margin = 10  # для того чтобы межу квадратиками был промежуток
#
# while True:
#     for event in pygame.event.get():  # цикл обработки событий
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     for col in range(10):  # надо заполнить первую строку
#         for row in range(10):
#             x = col * width + (col + 1) * margin  # меняется только координата x
#             y = row * height + (row + 1) * margin  #
#             pygame.draw.rect(screen, red, (x, y, width, height))
#     pygame.display.update()


"""
Научимся реагировать на мышку
"""
# pygame.init()
#
# size = (510, 510)  # размер игрового поля
# screen = pygame.display.set_mode(size)  # выводим на экран игровое поля
# pygame.display.set_caption('Game field')  # название игрового поля
#
# # зададим параметры квадратика
# width = height = 40  # ширина и высота квадратика
# red = (255, 0, 0)  # цвет квадратика
# margin = 10  # для того чтобы межу квадратиками был промежуток
#
# while True:
#     for event in pygame.event.get():  # цикл обработки событий
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         #  добавим блок - если у события был тип : нажатие на мышку,
#         #  то заводим две переменные, определяющие координаты этого события
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             print(f'x = {x_mouse} y = {y_mouse}')
#     for col in range(10):  # надо заполнить первую строку
#         for row in range(10):
#             x = col * width + (col + 1) * margin  # меняется только координата x
#             y = row * height + (row + 1) * margin  #
#             pygame.draw.rect(screen, red, (x, y, width, height))
#     pygame.display.update()

"""
Создадим массив, в которм будем хранить состояние на поле
"""
pygame.init()

size = (510, 510)  # размер игрового поля
screen = pygame.display.set_mode(size)  # выводим на экран игровое поля
pygame.display.set_caption('Game field')  # название игрового поля

# зададим параметры квадратика
width = height = 40  # ширина и высота квадратика
margin = 10  # для того чтобы межу квадратиками был промежуток
red = (255, 0, 0)  # цвет квадратика
white = (255, 255, 255)  # цвет квадратика
# массив будет состоять из нолей, создадим генератор списков
mas = [[0] * 10 for i in range(10)]
# развернуто
# mas = []
# for i in range(10):
#     a = [0] * 10
#     mas.append(a)

while True:
    for event in pygame.event.get():  # цикл обработки событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #  добавим блок - если у события был тип : нажатие на мышку,
        #  то заводим две переменные, определяющие координаты этого события
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x = {x_mouse} y = {y_mouse}')
            column = x_mouse // (margin + width)  # узнаем номер колонки
            row = y_mouse // (margin + height)  # узнаем номер строки
            mas[row][column] = mas[row][column] ^ 1  # побитово умножаем, то есть меняем на противоположенный
    for row in range(10):  # поменяли местами, как в стандартном обходе
        for col in range(10):  # добавим проверкуу цвета квадратика
            if mas[row][col] == 1:
                color = red
            else:
                color = white
            x = col * width + (col + 1) * margin  # меняется только координата x
            y = row * height + (row + 1) * margin  #
            pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.update()