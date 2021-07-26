# -*- coding: utf-8 -*-
"""
Функциональность словаря
"""


class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:  # is обозначет ==
            self.values = {}
        elif isinstance(values, dict):
            self.values = values
        else:
            raise ValueError()

    # Converting to string:
    def __str__(self):
        if self.values:
            return str(self.values)
        else:
            return ''
        # return str(self.values) if self.values else ''  # тоже самое

    # Items management: (методы словаря)
    def __getitem__(self, key):  # возвращают значение словаря
        return self.values[key]

    def __setitem__(self, key, value):  # назначают значение словаря
        self.values[key] = value

    def __delitem__(self, key):  # удаляют значение словаря
        del self.values[key]

    # Iteration:  #
    def __iter__(self):
        return iter(self.values)

    # `in` operation:  # поиск элемента словаря
    def __contains__(self, item):
        return item in self.values

    def __len__(self):  # получени длины словаря
        return len(self.values)  # self.values.__len__()


if __name__ == '__main__':
    l = DictFunctionality({'1key': 'some_value'})  # сработал метод __init__
    l[1] = 'item1'  # сработал метод __setitem__
    print(str(l), l[1])  # сработал метод __str__, __delitem__

    for item in l:
        print(item, l[item])  # сработал метод __iter__

    print('s' in l, 1 in l)  # сработал метод __contains__
    print(len(l))  # сработал метод __len__

"""
Полезное свойство
"""


class MathObject:
    def __init__(self):
        self.value = 2
        self.other = 3

    def j(self):
        pass


t = MathObject()

print(t.__dict__)  # {'value': 2, 'other': 3}

print(dir(t))

