class Perimeter:
    def __init__(self, a, b):
        self.__side_a = a  # сторона
        self.__side_b = b  # сторона
        self.__perimeter = None  # еще приватная переменная, изначально значение None

    @property
    def side_a(self):
        return self.__side_a

    @property
    def side_b(self):
        return self.__side_b

    @side_a.setter
    def side_a(self, value1):
        self.__side_a = value1
        self.__perimeter = None

    @side_b.setter
    def side_b(self, value2):
        self.__side_b = value2
        self.__perimeter = None

    @property
    def perimeter(self):  # найдем периметр квадрата
        if self.__perimeter is None:
            print('calculate perimeter')
            self.__perimeter = self.side_a * 2 + self.side_b * 2
        return self.__perimeter


d = Perimeter(7, 8)
print(d.perimeter)  # 28 - обращаемся не как к методу, а как к свойству
d = Perimeter(5, 8)
print(d.perimeter)
d.side_a = 12
print(d.perimeter)
