"""
Шрифты в Pygame. Добавляем текст в окно игры

https://www.youtube.com/watch?v=9s7YpBHJl70
"""
import pygame
pygame.init()

size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя программа')
# img = pygame.image.load('android.png')  # эти две строки создают иконку
# pygame.display.set_icon(img)

# Создаем шрифты.
# Чтобы выбрать шрифт набираем в консоли:
# import pygame
# pygame.font.get_fonts()
# получим список шрифтов:
# сохраним в переменную a = pygame.font.get_fonts()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

font = pygame.font.SysFont('microsofttaile', 32)
# Создаем текст. Аргументы: сам текст, сглаживание текста 1 или 0,
# цвет текста, фон
follow = font.render('Привет Сергей', 1, red, green)

# теперь текст надо разместить на экране

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(follow, (0, 0))  # закрепляем на экране по координатам верхнего левого угла прямоугольника
    pygame.display.update()  # чтобы надпись отобразилась на экране
