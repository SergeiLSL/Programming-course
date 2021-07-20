"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""


class Animal():
    animal_type = ''

    def __init__(self, animal_type):
        self.animal_type = animal_type


class Human():
    dangerous_animals = ['poisonous', 'predator']

    def is_dangerous(self, animal):
        return animal.animal_type.lower() in self.dangerous_animals


MyAnimal = Animal('herbivore')
MyAnimal1 = Animal('predator')
MyAnimal2 = Animal('poisonous')

MyHuman = Human()

print('Is {} animal dangerous for human? : {}'.format(MyAnimal.animal_type, MyHuman.is_dangerous(MyAnimal)))
print('Is {} animal dangerous for human? : {}'.format(MyAnimal1.animal_type, MyHuman.is_dangerous(MyAnimal1)))
print('Is {} animal dangerous for human? : {}'.format(MyAnimal2.animal_type, MyHuman.is_dangerous(MyAnimal2)))


