# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Test IngredientSlicer: Fraction words tests ----
# -------------------------------------------------------------------------------

def test_fraction_words_1():
    parse = IngredientSlicer("two thirds a cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "0.666"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []

def test_fraction_words_2():
    parse = IngredientSlicer("two and two thirds cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2.666"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []


def test_fraction_words_3():
    parse = IngredientSlicer("two and two thirds or 1 and 3 quarters cups of flour", debug = False)
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "2.208"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'flour'
    assert parsed['size_modifiers'] == []
######################
# IngredientSlicer.regex.PREP_WORDS_PATTERN.findall("3 tablespoons unsalted butter, softened at room temperature")
# IngredientSlicer.regex.print_matches("3 tablespoons unsalted butter, softened at room temperature")
# IngredientSlicer.regex.constants["PREP_WORDS"]

# ingredient = "1 and 2thirds cups of milk"
# # parser = IngredientSlicer(ingredient)
# # parser.parse()
# # parsed = parser.to_json()

# # IngredientSlicer.regex.constants["FRACTION_WORDS"]

# IngredientSlicer.regex.print_matches(ingredient)
    
##############################################################################################################
##############################################################################################################
    
# # ingredient = "3 and 2thirds cups of milk or 1 and 3 quarters tbs of lemon juice"
# ingredient = "I love a 3 and 2thirds cups of milk"
# # ingredient = " 2thirds cups of milk"
# # ingredient = "a 2thirds cups of milk"
# offset = 0

# # matches = IngredientSlicer.regex.NUMBER_WITH_FRACTION_WORD.findall(ingredient)

# pattern_iter = IngredientSlicer.regex.NUMBER_WITH_FRACTION_WORD_GROUPS.finditer(ingredient)

# for match in pattern_iter:
#     print(match)
#     print(match.start())
#     print(match.end())
#     print(match.group())
#     print(f"group 0: {match.group(0)}")
#     print(f"group 1: {match.group(1)}")
#     print(f"group 2: {match.group(2)}")
#     print(ingredient[match.start():match.end()])
#     print(ingredient[:match.start()])

#     start, end = match.start(), match.end()
#     # IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS.findall
#     # split_by_fraction_word = ingredient.split(match.group(0))
#     # if not split_by_fraction_word[0].strip():
#     #     print(f"No strings before fraction word")
#     # strings_before_fraction_word = split_by_fraction_word[0].strip().split(" ") 
#     # more_than_one_word = len(strings_before_fraction_word) > 1
#     # if more_than_one_word:
#     #     maybe_and = strings_before_fraction_word[-1]
#     #     maybe_number = strings_before_fraction_word[-2]
#     #     is_and_word = maybe_and == "and" or maybe_and == "&" or maybe_and == "+" or maybe_and == "plus"
#     #     is_number   = maybe_number.isdigit()

#     number_word   = match.group(1)
#     fraction_word = match.group(2)

#     fraction_value, decimal = IngredientSlicer.regex.constants["FRACTION_WORDS"][fraction_word]

#     updated_value = f" {str(float(number_word) * float(decimal))} "
#     # updated_value = f" {updated_value} "

#     ingredient = ingredient[:match.start()] + updated_value + ingredient[match.end():]

#     offset += len(updated_value) - (end - start)

#     print()

# ingredient

# # add_pattern_iter = IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS.finditer(ingredient)
# add_pattern_iter = IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.finditer(ingredient)
# # IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.findall(ingredient)
# # IngredientSlicer.regex.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.findall("I love a 3 plus  0.666  cups of milk")
# offset = 0

# for match in add_pattern_iter:
#     match_string = match.group(0)
    
#     print(match)
#     print(match.start())
#     print(match.end())
#     print(f"Match string: {match_string}")
#     print(f"group 0: {match.group(0)}")
#     print(f"group 1: {match.group(1)}")
#     print(f"group 2: {match.group(2)}")
#     print(ingredient[match.start():match.end()])
#     print(ingredient[:match.start()])
#     start, end = match.start(), match.end()

#     first_number = float(match.group(1).strip())
#     second_number = float(match.group(2).strip())

#     updated_value = f" {str(first_number + second_number)} "
#     ingredient = ingredient[:match.start()] + updated_value + ingredient[match.end():]
#     offset += len(updated_value) - (end - start)
#     print()

# IngredientSlicer.regex.__dict__.items()
# IngredientSlicer.regex.print_matches(ingredient)
# sorted_keys = sorted(IngredientSlicer.regex.__dict__.keys(), key=lambda x: x[0])
# IngredientSlicer.regex.__dict__["X_SEP_NUMBERS"]
# for key in sorted_keys:
#     print(f"{key}: {IngredientSlicer.regex.__dict__[key]}")

# sorted_attrs = sorted(IngredientSlicer.regex.__dict__.items(), key=lambda x: x[0])
# # regex for matching numbers/fractions/decimals separated by "and" or "&" (e.g. "1/2 and 3/4", "1/2 & 3/4")
# NUMBERS_SEPARATED_BY_ADD_SYMBOLS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&|\+|plus)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')

# # AND_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')

# NUMBERS_SEPARATED_BY_ADD_SYMBOLS.findall(ingredient)
# NUMBERS_SEPARATED_BY_ADD_SYMBOLS.findall('I love a 3 plus  0.666  cups of milk')


# NUMBERS_THEN_DECIMAL_SEPARATED_BY_ADDITION = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&|\+|plus)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')
# NUMBERS_THEN_DECIMAL_SEPARATED_BY_ADDITION.findall('I love a 3 plus 2 cups of milk')

# def _find_and_replace_fraction_words(self, ingredient: str) -> str:
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