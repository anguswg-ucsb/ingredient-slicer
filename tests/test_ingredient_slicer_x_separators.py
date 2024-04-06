# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the IngredientSlicer class ability to parse ingredients with "X" separators ----
# Main 2 cases are:
# 1. "X" separator between two numbers is used to represent a quantity to multiple the units by (i.e. "2 x cups of sugar")
# 2. "X" separator between two numbers is used to represent a dimension (i.e. "3 x 4 inch pan")
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- "x" used as a quantity multiplier ----
# -------------------------------------------------------------------------------

def test_ingredient_slicer_x_separators_quantity_multiplier_no_quantity_to_multiply_and_no_dimensions():

    slicer = IngredientSlicer("2 x cups of sugar")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '2 cups of sugar'
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
    assert parsed["dimensions"] == []
    assert parsed["parenthesis_content"] == []

def test_ingredient_slicer_x_separators_quantity_multiplier_with_number_quantity_to_multiply_and_no_dimensions():
    
    slicer = IngredientSlicer("2 x 3 cups of sugar")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '6 cups of sugar'
    assert parsed['quantity'] == "6"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == []
    assert parsed["parenthesis_content"] == []

def test_ingredient_slicer_x_separators_quantity_multiplier_with_fraction_quantity_to_multiply_and_no_dimensions():
        
    slicer = IngredientSlicer("3 x 1/2 cups of sugar")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '3.5 cups of sugar'
    assert parsed['quantity'] == "3.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == []
    assert parsed["parenthesis_content"] == []

def test_ingredient_slicer_x_separators_quantity_multiplier_with_decimal_quantity_to_multiply_and_no_dimensions():
                
    slicer = IngredientSlicer("3 x 0.5 cups of sugar")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '3.5 cups of sugar'
    assert parsed['quantity'] == "3.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == []
    assert parsed["parenthesis_content"] == []

def test_ingredient_slicer_x_separators_quantity_multiplier_with_number_quantity_to_multiply_and_single_dimension_unit():
                    
    slicer = IngredientSlicer("3 x 4oz salmon fillets (2 inch thick)")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '12 oz salmon fillets'

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []

    assert parsed['food'] == 'salmon'

    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == ['2 inch']

    assert parsed["parenthesis_content"] == ['thick']

def test_ingredient_slicer_x_separators_quantity_multiplier_with_fraction_quantity_to_multiply_and_single_dimension_unit():
                            
    slicer = IngredientSlicer("3 x 1/2oz salmon fillets (2 inch thick)")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '3.5 oz salmon fillets'

    assert parsed['quantity'] == "3.5"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []

    assert parsed['food'] == 'salmon'

    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == ['2 inch']

    assert parsed["parenthesis_content"] == ['thick']

def test_ingredient_slicer_x_separators_quantity_multiplier_with_decimal_quantity_to_multiply_and_single_dimension_unit():
                                    
    slicer = IngredientSlicer("3 x 0.5oz salmon fillets (2 inch thick)")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '3.5 oz salmon fillets'

    assert parsed['quantity'] == "3.5"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []

    assert parsed['food'] == 'salmon'

    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == ['2 inch']

    assert parsed["parenthesis_content"] == ['thick']

def test_ingredient_slicer_x_separators_quantity_multiplier_with_number_quantity_to_multiply_and_multiple_dimension_units_separated_by_x():
                                            
    slicer = IngredientSlicer("3 x 4oz salmon fillets (2 inch x 3 inch)")
    parsed = slicer.to_json()

    assert parsed["standardized_ingredient"] == '12 oz salmon fillets'

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []

    assert parsed['food'] == 'salmon'

    assert parsed['size_modifiers'] == []
    assert parsed["dimensions"] == ['2 inch x 3 inch']

    assert parsed["parenthesis_content"] == [''] # TODO:   