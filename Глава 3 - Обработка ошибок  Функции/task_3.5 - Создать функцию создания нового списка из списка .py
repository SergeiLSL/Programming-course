"""
Написать функцию, которая принимает два аргумента.
Первый - список чисел, второй - булевый флаг.
Если флаг действителен - возвращаем новый список
с нечетными числами из входного списка, если флаг
отрицателен - возвращаем новый список с четными
числами из входного списка

"""


def result(s, f = True):
    if f == False:
        print(1)
    else:
        print(s)


s = list(map(int, input().split()))
f = False
print(result(s, f))
