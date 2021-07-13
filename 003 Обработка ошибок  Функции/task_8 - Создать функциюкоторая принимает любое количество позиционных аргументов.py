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
    for i in range(len(n_s)):
        if len(n_s[i]) > 3:
            new_s += n_s[i] + ' '
    return glue.join(new_s.split())


origin = list(map(str, input().split()))
glue = ':'
print(stroka(origin, glue))


