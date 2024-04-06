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

def test_get_gram_weight_one_ounce_plural():
    gram_weights = _utils._get_gram_weight("chicken", "1", "ounces")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 28
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_ounce_plural_capitalized():
    gram_weights = _utils._get_gram_weight("chicken", "1", "Ounces")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 28
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_ounce_plural_uppercase():
    gram_weights = _utils._get_gram_weight("chicken", "1", "OUNCES")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 28
    assert min_gram_weight == None
    assert max_gram_weight == None


def test_get_gram_weight_multiple_ounces_plural():
    gram_weights = _utils._get_gram_weight("chicken", "10", "ounces")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 284
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_multiple_decimal_ounce():
    gram_weights = _utils._get_gram_weight("chicken", "10.5", "ounce")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 298
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_pound():
    gram_weights = _utils._get_gram_weight("chicken", "1", "pound")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 454
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_pound_plural():
    gram_weights = _utils._get_gram_weight("chicken", "1", "pounds")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 454
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_multiple_pound_plural():
    gram_weights = _utils._get_gram_weight("chicken", "10", "pounds")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4536
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_multiple_decimal_pound():
    gram_weights = _utils._get_gram_weight("chicken", "10.5", "pound")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4763
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_gram():
    gram_weights = _utils._get_gram_weight("chicken", "1", "gram")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 1
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_multiple_grams_plural():
    gram_weights = _utils._get_gram_weight("chicken", "10", "grams")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 10
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_multiple_decimal_grams():
    gram_weights = _utils._get_gram_weight("chicken", "10.5", "grams")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 10
    assert min_gram_weight == None
    assert max_gram_weight == None

def test_get_gram_weight_one_kilogram():
    gram_weights = _utils._get_gram_weight("chicken", "1", "kilogram")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 1000
    assert min_gram_weight == None
    assert max_gram_weight == None

# -------------------------------------------------------------------------------
# ---- _get_gram_weight() test for converting volumes ----
# -------------------------------------------------------------------------------

def test_get_gram_weight_one_milliliter_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "milliliter")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 1
    assert min_gram_weight == 1
    assert max_gram_weight == 1

    gram_weights = _utils._get_gram_weight("olive oil", "1", "milliliters")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 1
    assert min_gram_weight == 1
    assert max_gram_weight == 1

    gram_weights = _utils._get_gram_weight("olive oil", "1", "mL")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 1
    assert min_gram_weight == 1
    assert max_gram_weight == 1

def test_get_gram_weight_one_teaspoon_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4
    assert min_gram_weight == 4
    assert max_gram_weight == 5

    gram_weights = _utils._get_gram_weight("olive oil", "1", "tsp")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4
    assert min_gram_weight == 4
    assert max_gram_weight == 5

    gram_weights = _utils._get_gram_weight("olive oil", "1", "tsps")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4
    assert min_gram_weight == 4
    assert max_gram_weight == 5

def test_get_gram_weight_one_tablespoon_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "tablespoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 13
    assert min_gram_weight == 13
    assert max_gram_weight == 14

    gram_weights = _utils._get_gram_weight("olive oil", "1", "tbsp")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 13
    assert min_gram_weight == 13
    assert max_gram_weight == 14

    gram_weights = _utils._get_gram_weight("olive oil", "1", "tbsps")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 13
    assert min_gram_weight == 13
    assert max_gram_weight == 14

def test_get_gram_weight_one_cup_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "cup")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 215
    assert min_gram_weight == 208
    assert max_gram_weight == 227

    gram_weights = _utils._get_gram_weight("olive oil", "1", "cups")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 215
    assert min_gram_weight == 208
    assert max_gram_weight == 227

def test_get_gram_weight_one_pint_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "pint")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 431
    assert min_gram_weight == 416
    assert max_gram_weight == 454

    gram_weights = _utils._get_gram_weight("olive oil", "1", "pints")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 431
    assert min_gram_weight == 416
    assert max_gram_weight == 454

def test_get_gram_weight_one_quart_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "quart")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 862
    assert min_gram_weight == 833
    assert max_gram_weight == 908

    gram_weights = _utils._get_gram_weight("olive oil", "1", "quarts")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 862
    assert min_gram_weight == 833
    assert max_gram_weight == 908

def test_get_gram_weight_one_gallon_olive_oil():
    gram_weights = _utils._get_gram_weight("olive oil", "1", "gallon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3448
    assert min_gram_weight == 3331
    assert max_gram_weight == 3634

    gram_weights = _utils._get_gram_weight("olive oil", "1", "gallons")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3448
    assert min_gram_weight == 3331
    assert max_gram_weight == 3634

    gram_weights = _utils._get_gram_weight("olive oil", "1", "gals")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3448
    assert min_gram_weight == 3331
    assert max_gram_weight == 3634


def test_get_gram_weight_one_teaspoon_flour():
    gram_weights = _utils._get_gram_weight("flour", "1", "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3
    assert min_gram_weight == 2
    assert max_gram_weight == 5

    gram_weights = _utils._get_gram_weight("flour", "1", "tsp")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3
    assert min_gram_weight == 2
    assert max_gram_weight == 5

    gram_weights = _utils._get_gram_weight("almond flour", "1", "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3
    assert min_gram_weight == 2
    assert max_gram_weight == 5

    gram_weights = _utils._get_gram_weight("oat flour", "1", "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 3
    assert min_gram_weight == 2
    assert max_gram_weight == 5

def test_get_gram_weight_one_tablespoon_complex_flours():
    gram_weights = _utils._get_gram_weight("whole wheat oat flour", "1", "tablespoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 9
    assert min_gram_weight == 5
    assert max_gram_weight == 16

    gram_weights = _utils._get_gram_weight("whole grain wheat oat flour", "1", "tablespoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 9
    assert min_gram_weight == 5
    assert max_gram_weight == 16

    gram_weights = _utils._get_gram_weight("white flour", "1", "tablespoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 9
    assert min_gram_weight == 5
    assert max_gram_weight == 16


def test_get_gram_weight_one_cup_complex_flours():
    gram_weights = _utils._get_gram_weight("whole wheat oat flour", "1", "cup")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 137
    assert min_gram_weight == 83
    assert max_gram_weight == 253

    gram_weights = _utils._get_gram_weight("whole grain wheat oat flour", "1", "tablespoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 9
    assert min_gram_weight == 5
    assert max_gram_weight == 16

def test_get_gram_weight_integer_as_quantity():
    gram_weights = _utils._get_gram_weight("olive oil", 1, "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 4
    assert min_gram_weight == 4
    assert max_gram_weight == 5

def test_get_gram_weight_decimal_as_quantity():
    gram_weights = _utils._get_gram_weight("olive oil", 1.5, "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight == 7
    assert min_gram_weight == 7
    assert max_gram_weight == 7
def test_gret_gram_weight_zero_as_quantity():
    gram_weights = _utils._get_gram_weight("olive oil", 0, "teaspoon")

    gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    assert gram_weight is None
    assert min_gram_weight is None
    assert max_gram_weight is None
    
def test_get_gram_weight_fraction_as_quantity():
    with pytest.raises(ValueError):
        _utils._get_gram_weight("olive oil", "1/2", "teaspoon")

def test_get_gram_weight_invalid_unit():
    assert _utils._get_gram_weight("olive oil", "1", "fgdhdjgfhdf") == {"gram_weight": None, 
                                                                 "min_gram_weight": None, 
                                                                 "max_gram_weight": None}
    
