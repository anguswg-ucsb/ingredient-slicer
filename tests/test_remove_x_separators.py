# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _utils._remove_x_separators() function -----
# -------------------------------------------------------------------------------
# 
# ingredient = "2 oz (56g / 1/8 package) dry"
# ingredient = f"""large (7-1/4" to 8-/1/2" long)"""
# _utils._remove_x_separators("4x4  inch")
# IngredientSlicer(ingredient, debug = True).parsed_ingredient
# _utils._remove_x_separators

