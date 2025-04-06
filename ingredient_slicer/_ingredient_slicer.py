# Authors: Angus Watters, Melissa Terry 

import re
from typing import List, Dict, Any, Union, Tuple
from fractions import Fraction
from html import unescape
import warnings

# package imports
from . import _utils
from . import _regex_patterns
from . import _constants
from .standardizer._ingredient_standardizer import IngredientStandardizer 
from .parser.ingredient_parser import IngredientParser 

# # local dev import statements
# from ingredient_slicer import _utils
# from ingredient_slicer import _regex_patterns
# from ingredient_slicer import _constants

class IngredientSlicer:
    """
    A class to parse recipe ingredients into a standard format.

    Args:
        ingredient (str): The ingredient to parse.
        debug (bool): Whether to print debug statements (default is False)
    """

    def __init__(self, ingredient: str, debug = False):
        self.ingredient          = ingredient
        self.debug               = debug

        self.parser = None 
        self.parser = self._get_ingredient_parser(self.ingredient, self.debug)

    def _get_ingredient_parser(self, ingredient : str, debug : bool = False) -> IngredientParser:
        if self.parser:
            return self.parser 

        # Create an instance of IngredientStandardizer
        parser = IngredientParser(ingredient, debug)    
        return parser  

    def to_json(self) -> Dict[str, Any]:
        return self.parser.to_json()
    
    def standardized_ingredient(self) -> str:
        """
        Return the standardized ingredient string.
        Returns:
            str: The standardized ingredient string.
        """
        return self.parser.parsed_data.standardized_ingredient

    def food(self) -> str:
        """
        Return the food string.
        Returns:
            str: The food string.
        """
        return self.parser.parsed_data.food
    
    def quantity(self) -> str:
        """
        Return the quantity string.
        Returns:
            str: The quantity string.
        """
        return self.parser.parsed_data.quantity
    
    def unit(self) -> str:
        """
        Return the unit string.
        Returns:
            str: The unit string.
        """
        return self.parser.parsed_data.unit
    
    def standardized_unit(self) -> str:
        """
        Return the standardized unit string.
        Returns:
            str: The standardized unit string.
        """
        return self.parser.parsed_data.standardized_unit
    
    def secondary_quantity(self) -> str:
        """
        Return the secondary quantity string.
        Returns:
            str: The secondary quantity string.
        """
        return self.parser.parsed_data.secondary_quantity
    
    def secondary_unit(self) -> str:
        """
        Return the secondary unit string.
        Returns:
            str: The secondary unit string.
        """
        return self.parser.parsed_data.secondary_unit
    
    def standardized_secondary_unit(self) -> str:
        """
        Return the standardized secondary unit string.
        Returns:
            str: The standardized secondary unit string.
        """
        return self.parser.parsed_data.standardized_secondary_unit
    
    def density(self) -> Union[str, float, int, None]:
        """
        Return the density of the given ingredient.
        Returns:
            str: The density of the given ingredient. 
        """

        return self.parser.parsed_data.densities.get("density") if self.parser.parsed_data.densities else None
    
    def gram_weight(self) -> str:
        """
        Return the estimated gram weight of the given ingredient.
        Returns:
            str: The estimated gram weight of the given ingredient.
        """
        return self.parser.parsed_data.gram_weight
    
    def min_gram_weight(self) -> str:
        """
        Return the estimated minimum gram weight of the given ingredient.
        Returns:
            str: The estimated minimum gram weight of the given ingredient.
        """
        return self.parser.parsed_data.min_gram_weight
    
    def max_gram_weight(self) -> str:
        """
        Return the estimated maximum gram weight of the given ingredient.
        Returns:
            str: The estimated maximum gram weight of the given ingredient.
        """
        return self.parser.parsed_data.max_gram_weight
    
    def prep(self) -> list:
        """
        Return the prep list.
        Returns:
            list: The prep list.
        """
        return self.parser.parsed_data.prep
    
    def size_modifiers(self) -> list:
        """
        Return the size modifiers list.
        Returns:
            list: The size modifiers list.
        """
        return self.parser.parsed_data.size_modifiers
    
    def dimensions(self) -> list:
        """
        Return the dimensions list.
        Returns:
            list: The dimensions list.
        """
        return self.parser.parsed_data.dimensions
    
    def is_required(self) -> bool:
        """
        Check if the ingredient is required or optional.
        Returns:
            bool: True if the ingredient is required, False if the ingredient is optional.
        """

        return self.parser.parsed_data.is_required
    
    def parenthesis_content(self) -> list[str]:
        """
        Get a list of the text within parenthesis
        Returns:
            list[str]
        """

        return self.parser.parsed_data.parenthesis_content
    

    
    def parsed_ingredient(self) -> dict:
        """
        Return the parsed ingredient dictionary.
        Returns:
            dict: The parsed ingredient dictionary (duplicate to to_json()) method
        """

        return self.parser.to_json()
    
    def __str__(self) -> str:
        """
        Return a string representation of the IngredientSlicer object.
        Returns:
            str: A string representation of the IngredientSlicer object.
        """
        return f"""IngredientSlicer Object:
    \tIngredient: '{self.ingredient}'
    \tStandardized Ingredient: '{self.standardized_ingredient()}'
    \tFood: '{self.food()}'
    \tQuantity: '{self.quantity()}'
    \tUnit: '{self.unit()}'
    \tStandardized Unit: '{self.standardized_unit()}'
    \tSecondary Quantity: '{self.secondary_quantity()}'
    \tSecondary Unit: '{self.secondary_unit()}'
    \tStandardized Secondary Unit: '{self.standardized_secondary_unit()}'
    \tDensity: '{self.densities.get("density")}'
    \tGram Weight: '{self.gram_weight()}'
    \tPrep: '{self.prep()}'
    \tSize Modifiers: '{self.size_modifiers()}'
    \tDimensions: '{self.dimensions()}'
    \tIs Required: '{self.is_required()}'
    \tParenthesis Content: '{self.parenthesis_content()}'"""