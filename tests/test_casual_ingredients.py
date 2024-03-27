# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Casual units tests ----
# -------------------------------------------------------------------------------

def test_casual_units_no_quantities_1():

    slicer = IngredientSlicer("a pinch of salt")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_1():
    
    slicer = IngredientSlicer("5 pinches of salt")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "5"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_2():
      
    slicer = IngredientSlicer("a couple of pinches of salt")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_units_with_number_quantity_3():
        
    slicer = IngredientSlicer("a few pinches of salt")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_quantities_with_dozen_1():
        
    slicer = IngredientSlicer("a couple dozen eggs")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "24"
    assert parsed['unit'] == None
    assert parsed['standardized_unit'] == None
    assert parsed['food'] == 'eggs'
    assert parsed['is_required'] == True

def test_casual_quantities_with_dozen_2():

    slicer = IngredientSlicer("a few dozen eggs")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "36"
    assert parsed['unit'] == None
    assert parsed['standardized_unit'] == None
    assert parsed['food'] == 'eggs'
    assert parsed['is_required'] == True

def test_casual_quantities_at_end_of_ingredient():
    
    slicer = IngredientSlicer("large watermelon, or a couple of diced watermelons")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == None
    assert parsed['standardized_unit'] == None
    assert parsed['food'] == 'watermelon watermelons' # TODO: this is a bug, should be just watermelon
    assert parsed['is_required'] == True

# TODO: this seems like it should just be 3, options are to remove "few" from the CASUAL_QUANTITIES dictionary
# TODO:  or to deal with parenthesis that have an approximate quantity in them WITHOUT a unit (e.g. "(about 3)"
# TODO: For not this test will stay put...
def test_casual_quantities_in_parenthesis_1():

    slicer = IngredientSlicer("a few (about 3) pinches of salt")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "9"
    assert parsed['unit'] == 'pinches'
    assert parsed['standardized_unit'] == 'pinch'
    assert parsed['food'] == 'salt'
    assert parsed['is_required'] == True

def test_casual_quantities_in_parenthesis_2():

    slicer = IngredientSlicer("milk (a couple of cups) ")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == "cups"
    assert parsed['standardized_unit'] == "cup"
    assert parsed['food'] == 'milk'
    assert parsed['is_required'] == True


# input_ingredient = "a couple of pinches of salt"
# slicer = IngredientSlicer(input_ingredient)
# # slicer.parse()
# parsed = slicer.to_json()

# regex = IngredientTools()

# regex.print_matches(input_ingredient)

# def _find_and_replace_casual_quantities(self):
#     """
#     Find and replace matches of CASUAL_QUANTITIES_PATTERN with the key from the CASUAL_QUANTITIES dictionary
#     """

#     offset = 0
#     pattern_iter = regex.CASUAL_QUANTITIES_PATTERN.finditer(input_ingredient)

#     for match in pattern_iter:
#         match_string    = match.group()

#         # Get the start and end of the match and the modified start and end positions given the offset
#         start, end = match.start(), match.end()
#         modified_start = start + offset
#         modified_end = end + offset

#         replacement_str = regex.constants["CASUAL_QUANTITIES"][match_string] 

#         # Construct the modified string with the replacement applied
#         self.standard_ingredient = self.standard_ingredient[:modified_start] + str(replacement_str) + self.standard_ingredient[modified_end:]
#         # input_ingredient = input_ingredient[:modified_start] + str(replacement_str) + input_ingredient[modified_end:]

#         # Update the offset for subsequent removals # TODO: this is always 0 because we're removing the match, probably just remove...
#         offset += len(str(replacement_str)) - (end - start)
#         # print(f"""
#         # Match string: {match_string}
#         # -> Match: {match_string} at positions {start}-{end}
#         # --> Modified start/end match positions: {modified_start}-{modified_end}
#         # ---> Modified string: {string}""")

# # find and replace matches of CASUAL_QUANTITIES_PATTERN with the key from the CASUAL_QUANTITIES dictionary
# for match in regex.CASUAL_QUANTITIES_PATTERN.finditer(input_ingredient):
#     print(match.group(0))

    
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))
