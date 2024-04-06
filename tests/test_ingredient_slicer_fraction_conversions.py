# "4/0.48 Bites"

# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the fraction conversion outputs of the IngredientSlicer ----
# -------------------------------------------------------------------------------

def test_whole_number_numerartor_with_whole_number_denominator():
    parsed = IngredientSlicer("4/2 Bites")
    assert parsed.standardized_ingredient() == "2 bites"

def test_whole_number_numerartor_with_whole_number_denominato_no_space_before_next_word():
    parsed = IngredientSlicer("4/10Bites")
    assert parsed.standardized_ingredient() == '0.4 bites'

def test_whole_number_numerartor_with_whole_number_denominato_no_space_after_previous_word():
    parsed = IngredientSlicer("I need4/10 Bites")
    assert parsed.standardized_ingredient() == 'i need 0.4 bites'

def test_whole_number_numerartor_with_whole_number_denominato_no_space_before_next_word_no_space_after_previous_word():
    parsed = IngredientSlicer("I need4/10Bites")
    assert parsed.standardized_ingredient() == 'i need 0.4 bites'

def test_whole_number_numerartor_with_whole_number_denominator_spaces_in_numerator():
    parsed = IngredientSlicer("I need 2 /10 Bites")
    assert parsed.standardized_ingredient() == 'i need 0.2 bites'

def test_whole_number_numerartor_with_whole_number_denominator_spaces_in_denominator():
    parsed = IngredientSlicer("I need 2/ 10 Bites")
    assert parsed.standardized_ingredient() == 'i need 0.2 bites'

def test_whole_number_numerartor_with_whole_number_denominator_spaces_in_numerator_and_denominator():
    parsed = IngredientSlicer("I need 2 / 10 Bites")
    assert parsed.standardized_ingredient() == 'i need 0.2 bites'

def test_whole_number_numerartor_with_decimal_denominator():
    parsed = IngredientSlicer("4/0.48 Bites")
    assert parsed.standardized_ingredient() == "8.333 bites"

def test_decimal_numerartor_with_whole_number_denominator():
    parsed = IngredientSlicer("0.48/4 Bites")
    assert parsed.standardized_ingredient() == "0.12 bites"

def test_decimal_numerartor_with_decimal_denominator():
    parsed = IngredientSlicer("0.48/0.48 Bites")
    assert parsed.standardized_ingredient() == "1 bites"

def test_decimal_numerartor_with_decimal_denominator_no_space_before_next_word():
    parsed = IngredientSlicer("0.48/0.48Bites")
    assert parsed.standardized_ingredient() == "1 bites"

def test_decimal_numerartor_with_decimal_denominator_no_space_after_previous_word():
    parsed = IngredientSlicer("I need0.48/0.48 Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_no_space_before_next_word_no_space_after_previous_word():
    parsed = IngredientSlicer("I need0.48/0.48Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_spaces_in_numerator():
    parsed = IngredientSlicer("I need 0.48 /0.48 Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_spaces_in_denominator():
    parsed = IngredientSlicer("I need 0.48/ 0.48 Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_spaces_in_numerator_and_denominator():
    parsed = IngredientSlicer("I need 0.48 / 0.48 Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_spaces_in_numerator_and_denominator_no_space_before_next_word():
    parsed = IngredientSlicer("I need 0.48 / 0.48Bites")
    assert parsed.standardized_ingredient() == "i need 1 bites"

def test_decimal_numerartor_with_decimal_denominator_before_period_end_of_string():
    parsed = IngredientSlicer("I need 0.48/0.48.")
    assert parsed.standardized_ingredient() == "i need 1."

def test_whole_number_numerartor_with_decimal_denominator_before_period_end_of_string():
    parsed = IngredientSlicer("I need 4/0.48.")
    assert parsed.standardized_ingredient() == "i need 8.333 ."

def test_decimal_numerartor_with_whole_number_denominator_before_period_end_of_string():
    parsed = IngredientSlicer("I need 0.48/4.")
    assert parsed.standardized_ingredient() == 'i need 0.12.'

# TODO: Bug, this should probably be "12 bites"
def test_whole_number_numerator_and_denominator_directly_after_period_starting_sentence():
    parsed = IngredientSlicer(".48/4 Bites")
    # parsed.parsed_ingredient
    assert parsed.standardized_ingredient() == '.12 bites'
