# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _find_and_remove_hyphens_around_substring() utils function  ----
# -------------------------------------------------------------------------------

def test_single_digit_whole_number_1():
    assert _utils._make_int_or_float_str("2") == "2"

def test_single_digit_whole_number_2():
    assert _utils._make_int_or_float_str("9") == "9"

def test_single_digit_decimal_number_1():
    assert _utils._make_int_or_float_str("2.0") == "2"

def test_multi_digit_whole_number_1():
    assert _utils._make_int_or_float_str("200") == "200"

def test_multi_digit_whole_number_2():
    assert _utils._make_int_or_float_str("900") == "900"

def test_multi_digit_decimal_number_1():
    assert _utils._make_int_or_float_str("2.5") == "2.5"

def test_multi_digit_decimal_number_2():
    assert _utils._make_int_or_float_str("90.5") == "90.5"

def test_multi_digit_decimal_number_3():
    assert _utils._make_int_or_float_str("90.0") == "90"

def test_multi_digit_decimal_number_4():
    assert _utils._make_int_or_float_str("90.00") == "90"

def test_multi_digit_decimal_number_5():
    assert _utils._make_int_or_float_str("90.000") == "90"

def test_multi_digit_decimal_number_numbers_separated_by_space_1():
    assert _utils._make_int_or_float_str("90.00 2") == '90.002'
# raise a ValueError if "90.00 2.0" is passed to _make_int_or_float_str

def test_multi_digits_separated_by_non_digit_1():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00 x 2.0")

def test_multi_digits_separated_by_non_digit_2():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00 2.0 x")

# raise a ValueError if "90.00 2.0" is passed to _make_int_or_float_str
def test_multi_digit_decimal_number_numbers_separated_by_space_error_1():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00 2.0")

def test_multi_digit_decimal_number_numbers_separated_by_space_error_2():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00 2.0 3.0")

def test_multi_periods_in_same_number_error_1():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00.0")

def test_multi_periods_in_same_number_error_2():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.005 .")


def test_number_with_non_digit_characters_error_1():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.00.0a")

def test_number_with_non_digit_characters_error_2():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("90.005 a")

def test_number_with_non_digit_special_characters_error_1():
    with pytest.raises(ValueError):
        _utils._make_int_or_float_str("-90.0")