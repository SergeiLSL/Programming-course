"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""
# herbivore - травоядное животное
# predator - хищник
# poisonous - ядовитый


class Animal:

    def __init__(self, name, view, animal_type):
        self.name = name
        self.view = view
        self.animal_type = animal_type


class Human():

    def __init__(self, name):
        self.name = name

    # def dangerous_animals(self, animal):
    #     return animal.view, animal.animal_type.lower()


tiger = Animal('tiger', 'хищник', 'опасный')
cobra = Animal('cobra', 'змея', 'ядовитая')
giraffe = Animal('giraffe', 'травоядное животное', 'неопасное')
#
human = Human('Human')
#
print(f'{tiger.name} - {tiger.view}, {tiger.animal_type} для человека')
print(f'{cobra.name} - {cobra.view}, {cobra.animal_type} для человека')
print(f'{giraffe.name} - {giraffe.view}, {giraffe.animal_type} для человека')