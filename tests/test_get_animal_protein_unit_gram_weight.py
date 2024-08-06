# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- _get_animal_protein_gram_weight() tests ----
# -------------------------------------------------------------------------------

def test_get_animal_protein_gram_weight_animal_protein_gram_weight_for_all_animal_protein_units():
    animal_protein_units = sorted(list(_constants.ANIMAL_PROTEIN_UNITS_SET))
    for unit in animal_protein_units:
        quantities = [1, 2, 5, 8]
        for quantity in quantities:

            std_unit = _constants.ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT.get(unit)

            expected_result = str(round(quantity * _constants.ANIMAL_PROTEIN_UNITS_TO_GRAMS.get(std_unit), 2))
            result          = _utils._get_animal_protein_gram_weight(quantity, unit)
            
            assert result == expected_result

def test_get_animal_protein_gram_weight_animal_protein_unit_and_zero_int():
    assert _utils._get_animal_protein_gram_weight(0, "breasts") == '0.0'

def test_get_animal_protein_gram_weight_animal_protein_unit_and_zero_float():
    assert _utils._get_animal_protein_gram_weight(0.0, "breasts") == '0.0'

def test_get_animal_protein_gram_weight_animal_protein_unit_and_zero_string():
    assert _utils._get_animal_protein_gram_weight("0", "breasts") == '0.0'
    
def test_get_animal_protein_gram_weight_volume_unit_cups():
    assert _utils._get_animal_protein_gram_weight(1, "cups") == None

def test_get_animal_protein_gram_weight_weight_unit_ounces():
    assert _utils._get_animal_protein_gram_weight(1, "ounces") == None

def test_get_animal_protein_gram_weight_weight_none_as_unit():
    assert _utils._get_animal_protein_gram_weight(1, None) == None

def test_get_animal_protein_gram_weight_weight_none_as_quantity():
    assert _utils._get_animal_protein_gram_weight(None, "breasts") == '170.1'

def test_get_animal_protein_gram_weight_weight_none_as_quantity_and_unit():
    assert _utils._get_animal_protein_gram_weight(None, None) == None

def test_get_animal_protein_gram_weight_invalid_string_as_quantity():
    with pytest.raises(ValueError):
        _utils._get_animal_protein_gram_weight("fgjf", "breasts")

def test_get_animal_protein_gram_weight_invalid_list_type_as_quantity():
    with pytest.raises(TypeError):
        _utils._get_animal_protein_gram_weight([1, 2, 3], "breasts")

def test_get_animal_protein_gram_weight_invalid_list_type_as_unit():
    assert _utils._get_animal_protein_gram_weight(1, [1, 2, 3]) == None
    
