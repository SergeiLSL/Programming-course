"""
Создать словарь из 5 пар: int -> str, например {6: '6'},
вывести его в консоль попарно.
"""
# Задание некорректное.
# Поэтому:
# Вариант 1. Генерируем словарь и выводим в консоль.

n_d = {a: a ** 2 for a in range(1, 5)}

for item in n_d.items():
    print(*item)

print()

for k, v in n_d.items():
    print(k, v)

print()
# Вариант 2. Случайный словарь. Разные сортировки.

d = {5: 48, 8: 12, 9: 3, 7: 12, 6: 15}

print('просто вывод в консоль')
for item in d.items():
    print(*item)

print()
print('сортировка по ключам')
for i in sorted(d):
    if i in d:
        print(i, d[i])

print()
print('Отсортировано по значениям!\nНо не происходит сортировки по именам!')
for i, v in sorted(d.items(), key=lambda para: -para[1]):  # Отсортировано по значениям!
    print(i, v)   # Но не происходит сортировки по именам!

print()
print('Отсортировано по значениям!\nЗатем сортировка по именам!')
for i, v in sorted(d.items(), key=lambda para: (para[1], para[0])):  # Отсортировано по значениям!
    print(i, v)  # а затем сортировка по именам!

print()
print('Отсортировано по значениям!\nЗатем сортировка по именам!')
for i, v in sorted(d.items(), key=lambda para: (-para[1], para[0])):  # Отсортировано по значениям!
    print(i, v)  # а затем сортировка по именам!
