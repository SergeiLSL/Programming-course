"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""
# herbivore - травоядное животное
# predator - хищник
# poisonous - ядовитый

class Animal():
    animal_type = ''

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type


class Human():
    dangerous_animals = ['poisonous', 'predator']

    def is_dangerous(self, name, animal):
        if animal.animal_type.lower() in self.dangerous_animals:
            return self.name


tiger = Animal('tiger', 'predator')
cobra = Animal('cobra', 'poisonous')
giraffe = Animal('giraffe', 'herbivore')

MyHuman = Human()

# print('Is {} animal dangerous for human? : {}'.format(MyAnimal.animal_type, MyHuman.is_dangerous(MyAnimal)))
# print('Is {} animal dangerous for human? : {}'.format(MyAnimal1.animal_type, MyHuman.is_dangerous(MyAnimal1)))
# print('Is {} animal dangerous for human? : {}'.format(MyAnimal2.animal_type, MyHuman.is_dangerous(MyAnimal2)))

print(f'Is {tiger} {tiger.animal_type} animal dangerous for human? : ')
