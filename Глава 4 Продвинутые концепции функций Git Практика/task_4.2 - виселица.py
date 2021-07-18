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
my_life = len(word)
print(f'У вас {name} есть {my_life} попытки')

task_word = []
for b in word:
    task_word += ['_']

print(*task_word)

while True:
    user_letter = input(f'{name} введите букву: ')
    if user_letter in word:
        print(user_letter)
        a = int(word.find(user_letter))
        print(a, type(a))
        for i in range(len(task_word)):
            if i == a:
                task_word[i] = user_letter

        print(', '.join(task_word))

    # elif user_num < num:
    #     print('Слишком мало, попробуйте еще раз')
    # else:
    #     print('Вы угадали, поздравляем!')
    #     break