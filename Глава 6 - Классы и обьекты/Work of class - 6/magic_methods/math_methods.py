# -*- coding: utf-8 -*-


class MathObject(object):  # создает математический объект
    def __init__(self, value):
        self.value = value

    # Comparing:
    def __eq__(self, other):   # метод сравнения использует оператор сравнения
        return self.value == other

    def __ge__(self, other):   # использует оператор >=
        return self.value >= other

    def __gt__(self, other):   # использует оператор >
        return self.value > other

    def __lt__(self, other):   # использует оператор <
        return self.value < other

    # Operations:
    def __neg__(self):   # использует оператор -
        return -self.value

    def __add__(self, other):   # использует оператор +
        return self.value + other

    def __radd__(self, other):  # от перестановки мест слагаемых сумма меняется
        return self.__add__(other)

    def __iadd__(self, other):  # брибавляешь сам себе
        return self.__add__(other)

    def __mul__(self, other):  # использует оператор *
        return self.value * other


if __name__ == '__main__':
    m = MathObject(10.)
    print(m > 10)
    print(m >= 10)
    print(m == 10)

    print(-m)
    print(m + 2 == 2 + m)

    m += 3
    print(m)
    print(m * 2)
