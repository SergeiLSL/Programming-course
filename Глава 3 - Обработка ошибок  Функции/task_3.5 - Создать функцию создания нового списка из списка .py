"""
Написать функцию, которая принимает два аргумента.
Первый - список чисел, второй - булевый флаг.
Если флаг действителен - возвращаем новый список
с нечетными числами из входного списка, если флаг
отрицателен - возвращаем новый список с четными
числами из входного списка
12 24 13 18 2 7 9 4
"""


def result(s, f=True):
    n_s = []
    for i in range(len(s)):
        if f:
            if s[i] % 2 != 0:
                n_s.append(s[i])
        else:
            if s[i] % 2 == 0:
                n_s.append(s[i])
    return n_s


s = list(map(int, input().split()))
f = False
print(*result(s))
