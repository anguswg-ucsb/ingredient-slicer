# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- Assortment of different ingredients seen in the "wild" tests ----
# -------------------------------------------------------------------------------

def test_wild_ingredients_1():

    parse = IngredientSlicer("1 (10 ounce) package frozen chopped spinach, thawed, drained and squeezed dry")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "10"
    assert parsed['unit'] == 'ounce'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "package"
    assert parsed['standardized_secondary_unit'] == "package"

    assert parsed['is_required'] == True
    
    assert parsed['prep'] == ['chopped', 'drained', 'squeezed']
    assert parsed['food'] == 'spinach dry'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_2():

    ingredient = "4 large skinless, boneless chicken thighs, cut into bite-sized pieces"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()
    
    assert parsed['quantity'] == "4"
    assert parsed['unit'] == 'thighs'
    assert parsed['standardized_unit'] == 'thigh'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None
        
    assert parsed['is_required'] == True

    assert parsed['prep'] == ['cut']
    assert parsed['food'] == 'skinless boneless chicken' 
    assert parsed['size_modifiers'] == ['large']

def test_wild_ingredients_3():
    ingredient = "1 (6 ounce) can tomato paste"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "6"
    assert parsed['unit'] == 'ounce'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "can"
    assert parsed['standardized_secondary_unit'] == "can"

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'tomato paste'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_4():
    ingredient = "2 (15-ounce) cans chickpeas, rinsed and drained"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "30"
    assert parsed['unit'] == 'ounce'
    assert parsed['standardized_unit'] == 'ounce'

    assert parsed['secondary_quantity'] == "2"
    assert parsed['secondary_unit'] == "cans"
    assert parsed['standardized_secondary_unit'] == "can"

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['drained', 'rinsed']
    assert parsed['food'] == 'chickpeas'
    assert parsed['size_modifiers'] == []
    

def test_wild_ingredients_5():
    ingredient = "2 servings udon noodles (1.1 lb, 500 g frozen or parboiled udon noodles; 6.3 oz, 180 g dry udon noodles)"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2.2"
    assert parsed['unit'] == 'lb'
    assert parsed['standardized_unit'] == 'pound'

    assert parsed['secondary_quantity'] == "2"
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'udon noodles'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_6():
    ingredient = "1/2 medium fresh jalapeño chile pepper, finely chopped*"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == None
    assert parsed['standardized_unit'] == None

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['chopped', 'finely']
    assert parsed['food'] == 'fresh jalapeño chile pepper'
    assert parsed['size_modifiers'] == ['medium']

def test_wild_ingredients_7():
    
    ingredient = "1 cube Japanese curry roux (1 oz, 32 g)"
    
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "cube"
    assert parsed['standardized_secondary_unit'] == "cube"
    assert parsed['food'] == 'japanese curry roux'

def test_wild_ingredients_8():
    parse = IngredientSlicer("1 (8 ounce) container plain yogurt")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == 'ounce'
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "container"
    assert parsed['prep'] == []
    assert parsed['food'] == 'plain yogurt'

def test_wild_ingredients_9():
    parse = IngredientSlicer("1 (8.5 ounce) container plain yogurt")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8.5"
    assert parsed['unit'] == 'ounce'
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "container"
    assert parsed['prep'] == []
    assert parsed['food'] == 'plain yogurt'

def test_wild_ingredients_10():
    parse = IngredientSlicer("salt to taste", debug= True)
    # parse.parse()
    parsed = parse.to_json()
    assert parsed['quantity'] == None
    assert parsed['unit'] == "to taste"
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['food'] == 'salt'

def test_wild_ingredients_11():
    parse = IngredientSlicer("1/2 cup freshly grated Parmesan cheese, plus more for serving")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None

def test_wild_ingredients_additional_1():
    ingredient = "3 tablespoons unsalted butter, softened at room temperature"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "3"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['room temperature', 'softened']
    assert parsed['food'] == 'unsalted butter'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_2():
    ingredient = "1/4 cup sliced almonds, toasted"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.25"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['sliced', 'toasted']
    assert parsed['food'] == 'almonds'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_3():
    ingredient = "1 teaspoon minced fresh ginger"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'teaspoon'
    assert parsed['standardized_unit'] == 'teaspoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['minced']
    assert parsed['food'] == 'fresh ginger'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_4():
    ingredient = "2 cloves garlic, minced"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == None # TODO: need a special case for "cloves" as a unit vs. "cloves" as a food
    assert parsed['standardized_unit'] == None
    # assert parsed['unit'] == 'cloves'
    # assert parsed['standardized_unit'] == 'clove'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['minced']
    assert parsed['food'] == 'cloves garlic'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_5():
    ingredient = "1 cup cooked quinoa"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['cooked']
    assert parsed['food'] == 'quinoa'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_6():
    ingredient = "2 tablespoons chopped fresh parsley leaves"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tablespoons'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['chopped']
    assert parsed['food'] == 'fresh parsley leaves'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_7():
    ingredient = "1/2 cup grated Parmesan cheese"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['grated']
    assert parsed['food'] == 'parmesan cheese'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_8():
    ingredient = "1/4 teaspoon ground cinnamon"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.25"
    assert parsed['unit'] == 'teaspoon'
    assert parsed['standardized_unit'] == 'teaspoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['ground']
    assert parsed['food'] == 'cinnamon'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_9():
    ingredient = "1 cup packed light brown sugar"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "1"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['light', 'packed']
    assert parsed['food'] == 'brown sugar'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_10():
    ingredient = "1/2 cup thinly sliced green onions"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['sliced', 'thinly']
    assert parsed['food'] == 'green onions'
    assert parsed['size_modifiers'] == []


def test_wild_ingredients_additional_11():
    ingredient = "2 pieces dried shiitake mushrooms (17 g, 0.6 oz for the dashi broth and the minced mushrooms below)"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "34"
    assert parsed['unit'] == 'g'
    assert parsed['standardized_unit'] == 'gram'

    assert parsed['secondary_quantity'] == '2'
    assert parsed['secondary_unit'] == 'pieces'
    assert parsed['standardized_secondary_unit'] == 'piece'

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['minced']
    assert parsed['food'] == 'dried shiitake mushrooms'
    assert parsed['size_modifiers'] == []

def test_wild_ingredients_additional_12():
    ingredient = "1/2 tablespoon olive oil"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'tablespoon'
    assert parsed['standardized_unit'] == 'tablespoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == 'olive oil'
    assert parsed['size_modifiers'] == []


def test_wild_ingredients_additional_13():
    ingredient = "2 cloves garlic, minced"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == None
    assert parsed['standardized_unit'] == None

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['minced']
    assert parsed['food'] == 'cloves garlic'
    assert parsed['size_modifiers'] == []


def test_wild_ingredients_additional_14():
    ingredient = "1/4 cup chopped fresh cilantro leaves"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.25"
    assert parsed['unit'] == 'cup'
    assert parsed['standardized_unit'] == 'cup'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['chopped']
    assert parsed['food'] == 'fresh cilantro leaves'
    assert parsed['size_modifiers'] == []


def test_wild_ingredients_additional_15():
    ingredient = "1/2 teaspoon freshly ground black pepper, or to taste"
    parse = IngredientSlicer(ingredient)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == 'teaspoon'
    assert parsed['standardized_unit'] == 'teaspoon'

    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == ['freshly', 'ground']
    assert parsed['food'] == 'black pepper'
    assert parsed['size_modifiers'] == []

# "1 (14 ounce) can coconut milk"
# "1 (6 ounce) can tomato paste"
# "2 (15-ounce) cans chickpeas, rinsed and drained"
# "1/2 medium fresh jalapeño chile pepper, finely chopped*"
# "1 (9.25ounce) bag corn chips, such as Fritos® Scoops!®"
# "1/4 cup (1/2 stick) butter, divided"
# "Graham cracker crumbs or powdered sugar for topping"
# "1 large egg, lightly beaten"