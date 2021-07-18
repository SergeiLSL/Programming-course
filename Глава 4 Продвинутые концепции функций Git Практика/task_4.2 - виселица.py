"""
Виселица.
 Програма выбирает слово из списка. Дается количество жизней по длине слова.
 Игрок должен называть букву. Если буква в списке есть,
 программа должна поставить ее на место и вывести в консоль.
 если нет -1 жизнь
 И так пока игрок не угадает слово или его не повесят.
"""
import random

print("Игра - 'Виселица'")
name = input('Пожалуйста введите ваше имя: ')

words = ['Мама', 'окно', 'Магазин', 'стол', 'машина', 'шкаф', 'ручка', 'Молоко']

word = random.choice(words).lower()
print(word)

task_word = []
for b in word:
    task_word += ['_']

print(*task_word)

my_life = len(word)
print(f'У вас {name} есть {my_life} попытки')

while my_life != 0:
    user_letter = input(f'{name} введите букву: ')
    my_life -= 1
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
                elif i != a:
                    continue
                s -= 1

    print(', '.join(task_word))

