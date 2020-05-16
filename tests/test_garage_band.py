import pytest
from pythonic_garage_band.pythonic_garage_band import Band, Guitarist, Bassist, Drummer, Musician

# check Band name
def test_band_name():
    actual = Band("Beatles").name
    expected = "Beatles"
    assert expected == actual

# check if Band name is string
def test_band_name_string():
    actual = isinstance(Band(1).name,str)
    expected = True
    assert expected == actual

# check if there are instances of Band saved and returned
def test_band_names_instances():
    Band("Beatles")
    Band("One")
    Band("Five")
    actual = len(Band.to_list())
    expected = 3
    assert expected == actual

# check for __str__ in Band
def test_band_str():
    beatles = Band("Beatles")
    actual = beatles.__str__()
    expected = "this is the string inside Band class with instance Beatles"
    assert expected == actual

# check for __repr__ in Band
def test_band_repr():
    beatles = Band("Beatles")
    actual = beatles.__repr__()
    expected = "Beatles instance in Band class using repr"
    assert expected == actual

# check for Guitarist name
def test_guitarist_name():
    actual = Guitarist("Hermione").name
    expected = "      "
    assert expected == actual

# check for Guitarist name by default
def test_guitarist_name():
    actual = Guitarist().name
    expected = "unknown"
    assert expected == actual

# check for Bassist name
def test_bassist_name():
    actual = Bassist("Harry").name
    expected = "Harry"
    assert expected == actual

# check for Drummer name
def test_drummer_name():
    actual = Drummer("Ron").name
    expected = "Ron"
    assert expected == actual

# check for get instrument method in Guitarist
def test_guitarist_get_instrument():
    actual = Guitarist("Prongs").get_instrument()
    expected = "I love to play my Guitar"
    assert expected == actual

# check for play_solo method in Guitarist
def test_guitarist_play_solo():
    actual = Guitarist("Sirius").play_solo()
    expected = "I am playing my Guitar"
    assert expected == actual

# check for __str__ in Guitarist from Musician super class
def test_guitarist_str():
    moony = Guitarist("Moony")
    actual = moony.__str__()
    expected = "this is the string inside Musician superclass with instance Moony"
    assert expected == actual

# check for __repr__ in Guitarist from Musician super class
def test_guitarist_repr():
    gildroy = Guitarist("Gildroy")
    actual = gildroy.__repr__()
    expected = "Gildroy"
    assert expected == actual

# check for all the instances of musicians
def test_musician_to_all(create_band_members):
    actual = len(Musician.to_all())
    expected = 4
    assert expected == actual

# check Band members through Musician class attribute
def test_band_members(create_band_members):
    actual = len(Band("Beatles").members)
    expected = 4
    assert expected == actual
#----------------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def prep():
    """Reset the Band names list so it's fresh each test run"""
    Band.names = []
    Musician.members = []

@pytest.fixture
def create_band_members():
    Musician.members = []
    leah = Guitarist("Leah")
    ron = Drummer("Ron")
    hermy = Guitarist("Hermy")
    harry = Bassist("Harry")
