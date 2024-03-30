
# pytest library
import pytest

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _utils._fraction_str_to_decimal() utils function  ----
# -------------------------------------------------------------------------------

def test_fraction_str_to_decimal_whole_number():
    assert _utils._fraction_str_to_decimal("5") == '5'

def test_fraction_str_to_decimal_simple_fraction():
    assert _utils._fraction_str_to_decimal("1/2") == '0.5'

def test_fraction_str_to_decimal_complex_fraction():
    assert _utils._fraction_str_to_decimal("3/4") == '0.75'

def test_fraction_str_to_decimal_negative_fraction():
    assert _utils._fraction_str_to_decimal("-2/3") == '-0.667'

def test_fraction_str_to_decimal_zero_numerator():
    assert _utils._fraction_str_to_decimal("0/4") == '0'

def test_fraction_with_no_forward_slash():
    # with pytest.raises(ValueError):
    assert _utils._fraction_str_to_decimal("3.0") == '3'

def test_fraction_str_with_multiple_slashes():
    assert _utils._fraction_str_to_decimal("3/4/5") == "0.75" # TODO: probably should just raise an error

def test_whitespace_padded_fraction_1():
    assert _utils._fraction_str_to_decimal("  3/4  ") == '0.75'

def test_whitespace_padded_fraction_2():
    assert _utils._fraction_str_to_decimal("  3 /4  ") == '0.75'

def test_whitespace_padded_fraction_3():
    assert _utils._fraction_str_to_decimal("  3 / 4  ") == '0.75'

def test_decimals_in_fraction():
    assert  _utils._fraction_str_to_decimal("2.0/4.0") == '0.5'

def test_fraction_in_numerator_only():
    assert _utils._fraction_str_to_decimal("3.0/4") == '0.75'

def test_fraction_in_denominator_only():
    assert _utils._fraction_str_to_decimal("3/4.0") == '0.75'

def test_fraction_with_trailing_period():
    assert _utils._fraction_str_to_decimal("3/4.") == '0.75'

def test_fraction_with_leading_period():
    # assert _utils._fraction_str_to_decimal(".3/4") == '0' # NOTE: this should be 0.075 not 0
    assert _utils._fraction_str_to_decimal(".3/4") == '0.075' # NOTE: this should be 0.075 not 0

def test_fraction_with_leading_and_trailing_periods():
    # assert _utils._fraction_str_to_decimal(".3/4.") == '0' # NOTE: this should be 0.075 not 0
    assert _utils._fraction_str_to_decimal(".3/4.") == '0.075' # NOTE: this should be 0.075 not 0

# Error cases
def test_number_input_error():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal(3)

def test_float_input_error():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal(3.0)

def test_boolean_input_error():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal(True)

def test_invalid_characters_in_fraction_1():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal("43/aaaaa4")

def test_fraction_str_to_decimal_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        _utils._fraction_str_to_decimal("3/0")

def test_fraction_str_to_decimal_mixed_number_1():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal("1 1/2")

def test_fraction_str_to_decimal_mixed_number_2():
    with pytest.raises(ValueError):
        _utils._fraction_str_to_decimal("1/2 3")