"""
Classes as types
    You can also declare a class as the type of a variable
    Lets say you have a class Person, with a name

"""

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


p = Person("Tom")
print(get_person_name(p))
