# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Duplicate unit ranges tests ----
# -------------------------------------------------------------------------------

def test_fraction_dupe_units_range_quantity_1():
    parse = IngredientSlicer("1cup-1/2 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_fraction_dupe_units_range_quantity_2():
    parse = IngredientSlicer("1/2 cup-1 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "0.75"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_fraction_dupe_units_range_quantity_3():
    parse = IngredientSlicer("1/2cup-1cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "0.75"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True