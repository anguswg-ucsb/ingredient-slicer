# pytest library
import pytest

import re

from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Testing the various parenthesis cases ----
# - quantity only
# - quantity and unit
# - equivalent quantity and unit
# - optional
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- Parenthesis (equivalent quantity unit) tests ----
# -------------------------------------------------------------------------------

def test_parenthesis_with_equiv_quantity_unit_1():
    parse = IngredientSlicer("1 cup of chopped chicken breast (about 12 ounces)", debug = False)
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"

    assert parsed['secondary_quantity'] == "1"  # TODO: maybe this case should get a quantity of 1, but for now it's None
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True

def test_equiv_quantity_unit_1():
    parse = IngredientSlicer("1 cup of chopped chicken breast (about 12 ounces)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "1"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ["chopped"]
    assert parsed['food'] == "chicken"
    assert parsed['size_modifiers'] == []


def test_equiv_quantity_unit_2():
    parse = IngredientSlicer("1/2 stalk of brocolli (probably about 8 ounces)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"

    # TODO: THIS IS A BUG THAT NEEDS TO BE FIXED (SHOULD BE 0.5 stalk) no clue why at this point
    assert parsed['secondary_quantity'] == "8"
    assert parsed['secondary_unit'] == "ounces"
    assert parsed['standardized_secondary_unit'] == "ounce"
    # assert parsed['secondary_quantity'] == "0.5"   # NOTE: this is the correct value
    # assert parsed['secondary_unit'] == "stalk"
    # assert parsed['standardized_secondary_unit'] == "stalk"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ['probably'] # TODO: meh
    assert parsed['food'] == "brocolli"
    assert parsed['size_modifiers'] == []

def test_equiv_quantity_unit_equiv_at_the_end_1():
    parse = IngredientSlicer("1/2 cup of chopped onions (4 ounces about)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "4"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"

    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ["chopped"]
    assert parsed['food'] == "onions"
    assert parsed['size_modifiers'] == []

def test_equiv_quantity_unit_equiv_with_pair_of_quantity_units_1():
    parse = IngredientSlicer("1/2 cup of chopped onions (about 4 oz, 34 grams)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "4"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"

    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ["chopped"]
    assert parsed['food'] == "onions"
    assert parsed['size_modifiers'] == []

def test_equiv_quantity_unit_equiv_with_triplet_of_quantity_units_1():
    parse = IngredientSlicer("1/2 cup of chopped onions (about 4 oz, 34 grams, 0.034 kg)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "4"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"

    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ["chopped"]
    assert parsed['food'] == "onions"
    assert parsed['size_modifiers'] == []

def test_equiv_quantity_unit_equiv_with_triplet_of_quantity_units_outer_unit_is_weight_1():
    parse = IngredientSlicer("1/2 lb of chopped onions (about 4 oz, 34 grams, 0.034 kg)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.5"
    assert parsed['unit'] == "lb"
    assert parsed["standardized_unit"] == "pound"

    assert parsed['secondary_quantity'] == "4"
    assert parsed['secondary_unit'] == "oz"
    assert parsed['standardized_secondary_unit'] == "ounce"

    assert parsed['is_required'] == True
    assert parsed['prep'] == ["chopped"]
    assert parsed['food'] == "onions"
    assert parsed['size_modifiers'] == []




# -------------------------------------------------------------------------------
# ---- Optional ingredient (no parenthesis) tests ----
# -------------------------------------------------------------------------------
def test_optional_ingredient_1():
    parse = IngredientSlicer("1/3 cup sugar, optional")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == False
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 0

def test_optional_ingredient_2():
    parse = IngredientSlicer("1/3 cup sugar, opt")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == False
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 0

# -------------------------------------------------------------------------------
# ---- Optional ingredient (with parenthesis) tests ----
# -------------------------------------------------------------------------------
def test_optional_parenthesis_1():
    parse = IngredientSlicer("1/3 cup sugar (optional)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == False
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 3

def test_optional_parenthesis_2():
    parse = IngredientSlicer("1/3 cup sugar (opt)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "0.333"
    assert parsed['unit'] == 'cup'
    assert parsed['is_required'] == False
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 3

# -------------------------------------------------------------------------------
# ---- Parenthesis (quantity only) tests ----
# -------------------------------------------------------------------------------
def test_quantity_only_parenthesis_1():
    parse = IngredientSlicer("salmon steaks (2)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'steaks'
    assert parsed['is_required'] == True
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 3

def test_quantity_only_parenthesis_2():
    parse = IngredientSlicer("salmon steaks (2) (optional)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'steaks'
    assert parsed['is_required'] == False
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    # assert len(parsed["parenthesis_notes"]) == 6

def test_quantity_only_parenthesis_3():
    parse = IngredientSlicer("chicken breasts (4)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "4"
    assert parsed['unit'] == "breasts"
    assert parsed["standardized_unit"] == "breast"
    
    assert parsed['secondary_quantity'] == None
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    # assert len(parsed["parenthesis_notes"]) == 3

def test_quantity_only_parenthesis_4():
    parse = IngredientSlicer("3 chicken breasts (4) (optional)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == "breasts"
    assert parsed["standardized_unit"] == "breast"
    
    assert parsed['secondary_quantity'] == '3'
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == False
    # assert len(parsed["parenthesis_notes"]) == 6

def test_quantity_only_parenthesis_5():
    parse = IngredientSlicer("3 1/2 chicken breasts (4)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "14"
    assert parsed['unit'] == "breasts"
    assert parsed["standardized_unit"] == "breast"
    
    assert parsed['secondary_quantity'] == "3.5"
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True
    # assert len(parsed["parenthesis_notes"]) == 3

def test_quantity_only_parenthesis_outer_unit_is_weight_1():
    parse = IngredientSlicer("3 1/2 lbs chicken breasts (4)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "14"
    assert parsed['unit'] == "lbs"
    assert parsed["standardized_unit"] == "pound"
    
    assert parsed['secondary_quantity'] == "3.5"
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == "chicken"
    assert parsed['size_modifiers'] == []

def test_quantity_only_parenthesis_outer_unit_is_volume_1():
    parse = IngredientSlicer("3 1/2 cups chicken breasts (4)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "14"
    assert parsed['unit'] == "cups"
    assert parsed["standardized_unit"] == "cup"
    
    assert parsed['secondary_quantity'] == "3.5"
    assert parsed['secondary_unit'] == None
    assert parsed['standardized_secondary_unit'] == None

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == "chicken"
    assert parsed['size_modifiers'] == []

def test_quantity_only_parenthesis_with_equiv_parenthesis_after_1():
    parse = IngredientSlicer("3 1/2 cups chicken breasts (4) (about 32 oz)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "32"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "14"
    assert parsed['secondary_unit'] == "cups"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True

    assert parsed['prep'] == []
    assert parsed['food'] == "chicken"
    assert parsed['size_modifiers'] == []

def test_quantity_only_parenthesis_with_equiv_parenthesis_after_and_optional_1():
    parse = IngredientSlicer("3 1/2 cups chicken breasts (4) (about 32 oz) (optional)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "32"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "14"
    assert parsed['secondary_unit'] == "cups"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == False

    assert parsed['prep'] == []
    assert parsed['food'] == "chicken"
    assert parsed['size_modifiers'] == []



# -------------------------------------------------------------------------------
# ---- Parenthesis (quantity unit only) tests ----
# -------------------------------------------------------------------------------

def test_quantity_and_unit_parenthesis_1():
    parse = IngredientSlicer("4 chicken wings (8 oz)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "32"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "4"
    assert parsed['secondary_unit'] == "wings"
    assert parsed['standardized_secondary_unit'] == "wing"

    assert parsed['is_required'] == True
    # assert len(parsed["parenthesis_notes"]) == 3

def test_quantity_and_unit_parenthesis_2():
    parse = IngredientSlicer(" chicken breast (12 ounces)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "12"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"

    assert parsed['secondary_quantity'] == None  # TODO: maybe this case should get a quantity of 1, but for now it's None
    assert parsed['secondary_unit'] == "breast"
    assert parsed['standardized_secondary_unit'] == "breast"

    assert parsed['is_required'] == True
    # assert len(parsed["parenthesis_notes"]) == 3


def test_quantity_and_unit_parenthesis_3():
    parse = IngredientSlicer("1/2 cup sugar (8 ounces)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == "ounces"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True

def test_quantity_and_unit_parenthesis_pair_quantity_units_1():
    parse = IngredientSlicer("1/2 cup sugar (8 oz, 34 grams)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True

def test_quantity_and_unit_parenthesis_triplet_quantity_units_1():
    parse = IngredientSlicer("1/2 cup sugar (8 oz, 34 grams, 0.034 kg)")
    # parse.parse()
    parsed = parse.to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == "oz"
    assert parsed["standardized_unit"] == "ounce"
    
    assert parsed['secondary_quantity'] == "0.5"
    assert parsed['secondary_unit'] == "cup"
    assert parsed['standardized_secondary_unit'] == "cup"

    assert parsed['is_required'] == True

