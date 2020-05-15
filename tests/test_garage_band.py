import pytest

from pythonic_garage_band.pythonic_garage_band import Band, Guitarist, Bassist, Drummer

# check Band name
def test_band_name():
    actual = Band("Beatles").name
    expected = "Beatles"
    assert expected == actual

# check default Band members
def test_band_default_members():
    actual = Band("Beatles").members
    expected = "none presently"
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
    expected = "Hermione"
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
    expected = "this is the rpr string inside Musician class and instance Gildroy"
    assert expected == actual

#----------------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def prep():
    """Reset the Band names list so it's fresh each test run"""
    Band.names = []
