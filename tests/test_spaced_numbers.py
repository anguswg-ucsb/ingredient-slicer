# pytest library
import pytest

import re


from ingredient_slicer import IngredientRegexPatterns
# regex_map = IngredientRegexPatterns()

@pytest.fixture
def regex_map():
    return IngredientRegexPatterns()

def test_no_match_spaced_numbers(regex_map):
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with cups and teaspoons") == []
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 is 2 a test string with cups 3 a 2 nd teaspoons") == []
    assert regex_map.SPACE_SEP_NUMBERS.findall("3 and  1.2") == []


def test_single_spaced_numbers(regex_map):
    # whole number then whole number
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 2") == ['1 2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  2") == ['1  2']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 2") == ['1 2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  2  ") == ['1  2']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 2  ") == ['1 2']
    
    # whole number then decimal
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 0.25") == ['1 0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  0.25") == ['1  0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 0.25") == ['1 0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  0.25  ") == ['1  0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 0.25  ") == ['1 0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 .25") == ["1 .25"]
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  .25") == ["1  .25"]
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 .25") == ["1 .25"]
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  .25  ") == ["1  .25"]

    # whole number then fractions
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 1/2") == ['1 1/2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1   2/3") == ['1   2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 2 /3") == ['1 2 /3']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  2/3  ") == ['1  2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1 2/3  ") == ['1 2/3']

    # decimal then whole number
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25 1") == ['0.25 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  1") == ['0.25  1']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 1") == ['0.25 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  1  ") == ['0.25  1']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 1  ") == ['0.25 1']

    # decimal then decimal
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25 0.5") == ['0.25 0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  0.5") == ['0.25  0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 0.5") == ['0.25 0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  0.5  ") == ['0.25  0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 0.5  ") == ['0.25 0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" .25 0.5  ") == ['25 0.5'] # TODO: fix this case where first number is a decimal without a leading 0
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25 .5  ") == ['0.25 .5'] 
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25   .5") == ['0.25   .5']

    # decimal then fractions
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25 1/2") == ['0.25 1/2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  2/3") == ['0.25  2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 2 /3") == ['0.25 2 /3']
    assert regex_map.SPACE_SEP_NUMBERS.findall("0.25  2/3  ") == ['0.25  2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 0.25 2/3  ") == ['0.25 2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall(".25 1/2") == ['25 1/2'] # TODO: fix this case where first number is a decimal without a leading 0

    # fractions then whole number
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2 1") == ['1/2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2  1") == ['1/2  1']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1/2 1") == ['1/2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2  1  ") == ['1/2  1']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1/2 1  ") == ['1/2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/ 2 1") == ['1/ 2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 /2 1") == ['1 /2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 / 2  1") == ['1 / 2  1']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  /  2 1  ") == ['1  /  2 1']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1  /  2  1  ") == ['1  /  2  1']

    # fractions then decimal
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2 0.25") == ['1/2 0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2  0.25") == ['1/2  0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1/2 0.25") == ['1/2 0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2 .25") == ['1/2 .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2  .25") == ['1/2  .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1/ 2 .25") == ['1/ 2 .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 /2 .25") == ['1 /2 .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 / 2  .25") == ['1 / 2  .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  /  2  .25") == ['1  /  2  .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1  /  2  .25") == ['1  /  2  .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1/2  .25  ") == ['1/2  .25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1 / 2  00.25") == ['1 / 2  00.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("1  /  2  00.25") == ['1  /  2  00.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall(" 1  /  2  0.25") == ['1  /  2  0.25']
    

def test_multiple_spaced_numbers(regex_map):
    # all whole numbers
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 3 4 5 6 7 8 9 10") == ['1 2', '3 4', '5 6', '7 8', '9 10']

    # whole numbers and decimals
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 3 4 5 6 7 8 9 10 0.25 0.5 0.75") == ['1 2', '3 4', '5 6', '7 8', '9 10', '0.25 0.5']

    # mix of whole numbers and decimals and fractions
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 0.25 0.5 2 3 0.75 2 1.25") == ['1 0.25', '0.5 2', '3 0.75', '2 1.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 0.25 0.5 2 3 0.75 2") == ['1 0.25', '0.5 2', '3 0.75']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 0.25 0.5 2 3 0.75") == ['1 0.25', '0.5 2', '3 0.75']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 0.25 0.5 2.0 3") == ['1 2', '0.25 0.5', '2.0 3']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 0.25 0.5 2.0") == ['1 2', '0.25 0.5']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 0.25 inserted 0.5 inserted 3 2/3") == ['1 2', '3 2/3']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 0.25 inserted 0.5 inserted 3") == ['1 2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a test string with 1 2 0.25 inserted 0.5 inserted") == ['1 2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a 2   4 test string with 1 2 0.25 inserted") == ['2   4', '1 2']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a 2   4 test string with 1 inserted 2  0.25") == ['2   4', '2  0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a 2   2/4 test string with 1 inserted 2  0.25") == ['2   2/4', '2  0.25']
    assert regex_map.SPACE_SEP_NUMBERS.findall("This is a 2   2/4 test string with 1 inserted 2/3  0.25 inserted") == ['2   2/4', '2/3  0.25']

def test_whole_number_fraction_spaced_number_ranges(regex_map):

    regex_map.SPACE_SEP_NUMBERS.findall("1 1/2 - 2 1/2 cups of flour") == ['1 1/2', '2 1/2']
    regex_map.SPACE_SEP_NUMBERS.findall("1 1/2 - 2 cups of sugar") == ['1 1/2']
    regex_map.SPACE_SEP_NUMBERS.findall("1 1/2 - 2 1/2 kg of sugar") == ['1 1/2', '2 1/2']
    regex_map.SPACE_SEP_NUMBERS.findall("1/4 - 1/2 liters-milk") == []
    regex_map.SPACE_SEP_NUMBERS.findall("10 3/4 - 11 1/4 oz of chocolate chips") == ['10 3/4', '11 1/4']
    regex_map.SPACE_SEP_NUMBERS.findall("1/10 - 5 2/10 lb of butter") == ['5 2/10']
    regex_map.SPACE_SEP_NUMBERS.findall("1 - 2 3-4") == ['2 3'] # TODO: This should probably NOT match anything 

    regex_map.SPACE_SEP_NUMBERS.findall("1 1/2 - 2 ./2 cups of flour") == ['1 1/2']
    regex_map.SPACE_SEP_NUMBERS.findall("1 1/2 - 2 .2 cups of flour") == ['1 1/2', '2 .2']
    regex_map.SPACE_SEP_NUMBERS.findall("1 .6 - 0.5 1/2 cups of flour") == ['1 .6', '0.5 1/2']

