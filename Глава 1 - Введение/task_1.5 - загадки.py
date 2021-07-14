"""
Задача: реализовать игру в загадки

Требования:
Программа выводить в консоль текст загадки и ждать
ввода пользователя.
Программа после ввода пользователя ответа должна вывести
в консоль результат: правильный ли ответ дал пользователь
Загадок должно быть 10, тематика вопросов должна быть
по первому занятию.
Дополнительные требования (со звездочкой или сложные,
необязательно для выполнения):
Программа должна в конце игры сказать, сколько ответов
дал пользователь: сколько из них было верных
Программа должна не учитывать регистр ответа: "Python"
и "python" оба должны быть правильным ответом на вопрос
"Какой язык мы учим?"

"""

puzzles = [['Загадка 1', str.lower('Ответ1')],
           ['Загадка 2', str.lower('Ответ2')],
           ['Загадка 3', str.lower('Ответ3')],
           ['Загадка 4', str.lower('Ответ4')],
           ['Загадка 5', str.lower('Ответ5')]
           ]

yes = []
no = []


def new_puzzles():
    r = input('Введите Загадку: ')
    a = input('Введите Ответ: ')
    if [r, str.lower(a)] not in puzzles:
        puzzles.append([r, str.lower(a)])
    else:
        print('Такая загадка уже есть.')


def my_test():
    print('Выберите вопрос от 1 до {}: '.format(len(puzzles)))
    n = int(input()) - 1
    if 0 <= n < len(puzzles):
        print(puzzles[n][0])
        print('Ваш ответ: ')
        answer = input()
        if str.lower(answer) == puzzles[n][1]:
            yes.append(1)
            print('Правильно!')
        elif str.lower(answer) != puzzles[n][1]:
            no.append(1)
            print('Неправильно!')
    else:
        print(f'Введите число от 1 до {len(puzzles)}')


while True:
    flag = input('Следующий вопрос? [y/n]: ')
    if flag == 'y':
        my_test()
    elif flag == 'n':
        flag = input('Вы можете предложить свою задачу? [y/n]: ')
        if flag == 'y':
            new_puzzles()
        else:
            print(f'Всего ответов {len(yes) + len(no)}, правильных {len(yes)}')
            print('Good bay')
            break







