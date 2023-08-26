import pytest
from hashmap_left_join import HashTable  


def test_1():
    synonyms = {}
    antonyms = {}
    result = HashTable.left_join(synonyms, antonyms)
    assert result == []




def test_2():
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy"
    }
    antonyms = {}
    result = HashTable.left_join(synonyms, antonyms)
    assert result == [
        ["happy", "joyful", None],
        ["sad", "unhappy", None]
    ]




def test_3():
    synonyms = {}
    antonyms = {
        "happy": "unhappy",
        "sad": "joyful"
    }
    result = HashTable.left_join(synonyms, antonyms)
    assert result == []




def test_4():
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy"
    }
    antonyms = {
        "happy": "",
        "sad": ""
    }
    result = HashTable.left_join(synonyms, antonyms)
    assert result == [
        ["happy", "joyful", ""],
        ["sad", "unhappy", ""]
    ]




def test_5():
    synonyms = {
        "cat": "feline",
        "dog": "canine"
    }
    antonyms = {
        "bird": "avian",
        "fish": "aquatic"
    }
    result = HashTable.left_join(synonyms, antonyms)
    assert result == [
        ["cat", "feline", None],
        ["dog", "canine", None]
    ]


def test_6():
    synonyms = {}
    antonyms = {
        "happy": "unhappy",
        "sad": "joyful"
    }
    result = HashTable.left_join(synonyms, antonyms)
    assert result == []
