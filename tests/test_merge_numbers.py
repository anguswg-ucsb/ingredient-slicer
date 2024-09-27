# pytest library
import pytest

import re
# from fractions import Fraction
from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Test IngredientSlicer: Merge space separated numbers ----
# -------------------------------------------------------------------------------

def test_merge_numbers_1():
    parse = IngredientSlicer("1 2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_numbers_3():
    parse = IngredientSlicer("1 2/3 or 2 1/2 cups of flour", debug=True)
    parsed = parse.to_json()

    assert parsed['quantity'] == "2.0835"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fractions_with_extra_spaces_1():
    parse = IngredientSlicer("1 2 / 3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fractions_range_with_extra_spaces_1():
    parse = IngredientSlicer("1 2 / 3 - 2 1 / 2 cups of flour")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2.0835"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_spaces_1():
    parse = IngredientSlicer("1  2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_trailing_spaces_1():
    parse = IngredientSlicer("1 2/3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_and_trailing_spaces_1():
    parse = IngredientSlicer("1  2/3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_and_trailing_spaces_2():
    parse = IngredientSlicer("1  2 /3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_decimal_then_fraction_1():
    parse = IngredientSlicer("1.5 2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "2.167"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_decimal_then_mixed_fraction_1(): 
    parse = IngredientSlicer("1 2 2/3 cups of flour") # TODO: this is a bug and should really result in 2.667 cups
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