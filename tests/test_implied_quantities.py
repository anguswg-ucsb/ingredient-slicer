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

    assert slicer.quantity() is None
    assert slicer.secondary_quantity() is None


   
  





