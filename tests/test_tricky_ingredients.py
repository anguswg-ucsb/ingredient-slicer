# # pytest library
# import pytest

# import re

# from ingredient_slicer import IngredientSlicer

# # -------------------------------------------------------------------------------
# # ---- Startiung a file to address ingredients in this Github Issue: ----
# # Github Issue: https://github.com/anguswg-ucsb/ingredient-slicer/issues/6
# # -------------------------------------------------------------------------------

# tricky_ingredients = [
#     " ▢ 1 cup warm water (105 degrees f), warm water, 105, cup, cup,",
#     "1 10-ounce bag frozen cherries, cherries, 10, ounce, ounce,"
# ]

# @pytest.mark.parametrize("ingredient", tricky_ingredients)
# def test_tricky_ingredients(ingredient):
#     parse = IngredientSlicer(ingredient)
#     parsed = parse.to_json()
