# pytest library
import pytest

import re

from ingredient_slicer import IngredientRegexPatterns

# regex_map = IngredientRegexPatterns()

# regex_map.print_matches("twenty seven range is from 1-5")

@pytest.fixture
def regex_map():
    return IngredientRegexPatterns()


def test_prefixed_numbers_1(regex_map):

    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty seven is a number followed by a number") == [('twenty', 'seven')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("hundred twenty cabbages") == [('hundred', 'twenty')]

    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty-two lb bag") == [('twenty', 'two')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty -two lb bag") == [('twenty', 'two')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty - two lb bag") == [('twenty', 'two')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty -  two lb bag") == [('twenty', 'two')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty       two lb bag") == [('twenty', 'two')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty four") == [('eighty', 'four')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty-four") == [('eighty', 'four')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty - four") == [('eighty', 'four')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("nineteen eighty -four") == [('eighty', 'four')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("nineteen eighty - four") == [('eighty', 'four')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall(" eighty - eighty") == [('eighty', 'eighty')] # TODO: this seems like an odd match, should it match?
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty to forty five raisins") == [('forty', 'five')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty to forty-five raisins") == [('forty', 'five')]
    assert regex_map.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty-to-forty five raisins") == [('forty', 'five')]