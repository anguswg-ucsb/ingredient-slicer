# pytest library
import pytest

import re


from ingredient_slicer import _utils, _regex_patterns

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the find and remove utility function
# - _find_and_remove()
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- Test _find_and_remove() function -----
# -------------------------------------------------------------------------------

def test_find_and_remove_units_pattern():

    pattern = _regex_patterns.UNITS_PATTERN

    assert _utils._find_and_remove("cups of flour", pattern) == 'of flour'
    assert _utils._find_and_remove("1 cup of flour", pattern) == '1  of flour'
    assert _utils._find_and_remove("1/2 cup of flour", pattern) == '1/2  of flour'
    assert _utils._find_and_remove("1 1/2 cups of flour", pattern) == '1 1/2  of flour'
    assert _utils._find_and_remove("1 1/2 cups of flour", pattern) == '1 1/2  of flour'
    assert _utils._find_and_remove("1 1/2 cups of tablespoons flour", pattern) == '1 1/2  of  flour'
    assert _utils._find_and_remove("brocolli", pattern) == "brocolli"
    assert _utils._find_and_remove("brocolli stalks", pattern) == "brocolli"
    assert _utils._find_and_remove("brocolli florets", pattern) == "brocolli"

def test_find_and_remove_all_numbers_pattern():

    pattern = _regex_patterns.ALL_NUMBERS

    assert _utils._find_and_remove("1 cup of flour", pattern) == 'cup of flour'
    assert _utils._find_and_remove("1/2 cup of flour", pattern) == 'cup of flour'
    assert _utils._find_and_remove("1 1/2 cups of flour", pattern) == 'cups of flour'
    assert _utils._find_and_remove("1 1/2 cups of flour", pattern) == 'cups of flour'
    assert _utils._find_and_remove("1 1/2 cups of tablespoons flour", pattern) == 'cups of tablespoons flour'
    assert _utils._find_and_remove("brocolli", pattern) == "brocolli"
    assert _utils._find_and_remove("brocolli stalks", pattern) == "brocolli stalks"
    assert _utils._find_and_remove("brocolli florets", pattern) == "brocolli florets"

def test_find_and_remove_prep_words_pattern():

    pattern = _regex_patterns.PREP_WORDS_PATTERN

    assert _utils._find_and_remove("1 cup of flour", pattern) == '1 cup of flour'
    assert _utils._find_and_remove("brocolli", pattern) == "brocolli"
    assert _utils._find_and_remove("brocolli stalks", pattern) == "brocolli stalks"
    assert _utils._find_and_remove("brocolli florets", pattern) == "brocolli florets"

    assert _utils._find_and_remove("thinly sliced cheese", pattern) == "thinly  cheese"
    assert _utils._find_and_remove("diced and grated cheese", pattern) == "and  cheese"
    assert _utils._find_and_remove("firmly packed brown sugar", pattern) == "brown sugar"

def test_find_and_remove_words_ending_in_ly_pattern():

    pattern = _regex_patterns.WORDS_ENDING_IN_LY

    assert _utils._find_and_remove("1 cup of flour", pattern) == '1 cup of flour'
    assert _utils._find_and_remove("brocolli", pattern) == "brocolli"
    assert _utils._find_and_remove("brocolli stalks", pattern) == "brocolli stalks"
    assert _utils._find_and_remove("brocolli florets", pattern) == "brocolli florets"

    assert _utils._find_and_remove("thinly sliced cheese", pattern) == "sliced cheese"
    assert _utils._find_and_remove("diced and grated cheese", pattern) == "diced and grated cheese"
    assert _utils._find_and_remove("firmly packed brown sugar", pattern) == "packed brown sugar"
    assert _utils._find_and_remove("lightly finely majorly", pattern) == ""
