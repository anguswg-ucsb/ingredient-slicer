# __init__.py

__version__ = "1.1.21"

from ._ingredient_slicer import IngredientSlicer

from ._constants import UNITS, WEIGHT_UNITS, VOLUME_UNITS, FOOD_UNITS, DIMENSION_UNITS, \
    CASUAL_UNITS, CASUAL_QUANTITIES, PREP_WORDS, \
    FOOD_CATALOG, FOOD_CATEGORIES, FOOD_DENSITY_BY_GROUP, \
    PRIMARY_CATEGORIES, SECONDARY_CATEGORIES, \
    GRAM_CONVERSION_FACTORS, MILLILITER_CONVERSION_FACTORS \

# from ._regex_patterns import IngredientTools
# from ._utils import _make_int_or_float_str, _fraction_str_to_decimal, \
#     _find_substring_indices, _find_and_remove_hyphens_around_substring
    # _replace_and_with_hyphen, _replace_to_or_with_hyphen, _replace_to_with_hyphen, _replace_or_with_hyphen


__all__ = [
    # Constants
    "UNITS",
    "WEIGHT_UNITS",
    "VOLUME_UNITS",
    "FOOD_UNITS",
    "DIMENSION_UNITS", 
    "CASUAL_UNITS", 
    "CASUAL_QUANTITIES",
    "PREP_WORDS",
    "FOOD_CATALOG",
    "FOOD_CATEGORIES",
    "FOOD_DENSITY_BY_GROUP",
    "PRIMARY_CATEGORIES",
    "SECONDARY_CATEGORIES",
    "GRAM_CONVERSION_FACTORS",
    "MILLILITER_CONVERSION_FACTORS",
    # Main parser classe
    'IngredientSlicer'
    # 'IngredientTools',  # Old regex patterns class
    ]
