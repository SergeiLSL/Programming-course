"""
ЗАДАЧА 1:
Реализовать класс Person, у которого должно быть
два публичных поля: age и name.
Также у него должен быть следующий набор методов:
know(person), который позволяет
добавить другого человека в список знакомых.
И метод is_known(person), который возвращает знакомы ли два человека
"""


class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.known_persons = []  # Список знакомых

    def know(self, person):
        if person not in self.known_persons:
            self.known_persons.append(person)  # Если такого человека в списке нет, добавляем
        else:
            print(f'{self.name} уже знает человека по имени {person.name}')

    def is_known(self, person):
        text_action = {True: 'знает человека по имени', False: 'не знает человека по имени'}
        is_known_person = person in self.known_persons
        print(f'{self.name} {text_action[is_known_person]} {person.name}')

    def __str__(self):
        return f'Список знакомых {self.name} {self.known_persons}'


if __name__ == '__main__':
    ivan = Person('Ivan', 30)
    misha = Person('Misha', 28)
    anna = Person('Anna', 25)
    anna.know(ivan)
    anna.know(misha)
    anna.know(ivan)  # Anna уже знает человека по имени Ivan
    ivan.know(anna)
    ivan.know(misha)
    ivan.know(anna)  # Ivan уже знает человека по имени Anna
    misha.is_known(anna)  # Misha не знает человека по имени Anna
    misha.is_known(ivan)  # Misha не знает человека по имени Ivan
    print(ivan)
    print(anna)


    # print(misha)
