from time import *
from random import randint

print("Игра - 'Угадайка число!'")
name = input('Привет, как тебя зовут? ')
num = randint(1, 100)
while True:
    user_num = int(input(f'{name}, введи число от 1 до 100: '))
    sleep(1)
    if user_num > num:
        print('Слишком много, давай еще разок')
    elif user_num < num:
        print('Слишком мало, давай еще разок')
    else:
        print('Опана, ничесе, ты угадал!')
        sleep(2.5)
        print(f'{name}, хочешь еще сыграть?')
        sleep(0.5)
        if input() == 'да':
            sleep(1)
            print('')
            continue
        else:
            sleep(1.0)
            print('')
            print('Ясненько')
            sleep(1.2)
            print('Понятненько')
            sleep(1.2)
            print('Ну что ж, 'f'{name}, тогда удачи тебе. Береги себя. Пока! До встречи!')
            break
