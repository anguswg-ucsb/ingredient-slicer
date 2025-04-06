    
# Authors: Angus Watters, Melissa Terry 

import re
from typing import List, Dict, Any, Union, Tuple
from fractions import Fraction
from html import unescape
import warnings

# package imports
from ._ingredient_standardizer_builder import IngredientStandardizerBuilder

# # local dev import statements
# from ingredient_slicer import _utils
# from ingredient_slicer import _regex_patterns
# from ingredient_slicer import _constants
# from ingredient_slicer.standardizer._ingredient_standardizer_builder import IngredientStandardizerBuilder 

class IngredientStandardizer:
    """
    A class to standardize an ingredient into a common form using a builder.
    """
    def __init__(self, ingredient: str):
        self.ingredient = ingredient
        self._builder = IngredientStandardizerBuilder(ingredient)
        self._parse()

    def _parse(self):
        """Apply all building steps using the builder."""
        self._builder = (
            self._builder
            ._drop_special_dashes() 
            ._find_and_remove_percentages() 
            ._replace_number_followed_by_inch_symbol() 
            ._find_and_replace_casual_quantities() 
            ._find_and_replace_prefixed_number_words() 
            ._find_and_replace_number_words() 
            ._find_and_replace_fraction_words() 
            ._clean_html_and_unicode() 
            ._replace_unicode_fraction_slashes() 
            ._replace_emojis() 
            ._convert_fractions_to_decimals() 
            ._force_ws_between_numbers_and_chars() 
            ._remove_repeat_units_in_ranges() 
            ._separate_dimensions() 
            ._remove_x_separators() 
            ._clean_hyphen_padded_substrings() 
            ._merge_multi_nums() 
            ._fix_ranges() 
            ._find_and_replace_numbers_separated_by_add_numbers() 
            ._replace_a_or_an_quantities() 
            ._average_ranges() 
            ._separate_parenthesis() 
        )
        self._standardized_data = self._builder.get_standardized_ingredient_data()

    def get_standardized_ingredient_data(self) -> Dict[str, Any]:
        return self._standardized_data

    def get_standardized_ingredient(self) -> str:
        return self._standardized_data.get("_standardized_ingredient")

    def get_staged_ingredient(self) -> str:
        return self._standardized_data.get("_staged_ingredient")

    def get_parenthesis_content(self) -> list:
        return self._standardized_data.get("_parenthesis_content")

    def get_dimensions(self) -> list:
        return self._standardized_data.get("_dimensions")
