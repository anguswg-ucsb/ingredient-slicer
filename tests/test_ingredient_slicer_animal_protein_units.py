# pytest library
import pytest

import re

from ingredient_slicer import _constants, _utils, IngredientSlicer
# from ingredient_slicer import IngredientSlicer

# -------------------------------------------------------------------------------
# ---- _get_animal_protein_gram_weight tests ----
# -------------------------------------------------------------------------------

def test_get_animal_protein_gram_weight_chicken_breasts():
        
    parsed = IngredientSlicer("8 chicken breasts").to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == 'breasts'
    assert parsed['standardized_unit'] == 'breast'
    assert parsed['gram_weight'] == '1361'

def test_get_animal_protein_gram_weight_chicken_breasts():
        
    parsed = IngredientSlicer("8 ounce chicken breasts").to_json()

    assert parsed['quantity'] == "8"
    assert parsed['unit'] == 'ounce'
    assert parsed['standardized_unit'] == 'ounce'
    assert parsed['gram_weight'] == '226.8'


def test_animal_protein_as_unit_chicken_drumsticks():
    parsed = IngredientSlicer("12 chicken drumsticks").to_json()
    
    assert parsed['quantity'] == "12"
    assert parsed['unit'] == 'drumsticks'
    assert parsed['standardized_unit'] == 'drumstick'
    assert parsed['gram_weight'] == '1360.8'


def test_animal_protein_as_unit_chicken_tenders():
    parsed = IngredientSlicer("2 chicken tenders").to_json()
    
    assert parsed['quantity'] == "2"
    assert parsed['unit'] == 'tenders'
    assert parsed['standardized_unit'] == 'tender'
    assert parsed['gram_weight'] == '113.4'

def test_animal_protein_as_unit_chicken_thighs_with_real_weight_units():
    parsed = IngredientSlicer("4 chicken thighs (12 oz.)").to_json()
    
    assert parsed['quantity'] == "48"
    assert parsed['unit'] == 'oz'
    assert parsed['standardized_unit'] == 'ounce'
    assert parsed['secondary_unit'] == 'thighs'
    assert parsed['standardized_secondary_unit'] == 'thigh'
    assert parsed['gram_weight'] == '1360.78'

# def _is_number(x: Union[str, int, float, None]) -> bool:
    
#     if isinstance(x, str):
#         try:
#             x = float(x)
#             return True
#         except:
#             return False
    
#     if isinstance(x, (int, float)):
#         return True

# def _get_number(x: Union[str, int, float, None]) -> Union[int, float, None]:
    
#     if isinstance(x, str):
#         try:
#             x = float(x)
#             return x
#         except:
#             return
    
#     if isinstance(x, (int, float)):
#         return x
    
#     return 

# def _get_animal_protein_unit_gram_weight(
#         unit: Union[str, None] 
#         ) -> Union[int, float, None]:

#     if not isinstance(unit, str) or unit is None:
#         return

#     gram_weight_per_unit = None

#     if unit in _constants.ANIMAL_PROTEIN_UNITS_SET:
#         std_unit             = _constants.ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT.get(unit)
#         gram_weight_per_unit = _constants.ANIMAL_PROTEIN_UNITS_TO_GRAMS.get(std_unit)

#     return gram_weight_per_unit

# def _get_animal_protein_gram_weight(
#         quantity: Union[str, None], 
#         unit: Union[str, None]
#         ) -> Union[int, float, None]: 
    
#     """ Get the gran weight of a given animal protein unit (i.e. "breasts", "tenders", etc.)
#     """
#     # unit = "breasts"
#     # quantity = "8"
    
#     gram_weight = None

#     if _is_number(quantity):
#         quantity = _get_number(quantity)
#     else:
#         quantity = 1

#     if unit in _constants.ANIMAL_PROTEIN_UNITS_SET:
#         gram_weight     = _get_animal_protein_unit_gram_weight(unit)

#     if gram_weight:
#         gram_weight = round(float(gram_weight) * float(quantity))

#     return gram_weight

# _get_animal_protein_gram_weight("1", "breast")
# _get_animal_protein_gram_weight("2", "tenderloins")

# grams_map = _utils._get_gram_weight("flour" "1", "cup", "levenshtein")
# from typing import Dict, Union
# def test_get_gram_weight_one_ounce():
#     # _constants.ANIMAL_PROTEIN_UNITS

#     slicer = IngredientSlicer("8 chicken breasts")

#     parsed = slicer.to_json()
    
#     def _get_animal_protein_unit_gram_weight(
#             unit: Union[str, None], 
#             gram_weight: Union[int, float, None]
#             ) -> Union[int, float, None]:
        
#         gram_weight_per_unit = None

#         if not gram_weight:
#             if unit in _constants.ANIMAL_PROTEIN_UNITS_SET:
#                 std_unit    = _constants.ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT.get(unit)
#                 gram_weight_per_unit = _constants.ANIMAL_PROTEIN_UNITS_TO_GRAMS.get(std_unit)

#         return gram_weight_per_unit

#     quantity = parsed.get("quantity")
#     unit = parsed.get("unit") 
#     gram_weight  = parsed.get('gram_weight')

#     if not gram_weight:
#         print("NO GRAM WEIGHT")
#         if unit in _constants.ANIMAL_PROTEIN_UNITS_SET:
#             print(f'unit {unit} is an animal protein unit!!@!')
#             _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(unit)
#             std_unit = _constants.ANIMAL_PROTEIN_UNIT_TO_STANDARD_ANIMAL_PROTEIN_UNIT.get(unit)
#             print(f'std_unit: {std_unit}')
#             _constants.ANIMAL_PROTEIN_UNITS_TO_GRAMS.get(std_unit)

    # gram_weights = _utils._get_gram_weight("chicken", "1", "ounce")

    # gram_weight     = round(float(gram_weights["gram_weight"])) if gram_weights["gram_weight"] else None
    # min_gram_weight = round(float(gram_weights["min_gram_weight"])) if gram_weights["min_gram_weight"] else None
    # max_gram_weight = round(float(gram_weights["max_gram_weight"])) if gram_weights["max_gram_weight"] else None

    # assert gram_weight == 28
    # assert min_gram_weight == None
    # assert max_gram_weight == None