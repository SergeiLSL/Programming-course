"""
4.8 Slots: свойства(property) и наследования

https://stepik.org/lesson/427818/step/1?auth=registration&unit=417703
"""
"""
Теперь поговорим о наследовании
"""


class Rectangle:  # прямоугольник
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.__width = a  # ширина
        self.height = b  # высота

    @property  # переименуем наше свойство по названию атрибута
    def width(self):  # и это гетер
        return self.__width

    @width.setter  # становится свойством
    def width(self, value):  # определяем как класс, но нанего вешаем декоратор @property
        print('setter called')
        self.__width = value


class Square(Rectangle):  # создадим класс квадрат
    pass


s = Square(5, 5)  # создадим экземпляр и посмотрим, есть ли у него переменная __dict__
print(s.__dict__)  # {} - она есть, хотя у родителя есть __slots__
"""
Но раз она есть, то мы можем присваивать любые атрибуты и затем работать с ними, 
то есть это обычное динамическое расширение класса и мы можем присваивать 
любые свойства им или другими словами атрибуты нашим объектам.
"""
s.zz = 100
print(s.zz)  # 100
print(s.__dict__)  # {'zz': 100}

print('*' * 25)
"""
Чтобы задать дочерним классам __slots__ иы должны прописать им 
эти же значения __slots__ , но мы можем расширять свое поведение.
Допусти сроздадим еще одно значение - color, а затем проиницилизируем 
наш класс новыми значениями
"""


class Rectangle:  # прямоугольник
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.__width = a  # ширина
        self.height = b  # высота

    @property  # переименуем наше свойство по названию атрибута
    def width(self):  # и это гетер
        return self.__width

    @width.setter  # становится свойством
    def width(self, value):  # определяем как класс, но нанего вешаем декоратор @property
        print('setter called')
        self.__width = value


class Square(Rectangle):
    __slots__ = 'color'

    def __init__(self, a, b, color):  # принимать уже будем три значения
        super().__init__(a, b)
        self.color = color


d = Square(6, 6, 'red')
print(d.width, d.height, d.color)  # 6 6 red
"""
Но теперь у нас потеряна переменная __dict__ и теперь мы не 
сможем присваивать в нашу переменную d новые атрибуты, потому что
у нас теперь появился __slots__
"""
"""
Еще раз __slots__ дочернего класса расширяет __slots__ родительского класса, 
то есть нет необходимости дублировать эти имена в дочернем классе.
"""

print('+=' * 25)
"""
Но если вы не хотите раширять __slots__ родительского класса, 
то есть добавлять новые атрибуты в дочерние классы, 
то можно в  __slots__ дочернего класса задать какую то пустую коллекцию,
ну например сделать пустой кортеж
"""


class Rectangle:  # прямоугольник
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.__width = a  # ширина
        self.height = b  # высота

    @property  # переименуем наше свойство по названию атрибута
    def width(self):  # и это гетер
        return self.__width

    @width.setter  # становится свойством
    def width(self, value):  # определяем как класс, но нанего вешаем декоратор @property
        print('setter called')
        self.__width = value


class Square(Rectangle):
    __slots__ = tuple()

    def __init__(self, a, b):  # принимать уже будем три значения
        super().__init__(a, b)


m = Square(9, 12)
print(d.width, d.height)  # 6 6 -
"""есть ширина, высота но переменной __dict__ неё нет"""
