# pytest library
import pytest

import re

from ingredient_slicer import _regex_patterns
# from ingredient_slicer import IngredientTools
# regex_map = IngredientTools()

def test_ALL_NUMBERS():
    assert _regex_patterns.ALL_NUMBERS.findall("I need 2 cups and 3/4 liters of sugar") == ['2', '3/4']
    assert _regex_patterns.ALL_NUMBERS.findall("The recipe calls for 3.5 liters of water") == ['3.5']
    assert _regex_patterns.ALL_NUMBERS.findall("Add 1/4 teaspoon of salt") == ['1/4']
    assert _regex_patterns.ALL_NUMBERS.findall("There are 10 tablespoons of butter") == ['10']
    assert _regex_patterns.ALL_NUMBERS.findall("We need 2 tspns of vanilla extract") == ['2']
    assert _regex_patterns.ALL_NUMBERS.findall("The dough requires 1tbsp of olive oil") == ['1']
    assert _regex_patterns.ALL_NUMBERS.findall("She added 4oz of chocolate chips") == ['4']
    assert _regex_patterns.ALL_NUMBERS.findall("1/2 and 4.43 cups of 4 cheese no 5ounce cup") == ['1/2', '4.43', '4', '5']
    assert _regex_patterns.ALL_NUMBERS.findall("1/2and 4.43 cups of 4 cheese no 5ounce cup") == ['1/2', '4.43', '4', '5']
    assert _regex_patterns.ALL_NUMBERS.findall("1/2 and 4.43cupsof4 cheese no 5ounce cup") == ['1/2', '4.43', '4', '5']
    assert _regex_patterns.ALL_NUMBERS.findall("1/4 4353.432 43/45") == ['1/4', '4353.432', '43/45']
    assert _regex_patterns.ALL_NUMBERS.findall("1/and 4.43 cups of 4 cheese no 5ounce cup") == ['1', '4.43', '4', '5']
    assert _regex_patterns.ALL_NUMBERS.findall("1and 4.43 cups of 4 cheese no 5 ounce cup") == ['1', '4.43', '4', '5']

def test_SPACE_SEP_NUMBERS():
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("I need 2 1/4 cups of sugar") == ['2 1/4']
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("The recipe calls for 3.5 liters of water") == []
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("Add 1/4 teaspoon of salt and 1/2 cup of sugar") == []
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("There are 10 tablespoons of butter & 2 tspns of vanilla extract") == []

    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1 23") == ["1 23"]
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1 23 4") == ["1 23"]
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1 23 4 5") == ["1 23", "4 5"]
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1 23 4 5 6") == ["1 23", "4 5"]
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1 23 4 5 6 7 8") == ["1 23", "4 5", "6 7"]
    assert _regex_patterns.SPACE_SEP_NUMBERS.findall("1    23 4 5   6 7") == ["1    23", "4 5", "6 7"]

def test_QUANTITY_BASIC_UNIT_GROUPS():
    # Simple test cases
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("1 cup of sugar") == [('1', 'cup')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("2 tablespoons of oil") == [('2', 'tablespoons')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("0.5 tsp of salt") == [('0.5', 'tsp')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("3 lbs of apples") == [('3', 'lbs')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("100 grams of flour") == [('100', 'grams')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("2 liters of water") == [('2', 'liters')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cups") == [('1/2', 'cups')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cups tablespoons") == [('1/2', 'cups')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("17/8 9/10 cups tablespoons") == [('17/8', 'cups')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("2.555 cups tablespoons") == [('2.555', 'cups')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("2.555cups tablespoons") == [('2.555', 'tablespoons')] # TODO: this needs to big fixed, probably should match [('2.555', 'cups')] 
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11 22 33dsdf pints") == [('11', 'pints')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55dsdf pints") == [('11.22', 'pints')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 pints") == [('11.22', 'pints')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 pints 33") == [('11.22', 'pints')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 pints 33 33 cups") == [('11.22', 'pints'), ('33', 'cups')]

    # more complex test cases
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("Add 1/2 teaspoon of salt to the mixture and mix it well.") == [('1/2', 'teaspoon')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("Use 3 tbls of olive oil for frying the chicken and 2 cups of flour for coating.") == [('3', 'tbls'), ('2', 'cups')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("Prepare a batter with 1.5 cups of milk, 1/4 cup of sugar, and 2 tablespoons of melted butter.") == [('1.5', 'cups'), ('1/4', 'cup'), ('2', 'tablespoons')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("For the sauce, mix 300 ml of cream with 50 grams of grated cheese and a pinch of salt.") == [('300', 'ml'), ('50', 'grams')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("The recipe requires 2.5 lbs of beef, 1 liter of beef broth, and 3 tablespoons of soy sauce.") == [('2.5', 'lbs'), ('1', 'liter'), ('3', 'tablespoons')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("please 1 big ol' cup of regexes with 3 small tablespoons of unit tests") == [('1', 'cup'), ('3', 'tablespoons')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("please 1 big ol' cup of regexes with a tablespoon of unit tests") == [('1', 'cup')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("please 1 big ol' cup of regexes with a 3 2 tablespoon of unit tests") == [('1', 'cup'), ('3', 'tablespoon')]
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("please 1 big ol' cup of regexes with a 3 tablespoon cups plus 55 tablespoon of unit tests") == [('1', 'cup'), ('3', 'tablespoon'), ('55', 'tablespoon')]

    # no match cases
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("1 2 3 4 5 6 7 8 9 10") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("tablespoons") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 33") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 33 33") == []
    assert _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11 22 33dsdf pints") == [('11', 'pints')]

# make a similar test for non-basic units
def test_QUANTITY_NON_BASIC_UNIT_GROUPS():
    # Simple test cases
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("1 can of tomatoes") == [('1', 'can')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2 cans of tomatoes") == [('2', 'cans')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("1/2 can of tomatoes") == [('1/2', 'can')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("3 1/2 cans of tomatoes") == [('3', 'cans')] # TODO: Maybe this should match [('3 1/2', 'cans')] or [('3', 'cans')] or [('3', '1/2', 'cans')] or [('1/2', 'cans')] instead ?
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cans") == [('1/2', 'cans')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cans tablespoons") == [('1/2', 'cans')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("17/8 9/10 cans tablespoons") == [('17/8', 'cans')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2.555 cans tablespoons") == [('2.555', 'cans')]

    # More complex test cases

    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2 pkgs, 44 strips of bacon") == [('2', 'pkgs'), ('44', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("pkgs, 44 strips of bacon") == [('44', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("44 big cups of strips of bacon") == [('44', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11 22 33dsdf strips") == [('11', 'strips')]

    # Cases where the non-basic unit is not at the end of the string and there are basic units in the string as well
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2 cups, 44 strips of bacon") == [('2', 'strips')] # TODO: This should match [('44', 'strips')] instead not [('2', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2 handfuls cups, 44 strips of bacon") == [('2', 'handfuls'), ('44', 'strips')] 
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2 cups handfuls cups, 44 strips of bacon") == [('2', 'handfuls'), ('44', 'strips')] 
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2.55 cups handfuls cups, 44 strips of bacon") == [('2.55', 'handfuls'), ('44', 'strips')] 
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2.55cups handfulscups, 44 strips of bacon") == [('2.55', 'strips')] # TODO: This should either just match [('44', 'strips')] or it should match both [('2.55', 'strips')] and  [('44', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("4353463 scoops of large pkgs") == [('4353463', 'scoops')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("4522 scoops 4.5 pkgs") == [('4522', 'scoops'), ('4.5', 'pkgs')] 

    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55dsdf strips") == [('11.22', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 strips") == [('11.22', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 strips 33") == [('11.22', 'strips')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 strips 33 33 pkgs") == [('11.22', 'strips'), ('33', 'pkgs')]
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 cups 33 33 pkgs") == [('11.22', 'pkgs')] # TODO: This should match [('33', 'pkgs')] instead not [('11.22', 'pkgs')]

    # No match cases
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("2.555cans tablespoons") == [] 
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11 22 33dsdf pints") == []
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11.22.55dsdf pints") == []
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11.22.55 pints") == []
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11.22.55 pints 33") == []
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11 22 33dsdf pints") == []
    assert _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall("cans tablespoons cans tablespoons 11.22.55dsdf pints") == []


# now make a similar test for ALL units using the regex.map.QUANTITY_UNIT_GROUPS pattern
def test_QUANTITY_UNIT_GROUPS():
    # Simple test cases
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("1 cup of sugar") == [('1', 'cup')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 tablespoons of oil") == [('2', 'tablespoons')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("0.5 tsp of salt") == [('0.5', 'tsp')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("3 lbs of apples") == [('3', 'lbs')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("100 grams of flour") == [('100', 'grams')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 liters of water") == [('2', 'liters')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cups") == [('1/2', 'cups')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("1/2 3/4 5/6 7/8 9/10 cups tablespoons") == [('1/2', 'cups')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("17/8 9/10 cups tablespoons") == [('17/8', 'cups')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2.555 cups tablespoons") == [('2.555', 'cups')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2.555cups tablespoons") == [('2.555', 'tablespoons')] # TODO: this needs to big fixed, probably should match [('2.555', 'cups')] 
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2.555cans tablespoons") == [('2.555', 'tablespoons')] # TODO: this needs to big fixed, probably should match [('2.555', 'cans')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11 22 33dsdf pints") == [('11', 'pints')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55dsdf pints") == [('11.22', 'pints')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 pints") == [('11.22', 'pints')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55 pints 33") == [('11.22', 'pints')]

    # More complex test cases
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("Add 1/2 teaspoon of salt to the mixture and mix it well.") == [('1/2', 'teaspoon')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("Use 3 tbls of olive oil for frying the chicken and 2 cups of flour for coating.") == [('3', 'tbls'), ('2', 'cups')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("Prepare a batter with 1.5 cups of milk, 1/4 cup of sugar, and 2 tablespoons of melted butter.") == [('1.5', 'cups'), ('1/4', 'cup'), ('2', 'tablespoons')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("For the sauce, mix 300 ml of cream with 50 grams of grated cheese and a pinch of salt.") == [('300', 'ml'), ('50', 'grams')]

    # more cases of basic AND non basic units in the same string
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 pkgs, 44 strips of bacon") == [('2', 'pkgs'), ('44', 'strips')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("pkgs, 44 strips of bacon") == [('44', 'strips')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("44 big cups of strips of bacon") == [('44', 'cups')] 
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 diced cups of onions, 13 packages of yogurt, 1 slice apple, and 1.4232 gallons of milk") == [('2', 'cups'), ('13', 'packages'), ('1', 'slice'), ('1.4232', 'gallons')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 diced cups of onions, 13 12lb yogurts , 44 apples, and 1/2 a stick of butter") == [('2', 'cups'), ('13', 'stick')] # TODO: Fix needed, this should match [('2', 'cups'), ('13', 'lb'), ('1/2', 'stick')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 diced cups of onions, 12lbs yogurts , 44 apples, and 1/2 a stick of butter") == [('2', 'cups'), ('12', 'stick')] # TODO: this is a really odd, badly written string, not sure if it should match anything / its just okay that it fails to correctly get what we need 
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("2 diced cups of onions, 12 lbs yogurts , 44 ounces apples, and 1/2 a stick of butter") == [('2', 'cups'), ('12', 'lbs'), ('44', 'ounces'), ('1/2', 'stick')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons cups tablespoons 11.22.55dsdf strips") == [('11.22', 'strips')]
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cups tablespoons 12cups tablespoons 11.22.55dsdf strips") == [('12', 'tablespoons'), ('11.22', 'strips')] # TODO: This should match [('12', 'cups'), ('11.22', 'strips')]

    # no match cases
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cans tablespoons cans tablespoonsints") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cans tablespoons cans tablespoons ints") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cans tablespoons cans tpints") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cans tablespoons cans tablespoonsts 33") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("cans tablespoons cans tablespoons f pints") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("555555") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("123 4 333 fcsdgsas") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("") == []
    assert _regex_patterns.QUANTITY_UNIT_GROUPS.findall("1 1 1 1 111") == []


def test_EQUIV_QUANTITY_UNIT_GROUPS():
    # Simple test cases
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 1 cup of sugar") == [('about', '1', 'cup')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("approximately 2 tablespoons of oil") == [('approximately', '2', 'tablespoons')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around 0.5 tsp of salt") == [('around', '0.5', 'tsp')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("roughly 3 lbs of apples") == [('roughly', '3', 'lbs')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("est. 100 grams of flour") == [('est', '100', 'grams')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estimated 2 liters of water") == [('estimated', '2', 'liters')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim 1/2 3/4 5/6 7/8 9/10 cups") == [('estim', '1/2', 'cups')] # TODO: need to clean up this extra whitespace after the approximate unit string
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("approx 1/2 3/4 5/6 7/8 9/10 cups tablespoons") == [('approx', '1/2', 'cups')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 17/8 9/10 cups tablespoons") == [('about', '17/8', 'cups')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around 2.555 cups tablespoons") == [('around', '2.555', 'cups')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("est. 2.555cups tablespoons") == [('est', '2.555', 'tablespoons')] # TODO: need to fix this matching with the period issue, this should match the "est." with the period included but it does NOT
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estimated 2.555cans tablespoons") == [('estimated', '2.555', 'tablespoons')]

    # assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estimated cups tablespoons cups tablespoons 11 22 33dsdf pints") == [('estimated', '11', 'pints')]
    # assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cups tablespoons cups tablespoons 11.22.55dsdf pints") == [('estim', '11.22', 'pints')]
    # assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cups tablespoons cups tablespoons 11.22.55 pints") == [('estim', '11.22', 'pints')]
    # assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cups tablespoons cups tablespoons 11.22.55 pints 33") == [('estim', '11.22', 'pints')]

    # More complex test cases
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("roughly Add 1/2 teaspoon of salt to the mixture and mix it well.") == [('roughly', '1/2', 'teaspoon')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about Use 3 tbls of olive oil for frying the chicken and 2 cups of flour for coating.") == [('about', '3', 'tbls')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around Prepare a batter with 1.5 cups of milk, 1/4 cup of sugar, and 2 tablespoons of melted butter.") == [('around', '1.5', 'cups')] # TODO: maybe need to rework this so it matches the output of the commented out test below:
    # assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around Prepare a batter with 1.5 cups of milk, 1/4 cup of sugar, and 2 tablespoons of melted butter.") == [('around', '1.5', 'cups'), ('around', '1/4', 'cup'), ('around', '2', 'tablespoons')]

    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim For the sauce, mix 300 ml of cream with 50 grams of grated cheese and a pinch of salt.") == [('estim', '300', 'ml')]

    # more cases of basic AND non basic units in the same string
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 2 pkgs, 44 strips of bacon") == [('about', '2', 'pkgs')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("roughly pkgs, 44 strips of bacon") == [('roughly', '44', 'strips')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("approx 44 big cups of strips of bacon") == [('approx', '44', 'cups')] 
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around 2 diced cups of onions, 13 packages of yogurt, 1 slice apple, and 1.4232 gallons of milk") == [('around', '2', 'cups')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 2 diced cups of onions, 13 12lb yogurts , 44 apples, and 1/2 a stick of butter") == [('about', '2', 'cups')] # TODO: Fix needed, this should match [('about', '2', 'cups'), ('about', '13', 'lb'), ('about', '1/2', 'stick')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("approximately 2 diced cups of onions, 12lbs yogurts , 44 apples, and 1/2 a stick of butter") == [('approximately', '2', 'cups')] # TODO: this is a really odd, badly written string, not sure if it should match anything / its just okay that it fails to correctly get what we need 
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 2 stalks of celery") == [('about', '2', 'stalks')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cups tablespoons cups tablespoons 11.22.55dsdf strips") == [('estim', '11.22', 'strips')]
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cups tablespoons 12cups tablespoons 11.22.55dsdf strips") == [('estim', '12', 'tablespoons')] # TODO:need to fix spacing after estim

    # no match cases
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cans tablespoons cans tablespoonsints") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about cans tablespoons cans tablespoons ints") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("around cans tablespoons cans tpints") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("roughly cans tablespoons cans tablespoonsts 33") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim cans tablespoons cans tablespoons f pints") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("about 555555") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("approximately 123 4 333 fcsdgsas") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("est. ") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("estim 1 1 1 1 111") == []
    assert _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall("3 cups about") == []

# ------------------------------------------
# ---- Deprecated tests for old regexes ----
# ------------------------------------------
# def test_ANY_NUMBER():
#     assert _regex_patterns.ANY_NUMBER.findall("I need 2 cups of sugar") == ['2']
#     assert _regex_patterns.ANY_NUMBER.findall("The recipe calls for 3.5 liters of water") == ['3.5']
#     assert _regex_patterns.ANY_NUMBER.findall("Add 1/4 teaspoon of salt") == ['1/4']
#     assert _regex_patterns.ANY_NUMBER.findall("There are 10 tablespoons of butter") == ['10']
#     assert _regex_patterns.ANY_NUMBER.findall("We need 2 tspns of vanilla extract") == ['2']
#     assert _regex_patterns.ANY_NUMBER.findall("The dough requires 1tbsp of olive oil") == []
#     assert _regex_patterns.ANY_NUMBER.findall("She added 4oz of chocolate chips") == []
#     assert _regex_patterns.ANY_NUMBER.findall("1 2 of 3") == ['1', '2', '3']
#     assert _regex_patterns.ANY_NUMBER.findall("1/2 and 4.43 cups of 4 cheese no 5ounce cup") == ['1/2', '4.43', '4']
#     assert _regex_patterns.ANY_NUMBER.findall("1/and 4.43 cups of 4 cheese no 5ounce cup") == ['1', '4.43', '4']
#     assert _regex_patterns.ANY_NUMBER.findall("1and 4.43 cups of 4 cheese no 5 ounce cup") == ['4.43', '4', '5']

# def test_ANY_NUMBER_THEN_UNIT():
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("I need 2 cups of sugar") == ['2 cups']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("The recipe calls for 3.5 liters of water") == ['3.5 liters']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("Add 1/4 teaspoon of salt") == ['1/4 teaspoon']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("There are 10 tablespoons of butter") == ['10 tablespoons']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("We need 2 tspns of vanilla extract") == ['2 tspns']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("The dough requires 1tbsp of olive oil") == ['1tbsp']
#     assert _regex_patterns.ANY_NUMBER_THEN_UNIT.findall("She added 4oz of chocolate chips") == ['4oz']

# def test_ANY_NUMBER_THEN_ANYTHING_THEN_UNIT():
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("I need 2 cups of sugar") == ['2 cups']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("The recipe calls for 3.5 liters of water") == ['3.5 liters']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("Add 1/4 teaspoon of salt") == ['1/4 teaspoon']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("There are 10 tablespoons of butter") == ['10 tablespoons']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("We need 2 tspns of vanilla extract") == ['2 tspns']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("The dough requires 1tbsp of olive oil") == ['1tbsp']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("She added 4oz of chocolate chips") == ['4oz']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("1 cup of sugar") == ['1 cup']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("1/2 cup of sugar") == ['1/2 cup']
#     assert _regex_patterns.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT.findall("i love to eat buckets of sugar, but 1 full hearty cup is too much for me! cup of sugar") == ['1 full']

