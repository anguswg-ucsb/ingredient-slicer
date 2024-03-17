# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns, IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Simple standard form ingredients tests ----
# Standard form: "1 cup of sugar" (quantity, unit, ingredient)
# -------------------------------------------------------------------------------

def test_standard_formatted_ingredients():

    parse1 = IngredientSlicer("2 tablespoons of sugar")
    parse1.parse()
    parsed_ingredient = parse1.to_json()
    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == 'tablespoons'
    assert parsed_ingredient['is_required'] == True

    parse2 = IngredientSlicer("1/2 cup of sugar")
    parse2.parse()
    parsed_ingredient = parse2.to_json()
    assert parsed_ingredient['quantity'] == "0.5"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

    parse3 = IngredientSlicer("1 1/2 cups of sugar")
    parse3.parse()
    parsed_ingredient = parse3.to_json()
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_quantity_and_unit_1():
    parse = IngredientSlicer("3 pounds of beef")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "3"
    assert parsed_ingredient['unit'] == 'pounds'
    assert parsed_ingredient['is_required'] == True

def test_quantity_and_unit_2():
    parse = IngredientSlicer("14 lbs of lettuce")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "14"
    assert parsed_ingredient['unit'] == 'lbs'
    assert parsed_ingredient['standardized_unit'] == 'pound'
    assert parsed_ingredient['is_required'] == True

    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Multinumber (space separated) tests ----
# -------------------------------------------------------------------------------

def test_simple_multinumber_1():
    parse = IngredientSlicer("1 1/2 cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_simple_multinumber_2():
    parse = IngredientSlicer("1 1/2  cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_simple_multinumber_3():
    parse = IngredientSlicer("1 1/2 1/4 cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '1.5 0.25 cups of sugar'
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_multiple_multinumber_1():
    parse = IngredientSlicer("1 1/2 1/4 1/8 cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '1.5 0.375 cups of sugar'
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_multiple_multinumber_2():
    parse = IngredientSlicer("1 1/2 1/4 1/8 1/16 cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '1.5 0.375 0.062 cups of sugar'
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_multiple_multinumber_3():
    parse = IngredientSlicer("1.5 2/3 cups of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '2.167 cups of sugar'
    assert parsed_ingredient['quantity'] == "2.167"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_multiple_multinumber_3():
    parse = IngredientSlicer("3 12 cups of sugar (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '36 cups of sugar (optional)'
    assert parsed_ingredient['quantity'] == "36"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == False

# -------------------------------------------------------------------------------
# ---- Multinumber (space separated) tests ----
# -------------------------------------------------------------------------------

def test_multiple_multinumber_ranges_1():
    parse = IngredientSlicer("3 - 12 1/2 cups of sugar (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '7.75 cups of sugar (optional)'
    assert parsed_ingredient['quantity'] == "7.75"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == False

def test_multiple_multinumber_ranges_2():
    parse = IngredientSlicer("3 - 12 1/2 1/4 cups of sugar (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '7.75 0.25 cups of sugar (optional)'
    assert parsed_ingredient['quantity'] == "7.75"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == False

def test_multiple_multinumber_ranges_3():
    parse = IngredientSlicer("2 1/2 - 4  cups of sugar (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '3.25  cups of sugar (optional)'
    assert parsed_ingredient['quantity'] == "3.25"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['standardized_unit'] == 'cup'
    assert parsed_ingredient['is_required'] == False

# parse = IngredientSlicer('1.5 0.25 cups of sugar')
# parse.parse()
# parsed_ingredient = parse.to_json()
# parsed_ingredient
# TODO: Maybe implement this which makes sure to always reduce any SPACE_SEP_NUMBERS to a single number
# TODO:  where possible and do this RECURSIVELY until there are no space separated numbers left. 
# TODO: I've got to see/think if this is a risky approach, just need to narrow down the base case of the recursion...
# ingredient = "1 1/2 1/4 cups of sugar"
# while regex_map.SPACE_SEP_NUMBERS.findall(ingredient):
#     print(f"Start ingredient: {ingredient}")
#     print(f"Continuing reducing multinumbers...")

#     parse = IngredientSlicer(ingredient)
#     parse.parse()

#     ingredient = parsed_ingredient["standardized_ingredient"]
#     print(f"--> End ingredient: {ingredient}")
#     print(f"\n")

# regex_map.print_matches(ingredient)
# regex_map.print_matches("1.75 cups of sugar")

# -------------------------------------------------------------------------------
# ---- Badly designed ingredients tests ----
# -------------------------------------------------------------------------------
    
def test_quantity_only():
    parse = IngredientSlicer("2")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == None
    assert parsed_ingredient['is_required'] == True

def test_no_quantity():
    parse = IngredientSlicer("sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == None
    assert parsed_ingredient['unit'] == None
    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Fraction processing tests ----
# -------------------------------------------------------------------------------
    
def test_fraction_as_quantity():
    parse = IngredientSlicer("1/4 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.25"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_fraction_as_quantity_2():
    parse = IngredientSlicer("1 1/4 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "1.25"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Fraction/Range tests ----
# -------------------------------------------------------------------------------
    
def test_fraction_range_as_quantity_1():
    parse = IngredientSlicer("1-1/2 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_fraction_range_as_quantity_2():
    parse = IngredientSlicer("1/2-1 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_fraction_dupe_units_range_quantity_1():
    parse = IngredientSlicer("1cup-1/2 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_fraction_dupe_units_range_quantity_2():
    parse = IngredientSlicer("1/2 cup-1 cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_fraction_dupe_units_range_quantity_3():
    parse = IngredientSlicer("1/2cup-1cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == "0.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True
# -------------------------------------------------------------------------------
# ---- Unicode fraction tests ----
# -------------------------------------------------------------------------------
def test_single_unicode_fractions_1():
    parse = IngredientSlicer("½cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == ' 0.5 cup of sugar' # TODO: add a strip() to the end of the standardized_ingredient
    assert parsed_ingredient['quantity'] == "0.5"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_single_unicode_fractions_2():
    parse = IngredientSlicer("⅓ sugar cups")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == ' 0.333 sugar cups' # TODO: add a strip() to the end of the standardized_ingredient
    assert parsed_ingredient['quantity'] == "0.333"
    assert parsed_ingredient['unit'] == 'cups'
    assert parsed_ingredient['is_required'] == True

def test_unicode_fractions_1():
    parse = IngredientSlicer("1½cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '1.5 cup of sugar'
    assert parsed_ingredient['quantity'] == "1.5"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_unicode_fractions_2():
    parse = IngredientSlicer("1⅓cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '1.333 cup of sugar'
    assert parsed_ingredient['quantity'] == "1.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_unicode_fractions_3():
    parse = IngredientSlicer("2  ⅓cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient["standardized_ingredient"] == '2.333 cup of sugar'
    assert parsed_ingredient['quantity'] == "2.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Unicode fraction/range tests ----
# -------------------------------------------------------------------------------
    
def test_unicode_fraction_range_1():
    parse = IngredientSlicer("1-1½cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '1.25 cup of sugar'
    assert parsed_ingredient['quantity'] == "1.25"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_unicode_fraction_range_2():
    parse = IngredientSlicer("1½-2cup of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '1.75 cup of sugar'
    assert parsed_ingredient['quantity'] == "1.75"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

def test_unicode_fraction_range_3():
    parse = IngredientSlicer("1½-2½cup of sugar", debug=False)
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '2 cup of sugar'
    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- X Separator tests ----
# -------------------------------------------------------------------------------
def test_x_separator_1():
    parse = IngredientSlicer("1x 2 tablespoons of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == "2 tablespoons of sugar"

    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == 'tablespoons'
    assert parsed_ingredient['is_required'] == True

def test_x_separator_2():
    parse = IngredientSlicer("1x2 tablespoons of sugar")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == "2 tablespoons of sugar"

    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == 'tablespoons'
    assert parsed_ingredient['is_required'] == True

def test_x_separator_3():
    parse = IngredientSlicer("3 X 4lb hamburger patties")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient["standardized_ingredient"] == '12 lb hamburger patties'

    assert parsed_ingredient['quantity'] == "12"
    assert parsed_ingredient['unit'] == 'lb'
    assert parsed_ingredient['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Optional ingredient (no parenthesis) tests ----
# -------------------------------------------------------------------------------
def test_optional_ingredient_1():
    parse = IngredientSlicer("1/3 cup sugar, optional")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "0.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == False
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 0

def test_optional_ingredient_2():
    parse = IngredientSlicer("1/3 cup sugar, opt")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "0.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == False
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 0

# -------------------------------------------------------------------------------
# ---- Optional ingredient (with parenthesis) tests ----
# -------------------------------------------------------------------------------
def test_optional_parenthesis_1():
    parse = IngredientSlicer("1/3 cup sugar (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "0.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == False
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

def test_optional_parenthesis_2():
    parse = IngredientSlicer("1/3 cup sugar (opt)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "0.333"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == False
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

# -------------------------------------------------------------------------------
# ---- Parenthesis (quantity only) tests ----
# -------------------------------------------------------------------------------
def test_quantity_only_parenthesis_1():
    parse = IngredientSlicer("salmon steaks (2)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == None
    assert parsed_ingredient['is_required'] == True
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

def test_quantity_only_parenthesis_2():
    parse = IngredientSlicer("salmon steaks (2) (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "2"
    assert parsed_ingredient['unit'] == None
    assert parsed_ingredient['is_required'] == False
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 6

def test_quantity_only_parenthesis_3():
    parse = IngredientSlicer("chicken breasts (4)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "4"
    assert parsed_ingredient['unit'] == "breasts"
    assert parsed_ingredient["standardized_unit"] == "breast"
    
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    assert parsed_ingredient['standardized_secondary_unit'] == None

    assert parsed_ingredient['is_required'] == True
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

def test_quantity_only_parenthesis_4():
    parse = IngredientSlicer("3 chicken breasts (4) (optional)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "12.0"
    assert parsed_ingredient['unit'] == "breasts"
    assert parsed_ingredient["standardized_unit"] == "breast"
    
    assert parsed_ingredient['secondary_quantity'] == '3'
    assert parsed_ingredient['secondary_unit'] == None
    assert parsed_ingredient['standardized_secondary_unit'] == None

    assert parsed_ingredient['is_required'] == False
    # assert len(parsed_ingredient["parenthesis_notes"]) == 6

def test_quantity_only_parenthesis_5():
    parse = IngredientSlicer("3 1/2 chicken breasts (4)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "14.0"
    assert parsed_ingredient['unit'] == "breasts"
    assert parsed_ingredient["standardized_unit"] == "breast"
    
    assert parsed_ingredient['secondary_quantity'] == "3.5"
    assert parsed_ingredient['secondary_unit'] == None
    assert parsed_ingredient['standardized_secondary_unit'] == None

    assert parsed_ingredient['is_required'] == True
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

# -------------------------------------------------------------------------------
# ---- Parenthesis (quantity unit only) tests ----
# -------------------------------------------------------------------------------

def test_quantity_and_unit_parenthesis_1():
    parse = IngredientSlicer("4 chicken wings (8 oz)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "32.0"
    assert parsed_ingredient['unit'] == "oz"
    assert parsed_ingredient["standardized_unit"] == "ounce"
    
    assert parsed_ingredient['secondary_quantity'] == "4"
    assert parsed_ingredient['secondary_unit'] == "wings"
    assert parsed_ingredient['standardized_secondary_unit'] == "wing"

    assert parsed_ingredient['is_required'] == True
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

def test_quantity_and_unit_parenthesis_2():
    parse = IngredientSlicer(" chicken breast (12 ounces)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "12"
    assert parsed_ingredient['unit'] == "ounces"
    assert parsed_ingredient["standardized_unit"] == "ounce"

    assert parsed_ingredient['secondary_quantity'] == None  # TODO: maybe this case should get a quantity of 1, but for now it's None
    assert parsed_ingredient['secondary_unit'] == "breast"
    assert parsed_ingredient['standardized_secondary_unit'] == "breast"

    assert parsed_ingredient['is_required'] == True
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3


def test_quantity_and_unit_parenthesis_3():
    parse = IngredientSlicer("1/2 cup sugar (8 ounces)")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "8"
    assert parsed_ingredient['unit'] == "ounces"
    assert parsed_ingredient["standardized_unit"] == "ounce"
    
    assert parsed_ingredient['secondary_quantity'] == "0.5"
    assert parsed_ingredient['secondary_unit'] == "cup"
    assert parsed_ingredient['standardized_secondary_unit'] == "cup"

    assert parsed_ingredient['is_required'] == True
    
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3



# -------------------------------------------------------------------------------
# ---- Assortment of different ingredients seen in the "wild" tests ----
# -------------------------------------------------------------------------------
def test_wild_ingredients():

    parse = IngredientSlicer("1 (10 ounce) package frozen chopped spinach, thawed, drained and squeezed dry")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "10.0"
    assert parsed_ingredient['unit'] == 'ounce'
    assert parsed_ingredient['is_required'] == True
    assert parsed_ingredient['secondary_quantity'] == "1"
    assert parsed_ingredient['secondary_unit'] == "package"

    parse = IngredientSlicer("1 (8 ounce) container plain yogurt")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "8.0"
    assert parsed_ingredient['unit'] == 'ounce'
    assert parsed_ingredient['is_required'] == True
    assert parsed_ingredient['secondary_quantity'] == "1"
    assert parsed_ingredient['secondary_unit'] == "container"
    # assert len(parsed_ingredient["parenthesis_notes"]) == 3

    parse = IngredientSlicer("salt to taste", debug= True)
    parse.parse()
    parsed_ingredient = parse.to_json()
    assert parsed_ingredient['quantity'] == None
    assert parsed_ingredient['unit'] == None
    assert parsed_ingredient['is_required'] == True
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert parsed_ingredient["parenthesis_notes"] == []

    parse = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving")
    parse.parse()
    parsed_ingredient = parse.to_json()

    assert parsed_ingredient['quantity'] == "0.5"
    assert parsed_ingredient['unit'] == 'cup'
    assert parsed_ingredient['is_required'] == True
    assert parsed_ingredient['secondary_quantity'] == None
    assert parsed_ingredient['secondary_unit'] == None
    # assert len(parsed_ingredient["parenthesis_notes"]) == 0

################################################################################################
### Old code for manual testing
################################################################################################

# regex_map = IngredientRegexPatterns()
# parse1 = IngredientSlicer("30 g cake flour (¼ cup minus 1 tsp; weigh your flour or use the “fluff and sprinkle“ method and level it off; you can make your own Homemade Cake Flour) ¼ 1")
# parse1 = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving (8 ounces, optional), won't need more (but i do like to put extra on it)")
# parse1 = IngredientSlicer("1-4 cups of sugar, lightly chopped (about 8 oz) but please don't do it")
# parse1 = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving (8 ounces, optional), won't need more, but i do like to put extra on it")

# parse1.parse()
# ingredient_object = parse1.to_json()
# ingredient_object
# for key, val in ingredient_object.items():
#     print(f"{key}: > '{val}'")
#     print()

# def extract_foods(ingredient: str) -> str:

#     # ingredient = ingredient_object["standardized_ingredient"]
    
#     print(f"Best effort extraction of food words from: {ingredient}")

#     paranethesis_to_remove = regex_map.SPLIT_BY_PARENTHESIS.findall(ingredient)

#     print(f"Removing paranethesis: {paranethesis_to_remove}")

#     for parenthesis in paranethesis_to_remove:
#         ingredient = ingredient.replace(parenthesis, "")

#     # ingredient = '2.5 cups of sugar, lightly chopped (about 8 oz)'
#     stop_words_to_remove = regex_map.STOP_WORDS_PATTERN.findall(ingredient)

#     # remove any stop words
#     for stop_word in stop_words_to_remove:
#         ingredient = ingredient.replace(stop_word, "")

#     unit_matches        = regex_map.UNITS_PATTERN.findall(ingredient)
#     quantity_matches    = regex_map.ALL_NUMBERS.findall(ingredient)
#     # parenthesis_matches = regex_map.SPLIT_BY_PARENTHESIS.findall(ingredient)
#     prep_words_matches  = regex_map.PREP_WORDS_PATTERN.findall(ingredient)
#     ly_words_matches    = regex_map.WORDS_ENDING_IN_LY.findall(ingredient)

#     # make a single list of the strings to remove (IMPORATNT that parenthesis content is removed first)
#     strings_to_remove = unit_matches + quantity_matches + prep_words_matches + ly_words_matches

#     for match in strings_to_remove:
#         ingredient = ingredient.replace(match, "")
    
#     # remove any special characters
#     ingredient = re.sub(r'[^\w\s]', '', ingredient)

#     # remove any extra whitespace
#     ingredient = re.sub(r'\s+', ' ', ingredient).strip()

#     # is_single_food_word = len(ingredient.split()) == 1

#     return ingredient
    

    # # Function to remove matches from the ingredient string
    # def remove_matches(ingredient, matches):
    #     for match in matches:
    #         ingredient = re.sub(re.escape(match), '', ingredient)
    #     return ingredient

    # # Remove matches from the standard_ingredient string
    # standard_ingredient = remove_matches(standard_ingredient, parenthesis_matches)
    # standard_ingredient = remove_matches(standard_ingredient, unit_matches)
    # standard_ingredient = remove_matches(standard_ingredient, quantity_matches)

    # make a single list of the strings to remove (IMPORATNT that parenthesis content is removed first)

# NOTE: good simple function for normalziing whitespaces in a string (i.e. removing extra whitespace, only keeping single spaces)
# def normalize_whitespace(string: str) -> str:
#     """Strip leading/trailing whitespace and normalize internal whitespace to a single space.
#     Args:
#         string: The string to normalize.
#     Example:
#         normalize_whitespace("  a  b   c  ")  # "a b c"
#         normalize_whitespace("a   bc")  # "a bc"
#     """
#     return " ".join([i.strip() for i in string.split()])

# def best_effort_food_match(ingredient_object):

#     unit = ingredient_object["unit"]
#     quantity = ingredient_object["quantity"]
#     secondary_unit = ingredient_object["secondary_unit"]
#     secondary_quantity = ingredient_object["secondary_quantity"]
#     stashed_quantity = ingredient_object["stashed_quantity"]
#     stashed_unit = ingredient_object["stashed_unit"]
#     parenthesis_content = ingredient_object["parenthesis_content"]

#     standard_ingredient = ingredient_object["standardized_ingredient"]

#     strings_to_remove = [unit, quantity, secondary_unit, secondary_quantity, stashed_quantity, stashed_unit, parenthesis_content]
#     strings_to_remove = [i for sublist in strings_to_remove for i in (sublist if isinstance(sublist, (list, tuple)) else [sublist])]

#     # try and reduce the ingredient down to  a single food word if possible
#     reduced_ingredient = reduce_ingredient(standard_ingredient, strings_to_remove)

#     split_reduced_ingredient = reduced_ingredient.split() # split the reduced ingredient into words

#     is_single_food_word = len(split_reduced_ingredient) == 1

#     if is_single_food_word:
#         return normalize_whitespace(reduce_ingredient)
    

### KEEP recursive function to remove certain strings from an ingredient and try to get it down to just food words #####
# def reduce_ingredient(ingredient, strings_to_remove):

#     ingredient = " ".join([i.strip() for i in ingredient.split()])
#     # strip_ingredient = " ".join([i.strip() for i in ingredient.split()])
#     split_ingredient = ingredient.split()

#     # print(f"ingredient: '{ingredient}'")
#     # print(f"strip_ingredient: '{strip_ingredient}'")
#     # print(f"split_ingredient: '{split_ingredient}'")
#     # print(f"Any strings to remove in split_ingredient: '{[i for i in strings_to_remove if i in split_ingredient]}'")

#     # Base case: no more matches to remove from string, return the ingredient
#     if not strings_to_remove or not [i for i in strings_to_remove if i in split_ingredient]:
#         print(f" > Reached maximum ingredient reduction: '{ingredient}'\n===================\n")
#         return ingredient.strip()

#     reduced_ingredients = []

#     # print(f"Iterating through strings to remove....")

#     for word_to_drop in strings_to_remove:
#         # Remove the current word from the ingredient and add the result to the list
#         reduced_ingredients.append(ingredient.replace(word_to_drop, "").strip())

#     # Find the ingredient with the fewest characters remaining
#     shortest_ingredient = min(reduced_ingredients, key=len)

#     print(f"Reducing shortened ingredient: '{shortest_ingredient}'\n")

#     # Recur with the shortest ingredient and the remaining strings to remove
#     return reduce_ingredient(shortest_ingredient, strings_to_remove)


################################################################################################
################################################################################################