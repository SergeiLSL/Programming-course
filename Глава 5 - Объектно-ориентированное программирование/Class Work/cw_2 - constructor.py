# -*- coding: utf-8 -*-

# Constructor is called when new instance is created
class TestClass():

    def __init__(self):
        print('Constructor is called!')
        print('Self is the object itself!', self)


t = TestClass()  # Constructor is called!
t1 = TestClass()  # Self is the object itself! <__main__.TestClass object at 0x000001865B835FD0>


class Car:

    def __init__(self):
        self.color = 'red'


m = Car()
m1 = Car()


class Car:
    engine = 'V8 Turbo'

    def __init__(self, color='red'):
        self.color = color


m_1 = Car()
m_2 = Car('white')


# class TestClass():
#
#     def __init__(self, color, transmission='Auto'):
#         print('Constructor is called!')
#         print('Self is the object itself!', self)
#         self.color = color
#         self.transmission = transmission
#
#         # HERE ENGINE AND TRANSMISSION COMPAT CHECK
#
#
# t = TestClass()
#
# t1 = TestClass()


# Constructor can have parameters



class Table:
    # В этом случае обект сохраняется, а переменная (ch1) нет
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(
            number_of_legs))


ch1 = Table(4)  # New table has 4 legs
ch2 = Table(3)  # New table has 3 legs


# But we need to save them into the fields!

class Chair:
    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color)  # <__main__.Chair object at 0x0000025C84EB54C0> green

c1 = Chair('Red')
print(c1.color)  # Red
print('variable c did not change!', c.color)  # variable c did not change! green
