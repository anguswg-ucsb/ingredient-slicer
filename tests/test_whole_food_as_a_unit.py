# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils
from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Test if a unit like "whole fryer" can be used and detected correctly
# -------------------------------------------------------------------------------
# ing = "1 whole fryer, cut into 8 pieces"
# parsed = IngredientSlicer(ing).to_json()

# # TODO: need ability to calculate whole chickens and whole meats of varying names
def test_whole_fryer_chicken_ingredients_has_correct_units():

    ingredient_with_expected_units = [
        ("1 whole fryer, cut into 8 pieces", "whole fryer", "whole fryer"),
        ("2 whole fryers, cut into 8 pieces", "whole fryers", "whole fryer")
    ]

    for ing, expected_unit, expected_std_unit in ingredient_with_expected_units:
        # print(ing)
        # print(expected_unit)

        parsed = IngredientSlicer(ing).to_json()

        assert parsed['unit'] == expected_unit
        assert parsed['standardized_unit'] == expected_std_unit


def test_chicken_with_fryer_for_frying_is_not_whole_fryer_unit():
    
    ingredient_with_expected_units = [
        ("1 chicken (for frying), cut into 8 piece", "piece", "piece"),
        ("1 chicken (for frying), cut into 8 pieces", "pieces", "piece")
    ]

    for ing, expected_unit, expected_std_unit in ingredient_with_expected_units:
        # print(ing)
        # print(expected_unit)

        parsed = IngredientSlicer(ing).to_json()

        assert parsed['unit'] == expected_unit
        assert parsed['standardized_unit'] == expected_std_unit

# ing = "4-5 cups dark turkey meat, chopped"
# parsed = IngredientSlicer(ing).to_json()

ing = "1 cup walnut"
parsed = IngredientSlicer(ing).to_json()
parsed