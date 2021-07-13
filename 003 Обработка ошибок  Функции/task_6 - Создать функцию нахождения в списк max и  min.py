"""
Написать функцию, которая принимает любое количество
аргументов чисел. Среди них она находит максимальное
и минимальное. И возвращает оба.
10 15 24 3 56 18 8 6 4
"""


def result(s):
    res = s
    max_res = max(res)
    min_res = min(res)
    return max_res, min_res


s = list(map(int, input().split()))
print(result(s))


