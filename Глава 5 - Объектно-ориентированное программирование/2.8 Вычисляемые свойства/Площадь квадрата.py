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
