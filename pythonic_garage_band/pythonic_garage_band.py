from abc import ABC, abstractmethod

class Band:
    names = list() # this is class attribute

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.names.append(self)

    def play_solos(self):
        pass

    def __str__(self):
        print(f"this is the string inside class {self.name}")

    def __repr__(self):
        # return self.name
        pass

    @classmethod
    def to_list(cls):
        return cls.names


class Musician(ABC):
    def __init__(self, name):
        self.name=name

    def __str__(self):
        print(f"this is the string inside class {self.name}")

    # def __repr__(self):
    #     print(f"this is the rpr string inside class {self.name}")

class Guitarist(Musician):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

shredder = Band("shredder","401_students")
print(shredder.name)
print(shredder.members)
print(shredder)
print(rpr(shredder))
