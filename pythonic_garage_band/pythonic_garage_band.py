from abc import ABC, abstractmethod

class Band:
    names = list() # this is class attribute

    def __init__(self, name, members = "none presently"):
        self.name = str(name)
        self.members = members
        Band.names.append(self) #creates a list of instances of class

    def play_solos(self):  #get each member to play solo
        pass

    def __str__(self):
        return f"this is the string inside Band class with instance {self.name}"

    def __repr__(self):
        return f"{self.name} instance in Band class using repr"

    @classmethod
    def to_list(cls):
        return cls.names


class Musician(ABC):
    def __init__(self, name):
        self.name=name

    @abstractmethod
    def get_instrument(self):
        return "This is inside Musician Class and I play nothing"

    @abstractmethod
    def play_solo(self):
        return "I am playing nothing"

    def __str__(self):
        return f"this is the string inside Musician superclass with instance {self.name}"

    def __repr__(self):
        return f"this is the rpr string inside Musician class and instance {self.name}"

class Guitarist(Musician):
    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "I love to play my Guitar"

    def play_solo(self):
        return "I am playing my Guitar"

class Bassist(Musician):
    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "I love to play my Bass"

    def play_solo(self):
        return "I am playing my Bass"

class Drummer(Musician):
    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "I love to play my Drums"

    def play_solo(self):
        return "I am playing my Drums"


if __name__ == "__main__":
    # shredder = Band("shredder","401_students")
    # beatles = Band("Beatles")
    # one = Band("One")
    # print(Band.to_list())
    # print(beatles)
    # print(repr(beatles))
    leah = Guitarist("Leah")
    print(leah)
    print(leah.get_instrument())

