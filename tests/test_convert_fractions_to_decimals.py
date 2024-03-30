
# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the _convert_fractions_to_decimals() function -----
# -------------------------------------------------------------------------------

def test_convert_fractions_to_decimals_whole_number_alone():
    assert _utils._convert_fractions_to_decimals("5") == '5'

def test_convert_fractions_to_decimals_simple_fraction():
    assert _utils._convert_fractions_to_decimals("1/2") == '0.5'

def test_convert_fractions_to_decimals_simple_fraction_with_left_spaces():
    assert _utils._convert_fractions_to_decimals(" 1/2") == ' 0.5'

def test_convert_fractions_to_decimals_simple_fraction_with_right_spaces():
    assert _utils._convert_fractions_to_decimals("1/2 ") == '0.5 '

def test_convert_fractions_to_decimals_simple_fraction_with_both_spaces():
    assert _utils._convert_fractions_to_decimals(" 1/2 ") == ' 0.5 '

def test_convert_fractions_to_decimals_space_after_numerator():
    assert _utils._convert_fractions_to_decimals("1 /2") == '0.5'

def test_convert_fractions_to_decimals_space_after_denominator():
    assert _utils._convert_fractions_to_decimals("1/ 2") == '0.5'

def test_convert_fractions_to_decimals_space_after_numerator_and_before_denominator():
    assert _utils._convert_fractions_to_decimals("1 / 2") == '0.5'

def test_convert_fractions_to_decimals_decimal_numerator():
    assert _utils._convert_fractions_to_decimals("0.5/2") == '0.25'

def test_convert_fractions_to_decimals_decimal_denominator():
    assert _utils._convert_fractions_to_decimals("1/0.5") == '2'

def test_convert_fractions_to_decimals_decimal_numerator_and_denominator():
    assert _utils._convert_fractions_to_decimals("0.5/0.5") == '1'

def test_convert_fractions_to_decimals_negative_fraction():
    assert _utils._convert_fractions_to_decimals("-2/3") == '-0.667'

def test_convert_fractions_to_decimals_zero_numerator():
    assert _utils._convert_fractions_to_decimals("0/4") == '0'

def test_convert_fractions_to_decimals_fraction_with_no_forward_slash():
    assert _utils._convert_fractions_to_decimals("3.0") == '3.0'

def test_convert_fractions_to_decimals_fraction_with_multiple_slashes():
    assert _utils._convert_fractions_to_decimals("3/4/5") == "0.75/5" # TODO: probably should just raise an error
# 0.75/5
# _utils._convert_fractions_to_decimals(_utils._convert_fractions_to_decimals(_utils._convert_fractions_to_decimals("3/4/5")))

def test_convert_fractions_to_decimals_whitespace_padded_fraction_1():
    assert _utils._convert_fractions_to_decimals("  3/4  ") == '  0.75  '

def test_convert_fractions_to_decimals_simple_fraction_then_words_then_decimal_fraction():
    assert _utils._convert_fractions_to_decimals("1/2 words words words 0.5/2") == '0.5 words words words 0.25'

def test_convert_fractions_to_decimals_simple_fraction_then_words_then_decimal_fraction_with_spaces_after_numerator():
    assert _utils._convert_fractions_to_decimals("1 /2 words words words 0.5 /2") == '0.5 words words words 0.25'

def test_convert_fractions_to_decimals_simple_fraction_then_words_then_decimal_fraction_with_spaces_after_denominator():
    assert _utils._convert_fractions_to_decimals("1/ 2 words words words 0.5/ 2") == '0.5 words words words 0.25'

def test_convert_fractions_to_decimals_simple_fraction_then_words_then_decimal_fraction_with_spaces_after_numerator_and_before_denominator():
    assert _utils._convert_fractions_to_decimals("1 / 2 words words words 0.5 / 2") == '0.5 words words words 0.25'


def test_mixed_fractions_with_whole_number_fractions():
    assert _utils._convert_fractions_to_decimals("1 1/2") == '1 0.5'

def test_mixed_fractions_with_whole_number_fractions_with_spaces():
    assert _utils._convert_fractions_to_decimals("1 1 / 2") == '1 0.5'

def test_mixed_fractions_with_decimal_fractions():
    assert _utils._convert_fractions_to_decimals("1 0.5/2") == '1 0.25'

def test_mixed_fractions_whole_numbers_with_dash_between():
    assert _utils._convert_fractions_to_decimals("1-1/2") == '1-0.5'

def test_mixed_fractions_with_whole_number_fractions_with_dash_between_with_spaces():
    assert _utils._convert_fractions_to_decimals("1-1 / 2") == '1-0.5'

def test_mixed_fractions_with_decimal_fractions_with_multiple_dashes_between():
    assert _utils._convert_fractions_to_decimals("1--1/2") == '1--0.5'

def test_mixed_fractions_with_decimal_fractions_with_multiple_dashes_between_with_spaces():
    assert _utils._convert_fractions_to_decimals("1- -1 / 2") == '1- -0.5'

def test_mixed_fractions_with_decimal_fractions_with_multiple_dashes_between_with_spaces_and_words():
    assert _utils._convert_fractions_to_decimals("1- -1 / 2 words words words 0.5 / 2") == '1- -0.5 words words words 0.25'

def test_mixed_fractions_with_decimal_fractions_with_multiple_dashes_between_with_spaces_and_words_and_punctuation():
    assert _utils._convert_fractions_to_decimals("1- -1 / 2 words words words 0.5 / 2.") == '1- -0.5 words words words 0.25.'


def test_fraction_with_trailing_period():
    assert _utils._convert_fractions_to_decimals("3/4.") == '0.75.'

def test_fraction_with_leading_period():
    assert _utils._convert_fractions_to_decimals(".3/4") == '.0.75'

def test_fraction_with_leading_and_trailing_periods():
    assert _utils._convert_fractions_to_decimals(".3/4.") == '.0.75.'