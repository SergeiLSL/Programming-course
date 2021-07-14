"""
task_2.11 - Сортировка словаря по условию

Произвести сортировку списка водителей по дате рождения.
"""


def myFunc(e):
    return e['year']


personnel = [
    {'driver': 'Иванов', 'year': 1995},
    {'driver': 'Самойленко', 'year': 1986},
    {'driver': 'Цой', 'year': 2001},
    {'driver': 'Дубинин', 'year': 1978}
]

personnel.sort(key=myFunc)

print(personnel)  # вывод в строку
print()
for person in personnel:  # вывод в столбец
    print(person)
