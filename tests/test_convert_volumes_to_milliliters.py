# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- _get_gram_weight() tests ----
# -------------------------------------------------------------------------------

# food:str, 
# quantity:str, 
# unit:str

# -------------------------------------------------------------------------------
# ---- _get_gram_weight() test for converting simple weights ----
# -------------------------------------------------------------------------------
# grams_map = _utils._get_gram_weight("flour" "1", "cup", "levenshtein")

def test_get_gram_weight_one_ounce():
    gram_weights = _utils._get_gram_weight("chicken", "1", "ounce")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 28
    assert min_gram_weight == None
    assert max_gram_weight == None