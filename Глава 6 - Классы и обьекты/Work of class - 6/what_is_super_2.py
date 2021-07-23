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


class ExtendedCalc(Calc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print('Extender', self.value)

        self.k = k

    def count(self):
        a = self.k + 1
        previous = super().count()
        #  previous = self.value * 8 + 9
        return -1 * self.k * previous


b = Calc(4)
print(b.count())  # 41

e = ExtendedCalc(8, k=1.2)
print(e.count())  # -87.6

a = DoubleCalc(9)
print(a.count())  # 162
