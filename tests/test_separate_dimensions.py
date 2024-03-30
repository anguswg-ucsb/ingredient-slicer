# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _utils._separate_dimensions() function -----
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- NO DIMENSION UNITS ----
# -------------------------------------------------------------------------------

def test_separate_dimensions_with_no_dimension_units_1():
    assert _utils._separate_dimensions("a couple of large apples") == ["a couple of large apples", []]

def test_separate_dimensions_with_no_dimension_units_2():
    assert _utils._separate_dimensions("1 cup of flour (2 oz)") == ['1 cup of flour (2 oz)', []]

# -------------------------------------------------------------------------------
# ---- Two same dimension units separated by "x" ----
# -------------------------------------------------------------------------------

# lower case "x"
def test_separate_dimensions_two_same_dimension_units_separated_by_x():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches x 2 inches)") == ['apple medium slice (approx )', ['3 inches x 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_x_no_space_before_second_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches x2 inches)") == ['apple medium slice (approx )', ['3 inches x2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_x_no_space_after_first_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3inches x 2 inches)") == ['apple medium slice (approx )', ['3inches x 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_x_no_space_in_entire_range():
    assert _utils._separate_dimensions("apple medium slice (approx 3inchesx2inches)") == ['apple medium slice (approx )', ['3inchesx2inches']]

# Capital "X"
def test_separate_dimensions_two_same_dimension_units_separated_by_X():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches X 2 inches)") == ['apple medium slice (approx )', ['3 inches X 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_X_no_space_before_second_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches X2 inches)") == ['apple medium slice (approx )', ['3 inches X2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_X_no_space_after_first_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3inches X 2 inches)") == ['apple medium slice (approx )', ['3inches X 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_X_no_space_in_entire_range():
    assert _utils._separate_dimensions("apple medium slice (approx 3inchesX2inches)") == ['apple medium slice (approx )', ['3inchesX2inches']]


# -------------------------------------------------------------------------------
# ---- Two same dimension units separated by "by" ----
# -------------------------------------------------------------------------------

def test_separate_dimensions_two_same_dimension_units_separated_by_by():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches by 2 inches)") == ['apple medium slice (approx )', ['3 inches by 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_by_no_space_before_second_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches by2 inches)") == ['apple medium slice (approx )', ['3 inches by2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_by_no_space_after_first_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3inches by 2 inches)") == ['apple medium slice (approx )', ['3inches by 2 inches']]

def test_separate_dimensions_two_same_dimension_units_separated_by_by_no_space_in_entire_range():
    assert _utils._separate_dimensions("apple medium slice (approx 3inchesby2inches)") == ['apple medium slice (approx )', ['3inchesby2inches']]


# -------------------------------------------------------------------------------
# ---- Two different dimension units separated by "x" or "by" ----
# -------------------------------------------------------------------------------
    
def test_separate_dimensions_two_different_dimension_units_separated_by_x():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches x 2 cm)") == ['apple medium slice (approx )', ['3 inches x 2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_x_no_space_before_second_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches x2 cm)") == ['apple medium slice (approx )', ['3 inches x2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_x_no_space_after_first_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3inches x 2 cm)") == ['apple medium slice (approx )', ['3inches x 2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_x_no_space_in_entire_range():
    assert _utils._separate_dimensions("apple medium slice (approx 3inchesx2cm)") == ['apple medium slice (approx )', ['3inchesx2cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_by():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches by 2 cm)") == ['apple medium slice (approx )', ['3 inches by 2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_by_no_space_before_second_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3 inches by2 cm)") == ['apple medium slice (approx )', ['3 inches by2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_by_no_space_after_first_number():
    assert _utils._separate_dimensions("apple medium slice (approx 3inches by 2 cm)") == ['apple medium slice (approx )', ['3inches by 2 cm']]

def test_separate_dimensions_two_different_dimension_units_separated_by_by_no_space_in_entire_range():
    assert _utils._separate_dimensions("apple medium slice (approx 3inchesby2cm)") == ['apple medium slice (approx )', ['3inchesby2cm']]

# -------------------------------------------------------------------------------

# _separate_dimensions("apple medium slice (approx 3 inches x 2 inches x 0.25 inches)")
# _separate_dimensions("apple medium slice (approx 3 inches x 2 inches)")
# _separate_dimensions("apple medium slice (2 ounces or approx 3 inches x 2 inches x 1/25inch)")
# _separate_dimensions("apple medium slice (2 ounces or approx 3 inches x 2 inches)")