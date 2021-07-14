"""
Создать список с тремя значениями 'to-delete'
и нескольми любыми другими, удалить из него все значения 'to-delete'
"""
spisok = ['Москва', 'to-delete', 'Санкт-Петербург',
          'to-delete', 'Новосибирск', 'Екатринбург',
          'to-delete', 'Самара', 'Владивосток']

print('Развернутый вариант.')
n_spisok = []
for s in spisok:
    if s != 'to-delete':
        n_spisok.append(s)

print(*n_spisok)
print()

print('Вариант с генератором списков.')
s = [s for s in spisok if s != 'to-delete']
print(*s)

print()
print('Вариант с set и remove.')
n_s = list(set(spisok))
n_s.remove('to-delete')
print(*n_s)  # недотаток: Длинный код!!! и нарушен порядок

print()
print('Вариант с генератором списков и remove.')
unique = []
[unique.append(item) for item in spisok if item not in unique]
unique.remove('to-delete')
print(*unique)  # недотаток: Длинный код!!! Порядок сохранен.
