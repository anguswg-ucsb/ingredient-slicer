# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test parenthesis handling of IngredientSlicer ----
# -------------------------------------------------------------------------------

def test_parenthesis_no_content():
    ing = IngredientSlicer("flour ()")

    assert ing._parenthesis_content == ['']

def test_ingredient_with_quanitity_unit_then_parenthesis_with_about_quantity_only():
    slicer = IngredientSlicer('2 pounds Golden Delicious apples (about 4), peeled, cored, and each cut into 8 wedges')

    expected_output = {
        'ingredient': '2 pounds Golden Delicious apples (about 4), peeled, cored, and each cut into 8 wedges', 
        'standardized_ingredient': '2 pounds golden delicious apples , peeled, cored, and each cut into 8 wedges', 
        'food': 'golden delicious apples wedges', 
        'quantity': '2', 
        'unit': 'pounds', 
        'standardized_unit': 'pound', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None, 
        'density': None,
        'gram_weight': '907.18', 
        'prep': ['cored', 'cut', 'peeled'], 
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': ['about 4']
        }
    
    assert slicer.parsed_ingredient() == expected_output

