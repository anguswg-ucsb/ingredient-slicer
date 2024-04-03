# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Simple standard form ingredients tests ----
# Standard form: "1 cup of sugar" (quantity, unit, ingredient)
# -------------------------------------------------------------------------------

def test_standard_formatted_ingredients():

    slicer = IngredientSlicer("2 tablespoons of sugar")
    # slicer.parse()
    parsed = slicer.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['is_required'] == True

    parse2 = IngredientSlicer("1/2 cup of sugar")
    # parse2.parse()
    parsed = parse2.to_json()
    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

    parse3 = IngredientSlicer("1 1/2 cups of sugar")
    # parse3.parse()
    parsed = parse3.to_json()
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_quantity_and_unit_1():
    parse = IngredientSlicer("3 pounds of beef")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'pounds'
    assert parsed['is_required'] == True

def test_quantity_and_unit_2():
    parse = IngredientSlicer("14 lbs of lettuce")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "14"
    assert parsed['unit'] == 'lbs'
    assert parsed['standardized_unit'] == 'pound'
    assert parsed['is_required'] == True

    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Words-to-numbers (with prefixed word numbers) tests ----
# -------------------------------------------------------------------------------

def test_prefixed_number_words_1():
    parse = IngredientSlicer("twenty seven cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "27"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"
    assert parsed['is_required'] == True

def test_prefixed_number_words_2():
    parse = IngredientSlicer("hundred twenty cups of flour")
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "120"
    assert parsed['unit'] == 'cups'
    assert parsed['standardized_unit'] == "cup"
    assert parsed['is_required'] == True

def test_prefixed_number_words_3():
    parse = IngredientSlicer("a twenty-two lb bag of sugar", debug = True)
    # parse.parse()
    parsed = parse.to_json()
    

    assert parsed['quantity'] == "22"
    assert parsed['unit'] == 'lb'
    assert parsed['standardized_unit'] == "pound"
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Multinumber (space separated) tests ----
# -------------------------------------------------------------------------------

def test_simple_multinumber_1():
    parse = IngredientSlicer("1 1/2 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_simple_multinumber_2():
    parse = IngredientSlicer("1 1/2  cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_simple_multinumber_3():
    parse = IngredientSlicer("1 1/2 1/4 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '1.5 0.25 cups of sugar'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_multiple_multinumber_1():
    parse = IngredientSlicer("1 1/2 1/4 1/8 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '1.5 0.375 cups of sugar'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_multiple_multinumber_2():
    parse = IngredientSlicer("1 1/2 1/4 1/8 1/16 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '1.5 0.375 0.062 cups of sugar'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_multiple_multinumber_3():
    parse = IngredientSlicer("1.5 2/3 cups of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '2.167 cups of sugar'
    assert parsed['quantity'] == "2.167"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_multiple_multinumber_4():
    parse = IngredientSlicer("3 12 cups of sugar (optional)")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '36 cups of sugar'
    assert parsed['quantity'] == "36"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == False

# -------------------------------------------------------------------------------
# ---- Badly designed ingredients tests ----
# -------------------------------------------------------------------------------
    
def test_quantity_only():
    parse = IngredientSlicer("2")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == None
    assert parsed['is_required'] == True

def test_no_quantity():
    parse = IngredientSlicer("sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == None
    assert parsed['unit'] == None
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Fraction processing tests ----
# -------------------------------------------------------------------------------
    
def test_fraction_as_quantity():
    parse = IngredientSlicer("1/4 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "0.25"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_fraction_as_quantity_2():
    parse = IngredientSlicer("1 1/4 cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == "1.25"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# ---- Unicode fraction tests ----
# -------------------------------------------------------------------------------
def test_single_unicode_fractions_1():
    parse = IngredientSlicer("½cup of sugar")
    # IngredientSlicer("½cup of sugar", debug=True)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '0.5 cup of sugar' # TODO: add a strip() to the end of the standardized_ingredient
    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'sugar'
    assert parsed['size_modifiers'] == []

def test_single_unicode_fractions_2():
    parse = IngredientSlicer("⅓ sugar cups")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '0.333 sugar cups' # TODO: add a strip() to the end of the standardized_ingredient
    assert parsed['quantity'] == "0.333"
    assert parsed['unit'] == 'cups'
    assert parsed['is_required'] == True

def test_unicode_fractions_1():
    parse = IngredientSlicer("1½cup of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '1.5 cup of sugar'
    assert parsed['quantity'] == "1.5"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_unicode_fractions_2():
    parse = IngredientSlicer("1⅓cup of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '1.333 cup of sugar'
    assert parsed['quantity'] == "1.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

def test_unicode_fractions_3():
    parse = IngredientSlicer("2  ⅓cup of sugar")
    # parse.parse()
    parsed = parse.to_json()
    assert parsed["standardized_ingredient"] == '2.333 cup of sugar'
    assert parsed['quantity'] == "2.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# ---- X Separator tests ----
# -------------------------------------------------------------------------------
def test_x_separator_1():
    parse = IngredientSlicer("1x 2 tablespoons of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == "2 tablespoons of sugar"

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['is_required'] == True

def test_x_separator_2():
    parse = IngredientSlicer("1x2 tablespoons of sugar")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == "2 tablespoons of sugar"

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['is_required'] == True

def test_x_separator_3():
    parse = IngredientSlicer("3 X 4lb hamburger patties")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed["standardized_ingredient"] == '12 lb hamburger patties'

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == 'lb'
    assert parsed['is_required'] == True

# -------------------------------------------------------------------------------
# input_ingredient = "roughly 2.5 cups of sugar, lightly chopped (about 8 oz), to cut 1/2 inch pieces, large or medium, and a pinch too"
# input_ingredient = "1 1/2 cups of sugar"
# input_ingredient = "4 large skinless, boneless chicken thighs, cut into bite-sized pieces"
# input_ingredient = "1/2 cup of sugar"

# input_list = [
#     "4 large skinless, boneless chicken thighs, cut into bite-sized pieces",
#     "1 (14 ounce) can coconut milk", 
#     "1 (6 ounce) can tomato paste", "2 (15-ounce) cans chickpeas, rinsed and drained",
#     "1/2 medium fresh jalapeño chile pepper, finely chopped*",
#     "1 (9.25ounce) bag corn chips, such as Fritos® Scoops!®",
#     "1/4 cup (1/2 stick) butter, divided",
#     "Graham cracker crumbs or powdered sugar for topping",
#     "1 large egg, lightly beaten"]

# for input_ingredient in input_list:
#     slicer = IngredientSlicer(input_ingredient)
#     # slicer.parse()
#     parsed = slicer.to_json()
#     print(f"Original:\n > '{input_ingredient}'")
#     print(f"Food: '{parsed['food']}'")
#     print()

# slicer = IngredientSlicer(input_ingredient)
# # slicer.parse()
# parsed = slicer.to_json()
# parsed["food"]

# ingredient = parsed['standardized_ingredient']
# regex = IngredientTools()

# patterns_list = [
#     regex.SPLIT_BY_PARENTHESIS,
#     regex.UNITS_PATTERN,
#     regex.ALL_NUMBERS
#     ]

# for pattern in patterns_list:
#     print(f"Starting string:\n > '{ingredient}'")
#     # print(f"Current pattern: {pattern}")
#     ingredient = find_and_remove(ingredient, pattern)
#     print(f"Ending string:\n > '{ingredient}'")
#     print()



# def _extract_foods2(ingredient: str) -> str:
#     """Does a best effort attempt to extract foods from the ingredient by 
#     removing all extraneous details, words, characters and hope we get left with the food.
#     """

#     # # ingredient = "roughly 2.5 cups of sugar, lightly chopped (about 8 oz), to cut into 1/2 inch pieces, large or medium, and a pinch too"
#     # ingredient = parsed['standardized_ingredient']
#     # regex = IngredientTools()

#     print(f"Best effort extraction of food words from: {ingredient}")
#     # print(f"Best effort extraction of food words from: {ingredient}") if self.debug else None

#     # regular expressions to find and remove from the ingredient
#     # NOTE: important to remove "parenthesis" first and "stop words" last to.
#     # Parenthesis can contain other patterns and they need to be dealt with first (i.e. "(about 8 oz)" contains a number and a unit)
#     patterns_map = {
#         "parenthesis" : regex.SPLIT_BY_PARENTHESIS,
#         "units" : regex.UNITS_PATTERN,
#         "numbers" : regex.ALL_NUMBERS,
#         "prep words" : regex.PREP_WORDS_PATTERN,
#         "ly-words" : regex.WORDS_ENDING_IN_LY,
#         "unit modifiers" : regex.UNIT_MODIFIERS_PATTERN,
#         "dimension units" : regex.DIMENSION_UNITS_PATTERN,
#         "approximate strings" : regex.APPROXIMATE_STRINGS_PATTERN,
#         "sometimes units" : regex.SIZE_MODIFIERS_PATTERN,
#         "casual quantities" : regex.CASUAL_QUANTITIES_PATTERN,
#         "stop words" : regex.STOP_WORDS_PATTERN
#     }

#     for key, pattern in patterns_map.items():
#         print(f" > Removing '{key}' from the ingredient")
#         # print(f" > Removing '{key}' from the ingredient") if self.debug else None

#         # print(f"Starting ingredient:\n > '{ingredient}'")
#         ingredient = find_and_remove(ingredient, pattern)
#         # print(f"Ending ingredient:\n > '{ingredient}'")
#         print()

#     print(f" > Removing any remaining special characters from the ingredient")
#     # print(f" > Removing any remaining special characters") if self.debug else None
    
#     ingredient = re.sub(r'[^\w\s]', '', ingredient) # remove any special characters

#     print(f" > Removing any extra whitespaces")
#     # print(f" > Removing any extra whitespaces") if self.debug else None

#     ingredient = re.sub(r'\s+', ' ', ingredient).strip() # remove any extra whitespace

#     return ingredient

# # print(f"Best effort extraction of food words from: {ingredient}") if self.debug else None
# paranethesis_to_remove = IngredientSlicer.regex.SPLIT_BY_PARENTHESIS.findall(ingredient)

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
    
################################################################################################
### Old code for manual testing
################################################################################################

# regex_map = IngredientTools()
# slicer = IngredientSlicer("30 g cake flour (¼ cup minus 1 tsp; weigh your flour or use the “fluff and sprinkle“ method and level it off; you can make your own Homemade Cake Flour) ¼ 1")
# slicer = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving (8 ounces, optional), won't need more (but i do like to put extra on it)")
# slicer = IngredientSlicer("1-4 cups of sugar, lightly chopped (about 8 oz) but please don't do it")
# slicer = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving (8 ounces, optional), won't need more, but i do like to put extra on it")

# # slicer.parse()
# ingredient_object = slicer.to_json()
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

### TODO: KEEP recursive function to remove certain strings from an ingredient and try to get it down to just food words #####
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