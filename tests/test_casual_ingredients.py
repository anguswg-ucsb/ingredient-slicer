# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns, IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Casual units tests ----
# -------------------------------------------------------------------------------

def test_casual_units_no_quantities_1():

    parse1 = IngredientSlicer("a pinch of salt")
    parse1.parse()
    parsed_ingredient = parse1.to_json()
    assert parsed_ingredient['quantity'] == "1"
    assert parsed_ingredient['unit'] == 'pinch'
    assert parsed_ingredient['food'] == 'salt'
    assert parsed_ingredient['is_required'] == True

def test_casual_units_with_number_quantity_1():
    
        parse1 = IngredientSlicer("5 pinches of salt")
        parse1.parse()
        parsed_ingredient = parse1.to_json()
        assert parsed_ingredient['quantity'] == "5"
        assert parsed_ingredient['unit'] == 'pinches'
        assert parsed_ingredient['standardized_unit'] == 'pinch'
        assert parsed_ingredient['food'] == 'salt'
        assert parsed_ingredient['is_required'] == True

# def test_casual_units_with_number_quantity_2():
      
#         parse1 = IngredientSlicer("a couple of pinches of salt")
#         parse1.parse()
#         parsed_ingredient = parse1.to_json()
#         assert parsed_ingredient['quantity'] == "2"
#         assert parsed_ingredient['unit'] == 'pinches'
#         assert parsed_ingredient['standardized_unit'] == 'pinch'
#         assert parsed_ingredient['food'] == 'salt'
#         assert parsed_ingredient['is_required'] == True

# def test_casual_units_with_number_quantity_3():
        
#         parse1 = IngredientSlicer("a few pinches of salt")
#         parse1.parse()
#         parsed_ingredient = parse1.to_json()
#         assert parsed_ingredient['quantity'] == "3"
#         assert parsed_ingredient['unit'] == 'pinches'
#         assert parsed_ingredient['standardized_unit'] == 'pinch'
#         assert parsed_ingredient['food'] == 'salt'
#         assert parsed_ingredient['is_required'] == True

# input_ingredient = "a couple of pinches of salt"
# parse1 = IngredientSlicer(input_ingredient)
# parse1.parse()
# parsed_ingredient = parse1.to_json()

# regex = IngredientRegexPatterns()

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
