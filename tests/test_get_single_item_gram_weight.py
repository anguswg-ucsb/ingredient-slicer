# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- _get_gram_weight() tests ----
# -------------------------------------------------------------------------------
    
def test_get_single_item_gram_weight_one_egg():
    assert _utils._get_single_item_gram_weight("egg", "1", 0.5) == '56.7'
    
def test_get_single_item_gram_weight_two_eggs():
    assert _utils._get_single_item_gram_weight("egg", "2", 0.5) == '113.4'

def test_get_single_item_gram_weight_one_banana():
    assert _utils._get_single_item_gram_weight("banana", "1", 0.5) == '120.0'

def test_get_single_item_gram_weight_two_bananas():
    assert _utils._get_single_item_gram_weight("banana", "2", 0.5) == '240.0'

def test_get_single_item_gram_weight_one_and_a_half_bananas():
    assert _utils._get_single_item_gram_weight("banana", "1.5", 0.5) == '180.0'

def test_get_single_item_gram_weight_one_apple():
    assert _utils._get_single_item_gram_weight("apple", "1", 0.5)== '195.0'

def test_get_single_item_gram_weight_two_apples():
    assert _utils._get_single_item_gram_weight("apple", "2", 0.5)== '390.0'

def test_get_single_item_gram_weight_one_egg_no_quantity():
    assert _utils._get_single_item_gram_weight("egg", "", 0.5)== '56.7'

def test_get_single_item_gram_weight_one_egg_none_quantity():
    assert _utils._get_single_item_gram_weight("egg", None, 0.5) == '56.7'

# TODO: Need to refine behavior for foods that dont have a real unit or any unit at all
# TODO: Reference the _get_single_item_gram_weight() function that tries to take a food with no weight or volume unit 
# TODO: and get the gram weight. _get_single_item_gram_weight() assumes that if a food has no unit and or a Non weight/volume unit (i.e. 'heads') than the ingredient 
# TODO: is an individual item type ingredient where the food is also the unit (i.e. 2 eggs). There is a small/hacky SINGLE_ITEM_FOOD_WEIGHTS dictionary 
# TODO:  with an average gram weight of some common single item foods (primarly fruits, vegetables, and eggs)
def test_get_single_item_gram_weight_food_not_in_lookup_table():
    assert _utils._get_single_item_gram_weight("olive oil", "1", 0.5) ==  '5.0'


def test_error_with_giving_integers_for_food_and_quantity():
    with pytest.raises(TypeError):
        _utils._get_single_item_gram_weight(1, 1, 0.5)


def test_strict_threshold_for_word_eggplants():
    assert _utils._get_single_item_gram_weight("eggplants", "1", 1) is None

def test_looser_threshold_for_word_eggplants():
    assert _utils._get_single_item_gram_weight("eggplants", "1", 0.85) == '453.5'

def test_multiple_repeated_matching_words():
    assert _utils._get_single_item_gram_weight("eggplants eggplants", "1", 0.85) == '453.5'

def test_strict_threshold_for_word_eggplant():
    assert _utils._get_single_item_gram_weight("eggplant", "1", 1) == '453.5'

_utils._get_single_item_gram_weight("brocollini", "1", 0.5) 