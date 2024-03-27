# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer, _regex_patterns

# -------------------------------------------------------------------------------
# ---- Test IngredientSlicer: Words-to-numbers tests ----
# -------------------------------------------------------------------------------

def test_number_words_1():
    parse = IngredientSlicer("two cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []


def test_number_words_2():
    parse = IngredientSlicer("two cups of flour and three cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"
    
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour sugar' # TODO: not sure what the best way to handle 2 foods in one ingredient is...
    assert parsed['size_modifiers'] == []

def test_number_words_3():
    parse = IngredientSlicer("a dozen cups of melted butter")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "12"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['melted']
    assert parsed['food'] == 'butter'
    assert parsed['size_modifiers'] == []

def test_number_words_4():
    parse = IngredientSlicer("two or three tsp of room temp butter")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'tsp'
    assert parsed['standardized_unit'] == "teaspoon"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['room temp']
    assert parsed['food'] == 'butter'
    assert parsed['size_modifiers'] == []

def test_number_words_5():
    parse = IngredientSlicer("two to three tsp of room temp butter")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'tsp'
    assert parsed['standardized_unit'] == "teaspoon"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['room temp']
    assert parsed['food'] == 'butter'
    assert parsed['size_modifiers'] == []

# TODO: this seems like the best effort to handle "two and three" as a quantity, just a really poorly written ingredient
def test_number_words_6():
    parse = IngredientSlicer("two and three tsp of room temp butter")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "5"
    assert parsed['unit'] == 'tsp'
    assert parsed['standardized_unit'] == "teaspoon"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['room temp']
    assert parsed['food'] == 'butter'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- Test regex.NUMBER_WORDS_MAP: Words-to-numbers tests ----
# -------------------------------------------------------------------------------

def test_number_words_1():

    # numbers 2
    example_number_words = "two cups of flour"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][0] == "2"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]

def test_number_words_2():
    # numbers 2, 3
    example_number_words = "two cups of flour and three cups of sugar"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][0] == "2"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][0] == "3"
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]

def test_number_words_3():
    # numbers 2, 3, 4
    example_number_words = "two cups of flour and three cups of sugar and four cups of salt"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][0] == "2"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][0] == "3"
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]
    assert _regex_patterns.NUMBER_WORDS_MAP["four"][0] == "4"
    assert _regex_patterns.NUMBER_WORDS_MAP["four"][1].findall(example_number_words) == ["four"]

def test_number_words_4():
    # numbers 2, 3, 4, 5
    example_number_words = "two cups of flour and three cups of sugar and four cups of salt and five cups of water"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][0] == "2"
    assert _regex_patterns.NUMBER_WORDS_MAP["two"][1].findall(example_number_words) == ["two"]
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][0] == "3"
    assert _regex_patterns.NUMBER_WORDS_MAP["three"][1].findall(example_number_words) == ["three"]
    assert _regex_patterns.NUMBER_WORDS_MAP["four"][0] == "4"
    assert _regex_patterns.NUMBER_WORDS_MAP["four"][1].findall(example_number_words) == ["four"]
    assert _regex_patterns.NUMBER_WORDS_MAP["five"][0] == "5"
    assert _regex_patterns.NUMBER_WORDS_MAP["five"][1].findall(example_number_words) == ["five"]

def test_number_words_5():
    # numbers 20-90
    example_number_words = "twenty cups of flour and thirty cups of sugar and forty cups of salt and fifty cups of water"
    assert _regex_patterns.NUMBER_WORDS_MAP["twenty"][0] == "20"
    assert _regex_patterns.NUMBER_WORDS_MAP["twenty"][1].findall(example_number_words) == ["twenty"]
    assert _regex_patterns.NUMBER_WORDS_MAP["thirty"][0] == "30"
    assert _regex_patterns.NUMBER_WORDS_MAP["thirty"][1].findall(example_number_words) == ["thirty"]
    assert _regex_patterns.NUMBER_WORDS_MAP["forty"][0] == "40"
    assert _regex_patterns.NUMBER_WORDS_MAP["forty"][1].findall(example_number_words) == ["forty"]
    assert _regex_patterns.NUMBER_WORDS_MAP["fifty"][0] == "50"
    assert _regex_patterns.NUMBER_WORDS_MAP["fifty"][1].findall(example_number_words) == ["fifty"]
