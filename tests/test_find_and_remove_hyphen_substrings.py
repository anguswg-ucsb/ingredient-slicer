# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _find_and_remove_hyphens_around_substring() utils function  ----
# -------------------------------------------------------------------------------

def test_single_hyphens_around_a_to():
    assert _utils._find_and_remove_hyphens_around_substring("I love cats -to- dogs to ", "to") == "i love cats to dogs to"

def test_multiple_hyphen_padded_substrings_1():
    assert _utils._find_and_remove_hyphens_around_substring("g -to- -to- -to-", "to") == "g to to to"

def test_multiple_hyphen_padded_substrings_2():
    assert _utils._find_and_remove_hyphens_around_substring("-to- -to- -to-", "to") == "to to to"

def test_single_hyphen_padded_substrings_4():
    assert _utils._find_and_remove_hyphens_around_substring("1-to-three cups of tomato-juice", "to") == "1 to three cups of tomato-juice"

def test_for_more_than_one_substring_surrounded_with_hyphens_1():
    assert _utils._find_and_remove_hyphens_around_substring("i love chocolate cake -but- i won't --eat-- it", "but") == "i love chocolate cake but i won't --eat-- it"

def test_for_more_than_one_substring_surrounded_with_hyphens_2():
    assert _utils._find_and_remove_hyphens_around_substring("i love chocolate cake -but- i won't --eat-- it", "eat") == "i love chocolate cake -but- i won't eat it"

def test_substrings_that_include_hyphens():
    assert _utils._find_and_remove_hyphens_around_substring("remove -my- lovely hyphens!", "my-") == 'remove my lovely hyphens!'
    assert _utils._find_and_remove_hyphens_around_substring("remove -my- lovely hyphens!", "-my-") == 'remove my lovely hyphens!'
    assert _utils._find_and_remove_hyphens_around_substring("remove -my- lovely hyphens!", "-my") == 'remove my lovely hyphens!'
    assert _utils._find_and_remove_hyphens_around_substring("remove -my- lovely hyphens!", "my-------") == 'remove my lovely hyphens!'


def test_empty_substring():
    assert _utils._find_and_remove_hyphens_around_substring("I want tests to write themselves", "") == "i want tests to write themselves"
    assert _utils._find_and_remove_hyphens_around_substring("please ai save me somehow", "") == "please ai save me somehow"

def test_empty_string():
    assert _utils._find_and_remove_hyphens_around_substring("", "to") == ""
    assert _utils._find_and_remove_hyphens_around_substring("", "") == ""

def test_hyphen_only_string():
    assert _utils._find_and_remove_hyphens_around_substring("-", "to") == "-"
    assert _utils._find_and_remove_hyphens_around_substring("-", "-") == ""
    assert _utils._find_and_remove_hyphens_around_substring("-----", "") == "" # TODO: this is not right