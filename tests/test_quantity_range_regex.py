# Unit tests for regular expressions that match ranges of quantities in recipes
# pytest library
import pytest

import re


from ingredient_slicer import _regex_patterns

# Test cases for QUANTITY_DASH_QUANTITY
def test_QUANTITY_DASH_QUANTITY():
    
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1-5") == ['1-5']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-5-") == ["1-5"]
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-2-3") == ['1-2'] # TODO: Maybe this should fail or return both 1-2 and 2-3 or just 1-3 ? Not sure
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-2-3-") == ['1-2'] # TODO: Maybe this should fail or return both 1-2 and 2-3 or just 1-3 ? Not sure
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1 - 3") == ["1 - 3"] 
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1- 3") == ["1- 3"] 
    
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-2-3-4") == ['1-2', '3-4'] 

    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 0.5-2.5") == ['0.5-2.5']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1/2-3/4") == ['1/2-3/4']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 0.5-1/2") == ['0.5-1/2']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1-1.5") == ['1-1.5']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1.5-3") == ['1.5-3']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 3/4-1.5") == ['3/4-1.5']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 2.5-3/4") == ['2.5-3/4']

    # Multiple matches
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-2-3-4") == ['1-2', '3-4'] 
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("the range is 1-2-3-4-5-6-7)") == ['1-2', '3-4', '5-6']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1-5 and 0.5-2.5") == ['1-5', '0.5-2.5']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1/2-3/4 and 0.5-1/2") == ['1/2-3/4', '0.5-1/2']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1-1.5 and 1.5-3") == ['1-1.5', '1.5-3']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 3/4-1.5 and 2.5-3/4") == ['3/4-1.5', '2.5-3/4']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1-5 and 0.5-2.5 and 1/2-3/4 and 0.5-1/2") == ['1-5', '0.5-2.5', '1/2-3/4', '0.5-1/2']

    # no matches
    # assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 15 cups") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 0.5tablespoons") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 1/2pounds") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("The range is from 0.5grams") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1_5") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1-") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("11212/21") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("11555555 5454") == []
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1 -- 3") == [] # TODO: THIS SHOULD MATCH with ["1 -- 3"]
    assert _regex_patterns.QUANTITY_DASH_QUANTITY.findall("1- - 3") == [] # TODO: THIS SHOULD MATCH with ["1- - 3"]


# Test cases for QUANTITY_DASH_QUANTITY_UNIT
def test_QUANTITY_DASH_QUANTITY_UNIT():
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1-5 cups") == ['1-5 cups']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 0.5-2.5 tablespoons") == ['0.5-2.5 tablespoons']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1/2-3/4 pounds") == ['1/2-3/4 pounds']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 0.5-1/2 grams") == ['0.5-1/2 grams']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1-1.5 liters") == ['1-1.5 liters']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1.5-3 milliliters") == ['1.5-3 milliliters']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 3/4-1.5 kilograms") == ['3/4-1.5 kilograms']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 2.5-3/4 inches") == ['2.5-3/4'] # NOTE: Inches is NOT considered a unit for now

    # Multiple matches
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1-5 cups and 0.5-2.5 tablespoons") == ['1-5 cups', '0.5-2.5 tablespoons']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1/2-3/4 pounds and 0.5-1/2 grams") == ['1/2-3/4 pounds', '0.5-1/2 grams']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 1-1.5 liters and 1.5-3 milliliters") == ['1-1.5 liters', '1.5-3 milliliters']
    assert _regex_patterns.QUANTITY_DASH_QUANTITY_UNIT.findall("The range is from 3/4-1.5 kilograms and 2.5-3/4 inches") == ['3/4-1.5 kilograms', '2.5-3/4']


