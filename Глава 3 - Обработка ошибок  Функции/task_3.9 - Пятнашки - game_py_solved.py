"""
**Требования:
1. Игра пятнашки: https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_15
2. Поле состоит из клеток от 1 до 15 и пустой клетки
3. Управление ведется кнопками "wasd", двигается пустая клетка
4. В начале игры поле перемешено в случайном порядке
5. Пользователь не должен совершть непозволительные шаги.
Например, из-за ограничений рамки поля. Ему должно показываться
сообщение о том, что он пытается совершить непозволительный ход
6. Пользователю дожно быть видно поле. Оно представляет собой матрицу
4 на 4. Пустую клекту обозначаем как x. При каждом действии пользователя
поле рисуется еще раз - ниже в консоли
7. Игра заканчивается, когда все клетки стоят по-порядку, а пустая клетка
- последняя. В конце игры пользователю показывается, сколько ходов он совершил
8. Выход из игры происходит при помощи KeyboardInterrupt.
Исключение должно быть обработано. Пользователю должна быть
выведена фраза "shutting down"
"""

"""
**Дополнительно:
1. Обратите внимание, что не любое поле оставляет возможность 
закончить игру, необходимо придумать корректный алгоритм генерации 
взамен простого перемешивания
2. Тесты, которые приложены к работе должны проходить
3. Вам необходимо посмотреть, как работают самописные тесты, 
которые приложены к работе

**Прохождение тестов:
1. Создаем папку game_code
2. В ней создаем файл game.py
3. Рядом должен лежать мой файл tests.py
4. Вызываем python3 tests.py
"""

# -*- coding: utf-8 -*-
"""
https://gist.github.com/agavrish/edde1a0c4d219035b3a4f26d4e4c3583
"""
# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle

import random


# Empty tile, there's only one empty cell on a field:
# Пустая плитка, в поле только одна пустая ячейка:

EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
# Словарь возможных ходов, если форма:
# Клавиша -> дельта для перемещения пустой плитки по полю

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    Этот метод используется для создания поля в самом начале игры.
    : return: список из 16 случайно перемешанных плиток,
    один из которых - пустое место.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)

    # possible_moves = list(MOVES.keys())
    # applied_moves = 0
    # while applied_moves < 100:
    #     random_move = random.choice(possible_moves)

    #     try:
    #         field = perform_move(field, random_move)
    #         applied_moves += 1
    #     except IndexError:
    #         continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    Этот метод выводит поле пользователю.
    : param field: текущее состояние поля для печати.
    : return: Нет
    """
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    Этот метод проверяет, завершена ли игра.
    : param field: текущее состояние поля.
    : return: True, если игра завершена, иначе False.
    """
    ideal = list(range(1, 16))
    ideal.append(EMPTY_MARK)

    return ideal == field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    Перемещает пустую плитку внутри поля.
    : param field: текущее состояние поля.
    : param key: направление движения.
    : return: новое состояние поля (после перемещения).
    : raises: IndexError, если ход не может быть выполнен.
    """
    current_position = field.index(EMPTY_MARK)

    if key == 's' and current_position >= 12:
        raise IndexError('Cant move down')

    if key == 'd' and current_position % 4 == 3:
        raise IndexError('Cant move right')

    if key == 'w' and current_position < 4:
        raise IndexError('Cant move up')

    if key == 'a' and current_position % 4 == 0:
        raise IndexError('Cant move left')

    delta = MOVES[key]
    field[current_position], field[current_position + delta] = field[current_position + delta], field[current_position]
    return field

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    Обрабатывает ввод пользователя. Список принятых ходов:
        'w' - вверх,
        's' - вниз,
        'а' - влево,
        'd' - направо
    : return: <str> текущий ход.
    """
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    Основной метод. Он запускается при вызове программы.
    Он также вызывает другие методы.
    : return: Нет
    """
    field = shuffle_field()
    # field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'x', 15]

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)

    print('Game is finished!')


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
