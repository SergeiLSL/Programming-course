"""
*ЗАДАЧА 1:
1. Создать класс корзина, у которого можно выставить разную
вместительность для разных объектов.
В объекты класса корзина можно помещать разные объекты;
2. Вам нужно создать класс пакет, в который тоже можно
помещать предметы. У него тоже есть вместимость;
3. Создать любой класс, объекты которого можно было бы мощешать
в корзину и пакет;
4. Если вместимости недостаточно, сказать, что объект поместить нельзя.
"""


class HandBox(object):   # класс корзина

    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('Этот HandBox имеет размер = {}'.format(self.size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} этот предмет поместится в HandBox'.format(smth))
        else:
            print('{} этот предмет больше, чем размер HandBox = {}'.format(smth, self.size))


class Bag(HandBox):  # класс пакет
    def get_size(self):
        print('Этот Bag имеет размер = {}'.format(self.size))

    def put_smth(self, smth):
        if smth.size <= self.size:
            print('{} этот предмет поместится в Bag'.format(smth))
        else:
            print('{} этот предмет больше, чем размер = {}'.format(smth, self.size))


class Thing(object):
    def __init__(self, size):
        self.size = size


box1 = HandBox(20)
box1.get_size()

bag1 = Bag(123)
bag1.get_size()

smth1 = Thing(10)
smth2 = Thing(30)
smth3 = Thing(130)

box1.put_smth(smth1)
box1.put_smth(smth2)

bag1.put_smth(smth2)
bag1.put_smth(smth3)
