# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# ---- Test function for removing repeated units in ranges ----
# _remove_repeat_units_in_ranges()
# -------------------------------------------------------------------------------

def test_remove_repeat_units_in_ranges_same_unit():
    ingredient = "2 oz - 3 oz diced tomatoes"
    expected_result = "2 - 3 oz diced tomatoes"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_in_ranges_different_units():
    ingredient = "3cups-4 cups of cat food"
    expected_result = "3 - 4 cups of cat food"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_in_ranges_no_matches():
    ingredient = "1 cup of sugar"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == ingredient

def test_remove_repeat_units_in_ranges_mixed_case():
    ingredient = "2 Cups-3 cups of water"
    expected_result = "2 - 3 cups of water"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_in_ranges_decimal_quantities():
    ingredient = "1.5 cups - 2.5 cups of flour"
    expected_result = "1.5 - 2.5 cups of flour"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_in_ranges_fraction_quantities():
    ingredient = "1/2 cup - 2/3 cup of milk"
    expected_result = "1/2 - 2/3 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_ignores_plural_units_in_ranges_mixed_quantities():
    ingredient = "1/2 cup - 2.5 cups of milk"
    expected_result = "1/2 cup - 2.5 cups of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_ignores_differing_units_1():
    ingredient = "1 cup - 2 oz of milk"
    expected_result = "1 cup - 2 oz of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_ignores_differing_units_2():
    ingredient = "1 cup - 2 tablespoon of milk"
    expected_result = "1 cup - 2 tablespoon of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result


def test_remove_repeat_units_no_space_between_number_and_unit():
    ingredient = "1cup - 2cup of milk"
    expected_result = "1 - 2 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_no_space_between_number_and_unit_and_no_hypen_spaces():
    ingredient = "1cup-2cup of milk"
    expected_result = "1 - 2 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_hyphen_with_no_spaces():
    ingredient = "1 cup-2 cup of milk"
    expected_result = "1 - 2 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_hyphen_with_spaces_and_no_space_between_left_number_unit():
    ingredient = "1cup - 2 cup of milk"
    expected_result = "1 - 2 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result

def test_remove_repeat_units_hyphen_with_spaces_and_no_space_between_right_number_unit():
    ingredient = "1 cup - 2cup of milk"
    expected_result = "1 - 2 cup of milk"
    assert _utils._remove_repeat_units_in_ranges(ingredient) == expected_result