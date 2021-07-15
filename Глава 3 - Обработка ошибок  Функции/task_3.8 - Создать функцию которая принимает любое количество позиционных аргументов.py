"""
Написать функцию, которая принимает любое количество
 позиционных аргументов - строк и один парматер
 по-умолчанию glue, который равен ':'.
 Соединить все строки таким образом, чтобы в результат
 попали все строки, длинее 3 символов.
 Для соединения между любых двух строк вставлять glue

 abc cde fekl mnjp ldfg abwec cde feeekl mnjp ldoppfg
"""


def stroka(s, glue=':'):
    n_s = (list(s))
    new_s = ''
    for s in n_s:
        if len(s) > 3:
            new_s += s + ' '
    return glue.join(new_s.split())


origin = list(map(str, input().split()))
glue = ':'
print(stroka(origin, glue))

"""
Как вариант
"""


def fun(*strings, glue=':'):
    list = []
    for string in strings:
        if len(string) > 3:
            list.append(string)
    return glue.join(list)


print(fun('hello', 'www', 're', 'good', 'heljlo', 'wkww', 'rek'))
