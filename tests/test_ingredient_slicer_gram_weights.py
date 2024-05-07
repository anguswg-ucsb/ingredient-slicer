# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the gram_weight attribute of the IngredientSlicer ----
# -------------------------------------------------------------------------------

def test_eggs_with_quantity_and_no_unit():
    ing = IngredientSlicer("2 eggs")

    assert ing.gram_weight() == '113.4'

def test_egg_with_remaining_text_with_food_word_with_quantity_no_unit():
    ing = IngredientSlicer("2 farm-raised, fresh, eggs, beaten")
    # ing.gram_weight()
    # ing.food()

    assert ing.gram_weight() == '113.4'

def test_eggplant_with_remaining_text_with_food_word_with_quantity_no_unit():
    ing = IngredientSlicer("1 large eggplant, peeled and cubed")
    # ing.gram_weight()
    # ing.food()

    assert ing.gram_weight() == '453.5'

def test_banana_with_size_modifier_and_quantity():
    ing = IngredientSlicer("2 large bananas")
    # ing.gram_weight()
    # ing.food()
    assert ing.gram_weight() == '240.0'

def test_get_single_gram_weight_for_melon_with_quantity_of_integer_two():
    ing = IngredientSlicer("2 melons")
    # ing.gram_weight()
    # ing.food()
    assert ing.gram_weight() == '3000.0'

def test_get_single_gram_weight_for_melon_with_quantity_of_float_two():
    ing = IngredientSlicer("2.0 honeydew melons")
    # ing.gram_weight()
    # ing.food()

    assert ing.gram_weight() == '3600.0'






# IngredientSlicer("3 nuggets chopped", debug = True).gram_weight()
# IngredientSlicer("3 head of fresh organic brocolni, chopped", debug = True).gram_weight()
# IngredientSlicer("1 head of fresh organic brocollii, chopped", debug = True).gram_weight()
# IngredientSlicer("1 head of fresh organic chicken, chopped", debug = True).gram_weight()