# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the _replace_number_followed_by_inch_symbol() function -----

# -------------------------------------------------------------------------------

def test_replace_number_followed_by_inch_symbol_type1_1():
    assert _utils._replace_number_followed_by_inch_symbol("1 1/2\"") == "1 1/2inch"

def test_replace_number_followed_by_inch_symbol_type1_2():
    assert _utils._replace_number_followed_by_inch_symbol("1 1/2 inch") == "1 1/2 inch"

def test_replace_number_followed_by_inch_symbol_type1_3():
    assert _utils._replace_number_followed_by_inch_symbol('waffle round (4" dia)') == 'waffle round (4inch dia)'

def test_replace_number_followed_by_inch_symbol_type1_4():
    assert _utils._replace_number_followed_by_inch_symbol('waffle round (4 inch dia)') == 'waffle round (4 inch dia)'

def test_replace_number_followed_by_inch_symbol_type1_5():
    assert _utils._replace_number_followed_by_inch_symbol('waffle round (4 inch dia) 4"') == 'waffle round (4 inch dia) 4inch'

def test_replace_number_followed_by_inch_symbol_type2():
    assert _utils._replace_number_followed_by_inch_symbol('fruit (4-2/3” long x 2-3/4” dia)') =='fruit (4-2/3inch long x 2-3/4inch dia)'

def test_replace_number_followed_by_inch_symbol_type2_2():
    assert _utils._replace_number_followed_by_inch_symbol('fruit (4-2/3” long x 2-3/4” dia) 4"') =='fruit (4-2/3inch long x 2-3/4inch dia) 4inch'

def test_replace_number_followed_by_inch_symbol_decimal_type1():
    assert _utils._replace_number_followed_by_inch_symbol('1.5"') == '1.5inch'

def test_replace_number_followed_by_inch_symbol_decimal_type1_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('1.5  "') == '1.5  inch'

def test_replace_number_followed_by_inch_symbol_decimal_type2():
    assert _utils._replace_number_followed_by_inch_symbol('1.5”') == '1.5inch'

def test_replace_number_followed_by_inch_symbol_decimal_type2_multispaced():
     assert _utils._replace_number_followed_by_inch_symbol('1.5  ”') == '1.5  inch'

def test_replace_number_followed_by_inch_symbol_decimal_type2_multispaced_2():
        assert _utils._replace_number_followed_by_inch_symbol('1.5  ”  ') == '1.5  inch  '

def test_replace_number_followed_by_inch_symbol_fraction_type1():
    assert _utils._replace_number_followed_by_inch_symbol('1 1/2”') == '1 1/2inch'

def test_replace_number_followed_by_inch_symbol_fraction_type1_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('1 1/2  ”') == '1 1/2  inch'

def test_replace_number_followed_by_inch_symbol_fraction_type2():
    assert _utils._replace_number_followed_by_inch_symbol('1 1/2"') == '1 1/2inch'

def test_replace_number_followed_by_inch_symbol_fraction_type2_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('1 1/2  "') == '1 1/2  inch'

def test_replace_number_followed_by_inch_symbol_whole_number_type1():
    assert _utils._replace_number_followed_by_inch_symbol('4”') == '4inch'

def test_replace_number_followed_by_inch_symbol_whole_number_type1_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4  ”') == '4  inch'

def test_replace_number_followed_by_inch_symbol_whole_number_decimal_range_type1():
    assert _utils._replace_number_followed_by_inch_symbol('4-3/4”') == '4-3/4inch'

def test_replace_number_followed_by_inch_symbol_whole_number_decimal_range_type1_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4-3/4  ”') == '4-3/4  inch'

def test_replace_number_followed_by_inch_symbol_whole_number_decimal_range_type2():
    assert _utils._replace_number_followed_by_inch_symbol('4-3/4"') == '4-3/4inch'

def test_replace_number_followed_by_inch_symbol_whole_number_decimal_range_type2_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4-3/4  "') == '4-3/4  inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type1():
    assert _utils._replace_number_followed_by_inch_symbol('4.5-3/4”') == '4.5-3/4inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type1_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4.5-3/4  ”') == '4.5-3/4  inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type2():
    assert _utils._replace_number_followed_by_inch_symbol('4.5-3/4"') == '4.5-3/4inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type2_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4.5-3/4  "') == '4.5-3/4  inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type1_both_numbers_have_symbols():
    assert _utils._replace_number_followed_by_inch_symbol('4.5”-3/4”') == '4.5inch-3/4inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type1_both_numbers_have_symbols_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4.5  ”-3/4  ”') == '4.5  inch-3/4  inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type2_both_numbers_have_diff_symbols():
    assert _utils._replace_number_followed_by_inch_symbol('4.5”-3/4"') == '4.5inch-3/4inch'

def test_replace_number_followed_by_inch_symbol_decimal_decimal_range_type2_both_numbers_have_diff_symbols_multispaced():
    assert _utils._replace_number_followed_by_inch_symbol('4.5  ”-3/4  "') == '4.5  inch-3/4  inch'


    

