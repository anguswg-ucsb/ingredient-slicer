import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test edge case foods ----
# - Half and half
# - Half and half cream
# - Half and half milk
# - Half and half creamer
# - Garlic cloves vs. cloves
# -------------------------------------------------------------------------------

def test_half_and_half_single_spaced():
    ing = IngredientSlicer("1/2 cup half and half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half and half', 
        'standardized_ingredient': 
        '0.5 cup half and half', 
        'food': 'half and half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    assert output == expected_output

def test_half_n_half_single_spaced():
    ing = IngredientSlicer("1/2 cup half n half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half n half', 
        'standardized_ingredient': 
        '0.5 cup half n half', 
        'food': 'half n half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    
    assert output == expected_output

def test_half_ampersand_half_single_spaced():
    ing = IngredientSlicer("1/2 cup half & half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half & half', 
        'standardized_ingredient': 
        '0.5 cup half & half', 
        'food': 'half and half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    assert output == expected_output

def test_half_and_half_dash_sep():
    ing = IngredientSlicer("1/2 cup half-and-half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half-and-half', 
        'standardized_ingredient': 
        '0.5 cup half and half', 
        'food': 'half and half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    assert output == expected_output

def test_half_n_half_dash_sep():
    ing = IngredientSlicer("1/2 cup half-n-half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half-n-half', 
        'standardized_ingredient': 
        '0.5 cup half-n-half', 
        'food': 'half and half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    
    assert output == expected_output

def test_half_ampersand_half_dash_sep():
    ing = IngredientSlicer("1/2 cup half-&-half")
    output = ing.to_json()

    expected_output = {
        'ingredient': '1/2 cup half-&-half', 
        'standardized_ingredient': 
        '0.5 cup half & half', 
        'food': 'half and half', 
        'quantity': '0.5', 
        'unit': 'cup',
        'standardized_unit': 'cup', 
        'secondary_quantity': None, 
        'secondary_unit': None, 
        'standardized_secondary_unit': None,
        'density': 0.827,
        'gram_weight': '97.83', 
        'prep': [],
        'size_modifiers': [], 
        'dimensions': [], 
        'is_required': True, 
        'parenthesis_content': []
        }
    assert output == expected_output