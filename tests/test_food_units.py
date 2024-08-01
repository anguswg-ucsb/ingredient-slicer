# pytest library
import pytest
# import random
import re

from ingredient_slicer import _constants, _utils

# -------------------------------------------------------------------------------
# ---- _get_food_unit() tests ----
# -------------------------------------------------------------------------------
 
def test_get_food_units_with_empty_string():
    assert _utils._get_food_unit("") == None

def test_get_food_units_with_no_units():
    assert _utils._get_food_unit("1 cup") == None

def test_get_food_units_with_no_units_and_no_number():
    assert _utils._get_food_unit("cup") == None

def test_get_food_units_food_with_standard_unit():
    assert _utils._get_food_unit("1 cup flour") == None

def test_get_food_units_food_with_non_standard_unit():
    assert _utils._get_food_unit("1 can flour") == None

def test_get_food_units_food_with_food_unit_and_standard_unit():
    assert _utils._get_food_unit("1 tortilla (2 cups)") == 'tortilla'

def test_get_food_units_food_with_food_unit_and_no_other_unit():
    assert _utils._get_food_unit("1 tortilla") == 'tortilla'

def test_get_food_units_all_units_in_FOOD_UNITS():
    for i, unit in enumerate(_constants.FOOD_UNITS_SET):
        random_ingredient = f"{i} {unit}"
        food_unit = _utils._get_food_unit(random_ingredient)

        # assert food_unit == unit
        assert _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(food_unit) == _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(unit)

def test_get_food_units_with_ingredient_that_has_two_food_units():
    assert _utils._get_food_unit("1 corn tortilla ") == 'tortilla'   
    assert _utils._get_food_unit("1 tortilla corn ") == 'corn' 

def test_get_food_unit_list_with_empty_string():
    assert _utils._get_food_unit_list("") == []

def test_get_food_unit_list_with_no_units():
    assert _utils._get_food_unit_list("1 cup") == []

def test_get_food_unit_list_with_food_units(): 
    assert _utils._get_food_unit_list("1 tortilla (2 cups)") == ['tortilla']
    assert _utils._get_food_unit_list("1 tortilla") == ['tortilla']
    assert _utils._get_food_unit_list("1 tortilla corn") == ['tortilla', 'corn']
    assert _utils._get_food_unit_list("1 egg (or 2 eggs whites)") == ['egg', 'eggs']
    assert _utils._get_food_unit_list("14 heads of broccoli") == ['broccoli']

    
