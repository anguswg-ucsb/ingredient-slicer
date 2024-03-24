import pytest
from ingredient_slicer import _utils

@pytest.mark.parametrize("input_string, expected_output", [
    ("1/2 - 2 oz", "1.25 oz"),
    ("5-10 oz of steak", "7.5 oz of steak"),
    ("1 - 2 or 5-10 oz", "1.5 or 7.5 oz"),
    ("1 - 2 - 4 ft", "2.75 ft"),
    ("1 - 2 or 5-10 oz", "1.5 or 7.5 oz"),
    ("1/2 - 2 oz", "1.25 oz"),
    ("23300------3223", "23300------3223"),
    ("1 ft", "1 ft"),
    ("testing is so fun", "testing is so fun"),
    ("i love 2-4 tests per day", "i love 3 tests per day"),
    ("1- 3 1/2 tests a day keeps the doctor away", "2 1/2 tests a day keeps the doctor away"),

])

def test_avg_ranges(input_string, expected_output):
    assert _utils.avg_ranges(input_string) == expected_output

def test_no_number_ranges():
    assert _utils.avg_ranges("testing is so fun") == "testing is so fun"

def test_hyphen_only_ranges():
    assert _utils.avg_ranges(" - ") == "-"

def test_single_number_than_hyphen():
    assert _utils.avg_ranges("1 - ") == "1 -"

def test_single_number_than_hyphen_than_number():
    assert _utils.avg_ranges("1 - 2") == "1.5"

def test_single_number_than_hyphen_than_number_than_hyphen():
    assert _utils.avg_ranges("1 - 2 -") == "1.5 -"

def test_single_number_than_hyphen_than_number_than_hyphen_than_number():
    assert _utils.avg_ranges("1 - 2 - 3") == "2.25"

def test_single_number_than_hyphen_than_number_than_hyphen_than_number_than_hyphen():
    assert _utils.avg_ranges("1 - 2 - 3 -") == "2.25 -"

def test_single_number_than_hyphen_than_number_than_hyphen_than_number_than_hyphen_than_number():
    assert _utils.avg_ranges("1 - 2 - 3 - 4") == "3.125"

def test_integer_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges(1)

def test_list_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges([1,2,3])

def test_dict_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges({"1": 1, "2": 2})

def test_tuple_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges((1,2,3))

def test_float_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges(1.5)

def test_boolean_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges(True)
    with pytest.raises(ValueError):
        _utils.avg_ranges(False)
                          
def test_none_input():
    with pytest.raises(ValueError):
        _utils.avg_ranges(None)
            

