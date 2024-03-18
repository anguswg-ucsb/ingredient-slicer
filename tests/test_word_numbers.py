# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns

# regex_map = IngredientRegexPatterns()

@pytest.fixture
def regex_map():
    return IngredientRegexPatterns()


def test_number_words_1(regex_map):

    # numbers 2
    example_number_words = "two cups of flour"
    assert regex_map.NUMBER_WORDS_MAP["two"][0] == "2"
    assert regex_map.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]

def test_number_words_2(regex_map):
    # numbers 2, 3
    example_number_words = "two cups of flour and three cups of sugar"
    assert regex_map.NUMBER_WORDS_MAP["two"][0] == "2"
    assert regex_map.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert regex_map.NUMBER_WORDS_MAP["three"][0] == "3"
    assert regex_map.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]

def test_number_words_3(regex_map):
    # numbers 2, 3, 4
    example_number_words = "two cups of flour and three cups of sugar and four cups of salt"
    assert regex_map.NUMBER_WORDS_MAP["two"][0] == "2"
    assert regex_map.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert regex_map.NUMBER_WORDS_MAP["three"][0] == "3"
    assert regex_map.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]
    assert regex_map.NUMBER_WORDS_MAP["four"][0] == "4"
    assert regex_map.NUMBER_WORDS_MAP["four"][1].findall(example_number_words) == ["four"]

def test_number_words_4(regex_map):
    # numbers 2, 3, 4, 5
    example_number_words = "two cups of flour and three cups of sugar and four cups of salt and five cups of water"
    assert regex_map.NUMBER_WORDS_MAP["two"][0] == "2"
    assert regex_map.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert regex_map.NUMBER_WORDS_MAP["three"][0] == "3"
    assert regex_map.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]
    assert regex_map.NUMBER_WORDS_MAP["four"][0] == "4"
    assert regex_map.NUMBER_WORDS_MAP["four"][1].findall(example_number_words) == ["four"]
    assert regex_map.NUMBER_WORDS_MAP["five"][0] == "5"
    assert regex_map.NUMBER_WORDS_MAP["five"][1].findall(example_number_words) == ["five"]

def test_number_words_5(regex_map):
    # numbers 20-90
    example_number_words = "twenty cups of flour and thirty cups of sugar and forty cups of salt and fifty cups of water"
    assert regex_map.NUMBER_WORDS_MAP["twenty"][0] == "20"
    assert regex_map.NUMBER_WORDS_MAP["twenty"][1].findall(example_number_words) == ["twenty"]
    assert regex_map.NUMBER_WORDS_MAP["thirty"][0] == "30"
    assert regex_map.NUMBER_WORDS_MAP["thirty"][1].findall(example_number_words) == ["thirty"]
    assert regex_map.NUMBER_WORDS_MAP["forty"][0] == "40"
    assert regex_map.NUMBER_WORDS_MAP["forty"][1].findall(example_number_words) == ["forty"]
    assert regex_map.NUMBER_WORDS_MAP["fifty"][0] == "50"
    assert regex_map.NUMBER_WORDS_MAP["fifty"][1].findall(example_number_words) == ["fifty"]
