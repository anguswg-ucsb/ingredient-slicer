# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the _extract_dimensions() function -----
# -------------------------------------------------------------------------------

# ---- NO DIMENSION UNITS ----
def test_no_dimension_units_1():
    assert _utils._extract_dimensions("a couple of large apples") == ["a couple of large apples", []]

def test_no_dimension_units_2():
    assert _utils._extract_dimensions("1 cup of flour") == ["1 cup of flour", []]

# # -------------------------------------------------------------------------------
# # ---- Specific dimension units tests for each individual unit ----
# # -------------------------------------------------------------------------------
    
# ---- INCH ----
def test_number_with_inch_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 inch)") == ["a cup of flour ()", ["4 inch"]]

def test_number_then_inch_unit_no_space():
    assert _utils._extract_dimensions("a cup of flour 4inch") == ["a cup of flour", ["4inch"]]

def test_number_then_inch_unit_with_space():
    assert _utils._extract_dimensions("a cup of flour 4 inch") == ["a cup of flour", ["4 inch"]]

# # ---- INCHES ----
def test_number_with_inches_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 inches)") == ["a cup of flour ()", ["4 inches"]]

def test_number_then_inches_unit_no_space():
    assert _utils._extract_dimensions("a cup of flour 4inches") == ["a cup of flour", ["4inches"]]

def test_number_then_inches_unit_with_space():
    assert _utils._extract_dimensions("a cup of flour 4 inches") == ["a cup of flour", ["4 inches"]]

# ---- centimeters ----
def test_number_with_centimeters_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 centimeters)") == ["a cup of flour ()", ["4 centimeters"]]

# # ---- centimeter ----
def test_number_with_centimeter_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 centimeter)") == ["a cup of flour ()", ["4 centimeter"]]

def test_number_then_centimeter_unit_no_space():
    assert _utils._extract_dimensions("a cup of flour 4centimeter") == ["a cup of flour", ["4centimeter"]]

def test_number_then_centimeter_unit_with_space():
    assert _utils._extract_dimensions("a cup of flour 4 centimeter") == ["a cup of flour", ["4 centimeter"]]

# # ---- cm ----
def test_number_with_cm_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 cm)") == ["a cup of flour ()", ["4 cm"]]

def test_number_then_cm_unit_no_space():
    assert _utils._extract_dimensions("a cup of flour 4cm") == ["a cup of flour", ["4cm"]]

def test_number_then_cm_unit_with_space():
    assert _utils._extract_dimensions("a cup of flour 4 cm") == ["a cup of flour", ["4 cm"]]

# ---- millimeter ----
def test_number_with_millimeter_unit_in_parenthesis_with_space():
    assert _utils._extract_dimensions("a cup of flour (4 millimeter)") == ["a cup of flour ()", ["4 millimeter"]]


# # -------------------------------------------------------------------------------
# # ---- multiple dimension units next to each other ----
# # -------------------------------------------------------------------------------

# # ---- INCH ----
def test_multiple_inch_units_next_to_each_other():
    assert _utils._extract_dimensions("a cup of flour 4 inch 3 inch") == ["a cup of flour", ["4 inch", "3 inch"]]

def test_multiple_inch_units_next_to_each_other_without_space():
    assert _utils._extract_dimensions("a cup of flour 4inch 3inch") == ["a cup of flour", ["4inch", "3inch"]]

def test_multiple_inch_units_next_to_each_other_with_single_hyphen():
    assert _utils._extract_dimensions("a cup of flour 4-inch 3-inch") == ["a cup of flour", ["4-inch", "3-inch"]]

def test_multiple_inch_units_next_to_each_other_with_double_hyphen():
    assert _utils._extract_dimensions("a cup of flour 4--inch 3--inch") == ["a cup of flour", ["4--inch", "3--inch"]]

def test_multiple_inch_units_next_to_each_other_with_single_hyphen_and_space():
    assert _utils._extract_dimensions("a cup of flour 4- inch 3- inch") == ["a cup of flour", ["4- inch", "3- inch"]]

def test_multiple_inch_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides():
    assert _utils._extract_dimensions("a cup of flour 4 - inch 3 - inch") == ["a cup of flour", ["4 - inch", "3 - inch"]]

def test_multiple_inch_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides_and_extra_spaces():
    assert _utils._extract_dimensions("a cup of flour 4 -  inch 3 -  inch") == ["a cup of flour", ["4 -  inch", "3 -  inch"]]

def test_multiple_inch_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides_and_extra_spaces_and_extra_hyphens():
    assert _utils._extract_dimensions("a cup of flour 4 -  inch 3 -  inch 4--inch 3--inch") == ["a cup of flour", ["4 -  inch", "3 -  inch", "4--inch", "3--inch"]]

def test_two_inch_units_separated_by_x():
    assert _utils._extract_dimensions("a cup of flour 4 inch x 3 inch") == ["a cup of flour  x", ["4 inch", "3 inch"]]

def test_two_inch_units_separated_by_x_no_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4inch x 3inch") == ["a cup of flour  x", ["4inch", "3inch"]]

def test_number_without_unit_then_x_then_number_with_inch_units_no_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4 x 3inch") == ["a cup of flour 4 x", ["3inch"]]

def test_number_without_unit_then_x_then_number_with_inch_units_with_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4inch x3 inch") == ["a cup of flour  x", ["4inch", "3 inch"]]

# ---- INCHES ----
def test_multiple_inches_units_next_to_each_other():
    assert _utils._extract_dimensions("a cup of flour 4 inches 3 inches") == ["a cup of flour", ["4 inches", "3 inches"]]

def test_multiple_inches_units_next_to_each_other_without_space():
    assert _utils._extract_dimensions("a cup of flour 4inches 3inches") == ["a cup of flour", ["4inches", "3inches"]]

def test_multiple_inches_units_next_to_each_other_with_single_hyphen():
    assert _utils._extract_dimensions("a cup of flour 4-inches 3-inches") == ["a cup of flour", ["4-inches", "3-inches"]]

def test_multiple_inches_units_next_to_each_other_with_double_hyphen():
    assert _utils._extract_dimensions("a cup of flour 4--inches 3--inches") == ["a cup of flour", ["4--inches", "3--inches"]]

def test_multiple_inches_units_next_to_each_other_with_single_hyphen_and_space():
    assert _utils._extract_dimensions("a cup of flour 4- inches 3- inches") == ["a cup of flour", ["4- inches", "3- inches"]]

def test_multiple_inches_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides():
    assert _utils._extract_dimensions("a cup of flour 4 - inches 3 - inches") == ["a cup of flour", ["4 - inches", "3 - inches"]]

def test_multiple_inches_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides_and_extra_spaces():
    assert _utils._extract_dimensions("a cup of flour 4 -  inches 3 -  inches") == ["a cup of flour", ["4 -  inches", "3 -  inches"]]

def test_multiple_inches_units_next_to_each_other_with_single_hyphen_and_space_on_both_sides_and_extra_spaces_and_extra_hyphens():
    assert _utils._extract_dimensions("a cup of flour 4 -  inches 3 -  inches 4--inches 3--inches") == ["a cup of flour", ["4 -  inches", "3 -  inches", "4--inches", "3--inches"]]

def test_two_inches_units_separated_by_x():
    assert _utils._extract_dimensions("a cup of flour 4 inches x 3 inches") == ["a cup of flour  x", ["4 inches", "3 inches"]]

def test_two_inches_units_separated_by_x_no_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4inches x 3inches") == ["a cup of flour  x", ["4inches", "3inches"]]

def test_number_without_unit_then_x_then_number_with_inches_units_no_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4 x 3inches") == ["a cup of flour 4 x", ["3inches"]]

def test_number_without_unit_then_x_then_number_with_inches_units_with_spaces_between_number_and_unit():
    assert _utils._extract_dimensions("a cup of flour 4inches x3 inches") == ["a cup of flour  x", ["4inches", "3 inches"]]