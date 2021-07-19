"""
Крестики нолики
https://www.youtube.com/watch?v=GElUzJ7-bcI
Артем Егоров
"""
import pygame
import sys

pygame.init()  # создаем блок размером 100 на 100
size_blok = 100  # размер блока 100 пикселей
margin = 15  # отступ 15 пикселей
width = height = size_blok * 3 + margin * 4  # по высоте и ширине по 3 блока и 4 отступа

size_window = (width, height)  # выводим в окно
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')

# подбираем цвета
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]  # поготовим массив, заполненный нулями.
# нули обозначают, что клетка еще пустая

while True:
    for event in pygame.event.get():  # цикл обработки событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(3):  # цикл обхода строк и столбцов
        for col in range(3):  # находим координаты левого верхнего блока
            x = col * size_blok + (col + 1) * margin  # координата x
            y = row * size_blok + (row + 1) * margin  # координата y
            pygame.draw.rect(screen, white, (x, y, size_blok, size_blok))  # зная координаты
            # обращаемся к модулю pygame, draw, выводим на экран белого цвета с координатами
            # x, y и нижний блок с координатами size_blok, size_blok
        pygame.display.update()  # вызываем изменения на экране




