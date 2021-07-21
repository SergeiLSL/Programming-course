"""
4.8 Slots: свойства(property) и наследования

https://stepik.org/lesson/427818/step/1?auth=registration&unit=417703
"""


class Rectangle:  # прямоугольник
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a  # ширина
        self.height = b  # высота


p = Rectangle(3, 4)
print(p.width)  # 3
print(p.height)  # 4
# не можем создавать другие атрибуты типа p.zz = 25
"""
Попробуем в этот класс какие то определённые свойства
"""
print('*' * 25)


class Rectangle:  # прямоугольник
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a  # ширина
        self.height = b  # высота

    @property  # становится свойством
    def perimetr(self):  # определяем как класс, но нанего вешаем декоратор @property
        return (self.width + self.height) * 2

    @property  # становится свойством
    def area(self):  # определяем как класс, но нанего вешаем декоратор @property
        return self.width * self.height


p = Rectangle(3, 4)
print(p.width)  # 3
print(p.height)  # 4
p = Rectangle(5, 6)
print(p.area)  # 30
print(p.perimetr)  # 22
# не можем попрежнему создавать другие атрибуты и обращяться к переменной __dict__
"""
В этих примерах использовали два свойства, которые являются
вычисляемыми, то есть они не зменяют наши атрибуты.
Но можно создать свойства, которы будут являться geter и seter.
Для этого надо сделать один атрибут защищенным
"""