"""
2.Написать функцию, которая принимает 3 аргумента - числа,
найти среди них два максимальных, вывести в консоль

"""


def result(s):
    res = s
    min_res = min(res)
    res.remove(min_res)
    print(*res)


s = list(map(int, input().split()))
result(s)
