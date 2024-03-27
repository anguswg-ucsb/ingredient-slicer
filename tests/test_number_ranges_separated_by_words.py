# pytest library
import pytest

import re

# from fractions import Fraction

from ingredient_slicer import IngredientSlicer, _utils

# -------------------------------------------------------------------------------
# ---- Simple number ranges (whole numbers/decimals to whole numbers/decimals) ----
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- <number> "to" <number>" tests ----
# -------------------------------------------------------------------------------
def test_numbers_separated_by_to_1():
    slicer = IngredientSlicer("1 to 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_numbers_separated_by_to_2():
    slicer = IngredientSlicer("1.5 to 4.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_number_and_decimal_separated_by_to_1():
    slicer = IngredientSlicer("1 to 4.5 cups of sugar", debug=True)
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_decimal_separated_by_to_1():
    slicer = IngredientSlicer("1.5 to 4.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()
    
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_decimal_and_decimal_separated_by_to_with_hyphens_1():
    slicer = IngredientSlicer("1.5-to-4.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_mixed_fraction_and_mixed_fraction_separated_by_to_1():
    slicer = IngredientSlicer("1 1/2 to 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_to_with_hypens_1():
    slicer = IngredientSlicer("1 1/2-to-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_to_with_left_hyphen_1():
    slicer = IngredientSlicer("1 1/2-to 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_to_with_right_hyphen_1():
    slicer = IngredientSlicer("1 1/2 to-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_to_with_hyphens_1():
    slicer = IngredientSlicer("1.5-to-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_to_with_left_hyphen_1():
    slicer = IngredientSlicer("1.5-to 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []
    

def test_decimal_and_mixed_fraction_separated_by_to_with_right_hyphen_1():
    slicer = IngredientSlicer("1.5-to 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_mixed_fraction_and_decimal_separated_by_to_with_hyphens_1():
    slicer = IngredientSlicer("1 1/2-to-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_decimal_separated_by_to_with_left_hyphen_1():
    slicer = IngredientSlicer("1 1/2-to 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_to_with_left_hyphen_2():
    slicer = IngredientSlicer("1.5- to 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_decimal_separated_by_to_with_right_hyphen_1():
    slicer = IngredientSlicer("1 1/2 to-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_to_with_right_hyphen_2():
    slicer = IngredientSlicer("1.5 to- 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_number_and_mixed_fraction_separated_by_to_1():
    slicer = IngredientSlicer("5 to 5 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "5.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_number_and_mixed_fraction_separated_by_to_with_hyphens_1():

    slicer = IngredientSlicer("5-to-5 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "5.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []
# -------------------------------------------------------------------------------
# ---- <number> "or" <number>" tests ----
# -------------------------------------------------------------------------------
def test_numbers_separated_by_or_1():
    slicer = IngredientSlicer("1 or 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_numbers_separated_by_or_2():
    slicer = IngredientSlicer("1    or 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_fraction_and_fraction_separated_by_or_1():
    slicer = IngredientSlicer("1/2 or 2/3 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "0.5835"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_number_and_mixed_fraction_separated_by_or_2():
    slicer = IngredientSlicer("5 or 5 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "5.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_number_and_mixed_fraction_separated_by_or_with_hyphens_2():
    slicer = IngredientSlicer("5-or-5 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "5.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_or_no_hyphens_1():
    slicer = IngredientSlicer("1 1/2 or 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_or_with_hyphens_1():
    slicer = IngredientSlicer("1 1/2-or-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_mixed_fraction_and_mixed_fraction_separated_by_or_with_left_hyphen_1():
    slicer = IngredientSlicer("1 1/2-or 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_mixed_fraction_and_mixed_fraction_separated_by_or_with_right_hyphen_1():
    slicer = IngredientSlicer("1 1/2 or-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_or_with_hyphens_1():
    slicer = IngredientSlicer("1.5-or-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []


def test_decimal_and_mixed_fraction_separated_by_or_with_left_hyphen_1():
    slicer = IngredientSlicer("1.5-or 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_or_with_right_hyphen_1():

    slicer = IngredientSlicer("1.5 or-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_decimal_and_mixed_fraction_separated_by_or_no_hyphen_1():
    slicer = IngredientSlicer("1.5 or 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- "between <number> and <number>" tests ----
# -------------------------------------------------------------------------------
    
def test_between_number_and_number_1():
    slicer = IngredientSlicer("between 1 and 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

    
def test_between_number_and_number_with_hyphens():
    slicer = IngredientSlicer("between 1-and-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_left_hyphen():
    slicer = IngredientSlicer("between 1-and 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_right_hyphen():
    slicer = IngredientSlicer("between 1 and-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_hyphens_and_spaces():
    slicer = IngredientSlicer("between 1 - and - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_hyphens_and_spaces_and_extra_spaces():
    slicer = IngredientSlicer("between 1 - and    - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens():
    slicer = IngredientSlicer("between 1 - and    - 4 - cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_and_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens_and_extra_and():
    slicer = IngredientSlicer("between 1 - and    - 4 - and cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# Decimal "and" Number
def test_between_decimal_and_number_1():
    slicer = IngredientSlicer("between 1.5 and 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_hyphens_1():
    slicer = IngredientSlicer("between 1.5-and-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1.5-and 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1.5 and-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1.5 - and - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_hyphens_and_spaces_and_extra_spaces_1():
    slicer = IngredientSlicer("between 1.5 - and    - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens_1():
    slicer = IngredientSlicer("between 1.5 - and    - 4 - cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens_and_extra_and_1():
    slicer = IngredientSlicer("between 1.5 - and    - 4 - and cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- "between <decimal> and <mixed fraction>" tests ----
# -------------------------------------------------------------------------------
    
def test_between_decimal_and_mixed_fraction_1():
    slicer = IngredientSlicer("between 1.5 and 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_hyphens_1():
    slicer = IngredientSlicer("between 1.5-and-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1.5-and 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1.5 and-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1.5 - and - 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_hyphens_and_spaces_and_extra_spaces_1():
    slicer = IngredientSlicer("between 1.5 - and    - 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_and_mixed_fraction_with_hyphens_and_spaces_and_extra_spaces_and_extra_and_1():
    slicer = IngredientSlicer("between 1.5 - and    - 2 - and 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- "between <mixed fraction> and <decimal>" tests ----
# -------------------------------------------------------------------------------

def test_between_mixed_fraction_and_decimal_1():
    slicer = IngredientSlicer("between 1 1/2 and 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_and_decimal_with_hyphens_1():
    slicer = IngredientSlicer("between 1 1/2-and-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_and_decimal_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1 1/2-and 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_and_decimal_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1 1/2 and-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_and_decimal_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1 1/2 - and - 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []






# -------------------------------------------------------------------------------
# ---- "between <number> & <number>" tests (ampersand versions) ----
# -------------------------------------------------------------------------------
    
def test_between_number_ampersand_number_1():
    slicer = IngredientSlicer("between 1 & 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

    
def test_between_number_ampersand_number_with_hyphens():
    slicer = IngredientSlicer("between 1-&-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_left_hyphen():
    slicer = IngredientSlicer("between 1-& 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_right_hyphen():
    slicer = IngredientSlicer("between 1 &-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_hyphens_ampersand_spaces():
    slicer = IngredientSlicer("between 1 - & - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_hyphens_and_spaces_and_extra_spaces():
    slicer = IngredientSlicer("between 1 - &    - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens():
    slicer = IngredientSlicer("between 1 - &    - 4 - cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_number_ampersand_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens_and_extra_and():
    slicer = IngredientSlicer("between 1 - &    - 4 - & cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# Decimal "and" Number
def test_between_decimal_ampersand_number_1():
    slicer = IngredientSlicer("between 1.5 & 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_hyphens_1():
    slicer = IngredientSlicer("between 1.5-&-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1.5-& 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1.5 &-4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1.5 - & - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_hyphens_and_spaces_and_extra_spaces_1():
    slicer = IngredientSlicer("between 1.5 - &    - 4 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_hyphens_and_spaces_and_extra_spaces_and_extra_hyphens_1():
    slicer = IngredientSlicer("between 1.5 - &    - 4 - cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_number_with_hyphens_ampersand_spaces_and_extra_spaces_and_extra_hyphens_and_extra_ampersand_1():
    slicer = IngredientSlicer("between 1.5 - &    - 4 - & cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- "between <decimal> & <mixed fraction>" tests ----
# -------------------------------------------------------------------------------
    
def test_between_decimal_ampersand_mixed_fraction_1():
    slicer = IngredientSlicer("between 1.5 & 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_hyphens_1():
    slicer = IngredientSlicer("between 1.5-&-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1.5-& 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1.5 &-2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1.5 - & - 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_hyphens_and_spaces_and_extra_spaces_1():
    slicer = IngredientSlicer("between 1.5 - &    - 2 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_decimal_ampersand_mixed_fraction_with_hyphens_and_spaces_and_extra_spaces_and_extra_and_1():
    slicer = IngredientSlicer("between 1.5 - &    - 2 - & 1/2 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- "between <mixed fraction> & <decimal>" tests ----
# -------------------------------------------------------------------------------

def test_between_mixed_fraction_ampersand_decimal_1():
    slicer = IngredientSlicer("between 1 1/2 & 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_ampersand_decimal_with_hyphens_1():
    slicer = IngredientSlicer("between 1 1/2-&-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_ampersand_decimal_with_left_hyphen_1():
    slicer = IngredientSlicer("between 1 1/2-& 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_ampersand_decimal_with_right_hyphen_1():
    slicer = IngredientSlicer("between 1 1/2 &-2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_between_mixed_fraction_ampersand_decimal_with_hyphens_and_spaces_1():
    slicer = IngredientSlicer("between 1 1/2 - & - 2.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []





