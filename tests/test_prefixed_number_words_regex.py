# pytest library
import pytest

import re

from ingredient_slicer import _regex_patterns

def test_prefixed_number_words_1():
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty five eggs") == [('twenty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("hundred twenty eggs") == [('hundred', 'twenty')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty-two lb bag") == [('twenty', 'two')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty -two lb bag") == [('twenty', 'two')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty - two lb bag") == [('twenty', 'two')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty -  two lb bag") == [('twenty', 'two')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty       two lb bag") == [('twenty', 'two')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty four") == [('eighty', 'four')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty-four") == [('eighty', 'four')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("19 eighty - four") == [('eighty', 'four')]


def test_prefixed_number_words_2():
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("nineteen eighty -four") == [('eighty', 'four')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("nineteen eighty - four") == [('eighty', 'four')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall(" eighty - eighty") == [('eighty', 'eighty')] # TODO: this seems like an odd match, should it match?
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty to forty five raisins") == [('forty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty to forty-five raisins") == [('forty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("forty-to-forty five raisins") == [('forty', 'five')]

def test_prefixed_number_words_3():

    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("twenty seven is a number followed by a number") == [('twenty', 'seven')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("hundred twenty cabbages") == [('hundred', 'twenty')]

def test_prefixed_number_words_4():

    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty five lb bag") == [('twenty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a fifty four and twenty-five lb bag") == [('fifty', 'four'), ('twenty', 'five')] 
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a fifty four and twenty five lb bag") == [('fifty', 'four'), ('twenty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty hundreds") == [('twenty', 'hundreds')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty hundred") == [('twenty', 'hundred')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a two hundred and twenty five") == [('twenty', 'five')]
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("55 grams of cereal with a thirty-two miligrams of milk") == [('thirty', 'two')]

def test_prefixed_number_words_5():
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a 20 five lb bag") == []
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a two hundred") == []
    assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a two hundred and twenty") == []
