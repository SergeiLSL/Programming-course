"""
Виселица.
 Програма выбирает слово из списка. Дается количество жизней по длине слова.
 Игрок должен называть букву. Если буква в списке есть,
 программа должна поставить ее на место и вывести в консоль.
 если нет -1 жизнь
 И так пока игрок не угадает слово или его не повесят.
"""
import random


def attempt(x):
    if (10 < n < 20) or (n % 10 in [0, 5, 6, 7, 8, 9]):
        return f'У вас есть {n} попыток.'
    elif n % 10 == 1:
        return f'У вас есть {n} попытка.'
    else:
        return f'У вас есть {n} попытки.'


def is_alpha(letter):
    if letter.isalpha():
        return str(letter)
    else:
        print('Введите букву: ')
        return is_alpha(input())


print("*" * 3, " Игра 'Виселица' ", "*" * 3)
name = input('Пожалуйста введите ваше имя: ')

words = ['Животное', 'крокодил', 'птица', 'Пирамида', 'треугольник', 'мячик',
         'Обруч', 'Скакалка', 'Мама', 'окно', 'Магазин', 'стол', 'машина',
         'шкаф', 'ручка', 'Молоко', 'телевизор', 'телефон', 'Париж']

word = random.choice(words).lower()
print(word)

task_word = []
for b in word:
    task_word += ['_']

print(*task_word)

n = len(word) + len(word) // 2
print(attempt(n))

print('Введите букву: ')
count = 0

while True:
    if count == len(word):
        print('Вы спасли себе жизнь!')
        break
    elif n == 0:
        print('Увы, Вас повесят!')
        break
    elif ''.join(task_word).isalpha():
        print('Вы спасли себе жизнь!')
        break
    user_letter = is_alpha(input())
    n -= 1
    if user_letter in word:
        print(user_letter)
        for i in range(len(task_word)):
            s = len(task_word)
            a = -1
            while s != 0:
                a = word.find(user_letter, a+1)
                if a == -1:
                    break
                elif i == a:
                    task_word[i] = user_letter
                    count += 1
                elif i != a:
                    continue
                s -= 1

    print(''.join(task_word))
    print(f'У вас осталось {attempt(n)}')


