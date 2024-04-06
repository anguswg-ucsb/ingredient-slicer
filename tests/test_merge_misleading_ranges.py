# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _merge_misleading_ranges() utils function  ----
# -------------------------------------------------------------------------------

def test_misleading_range_whole_number_then_fraction():
    assert _utils._merge_misleading_ranges("1-1/2 cups of milk") == "1.5  cups of milk"

def test_misleading_range_whole_number_then_smaller_decimal_1():
    assert _utils._merge_misleading_ranges("1-0.5 cups of milk") == "1.5  cups of milk"

def test_misleading_range_whole_number_then_smaller_decimal_2():
    assert _utils._merge_misleading_ranges("3-0.5 cups of milk") == "3.5  cups of milk"

def test_misleading_range_whole_number_then_larger_decimal():
    assert _utils._merge_misleading_ranges("1-1.5 cups of milk") == "1-1.5 cups of milk"

def test_misleading_range_whole_number_then_smaller_whole_number():
    assert _utils._merge_misleading_ranges("3-2 cups of milk") == "6  cups of milk"

def test_misleading_range_whole_number_then_fraction_no_space_so_no_change():
    assert _utils._merge_misleading_ranges("1-1/2cups of milk") == "1-1/2cups of milk"

# -------------------------------------------------------------------------------
# ---- Error handling  ----
# -------------------------------------------------------------------------------

def test_misleading_range_integer_error():
    with pytest.raises(TypeError):
        assert _utils._merge_misleading_ranges(1)

def test_misleading_range_list_error():
    with pytest.raises(TypeError):
        assert _utils._merge_misleading_ranges([1,2,3])

def test_misleading_range_dict_error():
    with pytest.raises(TypeError):
        assert _utils._merge_misleading_ranges({"1": 1, "2": 2})

def test_misleading_range_tuple_error():
    with pytest.raises(TypeError):
        assert _utils._merge_misleading_ranges((1,2,3))

def test_misleading_range_float_error():
    with pytest.raises(TypeError):
        assert _utils._merge_misleading_ranges(1.5)

