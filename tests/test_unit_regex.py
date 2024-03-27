# pytest library
import pytest

import re


from ingredient_slicer import _regex_patterns

def test_units_pattern():

    assert _regex_patterns.UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == ['cups', 'teaspoons']
    assert _regex_patterns.UNITS_PATTERN.findall("This is another test string with pounds and liters") == ['pounds', 'liters']
    assert _regex_patterns.UNITS_PATTERN.findall("No units in this string") == [] # TODO: Address "in" in the string, what if this was the unit "in" for inches?
    assert _regex_patterns.UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ['cup', 'stalks']

    assert _regex_patterns.UNITS_PATTERN.findall("cup cup cup cup") == ['cup', 'cup', 'cup', 'cup']
    assert _regex_patterns.UNITS_PATTERN.findall("cups tbs tablespoon ml ML mm") == ['cups', 'tbs', 'tablespoon', 'ml', 'ML'] # NOTE: mm is not a unit for now (removed with other dimension like units (i.e. inches, feet, etc.))

    assert _regex_patterns.UNITS_PATTERN.findall("1cup") == []
    assert _regex_patterns.UNITS_PATTERN.findall("1 cup") == ['cup']
    assert _regex_patterns.UNITS_PATTERN.findall("cupcup") == []
    assert _regex_patterns.UNITS_PATTERN.findall("cup    cup") == ['cup', 'cup']

def test_basic_units_pattern():

    # brute force test
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("teaspoons tablespoon teaspoonful tablespoons table teaspoon tsp tspn tspns tspn. tspns. ts t t.") == ['teaspoons', 'tablespoon', 'teaspoonful', 'tablespoons', 'teaspoon', 'tsp', 'tspn', 'tspns', 'tspn', 'tspns', 'ts', 't', 't']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("tbsp tbs tbsps tbl tbls tbsps. tbls. T") == ['tbsp', 'tbs', 'tbsps', 'tbl', 'tbls', 'tbsps', 'tbls', 'T']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("tsp tspn tspns tspn. tspns. ts t t.") == ['tsp', 'tspn', 'tspns', 'tspn', 'tspns', 'ts', 't', 't']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("cup cups C c") == ['cup', 'cups', 'C', 'c']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("pint pints pt pts") == ['pint', 'pints', 'pt', 'pts']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("quart quarts qt qts") == ['quart', 'quarts', 'qt', 'qts']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("gallon gallons gals gal") == ['gallon', 'gallons', 'gals', 'gal']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("fluid ounce fluid ounces fl oz fl ozs fluid oz fluid ozs fluid oz fluid ozs") == ['fluid ounce', 'fluid ounces', 'fl oz', 'fl ozs', 'fluid oz', 'fluid ozs', 'fluid oz', 'fluid ozs']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("milliliter milliliters ml mls") == ['milliliter', 'milliliters', 'ml', 'mls']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("liter liters l") == ['liter', 'liters', 'l']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("ounce ounces oz ozs oz ozs") == ['ounce', 'ounces', 'oz', 'ozs', 'oz', 'ozs']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("pound pounds lbs lb") == ['pound', 'pounds', 'lbs', 'lb']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("milligram milligrams mg mgs") == ['milligram', 'milligrams', 'mg', 'mgs']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("gram grams g") == ['gram', 'grams', 'g']

    # wilder tests
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == ['cups', 'teaspoons']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("This is another test string with pounds and liters") == ['pounds', 'liters']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("No units") == [] 
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ['cup']
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("tablespoonsstalks of lettuce") == []
    assert _regex_patterns.BASIC_UNITS_PATTERN.findall("tablespoons stalks of lettuce") == ['tablespoons']

def test_non_basic_units_pattern():

    # contains non-basic units
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("salmom fillet") == ['fillet']
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("1/2 cup of milk and 4 large stalks of lettuce") == ["stalks"]
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("tablespoons stalks of lettuce") == ["stalks"]

    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("100 cans of cubed thigh meat with a dash of meatloaf") == ["cans", "thigh", "dash"]
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("100 can of cubed thighs meat with a dashes of meatloaf") == ["can", "thighs", "dashes"]

    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("5 plates of wings") == ["plates", "wings"]
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("1 plate of wings") == ["plate", "wings"]

    # No non-basic units
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("This is a test string with cups and teaspoons") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("This is another test string with pounds and liters") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("No units") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("teaspoons tablespoon teaspoonful tablespoons table teaspoon tsp tspn tspns tspn. tspns. ts t t.") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("tbsp tbs tbsps tbl tbls tbsps. tbls. T") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("tsp tspn tspns tspn. tspns. ts t t.") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("cup cups C c") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("pint pints pt pts") == []
    assert _regex_patterns.NON_BASIC_UNITS_PATTERN.findall("tablespoonsstalks of lettuce") == []
