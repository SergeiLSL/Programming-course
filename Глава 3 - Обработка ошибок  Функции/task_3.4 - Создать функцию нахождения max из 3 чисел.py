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


"""
Как вариант
"""


def function(x, y, z):
    lst = [x, y, z]
    lst.sort()
    print(lst[1], lst[2])


a = int(input())
b = int(input())
c = int(input())

function(a, b, c)
