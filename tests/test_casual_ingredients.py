# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Casual units tests ----
# -------------------------------------------------------------------------------

def test_casual_units_no_quantities_1():

    slicer = IngredientSlicer("a pinch of salt")
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_1():
    
    slicer = IngredientSlicer("5 pinches of salt")
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "5"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_2():
      
    slicer = IngredientSlicer("a couple of pinches of salt")
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_3():
        
    slicer = IngredientSlicer("a few pinches of salt")
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_quantities_with_dozen_1():
        
    slicer = IngredientSlicer("a couple dozen eggs", debug=False)
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "24"
    assert parsed['unit'] == 'eggs'
    assert parsed['standardized_unit'] == 'egg'
    assert parsed['food'] == 'eggs'
    assert parsed['is_required'] == True

def test_casual_quantities_with_dozen_2():

    slicer = IngredientSlicer("a few dozen eggs")
    parsed = slicer.to_json()
    assert parsed['quantity'] == "36"
    assert parsed['unit'] == "eggs"
    assert parsed['standardized_unit'] == 'egg'
    assert parsed['food'] == 'eggs'
    assert parsed['is_required'] == True

def test_casual_quantities_at_end_of_ingredient():
    
    slicer = IngredientSlicer("large watermelon, or a couple of diced watermelons")
    
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'watermelons'
    assert parsed['standardized_unit'] == 'watermelon'
    assert parsed['food'] == 'watermelon watermelons' # TODO: this is a bug, should be just watermelon
    assert parsed['is_required'] == True

def test_casual_quantities_in_parenthesis_1():

    slicer = IngredientSlicer("a few (about 3) pinches of salt")
    parsed = slicer.to_json()
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_quantities_in_parenthesis_2():

    slicer = IngredientSlicer("milk (a couple of cups) ")
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == "cups"
    assert parsed['standardized_unit'] == "cup"
    assert parsed['food'] == 'milk'
    assert parsed['is_required'] == True


def test_casual_quantity_few_dashes_of_salt():
    
    slicer = IngredientSlicer("Few dashes of salt", debug=True)
    parsed = slicer.to_json()

    assert parsed['quantity'] == "3"
    assert parsed['unit'] == "dashes"
    assert parsed['standardized_unit'] == "dash"
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None
