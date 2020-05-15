from abc import ABC, abstractmethod

class Band:
    names = list() # this is class attribute

    def __init__(self, name, members = "none presently"):
        self.name = str(name)
        self.members = Musician.to_all()
        Band.names.append(self) #creates a list of instances of class

    def play_solos(self):  #get each member to play solo
        band_members = Musician.to_all()
        for person in band_members:
            print(f"I am playing solo in the Band, my name is {person}")

    def __str__(self):
        return f"this is the string inside Band class with instance {self.name}"

    def __repr__(self):
        return f"{self.name} instance in Band class using repr"

    @classmethod
    def to_list(cls):
        return cls.names


class Musician(ABC):
    members = []

    def __init__(self, name):
        self.name=name
        Musician.members.append(self)

    @abstractmethod
    def get_instrument(self):
        return "This is inside Musician Class and I play nothing"

    @abstractmethod
    def play_solo(self):
        return "I am playing nothing"

    @classmethod
    def to_all(cls):
        return cls.members

    def __str__(self):
        return f"this is the string inside Musician superclass with instance {self.name}"

    def __repr__(self):
        return self.name

class Guitarist(Musician):
    def __init__(self, name = "unknown"):
        super().__init__(name)

    def get_instrument(self):
        return "I love to play my Guitar"

    def play_solo(self):
        return "I am playing my Guitar"

class Bassist(Musician):
    def __init__(self, name = "unknown"):
        super().__init__(name)

    def get_instrument(self):
        return "I love to play my Bass"

    def play_solo(self):
        return "I am playing my Bass"

class Drummer(Musician):
    def __init__(self, name = "unknown"):
        super().__init__(name)

    def get_instrument(self):
        return "I love to play my Drums"

    def play_solo(self):
        return "I am playing my Drums"


if __name__ == "__main__":
    # shredder = Band("shredder","401_students")
    # one = Band("One")
    # print(Band.to_list())
    # print(beatles)
    # print(repr(beatles))
    leah = Guitarist("Leah")
    ron = Drummer("Ron")
    hermy = Guitarist("Hermy")
    harry = Bassist("Harry")
    print(Musician.to_all())
    beatles = Band("Beatles")
    print(beatles.play_solos())

