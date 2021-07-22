# -*- coding: utf-8 -*-

# Обратить внимание на подчеркивание!!!!


class Example(object):
    def __init__(self):
        self.a = 1  # полностью доступно, можно использовать в любой точке, где угодно
        self._b = 2  # доступно, но лучше не трогать (сигнал для разработчиков)
        self.__c = 3  # недоступно, доступ обеспечивается определённым образом
        print('{} {} {}'.format(self.a, self._b, self.__c))  # 1 2 3
        # внутри класса можно использовать все три поля
        # вне класса можем использовать а и _b

    def call(self):
        print('Called!')

    def _protected_method(self):
        pass

    def __private_method(self):
        pass


class Inh(Example):
    def nnn(self):
        self._b = 5
        self.__c = 6


example = Example()
print(example.a)  # 1
print(example._b)  # 2

# При обращении к с выдает ошибку и пишет, что это не атрибут 'Example'
try:
    print(example.__c)  # 'Example' object has no attribute '__c'
except AttributeError as ex:
    print(ex)  # 'Example' object has no attribute '__c'

"""
Три типа имен
1. a - полностью доступно, можно использовать в любой точке, где угодно
2. _b - доступно, но лучше не трогать (сигнал для разработчиков)
3. __c - недоступно, доступ обеспечивается определённым образом
"""