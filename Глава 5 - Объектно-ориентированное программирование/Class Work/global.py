# -*- coding: utf-8 -*-
"""
нерациональное использование функций !!!
GLOBAL_VALUE = 2


def do_work(value):
    return GLOBAL_VALUE * value + 2


def change_var(x):
    global GLOBAL_VALUE
    GLOBAL_VALUE = x

Правильно объявить класс и менять сколько
угодно глобальную переменную!!!
"""


class Calc:

    def __init__(self, param):
        self.param = param

    def do_work(self, value):
        return self.param * value + 2

    def change_var(self, x):
        self.param = x


c = Calc(5)
print(c.do_work(3))  # 17
c.change_var(8)
print(c.do_work(3))  # 26
