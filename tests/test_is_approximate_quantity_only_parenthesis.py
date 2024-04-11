import pytest


from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Test _is_approximate_quantity_only_parenthesis() utils function  ----
# -------------------------------------------------------------------------------


def test_is_approximate_quantity_only_parenthesis_about_then_single_number():
    assert _utils._is_approximate_quantity_only_parenthesis("about 4") == True

def test_is_approximate_quantity_only_parenthesis_about_then_single_number_with_comma():
    assert _utils._is_approximate_quantity_only_parenthesis("about 4,") == True

def test_is_approximate_quantity_only_parenthesis_about_then_single_number_with_period():
    assert _utils._is_approximate_quantity_only_parenthesis("about 4.") == True

def test_is_approximate_quantity_only_parenthesis_approx_then_single_number():
    assert _utils._is_approximate_quantity_only_parenthesis("approx 4") == True

def test_is_approximate_quantity_only_parenthesis_about_with_number_then_unit():
    assert _utils._is_approximate_quantity_only_parenthesis("about 4 cups") == False

def test_is_approximate_quantity_only_parenthesis_about_with_number_then_unit_with_comma():
    assert _utils._is_approximate_quantity_only_parenthesis("about 4 cups,") == False

def test_is_approximate_quantity_only_parenthesis_about_with_number_then_unit_no_space_between_quanity_and_about():
    assert _utils._is_approximate_quantity_only_parenthesis("about4 cups") == False

def test_is_approximate_quantity_only_parenthesis_about_with_number_no_space_between_quanity_and_about():
    assert _utils._is_approximate_quantity_only_parenthesis("about4") == False

def test_is_approximate_quantity_only_parenthesis_about_with_number_no_space_between_quanity_and_about_with_comma():
    assert _utils._is_approximate_quantity_only_parenthesis("about4,") == False

def test_is_approximate_quantity_only_parenthesis_unit_number_about():
    assert _utils._is_approximate_quantity_only_parenthesis("cups about 4") == False

def test_is_approximate_quantity_only_parenthesis_number_then_character_then_about():
    assert _utils._is_approximate_quantity_only_parenthesis("4 gfdfhafsdgsdfgd about") == True

def test_is_approximate_quantity_only_parenthesis_about_then_characters_then_number():
    assert _utils._is_approximate_quantity_only_parenthesis("about gfdfhafsdgsdfgd 4") == True

def test_is_approximate_quantity_only_parenthesis_about_then_fraction():
    assert _utils._is_approximate_quantity_only_parenthesis("about 1/2") == True

def test_is_approximate_quantity_only_parenthesis_about_then_decimal():
    assert _utils._is_approximate_quantity_only_parenthesis("about 1.5") == True

def test_is_approximate_quantity_only_parenthesis_about_then_fraction_with_unit():
    assert _utils._is_approximate_quantity_only_parenthesis("about 1/2 cups") == False

def test_is_approximate_quantity_unit_only_patenthesis_integer_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis(3) == False

def test_is_approximate_quantity_unit_only_patenthesis_float_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis(3.5) == False

def test_is_approximate_quantity_unit_only_patenthesis_string_integer_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis("3") == False

def test_is_approximate_quantity_unit_only_patenthesis_string_float_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis("3.5") == False

def test_is_approximate_quantity_unit_only_patenthesis_boolean_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis(True) == False

def test_is_approximate_quantity_unit_only_patenthesis_list_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis([3]) == False

def test_is_approximate_quantity_unit_only_patenthesis_tuple_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis((3,)) == False

def test_is_approximate_quantity_unit_only_patenthesis_dict_is_false():
    assert _utils._is_approximate_quantity_only_parenthesis({"3": 3}) == False