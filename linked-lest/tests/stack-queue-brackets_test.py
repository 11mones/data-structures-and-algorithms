import pytest
from linked_list.implementation import linked_list , Stack , Queue,validate_brackets
def test_1_brackets():
    brackets_str = "()"
    result = validate_brackets(brackets_str)
    actual = result
    expected = True

    assert actual == expected



def test_2_brackets():
    brackets_str = "{}(){}"
    result = validate_brackets(brackets_str)
    actual = result
    expected = True

    assert actual == expected

def test_3_brackets():
    brackets_str = "()[[Extra Characters]]"
    result = validate_brackets(brackets_str)
    actual = result
    expected = True

    assert actual == expected



def test_4_brackets():
    brackets_str = "(){}[[]]"
    result = validate_brackets(brackets_str)
    actual = result
    expected = True

    assert actual == expected



def test_5_brackets():
    brackets_str = "{}{Code}[Fellows](())"
    result = validate_brackets(brackets_str)
    actual = result
    expected = True

    assert actual == expected




def test_6_brackets():
    brackets_str = "[({}]"
    result = validate_brackets(brackets_str)
    actual = result
    expected = False

    assert actual == expected

def test_7_brackets():
    brackets_str = "(]("
    result = validate_brackets(brackets_str)
    actual = result
    expected = False

    assert actual == expected

def test_8_brackets():
    brackets_str = "{(})"
    result = validate_brackets(brackets_str)
    actual = result
    expected = False

    assert actual == expected




