# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils, IngredientSlicer
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- general tests for ingredients with no explicit quantities ----
# -------------------------------------------------------------------------------

# TODO: should this scenario result in a default quantity of "1" ???
# TODO: Right now, this ingredient has 'None' quantity / secondary_quantity
def test_no_quantity_ingredient_with_food_and_unit():

    slicer = IngredientSlicer("cup of milk")
    assert slicer.quantity() == "1"
    # assert slicer.quantity() is None
    assert slicer.secondary_quantity() is None

def test_cup_of_sugar_with_no_explicit_quantity():

    slicer = IngredientSlicer("c. sugar")
    
    assert slicer.quantity() == "1" 
    # assert slicer.quantity() is None
    assert slicer.secondary_quantity() is None

def test_sugar_with_no_common_weight_or_volume_unit_and_no_explicit_quantity():

    slicer = IngredientSlicer("bucket of sugar")

    assert slicer.quantity() is None
    assert slicer.secondary_quantity() is None

def test_ingredient_with_not_common_unit_and_implied_one_quantity():

    slicer = IngredientSlicer("a bucket of sugar")

    assert slicer.quantity() == "1" 
    assert slicer.secondary_quantity() is None


   
  





