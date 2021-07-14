"""
task_2.4 - соеденить все слова

Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'],
соеденить все слова в единую строку,
чтобы получилось: 'Earth -> Russia -> Moscow'
"""

s = ['Earth', 'Russia', 'Moscow']

print(' -> '.join(s))
print()
print(f'{s[0]} -> {s[1]} -> {s[2]}')
