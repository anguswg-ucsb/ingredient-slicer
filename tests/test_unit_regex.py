# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns
# regex_map = IngredientRegexPatterns()

@pytest.fixture
def regex_map():
    return IngredientRegexPatterns()

def test_units_pattern(regex_map):

    assert regex_map.UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == ['cups', 'teaspoons']
    assert regex_map.UNITS_PATTERN.findall("This is another test string with pounds and liters") == ['pounds', 'liters']
    assert regex_map.UNITS_PATTERN.findall("No units in this string") == [] # TODO: Address "in" in the string, what if this was the unit "in" for inches?
    assert regex_map.UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ['cup', 'stalks']

    assert regex_map.UNITS_PATTERN.findall("cup cup cup cup") == ['cup', 'cup', 'cup', 'cup']
    assert regex_map.UNITS_PATTERN.findall("cups tbs tablespoon ml ML mm") == ['cups', 'tbs', 'tablespoon', 'ml', 'ML'] # NOTE: mm is not a unit for now (removed with other dimension like units (i.e. inches, feet, etc.))

    assert regex_map.UNITS_PATTERN.findall("1cup") == []
    assert regex_map.UNITS_PATTERN.findall("1 cup") == ['cup']
    assert regex_map.UNITS_PATTERN.findall("cupcup") == []
    assert regex_map.UNITS_PATTERN.findall("cup    cup") == ['cup', 'cup']

def test_basic_units_pattern(regex_map):

    # brute force test
    assert regex_map.BASIC_UNITS_PATTERN.findall("teaspoons tablespoon teaspoonful tablespoons table teaspoon tsp tspn tspns tspn. tspns. ts t t.") == ['teaspoons', 'tablespoon', 'teaspoonful', 'tablespoons', 'teaspoon', 'tsp', 'tspn', 'tspns', 'tspn', 'tspns', 'ts', 't', 't']
    assert regex_map.BASIC_UNITS_PATTERN.findall("tbsp tbs tbsps tbl tbls tbsps. tbls. T") == ['tbsp', 'tbs', 'tbsps', 'tbl', 'tbls', 'tbsps', 'tbls', 'T']
    assert regex_map.BASIC_UNITS_PATTERN.findall("tsp tspn tspns tspn. tspns. ts t t.") == ['tsp', 'tspn', 'tspns', 'tspn', 'tspns', 'ts', 't', 't']
    assert regex_map.BASIC_UNITS_PATTERN.findall("cup cups C c") == ['cup', 'cups', 'C', 'c']
    assert regex_map.BASIC_UNITS_PATTERN.findall("pint pints pt pts") == ['pint', 'pints', 'pt', 'pts']
    assert regex_map.BASIC_UNITS_PATTERN.findall("quart quarts qt qts") == ['quart', 'quarts', 'qt', 'qts']
    assert regex_map.BASIC_UNITS_PATTERN.findall("gallon gallons gals gal") == ['gallon', 'gallons', 'gals', 'gal']
    assert regex_map.BASIC_UNITS_PATTERN.findall("fluid ounce fluid ounces fl oz fl ozs fluid oz fluid ozs fluid oz fluid ozs") == ['fluid ounce', 'fluid ounces', 'fl oz', 'fl ozs', 'fluid oz', 'fluid ozs', 'fluid oz', 'fluid ozs']
    assert regex_map.BASIC_UNITS_PATTERN.findall("milliliter milliliters ml mls") == ['milliliter', 'milliliters', 'ml', 'mls']
    assert regex_map.BASIC_UNITS_PATTERN.findall("liter liters l") == ['liter', 'liters', 'l']
    assert regex_map.BASIC_UNITS_PATTERN.findall("ounce ounces oz ozs oz ozs") == ['ounce', 'ounces', 'oz', 'ozs', 'oz', 'ozs']
    assert regex_map.BASIC_UNITS_PATTERN.findall("pound pounds lbs lb") == ['pound', 'pounds', 'lbs', 'lb']
    assert regex_map.BASIC_UNITS_PATTERN.findall("milligram milligrams mg mgs") == ['milligram', 'milligrams', 'mg', 'mgs']
    assert regex_map.BASIC_UNITS_PATTERN.findall("gram grams g") == ['gram', 'grams', 'g']

    # wilder tests
    assert regex_map.BASIC_UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == ['cups', 'teaspoons']
    assert regex_map.BASIC_UNITS_PATTERN.findall("This is another test string with pounds and liters") == ['pounds', 'liters']
    assert regex_map.BASIC_UNITS_PATTERN.findall("No units") == [] 
    assert regex_map.BASIC_UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ['cup']
    assert regex_map.BASIC_UNITS_PATTERN.findall("tablespoonsstalks of lettuce") == []
    assert regex_map.BASIC_UNITS_PATTERN.findall("tablespoons stalks of lettuce") == ['tablespoons']

def test_non_basic_units_pattern(regex_map):

    # contains non-basic units
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("salmom fillet") == ['fillet']
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ["stalks"]
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("tablespoons stalks of lettuce") == ["stalks"]

    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("100 cans of cubed thigh meat with a dash of meatloaf") == ["cans", "thigh", "dash"]
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("100 can of cubed thighs meat with a dashes of meatloaf") == ["can", "thighs", "dashes"]

    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("5 plates of wings") == ["plates", "wings"]
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("1 plate of wings") == ["plate", "wings"]

    # No non-basic units
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("This is another test string with pounds and liters") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("No units") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("teaspoons tablespoon teaspoonful tablespoons table teaspoon tsp tspn tspns tspn. tspns. ts t t.") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("tbsp tbs tbsps tbl tbls tbsps. tbls. T") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("tsp tspn tspns tspn. tspns. ts t t.") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("cup cups C c") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("pint pints pt pts") == []
    assert regex_map.NON_BASIC_UNITS_PATTERN.findall("tablespoonsstalks of lettuce") == []
