# pytest library
import pytest

import re
# from fractions import Fraction
from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Test IngredientSlicer: Merge space separated numbers ----
# -------------------------------------------------------------------------------

def test_merge_numbers_1():
    parse = IngredientSlicer("1 2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

# def test_merge_numbers_2():
#     parse = IngredientSlicer("1 2/3 and 2 1/2 cups of flour")
#     # parse.parse()
#     parsed = parse.to_json()
#     assert parsed['quantity'] == "4.167"
#     assert parsed['unit'] == 'cups'
#     assert parsed['standardized_unit'] == "cup"

#     assert parsed['secondary_quantity'] == None
#     assert parsed['secondary_unit'] == None
#     assert parsed['standardized_secondary_unit'] == None

#     assert parsed['is_required'] == True
#     assert parsed['prep'] == []
#     assert parsed['food'] == 'flour'
#     assert parsed['size_modifiers'] == []

def test_merge_numbers_3():
    parse = IngredientSlicer("1 2/3 or 2 1/2 cups of flour", debug=True)
    # parse.parse()
    parsed = parse.to_json()

    # (1.667 + 2.5)

    assert parsed['quantity'] == "2.0835"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fractions_with_extra_spaces_1():
    parse = IngredientSlicer("1 2 / 3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fractions_range_with_extra_spaces_1():
    parse = IngredientSlicer("1 2 / 3 - 2 1 / 2 cups of flour")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2.0835"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_spaces_1():
    parse = IngredientSlicer("1  2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_trailing_spaces_1():
    parse = IngredientSlicer("1 2/3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_and_trailing_spaces_1():
    parse = IngredientSlicer("1  2/3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_merge_mixed_fraction_with_multiple_leading_and_trailing_spaces_2():
    parse = IngredientSlicer("1  2 /3  cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.667"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_decimal_then_fraction_1():
    parse = IngredientSlicer("1.5 2/3 cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "2.167"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_decimal_then_mixed_fraction_1(): 
    parse = IngredientSlicer("1 2 2/3 cups of flour") # TODO: this is a bug and should really result in 2.667 cups
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

# ingredient = '1 0.667 or 2 0.5 cups of flour'
# # ingredient = '1 0.667 - 2 0.5 cups of flour'
# # ingredient = '1 0.667 - 2 0.5 cups of flour'

# IngredientSlicer.regex.print_matches(ingredient)
# def _replace_to_or_with_hyphen(match):
#     # Replace "and" and "&" with hyphens
#     return match.replace("to", "-").replace("or", "-")

# def _make_int_or_float_str(number_str: str) -> str:
#     number = float(number_str.strip())  # Convert string to float
#     if number == int(number):  # Check if float is equal to its integer value
#         return str(int(number))  # Return integer value if it's a whole number
#     else:
#         return str(number)  # Return float if it's a decimal
        
# def _fraction_str_to_decimal(fraction_str: str) -> float:
#     """
#     Convert a string representation of a fraction to its decimal equivalent.
#     """
#     # Split the fraction string into its numerator and denominator
#     split_fraction = [i.strip() for i in fraction_str.split("/")]
#     # print(f"Split Fraction: {split_fraction}") if self.debug else None

#     # If the fraction is a whole number, return the number
#     if len(split_fraction) == 1:
#         # print(f"---> Only one part: {split_fraction[0]}")

#         converted_number = _make_int_or_float_str(split_fraction[0])

#         # print(f"---> OLD Output: {round(float(split_fraction[0]), 3)}")
#         # print(f"---> NEW Output: {converted_number}")
#         return converted_number

#     numerator = int(split_fraction[0])
#     denominator = int(split_fraction[1])

#     # Convert the fraction to a decimal
#     # return round(float(Fraction(numerator, denominator)), 3)
#     return _make_int_or_float_str(str(round(float(Fraction(numerator, denominator)), 3)))

# def _update_ranges(ingredient, pattern, replacement_function=None):
#     """Update the ranges in the ingredient string with the updated ranges
#     Args:
#         ingredient (str): The ingredient string to update
#         pattern (re.Pattern): The pattern to use to find the ranges
#         replacement_function (function, optional): A function to use to replace the matched ranges. Defaults to None.
#     Returns:
#         str: The updated ingredient string
#     """
#     ingredient = '1 0.667 or 2 0.5 cups of flour'
#     ingredient = '2 or 3 cups of flour'
#     # ingredient = '1 0.667 - 2 0.5 cups of flour'
    
#     # ingredient = ingredient
#     pattern = IngredientSlicer.regex.QUANTITY_TO_OR_QUANTITY

#     matches = pattern.findall(ingredient)
    
#     # matched_ranges = [match.split("-") for match in matches]
#     # replacement_function = _replace_to_or_with_hyphen

#     if replacement_function:
#         # print(f"Replacement Function given")
#         matched_ranges = [replacement_function(match).split("-") for match in matches]
#     else:
#         # print(f"No Replacement Function given")
#         matched_ranges = [match.split("-") for match in matches]

#     # print(f"Matched Ranges: \n > {matched_ranges}") if self.debug else None
#     [match for match in matched_ranges]
#     updated_ranges = [" - ".join([str(_fraction_str_to_decimal(i)) for i in match if i]) for match in matched_ranges]
#     # updated_ranges = [" - ".join([str(int(i)) for i in match if i]) for match in matched_ranges]
    
#     # Create a dictionary to map the matched ranges to the updated ranges
#     ranges_map = dict(zip(matches, updated_ranges))

#     # Replace the ranges in the original string with the updated ranges
#     for original_range, updated_range in ranges_map.items():
#         # print(f"Original Range: {original_range}")
#         # print(f"Updated Range: {updated_range}")
#         # if replacement_function:
#         #     print(f"Replacement Function given")
#         #     updated_range = replacement_function(updated_range)
#         ingredient = ingredient.replace(original_range, updated_range)
#         print("\n")

#     return ingredient

# def _find_and_update_ranges(ingredient, pattern, replacement_function=None):
#     """Update the ranges in the ingredient string with the updated ranges
#     Args:
#         ingredient (str): The ingredient string to update
#         pattern (re.Pattern): The pattern to use to find the ranges
#         replacement_function (function, optional): A function to use to replace the matched ranges. Defaults to None.
#     Returns:
#         str: The updated ingredient string
#     """
#     ingredient = '1 0.667 or 2 0.5 cups of flour'
#     # ingredient = '2 or 3 cups of flour'
#     # ingredient = '1 0.667 - 2 0.5 cups of flour'
    
#     # ingredient = ingredient
#     pattern = IngredientSlicer.regex.QUANTITY_TO_OR_QUANTITY

#     matched_ranges_iter = pattern.finditer(ingredient)
    
#     offset = 0
#     for match in matched_ranges_iter:
#         match_string    = match.group()

#         # Get the start and end of the match and the modified start and end positions given the offset
#         start, end = match.start(), match.end()
#         modified_start = start + offset
#         modified_end = end + offset

#         print(f"Match: {match_string}")
#         print(f"Start: {start}")
#         print(f"End: {end}")
#         print()
#         # replacement_str = ""

#         # # Construct the modified string with the replacement applied
#         # self.standard_ingredient = self.standard_ingredient[:modified_start] + str(replacement_str) + self.standard_ingredient[modified_end:]
#         # # ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]
        
#         # # Update the offset for subsequent removals 
#         # offset += len(str(replacement_str)) - (end - start)


#     for match in matched_ranges_iter:
#         start, end = match.span()
#         start += offset
#         end += offset
#         match_str = match.group()
#         updated_match_str = replacement_function(match_str) if replacement_function else match_str
#         ingredient = ingredient[:start] + updated_match_str + ingredient[end:]
#         offset += len(updated_match_str) - len(match_str)

#     # matched_ranges = [match.split("-") for match in matches]
#     # replacement_function = _replace_to_or_with_hyphen

#     if replacement_function:
#         # print(f"Replacement Function given")
#         matched_ranges = [replacement_function(match).split("-") for match in matches]
#     else:
#         # print(f"No Replacement Function given")
#         matched_ranges = [match.split("-") for match in matches]

#     # print(f"Matched Ranges: \n > {matched_ranges}") if self.debug else None
#     [match for match in matched_ranges]
#     updated_ranges = [" - ".join([str(_fraction_str_to_decimal(i)) for i in match if i]) for match in matched_ranges]
#     # updated_ranges = [" - ".join([str(int(i)) for i in match if i]) for match in matched_ranges]
    
#     # Create a dictionary to map the matched ranges to the updated ranges
#     ranges_map = dict(zip(matches, updated_ranges))

#     # Replace the ranges in the original string with the updated ranges
#     for original_range, updated_range in ranges_map.items():
#         # print(f"Original Range: {original_range}")
#         # print(f"Updated Range: {updated_range}")
#         # if replacement_function:
#         #     print(f"Replacement Function given")
#         #     updated_range = replacement_function(updated_range)
#         ingredient = ingredient.replace(original_range, updated_range)
#         print("\n")

#     return ingredient