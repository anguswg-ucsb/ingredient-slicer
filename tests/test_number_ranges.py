# pytest library
import pytest

import re

# from fractions import Fraction

from ingredient_slicer import IngredientSlicer, _utils

# -------------------------------------------------------------------------------
# ---- Simple number ranges (whole numbers/decimals to whole numbers/decimals) ----
# -------------------------------------------------------------------------------

def test_simple_number_range_1():
    slicer = IngredientSlicer("1-2 cups of sugar", debug = True)
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_simple_number_range_2():
    slicer = IngredientSlicer("1-3 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_simple_number_range_3():
    slicer = IngredientSlicer("1-1.5 cups of sugar")
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "1.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_simple_number_range_4():
    slicer = IngredientSlicer("4-1/2 cups of sugar", debug=True)
    # slicer.parse()
    parsed = slicer.to_json()

    assert parsed['quantity'] == "4.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- Fraction/Range tests ----
# -------------------------------------------------------------------------------
    
def test_fraction_range_as_quantity_1():
    parse = IngredientSlicer("1-1/2 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_fraction_range_as_quantity_2():
    parse = IngredientSlicer("1/2-1 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "0.75"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Unicode fraction/range tests ----
# -------------------------------------------------------------------------------
    
def test_unicode_fraction_range_1():
    parse = IngredientSlicer("1-1½cup of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '1.25 cup of sugar'
    assert parsed['quantity'] == "1.25"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_unicode_fraction_range_2():
    parse = IngredientSlicer("1½-2cup of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '1.75 cup of sugar'
    assert parsed['quantity'] == "1.75"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_unicode_fraction_range_3():
    parse = IngredientSlicer("1½-2½cup of sugar", debug=False)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '2 cup of sugar'
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True


# -------------------------------------------------------------------------------
# ---- Multinumber (space separated) tests ----
# -------------------------------------------------------------------------------

def test_multiple_multinumber_ranges_1():
    parse = IngredientSlicer("3 - 12 1/2 cups of sugar (optional)")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '7.75 cups of sugar'
    assert parsed['quantity'] == "7.75"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == False

def test_multiple_multinumber_ranges_2():
    parse = IngredientSlicer("3 - 12 1/2 cups of sugar (optional)")
    # parse.parse()
    parsed = parse.to_json()
    # 15.5/2
    assert parsed["standardized_ingredient"] == '7.75 cups of sugar'
    assert parsed['quantity'] == "7.75"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == False
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_multiple_multinumber_ranges_3():
    parse = IngredientSlicer("2 1/2 - 4  cups of sugar (optional)")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '3.25 cups of sugar'
    assert parsed['quantity'] == "3.25"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == False
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- Test averaging  ----
# -------------------------------------------------------------------------------

def test_average_from_two_whole_numbers_1():
    parse = IngredientSlicer("1-2 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '1.5 cups of sugar'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_average_from_two_whole_numbers_2():
    parse = IngredientSlicer("1-   8 tbsp of thickened cream")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '4.5 tbsp of thickened cream'
    assert parsed['quantity'] == "4.5"
    assert parsed['unit'] == 'tbsp'
    assert parsed['standardized_unit'] == 'tablespoon'
    
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['thickened']
    assert parsed['food'] == 'cream'
    assert parsed['size_modifiers'] == []

def test_average_from_two_whole_numbers_with_quantity_multiplier_1():
    parse = IngredientSlicer("15-20 oz large bananas, toasted (5)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '17.5 oz large bananas, toasted'
    assert parsed['quantity'] == "87.5"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == '17.5'
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['toasted']
    assert parsed['food'] == 'bananas'
    assert parsed['size_modifiers'] == ['large']

def test_average_from_two_whole_numbers_with_quantity_multiplier_2():
    parse = IngredientSlicer("1-2 cherries, no pits, (2 ounces each)", debug = False)
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed["standardized_ingredient"] == '1.5 cherries, no pits,'
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == "ounces"
    assert parsed['standardized_unit'] == "ounce"

    assert parsed['secondary_quantity'] == '1.5'
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == [] # TODO: should be ['no pits']
    assert parsed['food'] == 'cherries pits' # TODO: should be 'cherries'



# NOTE: this is a crazy scenario and lets hope this never really occurs in real life
def test_average_from_three_whole_numbers_1():
    parse = IngredientSlicer("1-3 or 4 cups of sugar", debug = False)
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '3 cups of sugar'
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# NOTE: this is a crazy scenario and lets hope this never really occurs in real life
def test_average_from_four_whole_numbers_1():
    parse = IngredientSlicer("1-3 or 10-20 cups of sugar", debug = False)
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '13 cups of sugar'
    assert parsed['quantity'] == "13"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

# -------------------------------------------------------------------------------
# ---- Test misleading number ranges ----
# -------------------------------------------------------------------------------

def test_misleading_number_ranges_1():
    parse = IngredientSlicer("1-1/2 tbsp of raw honey")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '1.5 tbsp of raw honey'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'tbsp'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'raw honey'
    assert parsed['size_modifiers'] == []

def test_misleading_number_ranges_2():
    parse = IngredientSlicer("1-1/2 to 3 tbsp, coconut oil")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '2.25 tbsp, coconut oil'
    assert parsed['quantity'] == "2.25"
    assert parsed['unit'] == 'tbsp'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'coconut oil'
    assert parsed['size_modifiers'] == []


def test_misleading_number_ranges_3():
    parse = IngredientSlicer("1-1/2 to 5-10 tbsp, coconut oil")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '6.625 tbsp, coconut oil'
    assert parsed['quantity'] == "6.625"
    assert parsed['unit'] == 'tbsp'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'coconut oil'
    assert parsed['size_modifiers'] == []

#############################################################################################
#####################################################################################################
#############################################################################################
#####################################################################################################

# def _find_and_replace_fraction_words(self) -> None:

#     ingredient = "2 quarter cups of milk, 3 eighths of a cup of sugar, 5-twelfths cup of flour 34-quarterseconds"

#     for key, pattern in IngredientSlicer.regex.NUMBER_WITH_FRACTION_WORD_MAP.items():
#         print(f"Key: {key}")
#         pattern_iter = pattern.finditer(ingredient)
#         offset = 0
#         for match in pattern_iter:
#             match_string = match.group()
#             start, end = match.start(), match.end()
#             modified_start = start + offset
#             modified_end = end + offset
#             match_string = match_string.replace("-", " ")
#             print(f"Match: {match_string}")
#             # match_string = match_string.replace("-", " ")
#             split_match = match_string.split(" ")
#             split_match = [i.strip() for i in split_match]

#             print(f"Split Match: {split_match}")

#             number_word = split_match[0]
#             fraction_word = split_match[1]

#             fraction_value, decimal = IngredientSlicer.regex.constants["FRACTION_WORDS"][fraction_word]

#             updated_value = str(float(number_word) * float(decimal))

#             ingredient = ingredient[:modified_start] + str(updated_value) + ingredient[modified_end:]
#             offset += len(str(updated_value)) - (end - start)

#     """ Find and replace fraction words with their corresponding numerical values in the parsed ingredient."""
#     pattern_iter = IngredientSlicer.regex.NUMBER_WITH_FRACTION_WORD_GROUPS.finditer(self.standard_ingredient)

#     offset = 0

#     for match in pattern_iter:
#         start, end = match.start(), match.end()

#         number_word   = match.group(1)
#         fraction_word = match.group(2)

#         fraction_value, decimal = IngredientSlicer.regex.constants["FRACTION_WORDS"][fraction_word]

#         # multiply first number in match by the decimal value of the fraction word (i.e. "2 third" -> 2 * 1/3)
#         updated_value = str(float(number_word) * float(decimal))

#         self.standard_ingredient = self.standard_ingredient[:match.start()] + str(updated_value) + self.standard_ingredient[match.end():]

#         offset += len(updated_value) - (end - start)
    
#     return 
# def _find_and_remove_percentages(self) -> None:
#         """
#         Find and remove percentages from the ingredient string.
#         """

#         # # Find percentages in the ingredient string
#         # percentage_matches = IngredientSlicer.regex.PERCENTAGE_PATTERN.findall(self.standard_ingredient)
#         # # Remove percentages from the ingredient string
#         # for match in percentage_matches:
#         #     self.standard_ingredient = self.standard_ingredient.replace(match, "")
#         ingredient = "1 cup of 2% heavy cream"
        
#         for key, pattern in IngredientSlicer.regex.PCT_REGEX_MAP.items():
#             print(f"Key: {key}")
#             pattern_iter = pattern.finditer(ingredient)
#             offset = 0
#             for match in pattern_iter:
#                 match_string = match.group()
#                 start, end = match.start(), match.end()
#                 modified_start = start + offset
#                 modified_end = end + offset

#                 replacement_str = ""

#                 # Construct the modified string with the replacement applied
#                 # self.standard_ingredient = self.standard_ingredient[:modified_start] + str(replacement_str) + self.standard_ingredient[modified_end:]
#                 ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]
#                 offset += len(str(replacement_str)) - (end - start)

#         pattern_iter = IngredientSlicer.regex.NUMBERS_FOLLOWED_BY_PERCENTAGE.finditer(self.standard_ingredient)
#         # pattern_iter = IngredientSlicer.regex.NUMBERS_FOLLOWED_BY_PERCENTAGE.finditer(ingredient)

#         offset = 0

#         for match in pattern_iter:
#             match_string    = match.group()

#             # Get the start and end of the match and the modified start and end positions given the offset
#             start, end = match.start(), match.end()
#             modified_start = start + offset
#             modified_end = end + offset

#             replacement_str = ""

#             # Construct the modified string with the replacement applied
#             self.standard_ingredient = self.standard_ingredient[:modified_start] + str(replacement_str) + self.standard_ingredient[modified_end:]
#             # ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]
            
#             # Update the offset for subsequent removals 
#             offset += len(str(replacement_str)) - (end - start)
        
#         return

# def _find_and_replace_numbers_separated_by_add_numbers(self) -> None:
#         """Find numbers separated by "and", "&", "plus", or "+" and replace the matched strings with their sum of the 2 number values
#         Examples:
#         "1 and 0.5" -> "1.5"
#         "1 & 0.5" -> "1.5"
#         "2 plus 0.66" -> "2.66"
#         "2 + 0.66" -> "2.66"
#         """

#         ingredient = "1 cup of 2% heavy cream"
        
#         for key, pattern in IngredientSlicer.regex.PCT_REGEX_MAP.items():
#             pattern_iter = pattern.finditer(ingredient)
#             for match in pattern_iter:
#                 match_string = match.group(0)
#                 start, end = match.start(), match.end()

#                 replacement_str = IngredientSlicer.regex.PCT_REGEX_MAP[key].sub("", match_string)
#                 ingredient = ingredient[:start] + str(replacement_str) + ingredient[end:]

#         add_pattern_iter = IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.finditer(self.standard_ingredient)

#         offset = 0

#         for match in add_pattern_iter:
#             match_string = match.group(0)
#             start, end = match.start(), match.end()

#             first_number = float(match.group(1).strip())
#             second_number = float(match.group(2).strip())

#             updated_value = f" {self._make_int_or_float_str(str(first_number + second_number))} "
#             self.standard_ingredient = self.standard_ingredient[:match.start()] + updated_value + self.standard_ingredient[match.end():]
#             offset += len(updated_value) - (end - start)
        
#         return

# #############################################################################################
# #####################################################################################################
# #############################################################################################
# #####################################################################################################

# def average_numbers_in_string(input_string):
#     while True:
#         start_index = -1
#         end_index = -1

#         # Find the start index of the next pair of numbers separated by hyphen
#         for i in range(len(input_string)):
#             if input_string[i].isdigit() or input_string[i] == '.':
#                 start_index = i
#                 break

#         if start_index == -1:  # No more matches found
#             break

#         # Find the end index of the next pair of numbers separated by hyphen
#         for j in range(start_index + 1, len(input_string)):
#             if not input_string[j].isdigit() and input_string[j] != '.':
#                 if input_string[j] == '-':
#                     end_index = j
#                     break
#                 else:
#                     start_index = -1  # Reset start_index if hyphen is not found
#                     break

#         if end_index == -1:  # No more matches found
#             break

#         # Extract the numbers and calculate their average
#         num1 = float(input_string[start_index:end_index].strip())
#         next_index = end_index + 1
#         while next_index < len(input_string) and input_string[next_index] == ' ':
#             next_index += 1
#         while next_index < len(input_string) and input_string[next_index].isdigit() is False and input_string[next_index] != '.':
#             next_index += 1
#         if next_index >= len(input_string):
#             break
#         start_index = next_index
#         end_index = start_index
#         while end_index < len(input_string) and (input_string[end_index].isdigit() or input_string[end_index] == '.'):
#             end_index += 1
#         num2 = float(input_string[start_index:end_index].strip())
#         avg = (num1 + num2) / 2

#         # Replace the matched substring with the average
#         input_string = input_string[:start_index] + str(avg) + input_string[end_index:]

#     return input_string

# # Test the algorithm
# input_string = "1-3.0 to 5-10 tbsp, coconut oil"
# output_string = average_numbers_in_string(input_string)
# print(output_string)  # Output: "2.0 to 7.5 tbsp, coconut oil"
# parse = IngredientSlicer('1.5 0.25 cups of sugar')
# # parse.parse()
# parsed = parse.to_json()
# parsed
# TODO: Maybe implement this which makes sure to always reduce any SPACE_SEP_NUMBERS to a single number
# TODO:  where possible and do this RECURSIVELY until there are no space separated numbers left. 
# TODO: I've got to see/think if this is a risky approach, just need to narrow down the base case of the recursion...
# ingredient = "1 1/2 1/4 cups of sugar"
# while regex_map.SPACE_SEP_NUMBERS.findall(ingredient):
#     print(f"Start ingredient: {ingredient}")
#     print(f"Continuing reducing multinumbers...")

#     parse = IngredientSlicer(ingredient)
#     # parse.parse()

#     ingredient = parsed["standardized_ingredient"]
#     print(f"--> End ingredient: {ingredient}")
#     print(f"\n")

# regex_map.print_matches(ingredient)
# regex_map.print_matches("1.75 cups of sugar")
    
# ingredient = "1.5  - 5 - 10 tbsp, coconut oil"

# IngredientSlicer.regex.print_matches(ingredient)

# def _avg_ranges(self) -> None:
#     """
#     Replace ranges of numbers with their average in the parsed ingredient.
#     Examples:
#     "1-2 oz" -> "1.5 oz"
#     "1 - 2 ft" -> "1.5 ft"
#     """

#     search_ranges = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY.search(self.standard_ingredient)
#     # search_ranges = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY_GROUPS.search(ingredient)

#     print(f"Starting while loop searching for ranges in ingredient: {self.standard_ingredient}") if self.debug else None
#     while search_ranges:

#         start, end = search_ranges.start(), search_ranges.end()
#         match_string = search_ranges.group()
        
#         left_range, right_range = match_string.split("-")
        
#         left_range = left_range.strip()
#         right_range = right_range.strip()

#         print(f"Match: {match_string}") if self.debug else None
#         print(f"left_range: {left_range}") if self.debug else None
#         print(f"right_range: {right_range}") if self.debug else None
#         print(f"Start: {start}") if self.debug else None
#         print(f"End: {end}") if self.debug else None

#         first_number  = float(_fraction_str_to_decimal(left_range).strip())
#         second_number = float(_fraction_str_to_decimal(right_range).strip())
        
#         range_average = f" {_make_int_or_float_str(str((first_number + second_number) / 2))} "
#         self.standard_ingredient = self.standard_ingredient[:start] + range_average + self.standard_ingredient[end:]

#         search_ranges = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY.search(self.standard_ingredient)
#         # search_ranges = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY_GROUPS.search(ingredient)
    
#     print(f"All ranges have been updated: {self.standard_ingredient}") if self.debug else None

#     self.standard_ingredient = self.standard_ingredient.strip()

#     return

# # ingredient = '4 - 0.5 cups of sugar'

# # IngredientSlicer.regex.print_matches(ingredient)
# # IngredientSlicer.regex.QUANTITY_DASH_QUANTITY.findall(ingredient)
# # IngredientSlicer.regex.QUANTITY_DASH_QUANTITY_GROUPS.findall(ingredient)

# def _fraction_str_to_decimal(fraction_str: str) -> float:
#         """
#         Convert a string representation of a fraction to its decimal equivalent.
#         """
#         # Split the fraction string into its numerator and denominator
#         split_fraction = [i.strip() for i in fraction_str.split("/")]
#         # print(f"Split Fraction: {split_fraction}") if self.debug else None

#         # If the fraction is a whole number, return the number
#         if len(split_fraction) == 1:
#             # print(f"---> Only one part: {split_fraction[0]}")

#             converted_number = _make_int_or_float_str(split_fraction[0])

#             # print(f"---> OLD Output: {round(float(split_fraction[0]), 3)}")
#             # print(f"---> NEW Output: {converted_number}")
#             return converted_number

#         numerator = int(split_fraction[0])
#         denominator = int(split_fraction[1])

#         # Convert the fraction to a decimal
#         # return round(float(Fraction(numerator, denominator)), 3)
#         return _make_int_or_float_str(str(round(float(Fraction(numerator, denominator)), 3)))


# def _make_int_or_float_str(number_str: str) -> str:
#     number = float(number_str.strip())  # Convert string to float
#     if number == int(number):  # Check if float is equal to its integer value
#         return str(int(number))  # Return integer value if it's a whole number
#     else:
#         return str(number)  # Return float if it's a decimal

# def _merge_misleading_ranges(ingredient: str ) -> str:
#     # ingredient = '4 - 0.5 cups of sugar, 1 - 4 cups of flour'
#     # ingredient = '1-1/2 cups of sugar, 1 - 4 cups of flour'
#     # ingredient = '1-1/2 cups of sugar'

#     # Find all the ranges in the ingredient
#     range_iter = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY_GROUPS.finditer(ingredient)

#     offset = 0

#     for match in range_iter:
#         match_string    = match.group()
#         start, end = match.start(), match.end()
#         modified_start = start + offset
#         modified_end = end + offset

#         print(f"Match: {match_string}")
#         print(f"Match 1: {match.group(1)}")
#         print(f"Match 2: {match.group(2)}")
#         print(f"Start: {start}")
#         print(f"End: {end}")

#         left_range = match.group(1).strip()
#         right_range = match.group(2).strip()
#         first_number  = float(_fraction_str_to_decimal(left_range).strip())
#         second_number = float(_fraction_str_to_decimal(right_range).strip())

#         # first_number = float(match.group(1).strip())
#         # second_number = float(match.group(2).strip())

#         # If the second number is less than the first number, then the range is misleading and the numbers should be merged
#         if second_number < first_number:
#             # print(f"Fixing misleading range: {match_string} with ")
#             second_number_is_fraction = second_number < 1
#             multiply_or_add_str = "add" if second_number_is_fraction else "multiply"

#             print(f"Second number is a fraction: {second_number_is_fraction}\n > {multiply_or_add_str} {first_number} and {second_number}")

#             updated_value = f" {_make_int_or_float_str(str(first_number + second_number))} " if second_number_is_fraction else f" {_make_int_or_float_str(str(first_number * second_number))} "
#             # updated_value = f" {_make_int_or_float_str(str(first_number + second_number))} "
#             print(f"Fixing misleading range: {match_string} with {updated_value}")
#             ingredient = ingredient[:modified_start] + updated_value + ingredient[modified_end:]
#             offset += len(updated_value) - (end - start)
#             print(f"Ingredient after updating: {ingredient}")
#         print()

#     ingredient = ingredient.strip()

#     return ingredient

# # ingredient = '4 - 0.5 cups of sugar, 1 - 4 cups of flour'
# # ingredient = '4 - 0.5 cups of sugar'
# ingredient = '4 - 0.5 cups of sugar, 1 - 4 cups of flour'

# _merge_misleading_ranges('4 - 0.5 cups of sugar, 1 - 4 cups of flour')
# _merge_misleading_ranges('4 - 0.5 cups of sugar, 1-0.5')
# _merge_misleading_ranges('4 - 0.5 cups of sugar, 1 - 4 cups of flour')
# _merge_misleading_ranges('1-1/2 cups of sugar')
# _merge_misleading_ranges('1 - 1/2 cups of sugar, 1 - 4 cups of flour')
# _merge_misleading_ranges('1-6 5-3 4/8 - 1/8 cups of 3-4 sugar, 8 -1/2 cups of flour')


# ingredient = "XF 1.25-3.0 to 5- 10 tbsp, coconut oil" # 'XF 2.125 to 7.5 tbsp, coconut oil'
# ingredient = '4 - 0.5 cups of sugar, 1-0.5' # '2.25 cups of sugar, 0.75'

# start = 0
# end = start

# while start < len(ingredient) and end < len(ingredient):
#     print(f"start: {start}")
#     print(f"end: {end}")
#     print(f"Char: {ingredient[start]}")
#     char = ingredient[start]

#     if char.isdigit() or char == '.':
#         end = start
#         left_num = []
#         while end < len(ingredient) and ingredient[end].isdigit():
#             print(f"end: {end}")
#             print(f"ingredient[end]: {ingredient[end]}")
#             left_num.append(ingredient[end])
#             end += 1
#             print(f"----" * 5)

#         # found a "." with a number after
#         if end < len(ingredient) and ingredient[end] == "." and ingredient[end+1].isdigit():
#             left_num.append(ingredient[end])
#             end += 1
#             while end < len(ingredient) and ingredient[end].isdigit():
#                 print(f"end: {end}")
#                 print(f"ingredient[end]: {ingredient[end]}")
#                 left_num.append(ingredient[end])
#                 end += 1
#                 print(f"----" * 5)

#         # got done with first number, now go through any whitespaces and hypens to arrive at next number
#         while end < len(ingredient) and ingredient[end] == " " or ingredient[end] == "-":
#             print(f"end: {end}")
#             print(f"ingredient[end]: {ingredient[end]}")
#             end += 1
#             print(f"----" * 5)

#         right_num = []
#         while end < len(ingredient) and ingredient[end].isdigit():
#             print(f"end: {end}")
#             print(f"ingredient[end]: {ingredient[end]}")
#             right_num.append(ingredient[end])
#             end += 1
#             print(f"----" * 5)

#         # found another "." with a number after
#         if end < len(ingredient) and ingredient[end] == "." and ingredient[end+1].isdigit():
#             right_num.append(ingredient[end])
#             end += 1
#             while end < len(ingredient) and ingredient[end].isdigit():
#                 print(f"end: {end}")
#                 print(f"ingredient[end]: {ingredient[end]}")
#                 right_num.append(ingredient[end])
#                 end += 1
#                 print(f"----" * 5)

#         # if we never got to another number, continue on 
#         if not right_num:
#             print(f"--> Skipping char: {char}")
#             print(f"----> Didn't end up finding another number after {''.join(left_num)}")
#             start += 1

#             continue
#         LEFT_RANGE = "".join(left_num)
#         RIGHT_RANGE = "".join(right_num)

#         UPDATED_VALUE = str((float(LEFT_RANGE) + float(RIGHT_RANGE))/2)

#         ingredient = ingredient[:start] + UPDATED_VALUE + ingredient[end:]

#         # calculate offset
#         start += len(UPDATED_VALUE) - len(LEFT_RANGE + RIGHT_RANGE)
#         print(f"Final ingredient: {ingredient}")
#         print(f"New offset: {start}")
#         print(f"-------" * 4)
#     else:
#         print(f"Skipping char: {char}")
#         start += 1
#     print()


# def average_numbers_in_ingredient(ingredient):
#     start = 0
#     end = start

#     while start < len(ingredient) and end < len(ingredient):
#         char = ingredient[start]

#         print(f"Start index: {start}, End index: {end}")
#         print(f"Current character: {char}")

#         if char.isdigit() or char == '.':
#             end = start
#             left_num = []
#             while end < len(ingredient) and ingredient[end].isdigit():
#                 left_num.append(ingredient[end])
#                 end += 1
#                 print(f"Left number so far: {''.join(left_num)}")

#             # found a "." with a number after
#             if end < len(ingredient) and ingredient[end] == "." and ingredient[end+1].isdigit():
#                 left_num.append(ingredient[end])
#                 end += 1
#                 while end < len(ingredient) and ingredient[end].isdigit():
#                     left_num.append(ingredient[end])
#                     end += 1
#                 print(f"Found a decimal point, updated left number: {''.join(left_num)}")

#             # got done with first number, now go through any whitespaces and hyphens to arrive at next number
#             while end < len(ingredient) and (ingredient[end] == " " or ingredient[end] == "-"):
#                 end += 1
#                 print(f"Skipping whitespace or hyphen, new end index: {end}")

#             right_num = []
#             while end < len(ingredient) and ingredient[end].isdigit():
#                 right_num.append(ingredient[end])
#                 end += 1
#                 print(f"Right number so far: {''.join(right_num)}")

#             # found another "." with a number after
#             if end < len(ingredient) and ingredient[end] == "." and ingredient[end+1].isdigit():
#                 right_num.append(ingredient[end])
#                 end += 1
#                 while end < len(ingredient) and ingredient[end].isdigit():
#                     right_num.append(ingredient[end])
#                     end += 1
#                 print(f"Found a decimal point, updated right number: {''.join(right_num)}")

#             # if we never got to another number, continue on 
#             if not right_num:
#                 start += 1
#                 print("Continuing to next character...")
#                 print(f"===" * 5)
#                 print()
#                 continue
            
#             LEFT_RANGE = "".join(left_num)
#             RIGHT_RANGE = "".join(right_num)

#             UPDATED_VALUE = str((float(LEFT_RANGE) + float(RIGHT_RANGE))/2)
#             print(f"Average of {LEFT_RANGE} and {RIGHT_RANGE} is: {UPDATED_VALUE}")

#             ingredient = ingredient[:start] + UPDATED_VALUE + ingredient[end:]

#             # calculate offset
#             start += len(UPDATED_VALUE) - len(LEFT_RANGE + RIGHT_RANGE)
#             print(f"Updated ingredient: {ingredient}")
#             print(f"New start index: {start}")
#             print()
#         else:
#             start += 1
#             print("Skipping character...")
#             print(f"===" * 5)
#             print()

#     return ingredient
# ingredient = "1-2 3-4 5-6"
# average_numbers_in_ingredient(ingredient)
# assert average_numbers_in_ingredient(ingredient) == "1.5 3.5 5-6" # actual output: '11223.34375'

# assert average_numbers_in_ingredient(ingredient) == "XF 2.125 to 7.5 tbsp, coconut oil"

# def average_numbers_in_ingredient(ingredient):
#     start = 0
#     end = start

#     while start < len(ingredient) and end < len(ingredient):
#         char = ingredient[start]

#         if char.isdigit() or char == '.':
#             end = start
#             left_num = []
#             while end < len(ingredient) and (ingredient[end].isdigit() or ingredient[end] == '.'):
#                 left_num.append(ingredient[end])
#                 end += 1

#             left_num_str = ''.join(left_num)
#             if left_num_str:
#                 if '.' in left_num_str:
#                     left_num_float = float(left_num_str)
#                 else:
#                     left_num_float = int(left_num_str)
#             else:
#                 left_num_float = 0  # Set to 0 if left_num_str is empty

#             # Skip whitespaces and hyphens
#             while end < len(ingredient) and (ingredient[end] == " " or ingredient[end] == "-"):
#                 end += 1

#             right_num = []
#             while end < len(ingredient) and (ingredient[end].isdigit() or ingredient[end] == '.'):
#                 right_num.append(ingredient[end])
#                 end += 1

#             right_num_str = ''.join(right_num)
#             if '.' in right_num_str:
#                 right_num_float = float(right_num_str)
#             else:
#                 right_num_float = int(right_num_str)

#             # Calculate the average
#             avg = (left_num_float + right_num_float) / 2

#             # Replace the numbers with the average
#             ingredient = ingredient[:start] + str(avg) + ingredient[end:]

#             # Update the start index
#             start += len(str(avg))

#         else:
#             start += 1

#     return ingredient

# # Test the function
# ingredient = "1-2 3-4 5-6"
# print(average_numbers_in_ingredient(ingredient))  # Output: "1.5 3.5 5-6"

# sample_strings = [
#     "1-2 3-4 5-6",             # Expected output: "1.5 3.5 5-6"
#     "4 - 0.5 cups of sugar, 1-0.5",  # Expected output: "2.25 cups of sugar, 0.75"
#     "XF 1.25-3.0 to 5- 10 tbsp, coconut oil",  # Expected output: "XF 2.125 to 7.5 tbsp, coconut oil"
#     "1.5  - 5 - 10 tbsp, coconut oil",  # Expected output: "2.25 to 7.5 tbsp, coconut oil"
#     "1-1 2-2 3-3 4-4",         # Expected output: "1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5"
#     "1.0 - 1.5 - 2.0 - 2.5",    # Expected output: "1.25 1.75 2.25"
#     "1.5 - 2.5 - 3.5",          # Expected output: "2.0 3.0"
#     "1-2-3",                    # Expected output: "1.5-3"
#     "1.5-3.0",                  # Expected output: "2.25"
#     "1-2-3-4-5-6",              # Expected output: "1.5-3.5-5.5"
#     "1-1-1-1-1-1",              # Expected output: "1"
# ]

# for sample in sample_strings:
#     print(f"Input: {sample}")
#     print(f"Output: {average_numbers_in_ingredient(sample)}")
#     print()


# def average_numbers_in_ingredient(ingredient):
#     start = 0
#     end = start

#     while start < len(ingredient) and end < len(ingredient):
#         char = ingredient[start]

#         if char.isdigit() or char == '.':
#             print("Processing digit or dot")
#             end = start
#             left_num = []
#             while end < len(ingredient) and (ingredient[end].isdigit() or ingredient[end] == '.'):
#                 left_num.append(ingredient[end])
#                 end += 1

#             left_num_str = ''.join(left_num)
#             print("Left num string:", left_num_str)
#             if left_num_str:
#                 if '.' in left_num_str:
#                     left_num_float = float(left_num_str)
#                 else:
#                     left_num_float = int(left_num_str)
#                 print("Left num:", left_num_float)
#             else:
#                 print("Empty left_num_str")
#                 left_num_float = 0  # Set to 0 if left_num_str is empty

#             # Skip whitespaces and hyphens
#             while end < len(ingredient) and (ingredient[end] == " " or ingredient[end] == "-"):
#                 print("Skipping whitespace or hyphen")
#                 end += 1

#             right_num = []
#             while end < len(ingredient) and (ingredient[end].isdigit() or ingredient[end] == '.'):
#                 right_num.append(ingredient[end])
#                 end += 1

#             right_num_str = ''.join(right_num)
#             print("Right num string:", right_num_str)
#             if '.' in right_num_str:
#                 right_num_float = float(right_num_str)
#             else:
#                 right_num_float = int(right_num_str)
#             print("Right num:", right_num_float)

#             # Calculate the average
#             avg = (left_num_float + right_num_float) / 2
#             print("Average:", avg)

#             # Replace the numbers with the average
#             ingredient = ingredient[:start] + str(avg) + ingredient[end:]
#             print("Updated ingredient:", ingredient)

#             # Update the start index
#             start += len(str(avg))
#             print("New start index:", start)

#         else:
#             print("Skipping non-digit and non-dot")
#             start += 1

#         print("----" * 5)

#     return ingredient

# # Test the function
# ingredient = "1.5  - 5 - 10 tbsp, coconut oil"
# print(average_numbers_in_ingredient(ingredient))

# # Test the function
# ingredient = "1.5  - 5 - 10 tbsp, coconut oil"
# print(average_numbers_in_ingredient(ingredient))

# def average_numbers_in_ingredient(ingredient):
#     stack = []
#     i = 0

#     while i < len(ingredient):
#         char = ingredient[i]

#         if char.isdigit() or char == '.':
#             # Extract the number
#             num = []
#             while i < len(ingredient) and (ingredient[i].isdigit() or ingredient[i] == '.'):
#                 num.append(ingredient[i])
#                 i += 1
#             stack.append(''.join(num))

#         elif char == '-':
#             # Check if it's a range separator
#             if i + 1 < len(ingredient) and ingredient[i + 1] == ' ':
#                 # Pop the last number from the stack and compute average with the next number
#                 if len(stack) >= 2:
#                     right_num = float(stack.pop())
#                     left_num = float(stack.pop())
#                     avg = (left_num + right_num) / 2
#                     stack.append(str(avg))
#                 else:
#                     # Handle case when there's not enough numbers on the stack
#                     stack.append(char)
#             else:
#                 stack.append(char)

#             i += 1

#         elif char == ' ':
#             # Ignore whitespace
#             i += 1

#         else:
#             # Add non-numeric characters directly to the stack
#             stack.append(char)
#             i += 1

#     return ''.join(stack)

# # Test the function
# ingredient = "1.5  - 5 - 10 tbsp, coconut oil"
# print(average_numbers_in_ingredient(ingredient))