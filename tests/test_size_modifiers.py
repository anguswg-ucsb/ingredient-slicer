# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Size modifier words tests ----
# testing ingredients with size modifier words (e.g. small, large, etc.) and the "size_modifier" attribute
# -------------------------------------------------------------------------------

def test_size_modifier_words_simple_1():

    slicer = IngredientSlicer("1 small apple")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'apple'
    assert parsed['food'] == 'apple'
    assert parsed['is_required'] == True
    assert parsed['size_modifiers'] == ['small']

def test_size_modifier_words_simple_2():
    
    slicer = IngredientSlicer("1 large apple")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'apple'
    assert parsed['food'] == 'apple'
    assert parsed['is_required'] == True
    assert parsed['size_modifiers'] == ['large']

def test_size_modifier_words_simple_3():
        
    slicer = IngredientSlicer("2 medium apples")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'apples'
    assert parsed['food'] == 'apples'
    assert parsed['is_required'] == True
    assert parsed['size_modifiers'] == ['medium']

def test_size_modifier_words_simple_4():
            
    slicer = IngredientSlicer("1 small to medium apple")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'apple'
    assert parsed['food'] == 'apple'
    assert parsed['is_required'] == True
    assert parsed['size_modifiers'] == ['medium', 'small']


