"""
2.8 Property Вычисляемые свойства
"""
# Проведем вычисления с квадратом


class Square:
    def __init__(self, s):
        self.side = s  # сторона квадрата

    def area(self):  # найдем площадь квадрата
        return self.side ** 2


a = Square(5)
print(a.area())  # 25
# ==============================================
# Превратим в свойство


class Square:
    def __init__(self, s):
        self.side = s  # сторона квадрата

    @property
    def area(self):  # найдем площадь квадрата
        return self.side ** 2


a = Square(5)
print(a.area)  # 25 - обращаемся не как к методу, а как к свойству
a = Square(10)
print(a.area)  # 100

# ==============================================
# Чтобы не повторять вычисления (в случае больших объемов)


class Square:
    def __init__(self, s):
        self.__side = s  # сторона квадрата
        self.__area = None  # еще приватная переменная, изначально значение None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):  # найдем площадь квадрата
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.__area


d = Square(7)
print(d.area)  # 49 - обращаемся не как к методу, а как к свойству
d = Square(10)
print(d.area)  # 100
d = Square(11)
print(d.area)  # 121
d.side = 4
print(d.area)  # 16

"""
Домашнее заданание - создать вычисляемое свойство - ПЕРИМЕТР
"""