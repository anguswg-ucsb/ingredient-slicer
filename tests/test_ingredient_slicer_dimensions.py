# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the dimensions attribute of the IngredientSlicer ----
# -------------------------------------------------------------------------------

def test_single_inch_ingredient_no_real_quantity_units():
    ing = IngredientSlicer("flour (4 inch)")

    assert ing.dimensions() == ["4 inch"]

def test_single_inch_ingredient_with_real_quantity_units():
    ing = IngredientSlicer("1 cup of flour (4 inch)")

    assert ing.dimensions() == ["4 inch"]

def test_single_inch_ingredient_with_real_quantity_units_and_no_space():
    ing = IngredientSlicer("1 cup of flour (4inch)")

    assert ing.dimensions() == ["4 inch"]

def test_multiple_inch_units():
    ing = IngredientSlicer("1 cup of flour (4 x 3 inch)")


    assert ing.dimensions() == ["4 x 3 inch"]

def test_multiple_inch_units_no_space():
    ing = IngredientSlicer("1 cup of flour (4x3 inch)")

    assert ing.dimensions() == ["4 x 3 inch"]

def test_multiple_inch_units_no_space_between_numbers():
    ing = IngredientSlicer("1 cup of flour (4x3inch)")

    assert ing.dimensions() == ["4 x 3 inch"]

def test_multiple_inch_units_no_space_between_numbers_and_no_space():
    ing = IngredientSlicer("1 cup of flour 12.5inch)")

    assert ing.dimensions() == ["12.5 inch"]

def test_multiple_inch_units_no_space_between_numbers_and_no_space_no_decimal():
    ing = IngredientSlicer("1 cup of flour 12inch)")

    assert ing.dimensions() == ["12 inch"]

def test_multiple_inch_units_no_space_between_numbers_and_no_space_no_decimal_no_number():
    ing = IngredientSlicer("1 cup of flour 12inch)")

    assert ing.dimensions() == ["12 inch"]

def test_two_sets_of_dimension_unit_ranges_separator_x():
    ing = IngredientSlicer("1 cup of flour (4 x 3 inch) (2 x 2 inch)")

    assert ing.dimensions() == ["4 x 3 inch", "2 x 2 inch"]

def test_two_sets_of_dimension_unit_ranges_separator_x_no_space():
    ing = IngredientSlicer("1 cup of flour (4x3 inch) (2x2 inch)")

    assert ing.dimensions() == ["4 x 3 inch", "2 x 2 inch"]

def test_two_sets_of_dimension_unit_ranges_separator_by():
    ing = IngredientSlicer("1 cup of flour (4 by 3 inch) (2 by 2 inch)")

    assert ing.dimensions() == ["4 by 3 inch", "2 by 2 inch"]

def test_two_sets_of_dimension_unit_ranges_separator_by_no_space():
    ing = IngredientSlicer("1 cup of flour (4by3 inch) (2by2 inch)")

    assert ing.dimensions() == ["4 by 3 inch", "2 by 2 inch"]

# TODO: this test is a bug and it needs to be fixed, i.e. the quantity/unit should be 1 cup and thats it. 
def test_three_consequetive_x_separated_dimension_units():
    ing = IngredientSlicer("1 cup of flour (4 x 3 x 2 inch)")

    expected_output = {
    'ingredient': "1 cup of flour (4 x 3 x 2 inch)", 
    'standardized_ingredient': '1 cup of flour', 
    'food': 'flour',
    'quantity': '12', 
    'unit': 'cup', 
    'standardized_unit': 'cup', 
    'secondary_quantity': '1', 
    'secondary_unit': None, 
    'standardized_secondary_unit': None, 
    'gram_weight': "1641.26",
    'prep': [], 
    'size_modifiers': [], 
    'dimensions': ['2 inch'],
    'is_required': True, 
    'parenthesis_content': ['12']
    }

    assert ing.parsed_ingredient() == expected_output