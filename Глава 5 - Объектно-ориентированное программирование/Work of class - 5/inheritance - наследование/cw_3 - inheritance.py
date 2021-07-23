""" inheritance - наследование """


# class Parent(object): запись ниже идеинтична
class Parent:

    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.value))


class Child(Parent):

    def __init__(self):
        print('Child inited')
        self.value = 'Child'


parent = Parent()  # Parent inited
parent.do()  # Parent do(): Parent
child = Child()  # Child inited
child.do()  # Parent inited




