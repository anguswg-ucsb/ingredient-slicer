# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# pattern_iter = IngredientSlicer.regex.NUMBERS_FOLLOWED_BY_PERCENTAGE.finditer(self.standard_ingredient)
# # pattern_iter = IngredientSlicer.regex.NUMBERS_FOLLOWED_BY_PERCENTAGE.finditer(ingredient)

# offset = 0

# for match in pattern_iter:
#     match_string    = match.group()

#     # Get the start and end of the match and the modified start and end positions given the offset
#     start, end = match.start(), match.end()
#     modified_start = start + offset
#     modified_end = end + offset

#     replacement_str = ""

#     # Construct the modified string with the replacement applied
#     self.standard_ingredient = self.standard_ingredient[:modified_start] + str(replacement_str) + self.standard_ingredient[modified_end:]
#     # ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]
    
#     # Update the offset for subsequent removals 
#     offset += len(str(replacement_str)) - (end - start)


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Simple standard form ingredients tests ----
# Standard form: "1 cup of sugar" (quantity, unit, ingredient)
# -------------------------------------------------------------------------------

def test_percentages_1():
    
    slicer = IngredientSlicer("1 cup of 2% milk")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'

    assert parsed["standardized_unit"] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'milk'
    assert parsed['size_modifiers'] == []


def test_percentages_2():
    slicer = IngredientSlicer("2% milk, 1 cup")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed["standardized_unit"] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'milk'
    assert parsed['size_modifiers'] == []

