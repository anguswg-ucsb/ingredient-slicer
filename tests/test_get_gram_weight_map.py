import pytest

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# ---- Test the _get_gram_weight_map() function -----
# -------------------------------------------------------------------------------

def test_get_gram_weight_map_with_defaults():
    result = _utils._get_gram_weight_map(100)

    # NOTE: round each value to an integer for testing purposes
    result = {key: round(value) for key, value in result.items()}

    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

def test_get_gram_weight_map_with_valid_kwargs():
    result = _utils._get_gram_weight_map(100, density=1.2, min_density=1, max_density=1.5)
    result = {key: round(value) for key, value in result.items()}
    
    assert result == {
        "gram_weight": 120,
        "min_gram_weight": 100,
        "max_gram_weight": 150,
    }

def test_get_gram_weight_map_with_string_milliliters():
    result = _utils._get_gram_weight_map("100", density=1.1)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 110,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

def test_get_gram_weight_map_with_valid_density_key_and_none_other_density_keys():
    result = _utils._get_gram_weight_map(200, density=1.1, min_density=None, max_density=None)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 220,
        "min_gram_weight": 180,
        "max_gram_weight": 220,
    }

def test_get_gram_weight_map_with_none_density():
    result = _utils._get_gram_weight_map(100, density=None)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

def test_get_gram_weight_map_with_empty_string_density():
    result = _utils._get_gram_weight_map(100, density="")
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

def test_get_gram_weight_map_with_none_and_empty_string_values():
    result = _utils._get_gram_weight_map(100, density=None, min_density='', max_density=None)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

def test_get_gram_weight_map_with_zero_milliliters():
    result = _utils._get_gram_weight_map(0, density=1.2, min_density=1, max_density=1.5)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 0,
        "min_gram_weight": 0,
        "max_gram_weight": 0,
    }

def test_get_gram_weight_map_with_negative_milliliters():
    result = _utils._get_gram_weight_map(-100, density=1.2, min_density=1, max_density=1.5)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": -120,
        "min_gram_weight": -100,
        "max_gram_weight": -150,
    }

def test_get_gram_weight_map_with_partial_kwargs():
    result = _utils._get_gram_weight_map(100, density=1.1)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 110,
        "min_gram_weight": 90,
        "max_gram_weight": 110,
    }

    result = _utils._get_gram_weight_map(100, min_density=0.8)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 80,
        "max_gram_weight": 110,
    }

    result = _utils._get_gram_weight_map(100, max_density=1.2)
    result = {key: round(value) for key, value in result.items()}
    assert result == {
        "gram_weight": 100,
        "min_gram_weight": 90,
        "max_gram_weight": 120,
    }

def test_get_gram_weight_map_with_invalid_milliliters():
    with pytest.raises(ValueError):
        _utils._get_gram_weight_map([100], density=1.1)

def test_get_gram_weight_map_with_invalid_kwargs():
    with pytest.raises(ValueError):
        _utils._get_gram_weight_map(100, invalid_key=1.1)
