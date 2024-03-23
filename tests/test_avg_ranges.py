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

# "1/2 - 2 or 1/2 - 4"
# "1/2 - 2 - 1/2 - 4"
# avg_ranges("1-2 oz")
# avg_ranges("1 - 2 - 4 ft")
# avg_ranges("1 - 2 or 5-10 ft")
# avg_ranges("1 - 2 - 5-10 ft")
# avg_ranges("1 - 2 - 5-10 ft")
# avg_ranges("1 - 2 - 5-10 ft")
# _utils.avg_ranges("1- 3 1/2 tests a day keeps the doctor away")

# _utils.avg_ranges("1/2 - 2 oz")
# avg_ranges("1/2 - 2 - 1/2 - 4 oz")
# avg_ranges("1/2 - 2 or 1/2 - 4 oz - 2") # "1/2 - 3 oz - 2"

def test_avg_ranges(input_string, expected_output):
    assert _utils.avg_ranges(input_string) == expected_output
