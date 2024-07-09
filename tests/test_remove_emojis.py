# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# ---- Test utils._remove_emojis(): Removes emojis from strings... ----
# -------------------------------------------------------------------------------

def test_remove_emojis():
    assert _utils._remove_emojis("🥕 2 carrots, chopped") == " 2 carrots, chopped"
    assert _utils._remove_emojis("🍅 3 tomatoes, diced") == " 3 tomatoes, diced"
    assert _utils._remove_emojis("🧄 4 cloves of garlic, minced") == " 4 cloves of garlic, minced"
    assert _utils._remove_emojis("🥬 1 head of lettuce, shredded") == " 1 head of lettuce, shredded"
    assert _utils._remove_emojis("🥒 2 cucumbers, sliced") == " 2 cucumbers, sliced"

def test_remove_emoji_only_string():
    assert _utils._remove_emojis("🥕") == ""

def test_remove_multiple_emojis_from_emoji_only_string():
    assert _utils._remove_emojis("🥕🍅🧄🥬🥒") == ""

def test_remove_multiple_emojis_from_string_with_mixed_chars():
    assert _utils._remove_emojis("🥕 2 carrots, 🍅🧄🥬🥒 chopped") == ' 2 carrots,  chopped' 

def test_remove_emojis_empty_string():
    assert _utils._remove_emojis("") == ""

def test_remove_emojis_none_string():
    assert _utils._remove_emojis(None) == ""

def test_remove_emojis_no_emojis():
    assert _utils._remove_emojis("2 carrots, chopped") == "2 carrots, chopped"
    assert _utils._remove_emojis("3 tomatoes, diced") == "3 tomatoes, diced"

# TODO: Parameterize this test using this list...
# TODO: probably need to make this a tuple with (emoji string, expected result) pairs
# emoji_ingredients = [
#     "🥕 2 carrots, chopped",
#     "🍅 3 tomatoes, diced",
#     "🧄 4 cloves of garlic, minced",
#     "🥬 1 head of lettuce, shredded",
#     "🥒 2 cucumbers, sliced",
#     "🍚 1 cup of rice",
#     "🥩 500g of beef, sliced",
#     "🍞 2 slices of bread",
#     "🧀 100g of cheese, grated",
#     "🍓 200g of strawberries",
#     "🍌 3 bananas",
#     "🍗 2 chicken breasts",
#     "🥛 1 liter of milk",
#     "🧈 100g of butter",
#     "🥔 5 potatoes, peeled and cubed",
#     "🍏 4 green apples, sliced",
#     "🍤 200g of shrimp",
#     "🍋 1 lemon, juiced",
#     "🥖 1 baguette, sliced",
#     "🍫 100g of dark chocolate, chopped"
# ]

# @pytest.mark.parametrize("ingredient", emoji_ingredients)
# def test_remove_emojis(ingredient):
    # pass