# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- _convert_volumes_to_milliters() tests for converting volumes to milliters ----
# -------------------------------------------------------------------------------

def test_convert_volumes_to_milliters_one_cup():
    assert round(_utils._convert_volumes_to_milliliters("1",  "cup")) == 237

def test_convert_volumes_to_milliters_one_tablespoon():
    assert round(_utils._convert_volumes_to_milliliters("1",  "tbs")) == 15

def test_convert_volumes_to_milliters_one_teaspoon():
    assert round(_utils._convert_volumes_to_milliliters("1",  "tsp")) == 5

def test_convert_volumes_to_milliters_one_fluid_ounce():
    assert round(_utils._convert_volumes_to_milliliters("1",  "fluid oz")) == 30

def test_convert_volumes_to_milliters_one_gallon(): 
    assert round(_utils._convert_volumes_to_milliliters("1",  "gallon")) == 3785

def test_convert_volumes_to_milliters_one_pint():
    assert round(_utils._convert_volumes_to_milliliters("1",  "pint")) == 473

def test_convert_volumes_to_milliters_one_quart():
    assert round(_utils._convert_volumes_to_milliliters("1",  "quart")) == 946

def test_convert_volumes_to_milliters_one_liter():
    assert round(_utils._convert_volumes_to_milliliters("1",  "liter")) == 1000

def test_convert_volumes_to_milliters_one_milliliter():
    assert round(_utils._convert_volumes_to_milliliters("1",  "ml")) == 1

def test_convert_volumes_to_milliters_number_quantity():
    assert round(_utils._convert_volumes_to_milliliters(2,  "cup")) == 473

def test_convert_volumes_to_milliters_decimal_quantity():
    assert round(_utils._convert_volumes_to_milliliters(2.5,  "cup")) == 591

def test_convert_volumes_to_milliters_fraction_quantity_error():
    with pytest.raises(ValueError):
        _utils._convert_volumes_to_milliliters("1/2",  "cup")

def test_convert_volumes_to_milliters_invalid_unit_error():
    assert _utils._convert_volumes_to_milliliters("1",  "CPOP") is None
