# __init__.py

__version__ = "0.0.6"

# from ._constants import NUMBER_WORDS,  NUMBER_PREFIX_WORDS, \
#     MULTI_FRACTION_WORDS, FRACTION_WORDS, DENOMINATOR_WORDS, UNICODE_FRACTIONS, \
#     UNITS, BASIC_UNITS, VOLUME_UNITS, WEIGHT_UNITS, DIMENSION_UNITS, \
#     CASUAL_QUANTITIES, CASUAL_UNITS, UNITS_SET, \
#     BASIC_UNITS_SET, NON_BASIC_UNITS_SET, SIZE_MODIFIERS_SET, \
#     VOLUME_UNITS_SET, WEIGHT_UNITS_SET, DIMENSION_UNITS_SET, CASUAL_QUANTITIES_SET, CASUAL_UNITS_SET, \
#     UNIT_MODIFIERS, PREP_WORDS, APPROXIMATE_STRINGS

from ._constants import UNITS, WEIGHT_UNITS, DIMENSION_UNITS, \
    CASUAL_UNITS, CASUAL_QUANTITIES, PREP_WORDS, \
    FOOD_CATALOG, FOOD_CATEGORIES

# from ._utils import _make_int_or_float_str, _fraction_str_to_decimal, \
#     _find_substring_indices, _find_and_remove_hyphens_around_substring
    # _replace_and_with_hyphen, _replace_to_or_with_hyphen, _replace_to_with_hyphen, _replace_or_with_hyphen

from ._regex_patterns import IngredientTools
from ._ingredient_slicer import IngredientSlicer

__all__ = [
    # Constants
    "UNITS",
    "WEIGHT_UNITS",
    "DIMENSION_UNITS", 
    "CASUAL_UNITS", 
    "CASUAL_QUANTITIES",
    "PREP_WORDS",
    "FOOD_CATALOG",
    "FOOD_CATEGORIES",

    # Recipes regex and parser classes
    # 'IngredientTools', 
    'IngredientSlicer'
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