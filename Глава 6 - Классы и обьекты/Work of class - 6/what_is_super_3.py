# -*- coding: utf-8 -*-


class Calc(object):
    def __init__(self, value):
        print('Calc constructor is called')
        self.value = value

    def count(self):
        return self.value * 8 + 9


class DoubleCalc(Calc):
    def count(self):
        return 2 * super().count()


class ExtendedCalc(DoubleCalc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print('Extender', self.value)

        self.k = k

    def count(self):
        a = self.k + 1
        previous = super().count()
        #  previous = self.value * 8 + 9
        return -1 * self.k * previous



"""
Замечательная функция __mro__, которая показывает 
в какой последовательности вызываются функции
"""
print(Calc.__mro__)  # (<class '__main__.Calc'>, <class 'object'>)
b = Calc(4)
print(b.count())  # 41

print()  # ==================================================
print(ExtendedCalc.__mro__)  # (<class '__main__.ExtendedCalc'>,
                                # <class '__main__.DoubleCalc'>,
                                # <class '__main__.Calc'>,
                                # <class 'object'>)
e = ExtendedCalc(8, k=1.2)
print(e.count())  # -175,2

print()  # ==================================================
print(DoubleCalc.__mro__)  # (<class '__main__.DoubleCalc'>,
                            # <class '__main__.Calc'>,
                            # <class 'object'>)
a = DoubleCalc(9)
print(a.count())  # 162
