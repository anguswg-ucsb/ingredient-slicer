# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test the parenthesis utility functions that split ingredients by the parenthesis values
# - _split_by_parenthesis()
# - _is_valid_parenthesis()
# - _remove_parenthesis_from_str()
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# ---- Test _split_by_parenthesis() function -----
# -------------------------------------------------------------------------------
def test_split_by_parenthesis_1():
    ingredient = "a cup of flour"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of flour'
    assert parenthesis_content == []
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_2():
    ingredient = "a cup of (flour)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of'
    assert parenthesis_content == ['flour']
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_two_sets_1():
    ingredient = "a cup of (flour) and (sugar)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and'
    assert parenthesis_content == ['flour', 'sugar']
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_three_sets_1():
    ingredient = "a cup of (flour) and (sugar) and (water)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and and'
    assert parenthesis_content == ['flour', 'sugar', 'water']
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_two_sets_first_nested_depth1_1():
    ingredient = "a cup of ((flour)) and (sugar)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and'
    assert parenthesis_content == ['flour', 'sugar']
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_two_sets_first_nested_depth1_2():

    ingredient = "a cup of (flour (but not too much)) and (sugar)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and'
    assert parenthesis_content == ['flour but not too much', 'sugar']
    assert type(updated_ingredient) == str
    assert type(parenthesis_content) == list

def test_split_by_parenthesis_two_sets_first_nested_depth2_1():
    ingredient = "a cup of ((flour (but not too much))) and (sugar)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and'
    assert parenthesis_content == ['flour but not too much', 'sugar']

def test_split_by_parenthesis_two_sets_both_nested_depth1_1():
    ingredient = "a cup of ((flour (but not too much))) and ((sugar (but not too much)))"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of and'
    assert parenthesis_content == ['flour but not too much', 'sugar but not too much']

def test_split_by_parenthesis_one_set_nested_depth3_1():
    ingredient = "a cup of (((flour (but not too much))))"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of'
    assert parenthesis_content == ['flour but not too much']

def test_invalid_parenthesis_three_left_one_right_1():
    ingredient = "a cup of ((flour (but not too much)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of flour but not too much'
    assert parenthesis_content == []

def test_invalid_parenthesis_two_left_one_right_2():
    ingredient = "a cup of (flour (but not too much)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of flour but not too much'
    assert parenthesis_content == []

def test_invalid_parenthesis_one_left_two_right_3():
    ingredient = "a cup of flour but not too much))"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of flour but not too much'
    assert parenthesis_content == []

def test_invalid_parenthesis_one_left_two_right_4():
    ingredient = "a cup of (flour but not too ) much)"
    updated_ingredient, parenthesis_content = _utils._split_by_parenthesis(ingredient)
    assert updated_ingredient == 'a cup of flour but not too much'
    assert parenthesis_content == []

# -------------------------------------------------------------------------------
# ---- Test _remove_parenthesis_from_str() function -----
# -------------------------------------------------------------------------------

def test_remove_parenthesis_from_str_no_parenthesis():
    ingredient = "a cup of flour"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of flour'

def test_remove_parenthesis_from_str_one_parenthesis():
    ingredient = "a cup of (flour)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'

def test_remove_parenthesis_from_str_two_parenthesis():
    ingredient = "a cup of (flour) and (sugar)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and'


def test_remove_parenthesis_from_str_three_parenthesis():
    ingredient = "a cup of (flour) and (sugar) and (water)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and and'

def test_remove_parenthesis_from_str_two_parenthesis_first_nested_depth1():
    ingredient = "a cup of ((flour)) and (sugar)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and'

def test_remove_parenthesis_from_str_two_parenthesis_first_nested_depth1_2():
    ingredient = "a cup of (flour (but not too much)) and (sugar)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and'

def test_remove_parenthesis_from_str_two_parenthesis_first_nested_depth2():
    ingredient = "a cup of ((flour (but not too much))) and (sugar)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and'


def test_remove_parenthesis_from_str_two_parenthesis_both_nested_depth1():
    ingredient = "a cup of ((flour (but not too much))) and ((sugar (but not too much)))"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and'

def test_remove_parenthesis_from_str_one_parenthesis_nested_depth3():
    ingredient = "a cup of (((flour but not too much)))"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'

def test_remove_parenthesis_from_str_invalid_parenthesis_two_left_one_right():
    ingredient = "a cup of ((flour but not too much)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'

def test_remove_parenthesis_from_str_invalid_parenthesis_one_left_two_right():
    ingredient = "a cup of (flour but not too much))"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'


def test_remove_parenthesis_from_str_invalid_parenthesis_one_left_two_right_2(): # TODO: buggy, should remove "much" but leaves it
    ingredient = "a cup of (flour but not too ) much)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of much'

def test_remove_parenthesis_from_str_invalid_parenthesis_three_sets():
    ingredient = "a cup of ((flour but not too much) and (sugar) and (water))"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'

def test_remove_parenthesis_from_str_invalid_parenthesis_three_sets_separate():
    ingredient = "a cup of (flour but not too much) and (sugar) and (water)"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of and and'

def test_remove_parenthesis_from_str_invalid_parenthesis_three_sets_nested_depth2():
    ingredient = "a cup of (flour but not too much (sugar(water)))"
    updated_ingredient = _utils._remove_parenthesis_from_str(ingredient)
    assert updated_ingredient == 'a cup of'



# -------------------------------------------------------------------------------
# ---- Test _is_valid_parenthesis() function -----
# -------------------------------------------------------------------------------

def test_is_valid_parenthesis_1():
    assert _utils._is_valid_parenthesis("(") == False

def test_is_valid_parenthesis_2():
    assert _utils._is_valid_parenthesis(")") == False

def test_is_valid_parenthesis_3():
    assert _utils._is_valid_parenthesis("()") == True

def test_is_valid_parenthesis_4():
    assert _utils._is_valid_parenthesis("(a)") == True

def test_is_valid_parenthesis_5():
    assert _utils._is_valid_parenthesis("(a") == False

def test_is_valid_parenthesis_6():
    assert _utils._is_valid_parenthesis("a)") == False

def test_is_valid_parenthesis_7():
    assert _utils._is_valid_parenthesis("a") == True # NOTE: No parenthesis is True

def test_is_valid_parenthesis_8():
    assert _utils._is_valid_parenthesis("()") == True

def test_is_valid_parenthesis_9():
    assert _utils._is_valid_parenthesis("I love test (cases) even if they take (lots of (time)) to write") == True

def test_is_valid_parenthesis_10():
    assert _utils._is_valid_parenthesis("I love test (cases) even if they take (lots of (time)) to write)") == False

def test_is_valid_parenthesis_11():
    assert _utils._is_valid_parenthesis("I love test (cases) even if they take (lots of (time) to write") == False

def test_is_valid_parenthesis_12():
    assert _utils._is_valid_parenthesis("I love test (cases) even if they take lots of (time (2 (do)) to write) properly") == True

def test_is_valid_parenthesis_13():
    assert _utils._is_valid_parenthesis("I love test (cases) even if they take lots of (time (2 (do)) to write) properly)") == False


