class Perimeter:
    def __init__(self, s):
        self.__side = s  # сторона квадрата
        self.__perimeter = None  # еще приватная переменная, изначально значение None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__perimeter = None

    @property
    def perimeter(self):  # найдем периметр квадрата
        if self.__perimeter is None:
            print('calculate perimeter')
            self.__perimeter = self.side * 4
        return self.__perimeter


d = Perimeter(7)
print(d.perimeter)  # 28 - обращаемся не как к методу, а как к свойству
d = Perimeter(10)
print(d.perimeter)  # 40
d = Perimeter(11)
print(d.perimeter)  # 44
d.side = 4
print(d.perimeter)  # 16
