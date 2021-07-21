"""
4.8 Slots: свойства(property) и наследования

https://stepik.org/lesson/427818/step/1?auth=registration&unit=417703
"""
"""
В этих примерах использовали два свойства, которые являются
вычисляемыми, то есть они не зменяют наши атрибуты.
Но можно создать свойства, которы будут являться geter и seter.
Для этого надо сделать один атрибут защищенным
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


p = Rectangle(7, 8)
print(p.width)  # 7
print(p._Rectangle__width)  # 7


