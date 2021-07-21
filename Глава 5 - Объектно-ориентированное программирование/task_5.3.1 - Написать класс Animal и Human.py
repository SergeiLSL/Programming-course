"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)

"""
# herbivore - травоядное животное
# predator - хищник
# poisonous - ядовитый


class Animal:

    def __init__(self, name, view, animal_type='опасное'):
        self.name = name
        self.view = view
        self.animal_type = animal_type


class Human():
    animals_dangerous = ['опасное', 'ядовитое']

    def dangerous_animals(self, animal):
        if animal.animal_type.lower() in self.animals_dangerous:
            return f'{animal.name} - {animal.view}, {animal.animal_type.lower()}'
        else:
            return f'{animal.name} - {animal.view}, неопасное'


tiger = Animal('тигр', 'хищник')
cobra = Animal('кобра', 'змея', 'ядовитое')
giraffe = Animal('жираф', 'травоядное животное', 'неопасное')
scorpio = Animal('скорпион', 'паук', 'ядовитое')
hippopotamus = Animal('бегемот', 'травоядное животное')
#
human = Human()
#
print(human.dangerous_animals(tiger))
print(human.dangerous_animals(cobra))
print(human.dangerous_animals(giraffe))
print(human.dangerous_animals(scorpio))
print(human.dangerous_animals(hippopotamus))
