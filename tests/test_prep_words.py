# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Prep words extraction tests ----
# testing ingredients with prep words (e.g. sliced, peeled, etc.)
# -------------------------------------------------------------------------------

def test_prep_words_simple_1():

    slicer = IngredientSlicer("1 cup sliced apples")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'apples'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['sliced']
    
def test_prep_words_simple_2():

    slicer = IngredientSlicer("1 cup peeled apples")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'apples'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['peeled']

def test_prep_words_simple_3():

    slicer = IngredientSlicer("2 cups of crushed and diced onions")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['food'] == 'onions'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['crushed', 'diced']

def test_prep_words_additional_1():
    slicer = IngredientSlicer("1 cup chopped and diced carrots")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'carrots'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['chopped', 'diced']

def test_prep_words_additional_2():
    slicer = IngredientSlicer("2 tablespoons thinly sliced scallions")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['food'] == 'scallions'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['sliced', 'thinly']

def test_prep_words_additional_3():
    slicer = IngredientSlicer("3 cloves minced garlic")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'cloves'            # TODO: need a special case for "cloves" as a unit vs. "cloves" as a food
    assert parsed['food'] == 'cloves garlic'   
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['minced']

def test_prep_words_additional_4():
    slicer = IngredientSlicer("1 cup packed brown sugar")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'brown sugar'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['packed']

def test_prep_words_additional_5():
    slicer = IngredientSlicer("2 tablespoons grated Parmesan cheese")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['food'] == 'parmesan cheese'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['grated']

def test_prep_words_additional_6():
    slicer = IngredientSlicer("1 cup toasted almonds")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'almonds'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['toasted']

def test_prep_words_additional_7():
    slicer = IngredientSlicer("1 teaspoon firmly packed brown sugar")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'teaspoon'
    assert parsed['food'] == 'brown sugar'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['firmly', 'packed']

def test_prep_words_additional_8():
    slicer = IngredientSlicer("1 cup halved strawberries")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'strawberries'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['halved']

def test_prep_words_additional_9():
    slicer = IngredientSlicer("2 tablespoons roughly chopped cilantro")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['food'] == 'cilantro'
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['chopped', 'roughly']

def test_prep_words_additional_10():
    slicer = IngredientSlicer("1 cup unsifted all-purpose flour")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['food'] == 'flour' 
    assert parsed['is_required'] == True
    assert parsed['prep'] == ['unsifted']