
# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test for _extract_quantity functions in _utils.py  ----
#  - _extract_quantity_unit_pairs
#  - _extract_quantities_only
#  - _extract_equivalent_quantity_units
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- _extract_quantity_unit_pairs() ----
# -------------------------------------------------------------------------------

def test_extract_quantity_unit_pairs_1():
    assert _utils._extract_quantity_unit_pairs("1 cup of sugar") == [("1", "cup")]


def test_extract_quantity_unit_pairs_mixed_number_1():
    # NOTE: this is intended behavior BUT not what will happen in IngredientSlicer 
    # because by this point any multi numbers like that will have been merged
    assert _utils._extract_quantity_unit_pairs("1 1/2 cups of sugar") == [("1", "cups"), ("1/2", "cups")] 

def test_extract_quantity_unit_pairs_decimal_1():
    assert _utils._extract_quantity_unit_pairs("1.5 cups of sugar") == [("1.5", "cups")]

def test_extract_quantity_unit_pairs_decimal_then_whole_number_with_second_unit():
    assert _utils._extract_quantity_unit_pairs("1.5 cups and 2 tbs of sugar") == [("1.5", "cups"), ("2", "tbs")]

def test_extract_quantity_unit_pairs_decimal_then_whole_number_with_second_unit_2():
    assert _utils._extract_quantity_unit_pairs("1.5 cups and 221 tbs of sugar") == [("1.5", "cups"), ("221", "tbs")]

def test_extract_quantity_unit_pairs_decimal_then_decimal_with_second_unit_3():
    assert _utils._extract_quantity_unit_pairs("1.5 cups and 0.5 tbs of sugar") == [("1.5", "cups"), ("0.5", "tbs")]

# -------------------------------------------------------------------------------
# ---- _extract_quantities_only() ----
# -------------------------------------------------------------------------------

def test_extract_quantities_only_1():
    assert _utils._extract_quantities_only("1 cup of sugar") == []

def test_extract_quantities_only_2():
    assert _utils._extract_quantities_only("1 1/2 cups of sugar") == []

def test_extract_quantities_only_3():
    assert _utils._extract_quantities_only("1.5 cups of sugar") == []

def test_extract_quantities_only_no_units_1():
    assert _utils._extract_quantities_only("1.5 of sugar") == ["1.5"]

def test_extract_quantities_only_no_units_2():
    assert _utils._extract_quantities_only("1 1/2 of sugar") == ["1", "1/2"]

def test_extract_quantities_only_no_units_decimal_1():
    assert _utils._extract_quantities_only("1.5 of sugar") == ["1.5"]

def test_extract_quantities_only_no_units_decimal_then_fraction_1():
    assert _utils._extract_quantities_only("1.5 of 1/2 sugar") == ["1.5", "1/2"]

def test_extract_quantity_no_quantity_no_units_1():
    assert _utils._extract_quantities_only("of sugar") == []

def test_extract_quantity_integer_error():
    with pytest.raises(ValueError):
        _utils._extract_quantities_only(115)

# -------------------------------------------------------------------------------
# ---- _extract_equivalent_quantity_units() ----
# -------------------------------------------------------------------------------

def test_extract_equivalent_quantity_units_no_approximate_1():
    assert _utils._extract_equivalent_quantity_units("1 cup of sugar") == []




