import pytest
from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# ---- Test IngredientSlicer: Replace "a" or "an" words at the start of ingredients with no quantities ----
# -------------------------------------------------------------------------------

def test_replace_a_or_an_with_1():
    ingredient = "a cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "1 cup of flour"

def test_replace_a_or_an_with_1_lowercase():
    ingredient = "an apple"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "1 apple"

def test_no_change_with_number_present():
    ingredient = "2 cups of sugar"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "2 cups of sugar"

def test_no_change_with_a_as_part_of_word():
    ingredient = "apple"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "apple"

def test_no_change_with_an_as_part_of_word():
    ingredient = "banana"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "banana"

def test_no_change_with_empty_string():
    ingredient = ""
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == ""

def test_no_change_with_multiple_words():
    ingredient = "a pinch of salt"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "1 pinch of salt"

def test_no_change_with_numbers_after_a_or_an():
    ingredient = "a 1/4 cup of milk"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "a 1/4 cup of milk"

def test_number_followed_by_a_1():
    ingredient = "1 and a half cups of milk"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == "1 and a half cups of milk"

def test_multiple_a_after_first_a_at_start_1():
    ingredient = "a aaa aa cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 aaa aa cup of flour'

def test_multiple_a_at_start_1():
    ingredient = "aaaa aa a aa cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 aa a aa cup of flour'

def test_multiple_an_at_start_2():
    ingredient = "an an aa a aa cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 an aa a aa cup of flour'

def test_multiple_an_after_first_an_at_start_2():
    ingredient = "an ana an aa a aa cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 ana an aa a aa cup of flour'

def test_capital_A_at_start():
    ingredient = "A cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 cup of flour'

def test_capital_An_at_start():
    ingredient = "An apple"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == '1 apple'

def test_capital_A_at_start_with_number():
    ingredient = "A 1/4 cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'a 1/4 cup of flour'

def test_capital_An_at_start_with_number():
    ingredient = "An 1/4 cup of flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'an 1/4 cup of flour'

def test_capital_A_at_end_of_word():
    ingredient = "Cup of flour A"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour 1'

def test_capital_An_at_end_of_word():
    ingredient = "Cup of flour An"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour 1'

def test_capital_A_at_end_of_word_with_number():
    ingredient = "Cup of flour A 1/4"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour a 1/4'

def test_capital_An_at_end_of_word_with_number():
    ingredient = "Cup of flour An 1/4"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour an 1/4'

def test_capital_A_at_end_of_word_with_number_and_no_space():
    ingredient = "Cup of flour A1/4"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour a1/4'

def test_capital_An_at_end_of_word_with_number_and_no_space():
    ingredient = "Cup of flour An1/4"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of flour an1/4'

def test_a_in_the_middle_of_word():
    ingredient = "Cup of a flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of 1 flour'

def test_an_in_the_middle_of_word():
    ingredient = "Cup of an flour"
    updated_ingredient = _utils._replace_a_or_an_quantities(ingredient)
    assert updated_ingredient == 'cup of 1 flour'

def test_replace_a_or_an_integer_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities(1)

def test_replace_a_or_an_list_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities([1,2,3])

def test_replace_a_or_an_dict_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities({"1": 1, "2": 2})

def test_replace_a_or_an_tuple_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities((1,2,3))

def test_replace_a_or_an_float_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities(1.5)

def test_replace_a_or_an_boolean_error():

    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities(True)

    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities(False)

def test_replace_a_or_an_none_error():
    with pytest.raises(ValueError):
        _utils._replace_a_or_an_quantities(None)