"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""
# herbivore - травоядное животное
# predator - хищник
# poisonous - ядовитый

class Animal(object):

    def __init__(self, name, aggressive):
        self.name = name
        self.aggressive = aggressive


    def attack_human(self, human):
        if self.aggressive and not human.aggressive:
            print('Атака {} на {} прошла успешно!'.format(self.name, human.name))
            human.dangerous_animals.append(self)
        else:
            print('Атака {} на {} не удалась!'.format(self.name, human.name))

class Human():

    def __init__(self, name, aggressive):
        self.name = name
        self.dangerous_animals = []
        self.aggressive = aggressive

    def is_dangerous(self, animal):
        answers = {True : 'ДА', False : 'НЕТ'}
        return answers[animal in self.dangerous_animals]


# tiger = Animal('tiger', 'хищник- опасный')
# cobra = Animal('cobra', 'ядовитая - опасная')
# giraffe = Animal('giraffe', 'травоядное животное - неопасное')
#
# human = Human('Human')
#
# print(f'Это {tiger.animal_type} для человека')
# print(f'Это {cobra.animal_type} для человека')
# print(f'Это {giraffe.animal_type} для человека')