import pytest
from repeated_word import HashTable

@pytest.fixture
def hashtable():
    ht = HashTable()
    return ht

def test_repeated_word(hashtable):
    input_string1 = "Once upon a time, there was a brave princess who..."
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    input_string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    assert hashtable.repeated_word(input_string1) == "a"
    assert hashtable.repeated_word(input_string2) == "it"
    assert hashtable.repeated_word(input_string3) == "summer"

def test_repeated_word_no_repeated_word(hashtable):
    input_string = "This is a test string without repeated words."
    assert hashtable.repeated_word(input_string) == None
