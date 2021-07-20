"""
Крестики нолики
https://www.youtube.com/watch?v=GElUzJ7-bcI
Артем Егоров
"""
import pygame
import sys
pygame.init()

def chek_win(mas, sign):
    """ Проверка на победу """ # вариантов много
    zeroes = 0
    for row in mas:  # проверяем строки на одинаковые знаки
        zeroes += row.count(0)
        if row.count(sign) == 3:  # считаем одинаковые знаки в строке
            return sign
    for col in range(3):  # проверяем колонки на одинаковые знаки
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:  # проверяем главную диагональ
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:  # проверяем вторую диагональ
        return sign
    if zeroes == 0:  # ничья
        return 'Piece'
    return False


# pygame.init()  # создаем блок размером 100 на 100
size_blok = 100  # размер блока 100 пикселей
margin = 10  # отступ 10 пикселей
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
# для того, чтобы цвета чередовались создадим переменную
query = 0  # будем постепенно увеличивать на 1 2 3 4 5 6 7.
# В этом ряду четные и нечетные числа. Значит проверкой на
# четность можем создать чередование, чтобы понимать какой игрок сейчас ходит
game_over = False

while True:
    for event in pygame.event.get():  # цикл обработки событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x = {x_mouse} y = {y_mouse}')
            col = x_mouse // (size_blok + margin)  # узнаем номер колонки
            row = y_mouse // (size_blok + margin)  # узнаем номер строки
            # сделаем проверку на занятость клетки
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)  # закрашиваем экран черным цветом
    if not game_over:
        for row in range(3):  # цикл обхода строк и столбцов
            for col in range(3):  # находим координаты левого верхнего блока
                if mas[row][col] == 'X':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_blok + (col + 1) * margin  # координата x
                y = row * size_blok + (row + 1) * margin  # координата y
                pygame.draw.rect(screen, color, (x, y, size_blok, size_blok))
                if color == red:
                    pygame.draw.line(screen, white, (x + 8, y + 8), (x + size_blok - 8, y + size_blok - 8), 4)
                    pygame.draw.line(screen, white, (x + size_blok - 8, y + 8), (x + 8, y + size_blok - 8), 4)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_blok//2, y + size_blok//2), size_blok//2 - 8, 4)
    if (query - 1) % 2 == 0:  # X
        game_over = chek_win(mas, 'X')
    else:
        game_over = chek_win(mas, 'o')

    if game_over:
        screen.fill(black)  # закрашиваем экран черным цветом
        font = pygame.render.SysFont('comicsansms', 80)  # создаем шрифт
        text1 = font.render(game_over, True, white)  # будет содержать game_over белым цветом
        text_rect = text1.get_rect()  # узнаем его координаты
        text_x = screen.get_width() / 2 - text_rect.width / 2   # находим центр экрана
        text_y = screen.get_height() / 2 - text_rect.height() / 2  # находим центр экрана
        screen.blit(text1, [text_x, text_y])  # прикрепляем текст по координатам

    pygame.display.update()  # вызываем изменения на экране




