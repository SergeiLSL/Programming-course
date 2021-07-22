# -*- coding: utf-8 -*-
"""
Полиморфизм
Позволяет использовать функции по разному, вне
зависимости от типа их параметров
"""


def sum_two_objects(one, two):
    return one + two


print(sum_two_objects(1, 2))  # 3 - если числа, то складываем
print(sum_two_objects('ab', 'cd'))  # abcd - если строки, то контагенацию
print(sum_two_objects(['a', 'b'], ['c', 'd']))  # ['a', 'b', 'c', 'd'] - объединение множеств
print(sum_two_objects(('a', 'b'), ('c', 'd')))  # ('a', 'b', 'c', 'd') - объединение множеств

# ========================================================


class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


class Example(object):
    def call(self):
        print('Ex')


def call_obj(obj):
    obj.call()


call_obj(Child())  # Child
call_obj(Parent())  # Parent
call_obj(Example())  # Ex








