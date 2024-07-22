# pytest library
import pytest

import re
import typing
from typing import Union

from ingredient_slicer import _constants, _utils
# from ingredient_slicer import IngredientSlicer

# TODO: add more tests here
# TODO: - error handling for invalid inputs
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- _get_food_density() tests ----
# -------------------------------------------------------------------------------

def test_get_food_density_egg():
    expected = {'density':0.44, 'min_density':0.35, 'max_density':0.6}

    assert _utils._get_food_density("egg") == expected 

def test_get_food_density_water():
    expected = {'density':1.0, 'min_density':1.0, 'max_density':1.0}

    assert _utils._get_food_density("water") == expected

def test_get_food_density_white_flour():
    expected = {'density':0.5781, 'min_density':0.35, 'max_density':1.07}

    assert _utils._get_food_density("white flour") == expected

def test_get_food_density_olive_oil():
    expected = {'density':0.9108, 'min_density':0.88, 'max_density':0.96}

    assert _utils._get_food_density("olive oil") == expected

def test_get_food_density_empty_string():
    expected = {'density':1.0, 'min_density':1.0, 'max_density':1.0}
    assert _utils._get_food_density("") == expected

def test_get_food_density_none_food():
    expected = {'density':1.0, 'min_density':1.0, 'max_density':1.0}
    assert _utils._get_food_density(None) == expected

def test_get_food_density_int_food_error():
    with pytest.raises(TypeError):
        _utils._get_food_density(1)

def test_get_food_density_food_string_invalid_method_error():
    with pytest.raises(ValueError):
        _utils._get_food_density("olive oil", method="invalid")