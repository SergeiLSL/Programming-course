""" inheritance - наследование """


# class Parent(object): запись ниже идеинтична
class Calc:

    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('-----')
        print('Number is', value_to_print)
        print('-----')


c = Calc(5)
c.calc_and_print()  # Number is 52
"""
Чуть чуть модернизируем, добавим дочерний класс
"""


class Calc:

    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('-----')
        print('Number is', value_to_print)
        print('-----')


class CalcExtraValue(Calc):

    def calc_value(self):
        return self.number - 100


c = Calc(5)
c.calc_and_print()  # Number is 52
# создадим экземпляр класса CalcExtraValue
c = CalcExtraValue(5)
c.calc_and_print()  # Number is -95

