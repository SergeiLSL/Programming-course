
import random, time
from tkinter import *
score = 100


def guess_the_number():
    global score
    print('Вы начали игру "Угадай число". Ваш общий счет: %s очков' % score)
    x = random.randint(1, 100)
    time.sleep(1)
    while True:
        print('')
        time.sleep(0.5)
        n = int(input('Как думаете, какое число было загадано? '))
        if x > n:
            score -= 1
            print('Ваша честь, вы не правы! Число больше! Ваш счет снизился на одно очко. Ваш общий счет: %s очков' % score)
        elif x < n:
            score -= 1
            print('Ваша честь, вы не правы! Число меньше! Ваш счет снизился на одно очко. Ваш общий счет: %s очков' % score)
        else:
            score += 10
            print('Ваша честь, вы угадали! Ваш счет увеличился на десять очков. Ваш общий счет: %s очков' % score)
            answer = input('Хотите сыграть еще раз? (yes or no) ')
            if answer.lower() == 'no':
                break
            x = random.randint(1, 100)


print('Добро пожаловать в Игральный модуль')
time.sleep(1)
print('Выберите игру из списка:')
tk = Tk()
btn = Button(tk, text='Угадай число', command=guess_the_number())
btn.pack()