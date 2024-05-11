# __init__.py

__version__ = "1.0.1"

from ._ingredient_slicer import IngredientSlicer

from ._constants import UNITS, WEIGHT_UNITS, VOLUME_UNITS, DIMENSION_UNITS, \
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

# # ---- OLD Constants ----
# 'NUMBER_WORDS', 
# 'NUMBER_PREFIX_WORDS',
# 'MULTI_FRACTION_WORDS',
# 'FRACTION_WORDS',
# 'DENOMINATOR_WORDS',
# 'UNICODE_FRACTIONS', 
# 'UNITS', 
# 'BASIC_UNITS', 
# 'VOLUME_UNITS',
# 'WEIGHT_UNITS',
# 'DIMENSION_UNITS',
# 'CASUAL_UNITS',
# 'CASUAL_QUANTITIES',
# 'UNITS_SET',
# 'BASIC_UNITS_SET', 
# 'NON_BASIC_UNITS_SET', 
# 'SIZE_MODIFIERS_SET', 
# 'VOLUME_UNITS_SET',
# 'WEIGHT_UNITS_SET',
# 'DIMENSION_UNITS_SET',
# 'CASUAL_UNITS_SET',
# 'CASUAL_QUANTITIES_SET',
# 'UNIT_MODIFIERS', 
# 'PREP_WORDS', 
# 'APPROXIMATE_STRINGS', 