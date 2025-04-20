import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test "whole30" string in an ingredient foods ----
# -------------------------------------------------------------------------------

def test_ingredient_with_whole30_diet_in_parenthesises():
    ing = IngredientSlicer("1 lb pork sausage (casings removed if necessary, sugar-free for whole30)")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1 lb pork sausage (casings removed if necessary, sugar-free for whole30)', 
        'standardized_ingredient': '1 lb pork sausage', 
        'food': 'pork sausage', 
        'quantity': '1', 
        'unit': 'lb', 
        'standardized_unit': 'pound', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None, 
        'density': None, 
        'gram_weight': '453.59', 
        'prep': [], 
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': ['casings removed if necessary, sugar-free for']
        }
    assert output == expected_output

# TODO: deal with this scenario
def test_ingredient_an_ingredient_with_add_5_minutes_in_parenthesis():
    ing = IngredientSlicer("1 lb pork sausage (add 5 minutes)")
    output = ing.to_json()

