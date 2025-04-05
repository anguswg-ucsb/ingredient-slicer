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
from ingredient_slicer.standardizer._ingredient_standardizer import IngredientStandardizer 
from ingredient_slicer.models.quantity_unit_data import QuantityUnitData
quantity_unit_data = QuantityUnitData(quantity="1", unit="1")
quantity_unit_data.quantity

# # local dev import statements
# from ingredient_slicer import _utils
# from ingredient_slicer import _regex_patterns
# from ingredient_slicer import _constants
def _address_equivalence_parenthesis2(self, parenthesis: str, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
    """
    Address the case where the parenthesis content contains any equivalence strings like "about" or "approximately", followed by a quantity and then a unit later in the sting.
    Attempts to update quantity_unit_data.quantity, quantity_unit_data.unit, quantity_unit_data.secondary_quantity, and quantity_unit_data.secondary_unit given 
    information from the parenthesis string and the current quantity_unit_data.quantity and quantity_unit_data.unit
    e.g. "(about 3 ounces)", "(about a 1/3 cup)", "(approximately 1 large tablespoon)"

    Args:
        parenthesis (str): A string containing parenthesis from the ingredients string
    Returns:
        None
    """

    # print(f"""Ingredient: '{self._reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{quantity_unit_data.quantity}'\nUnit: '{quantity_unit_data.unit}'""") if self.debug else None

    # check for the equivelency pattern (e.g. "<equivelent string> <quantity> <unit>" )
    equivalent_quantity_unit = _utils._extract_equivalent_quantity_units(parenthesis)
    # equivalent_quantity_unit = _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall(parenthesis)
    # equivalent_quantity_unit = [item for i in [regex.EQUIV_QUANTITY_UNIT_GROUPS.findall(i) for i in parenthesis] for item in i]

    # remove parenthesis and then split on whitespace
    split_parenthesis = parenthesis.replace("(", "").replace(")", "").split()

    # Case when: NO equivelence quantity unit matches 
    #           OR parenthesis contains a quantity per unit like string in the parenthesis (i.e. "(about 2 ounces each)" contains "each")
    # Then return early with NO UPDATES and keep the current quantity/unit as is
    if not equivalent_quantity_unit or any([True if i in _constants.QUANTITY_PER_UNIT_STRINGS else False for i in split_parenthesis]):
        # print(f"\n > Return early from EQUIVALENCE parenthesis") if self.debug else None
        quantity_unit_data.parenthesis_notes.append("not a equivalence quantity unit parenthesis")
        return quantity_unit_data
    
    # pull out the suffix word, parenthesis quantity and unit
    parenthesis_suffix, parenthesis_quantity, parenthesis_unit = equivalent_quantity_unit[0]
    
    # Case when: NO quantity, NO unit:
        # if no quantity AND no unit, then we can use the parenthesis quantity-unit as our quantity and unit
    if not quantity_unit_data.quantity and not quantity_unit_data.unit:

        quantity_unit_data.parenthesis_notes.append("used equivalence quantity unit as our quantity and unit")

        # set quantity/unit to the parenthesis values
        quantity_unit_data.quantity = parenthesis_quantity
        quantity_unit_data.unit = parenthesis_unit

        return quantity_unit_data
    
    # Case when: YES quantity, NO unit:
        # we can assume the equivelent quantity units 
        # in the parenthesis are actually a better fit for the quantities and units so 
        # we can use those are our quantities/units and then stash the original quantity in the "description" field 
        # with a "maybe quantity is " prefix in front of the original quantity for maybe use later on
    if quantity_unit_data.quantity and not quantity_unit_data.unit:

        # stash the old quantity with a trailing string before changing best_quantity
        quantity_unit_data.parenthesis_notes.append(f"maybe quantity is: {' '.join(quantity_unit_data.quantity)}")


        # make the secondary_quantity the starting quantity before converting the quantity to the value found in the parenthesis
        quantity_unit_data.secondary_quantity = quantity_unit_data.quantity

        # set the quantity/unit to the parenthesis values
        quantity_unit_data.quantity = parenthesis_quantity
        quantity_unit_data.unit = parenthesis_unit

        return quantity_unit_data

    # Case when: NO quantity, YES unit:
        # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are probably "better" so use the
        # parenthesis quantity/units and then stash the old unit in the description
    if not quantity_unit_data.quantity and quantity_unit_data.unit:

        # stash the old quantity with a trailing "maybe"
        quantity_unit_data.parenthesis_notes.append(f"maybe unit is: {quantity_unit_data.unit}")

        # make the secondary_unit the starting unit before converting the unit to the unit string found in the parenthesis
        quantity_unit_data.secondary_unit = quantity_unit_data.unit

        quantity_unit_data.quantity = parenthesis_quantity
        quantity_unit_data.unit = parenthesis_unit

        # return [parenthesis_quantity, parenthesis_unit, description]
        return quantity_unit_data
    
    # Case when: YES quantity, YES unit:
        # if we already have a quantity AND a unit, then we likely found an equivalent quantity/unit
        # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
    if quantity_unit_data.quantity and quantity_unit_data.unit:
        parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
        unit_is_basic = quantity_unit_data.unit in _constants.BASIC_UNITS_SET

        # Case when BOTH are basic units:  (# TODO: Maybe we should use parenthesis quantity/unit instead...?)
        #   use the original quantity/unit (stash the parenthesis in the description)
        if parenthesis_unit_is_basic and unit_is_basic:
            quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
            # return [quantity_unit_data.quantity, quantity_unit_data.unit, description]

            # set the secondary quantity/units to the values in the parenthesis
            quantity_unit_data.secondary_quantity = parenthesis_quantity
            quantity_unit_data.secondary_unit = parenthesis_unit

            return quantity_unit_data
        
        # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
        #   use the original quantity/unit (stash the parenthesis in the description)
        if not parenthesis_unit_is_basic and not unit_is_basic:
            quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
            # return [quantity_unit_data.quantity, quantity_unit_data.unit, description]
            
            # set the secondary quantity/units to the values in the parenthesis
            quantity_unit_data.secondary_quantity = parenthesis_quantity
            quantity_unit_data.secondary_unit = parenthesis_unit

            return quantity_unit_data

        # Case when: YES basic parenthesis unit, NO basic original unit: 
        #   then use the parenthesis quantity/unit (stash the original in the description)
        if parenthesis_unit_is_basic:
            quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {quantity_unit_data.quantity}/{quantity_unit_data.unit}")
            
            # set the secondary quantity/units to the original quantity/units
            quantity_unit_data.secondary_quantity = quantity_unit_data.quantity
            quantity_unit_data.secondary_unit = quantity_unit_data.unit

            # update the primary quantities/units to the parenthesis values
            quantity_unit_data.quantity = parenthesis_quantity
            quantity_unit_data.unit = parenthesis_unit
            
            # return [parenthesis_quantity, parenthesis_unit, description]
            return quantity_unit_data

        # Case when: NO basic parenthesis unit, YES basic original unit: 
        #   then use the original quantity/unit (stash the parenthesis in the description)
        if unit_is_basic:
            quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")

            # set the secondary quantity/units to the original quantity/units
            quantity_unit_data.secondary_quantity = parenthesis_quantity
            quantity_unit_data.secondary_unit = parenthesis_unit

            return quantity_unit_data


    quantity_unit_data.parenthesis_notes.append(f"used quantity/units from parenthesis with equivalent quantity/units")

    # set the secondary quantity/units to the original quantity/units
    quantity_unit_data.secondary_quantity = quantity_unit_data.quantity
    quantity_unit_data.secondary_unit = quantity_unit_data.unit

    quantity_unit_data.quantity = parenthesis_quantity
    quantity_unit_data.unit = parenthesis_unit

    return quantity_unit_data

class IngredientParser:
    """
    A class to parse recipe ingredients into a standard format.

    Args:
        ingredient (str): The ingredient to parse.
        debug (bool): Whether to print debug statements (default is False)
    """

    # regex = IngredientTools()

    def __init__(self, ingredient: str, debug = False):
        self.ingredient          = ingredient
        
        self._food              = None 
        self._quantity          = None    # the best quantity found in the ingredient string
        
        self._unit              = None    # the best unit found in the ingredient string
        self._standardized_unit = None   # "standard units" are the commonplace names for the found units (i.e. the standard unit of "oz" is "ounce")
        
        # make member variables for seconday quantities and units
        self._secondary_quantity = None
        self._secondary_unit     = None
        self._standardized_secondary_unit = None

        self._densities           = {}

        self._gram_weight         = None
        self._min_gram_weight     = None
        self._max_gram_weight     = None

        # "prep" are words that describe the state of the ingredient (i.e. "chopped", "diced", "minced")
        self._prep                  = []

        # "size modifiers" are words that describe the size of the ingredient (i.e. "large", "small", "medium")
        self._size_modifiers        = [] 

        self._is_required           = True    # default sets the ingredient as a required ingredient

        self.debug = debug

        self.ingredient_standardizer = self._get_ingredient_standardizer(self.ingredient)
        self._standardize() # standardize the ingredient string

        self._parse()

        self._parsed_ingredient = self.to_json()
    

    def _get_ingredient_standardizer(self, ingredient : str) -> IngredientStandardizer:
        # Create an instance of IngredientStandardizer
        ingredient_standardizer = IngredientStandardizer(ingredient)    
        return ingredient_standardizer

    def _standardize(self):

        # Get the standardized ingredient data (which is a dictionary)
        standardized_data = self.ingredient_standardizer.get_standardized_ingredient_data()

        # Iterate through the keys and set each key as the member variable
        # and the corresponding value as the member variable's value
        for key, value in standardized_data.items():
            setattr(self, key, value)
        
        return 
    
    def _is_ingredient_required(self, standardizer : IngredientStandardizer) -> bool:
        """
        Check if the ingredient is required or optional
        Returns a boolean indicating whether the ingredient is required or optional.
        """

        # check if the ingredient string contains the word "optional" or "required"
        # ingredient_is_required = self._check_if_required_string(self._reduced_ingredient)
        ingredient_is_required = self._check_if_required_string(standardizer.get_standardized_ingredient()) # TODO: testing this out

        # check the parenthesis content for the word "optional" or "required"
        parenthesis_is_required = self._check_if_required_parenthesis(standardizer.get_parenthesis_content())

        # if BOTH of the above conditions are True then return True otherwise return False
        return True if ingredient_is_required and parenthesis_is_required else False
    
    def _check_if_required_parenthesis(self, parenthesis_list: list) -> bool:
        """
        Check if the parenthesis content contains the word "optional".
        Args:
            parenthesis_list (list): A list of strings containing the content of the parenthesis in the ingredient string.
        Returns:
            bool: A boolean indicating whether the word "optional" is found in the parenthesis content.
        """

        optional_set = set(["option", "options", "optional", "opt.", "opts.", "opt", "opts", "unrequired"])
        required_set = set(["required", "requirement", "req.", "req"])
        
        # regex match for the words "optional" or "required" in the parenthesis content
        optional_match_flag = any([True if _regex_patterns.OPTIONAL_STRING.findall(i) else False for i in parenthesis_list])
        required_match_flag = any([True if _regex_patterns.REQUIRED_STRING.findall(i) else False for i in parenthesis_list])

        # check if any of the words in the parenthesis content are in the optional or required sets
        optional_str_flag = any([any([True if word in optional_set else False for word in i.replace("(", "").replace(")", "").replace(",", " ").split()]) for i in parenthesis_list])
        required_str_flag = any([any([True if word in required_set else False for word in i.replace("(", "").replace(")", "").replace(",", " ").split()]) for i in parenthesis_list])
        
        is_required = (True if required_match_flag or required_str_flag else False) or (False if optional_match_flag or optional_str_flag else True)

        return is_required

    def _check_if_required_string(self, ingredient: str) -> bool:
        """
        Check the ingredient string for optional or required text
        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            bool: A boolean indicating whether the ingredient is required or not.
        """
        # ingredient = reduced
        optional_set = set(["option", "options", "optional", "opt.", "opts.", "opt", "opts", "unrequired"])
        required_set = set(["required", "requirement", "req.", "req"])

        # regex match for the words "optional" or "required" in the ingredient string
        optional_match_flag = True if _regex_patterns.OPTIONAL_STRING.findall(ingredient) else False
        required_match_flag = True if _regex_patterns.REQUIRED_STRING.findall(ingredient) else False
        
        # check if any of the words in the ingredient string are in the optional or required sets
        optional_str_flag = any([True if word in optional_set else False for word in ingredient.replace(",", " ").split()])
        required_str_flag = any([True if word in required_set else False for word in ingredient.replace(",", " ").split()])

        # if any "required" strings were matched or found, or if no "optional" strings were matched or found, then the ingredient is required
        is_required = (True if required_match_flag or required_str_flag else False) or (False if optional_match_flag or optional_str_flag else True)

        return is_required

    def extract_first_quantity_unit(self, standardized_ingredient : str) -> QuantityUnitData:

        """
        Extract the first unit and quantity from an ingredient string.
        Function will extract the first unit and quantity from the ingredient string and set the self._quantity and self._unit member variables.
        Quantities and ingredients are extracted in this order and if any of the previous steps are successful, the function will return early.
        1. Check for basic units (e.g. 1 cup, 2 tablespoons)
        2. Check for nonbasic units (e.g. 1 fillet, 2 carrot sticks)
        3. Check for quantity only, no units (e.g. 1, 2)

        If none of the above steps are successful, then the self._quantity and self._unit member variables will be set to None.

        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            dict: A dictionary containing the first unit and quantity found in the ingredient string.
        Examples:
            >>> extract_first_unit_quantity('1 1/2 cups diced tomatoes, 2 tablespoons of sugar, 1 stick of butter')
            {'quantity': '1 1/2', 'unit': 'cups'}
            >>> extract_first_unit_quantity('2 1/2 cups of sugar')
            {'quantity': '2 1/2', 'unit': 'cups'}
        """
        
        # ---- STEP 1: CHECK FOR QUANTITY - BASIC UNITS (e.g. 1 cup, 2 tablespoons) ----
        # Example: "1.5 cup of sugar" -> quantity: "1.5", unit: "cup"

        # get the first number followed by a basic unit in the ingredient string
        basic_unit_matches = _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall(standardized_ingredient) # TODO: testing

        # remove any empty matches
        valid_basic_units = [i for i in basic_unit_matches if len(i) > 0]

        # if we have valid single number quantities, then set the self._quantity and the self._unit member variables and exit the function
        if basic_unit_matches and valid_basic_units:
            # self._quantity = valid_basic_units[0][0].strip()
            # self._unit = valid_basic_units[0][1].strip()
            return QuantityUnitData(
                quantity=valid_basic_units[0][0].strip(),
                unit=valid_basic_units[0][1].strip()
                )

        # ---- STEP 2: CHECK FOR QUANTITY - NONBASIC UNITS (e.g. 1 fillet, 2 carrot sticks) ----
        # Example: "1 fillet of salmon" -> quantity: "1", unit: "fillet"

        # If no basic units are found, then check for anumber followed by a nonbasic units
        nonbasic_unit_matches = _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall(standardized_ingredient) # TODO: testing

        # remove any empty matches
        valid_nonbasic_units = [i for i in nonbasic_unit_matches if len(i) > 0]

        # if we found a number followed by a non basic unit, then set the self._quantity and the self._unit member variables and exit the function
        if nonbasic_unit_matches and valid_nonbasic_units:
            # self._quantity = valid_nonbasic_units[0][0].strip()
            # self._unit = valid_nonbasic_units[0][1].strip()
            return QuantityUnitData(
                quantity=valid_nonbasic_units[0][0].strip(),
                unit=valid_nonbasic_units[0][1].strip()
            )
        
        # ---- STEP 3: CHECK FOR ANY QUANTITIES or ANY UNITS in the string, and use the first instances (if they exist) ----
        # Example: "cups, 2 juice of lemon" -> quantity: "2", unit: "juice"

        # if neither basic nor nonbasic units are found, then get all of the numbers and all of the units
        quantity_matches = _regex_patterns.ALL_NUMBERS.findall(standardized_ingredient) # TODO: testing
        unit_matches     = _regex_patterns.UNITS_PATTERN.findall(standardized_ingredient) # TODO: testing

        # remove any empty matches
        valid_quantities = [i for i in quantity_matches if len(i) > 0]
        valid_units     = [i for i in unit_matches if len(i) > 0]

        # if either have valid quantities then set the best quantity and best unit to 
        # the first valid quantity and units found, otherwise set as None
        # TODO: Drop this "if valid_quantities or valid_units"...?
        if valid_quantities or valid_units:
            # self._quantity = valid_quantities[0].strip() if valid_quantities else None
            # self._unit = valid_units[0].strip() if valid_units else None
            return QuantityUnitData(
                quantity = valid_quantities[0].strip() if valid_quantities else None,
                unit = valid_units[0].strip() if valid_units else None
                ) 

        # ---- STEP 4: NO MATCHES ----
        # just print a message if no valid quantities or units are found and return None
        # best_quantity and best_unit are set to None by default and will remain that way if no units or quantities were found.
        return QuantityUnitData(
            quantity = None,
            unit = None
            ) 
    
    def _address_quantity_only_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content only contains a quantity.
        Attempts to update self._quantity, self._unit, self._secondary_quantity, and self._secondary_unit given 
        information from the parenthesis string and the current self._quantity and self._unit
        (e.g. "(3)", "(2.5)", "(1/2)")
        Args:
            parenthesis (str): The content of the parenthesis in the ingredient string.
        Returns:
            None
        """

        # Set a None Description
        description = None

        # pull out the parenthesis quantity values
        numbers_only = _utils._extract_quantities_only(parenthesis) # NOTE: testing this out

        # if no numbers only parenthesis, then just return the original ingredient
        if not numbers_only:
            # print(f"\n > Return early from QUANTITY parenthesis") if self.debug else None
            description = f"not a quantity only parenthesis"
            self._parenthesis_notes.append(description)
            return
        
        is_approximate_quantity = _utils._is_approximate_quantity_only_parenthesis(parenthesis)

        # if the quantity is approximate, then add a note to the parenthesis notes and return early
        if is_approximate_quantity:
            description = f"approximate quantity only"
            self._parenthesis_notes.append(description)
            return

        # pull out the self._quantity from the parenthesis
        parenthesis_quantity = numbers_only[0]

        # if there is not a unit or a quantity, then we can use the parenthesis number as the quantity and
        #  return the ingredient with the new quantity
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if not self._quantity and not self._unit:
            description = f"maybe unit is: the 'food' or a 'sometimes unit'"
            self._parenthesis_notes.append(description)

            self._quantity = parenthesis_quantity
            return
        
        # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
        # then the unit is also likely the food 
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if self._quantity and not self._unit:
            updated_quantity = str(float(self._quantity) * float(parenthesis_quantity))
            
            description = f"maybe unit is: the 'food' or a 'sometimes unit'"
            self._parenthesis_notes.append(description)

            # set the secondary quantity to the ORIGINAL quantity/units
            self._secondary_quantity = self._quantity 

            # Update the quantity with the updated merged quantity
            self._quantity = _utils._make_int_or_float_str(updated_quantity)
            # self._quantity = updated_quantity

            # return [updated_quantity, self._unit, description]
            return
        
        # if there is a unit but no quantity, then we can use the parenthesis number as the quantity and 
        # return the ingredient with the new quantity
        if not self._quantity and self._unit:
            # updated_quantity = numbers_only[0]
            description = f"used quantity from parenthesis"
            self._parenthesis_notes.append(description)

            # set the secondary quantity to the ORIGINAL quantity/units
            self._secondary_quantity = self._quantity 

            # set the quantity to the parenthesis quantity
            self._quantity = parenthesis_quantity

            return

        # if there is a quantity and a unit, then we can try
        # to merge (multiply) the current quantity and the parenthesis quantity
        # then return the ingredient with the new quantity
        if self._quantity and self._unit:
            # if there is a quantity and a unit, then we can try to merge (multiply) the current quantity and the parenthesis quantity
            # then return the ingredient with the new quantity

            description = f"multiplied starting quantity with parenthesis quantity"
            self._parenthesis_notes.append(description)

            updated_quantity = str(float(self._quantity) * float(parenthesis_quantity))

            # set the secondary quantity to the ORIGINAL quantity/units
            self._secondary_quantity = self._quantity 

            # Update the quantity with the updated merged quantity (original quantity * parenthesis quantity)
            self._quantity = _utils._make_int_or_float_str(updated_quantity)
            # self._quantity = updated_quantity

            return

        description = f"used quantity from parenthesis with quantity only"
        self._parenthesis_notes.append(description)
        
        # set the secondary quantity to the ORIGINAL quantity/units
        self._secondary_quantity = self._quantity 

        # update the quantity with the parenthesis quantity value
        self._quantity = parenthesis_quantity

        return
    
    def _address_quantity_only_parenthesis2(self, parenthesis: str, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
        """
        Address the case where the parenthesis content only contains a quantity.
        Attempts to update self._quantity, self._unit, self._secondary_quantity, and self._secondary_unit given 
        information from the parenthesis string and the current self._quantity and self._unit
        (e.g. "(3)", "(2.5)", "(1/2)")
        Args:
            parenthesis (str): The content of the parenthesis in the ingredient string.
        Returns:
            None
        """

        # pull out the parenthesis quantity values
        numbers_only = _utils._extract_quantities_only(parenthesis) # NOTE: testing this out

        # if no numbers only parenthesis, then just return the original ingredient
        if not numbers_only:
            # print(f"\n > Return early from QUANTITY parenthesis") if self.debug else None
            quantity_unit_data.parenthesis_notes.append("not a quantity only parenthesis")
            return quantity_unit_data
        
        is_approximate_quantity = _utils._is_approximate_quantity_only_parenthesis(parenthesis)

        # if the quantity is approximate, then add a note to the parenthesis notes and return early
        if is_approximate_quantity:
            quantity_unit_data.parenthesis_notes.append("approximate quantity only")
            return quantity_unit_data 

        # pull out the quantity_unit_data.quantity from the parenthesis
        parenthesis_quantity = numbers_only[0]

        # if there is not a unit or a quantity, then we can use the parenthesis number as the quantity and
        #  return the ingredient with the new quantity
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if not quantity_unit_data.quantity and not quantity_unit_data.unit:
            quantity_unit_data.parenthesis_notes.append("maybe unit is: the 'food' or a 'sometimes unit'")
            quantity_unit_data.quantity = parenthesis_quantity
            return quantity_unit_data
        
        # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
        # then the unit is also likely the food 
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if quantity_unit_data.quantity and not quantity_unit_data.unit:
            updated_quantity = str(float(quantity_unit_data.quantity) * float(parenthesis_quantity))

            # update parenthesis notes 
            quantity_unit_data.parenthesis_notes.append("maybe unit is: the 'food' or a 'sometimes unit'")

            # set the secondary quantity to the ORIGINAL quantity/units
            quantity_unit_data.secondary_quantity = quantity_unit_data.quantity 

            # Update the quantity with the updated merged quantity
            quantity_unit_data.quantity = _utils._make_int_or_float_str(updated_quantity)
            # quantity_unit_data.quantity = updated_quantity

            # return [updated_quantity, quantity_unit_data.unit, description]
            return quantity_unit_data
        
        # if there is a unit but no quantity, then we can use the parenthesis number as the quantity and 
        # return the ingredient with the new quantity
        if not quantity_unit_data.quantity and quantity_unit_data.unit:
            # updated_quantity = numbers_only[0]
            quantity_unit_data.parenthesis_notes.append("used quantity from parenthesis")

            # set the secondary quantity to the ORIGINAL quantity/units
            quantity_unit_data.secondary_quantity = quantity_unit_data.quantity 

            # set the quantity to the parenthesis quantity
            quantity_unit_data.quantity = parenthesis_quantity

            return quantity_unit_data

        # if there is a quantity and a unit, then we can try
        # to merge (multiply) the current quantity and the parenthesis quantity
        # then return the ingredient with the new quantity
        if quantity_unit_data.quantity and quantity_unit_data.unit:
            # if there is a quantity and a unit, then we can try to merge (multiply) the current quantity and the parenthesis quantity
            # then return the ingredient with the new quantity

            quantity_unit_data.parenthesis_notes.append("multiplied starting quantity with parenthesis quantity")

            updated_quantity = str(float(quantity_unit_data.quantity) * float(parenthesis_quantity))

            # set the secondary quantity to the ORIGINAL quantity/units
            quantity_unit_data.secondary_quantity = quantity_unit_data.quantity 

            # Update the quantity with the updated merged quantity (original quantity * parenthesis quantity)
            quantity_unit_data.quantity = _utils._make_int_or_float_str(updated_quantity)
            # quantity_unit_data.quantity = updated_quantity

            return quantity_unit_data
    
        # update parenthesis notes
        quantity_unit_data.parenthesis_notes.append("used quantity from parenthesis with quantity only")
        
        # set the secondary quantity to the ORIGINAL quantity/units
        quantity_unit_data.secondary_quantity = quantity_unit_data.quantity 

        # update the quantity with the parenthesis quantity value
        quantity_unit_data.quantity = parenthesis_quantity

        return quantity_unit_data
        
    def _address_equivalence_parenthesis2(self, parenthesis: str, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
        """
        Address the case where the parenthesis content contains any equivalence strings like "about" or "approximately", followed by a quantity and then a unit later in the sting.
        Attempts to update quantity_unit_data.quantity, quantity_unit_data.unit, quantity_unit_data.secondary_quantity, and quantity_unit_data.secondary_unit given 
        information from the parenthesis string and the current quantity_unit_data.quantity and quantity_unit_data.unit
        e.g. "(about 3 ounces)", "(about a 1/3 cup)", "(approximately 1 large tablespoon)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self._reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{quantity_unit_data.quantity}'\nUnit: '{quantity_unit_data.unit}'""") if self.debug else None

        # check for the equivelency pattern (e.g. "<equivelent string> <quantity> <unit>" )
        equivalent_quantity_unit = _utils._extract_equivalent_quantity_units(parenthesis)
        # equivalent_quantity_unit = _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall(parenthesis)
        # equivalent_quantity_unit = [item for i in [regex.EQUIV_QUANTITY_UNIT_GROUPS.findall(i) for i in parenthesis] for item in i]

        # remove parenthesis and then split on whitespace
        split_parenthesis = parenthesis.replace("(", "").replace(")", "").split()

        # Case when: NO equivelence quantity unit matches 
        #           OR parenthesis contains a quantity per unit like string in the parenthesis (i.e. "(about 2 ounces each)" contains "each")
        # Then return early with NO UPDATES and keep the current quantity/unit as is
        if not equivalent_quantity_unit or any([True if i in _constants.QUANTITY_PER_UNIT_STRINGS else False for i in split_parenthesis]):
            # print(f"\n > Return early from EQUIVALENCE parenthesis") if self.debug else None
            quantity_unit_data.parenthesis_notes.append("not a equivalence quantity unit parenthesis")
            return quantity_unit_data
        
        # pull out the suffix word, parenthesis quantity and unit
        parenthesis_suffix, parenthesis_quantity, parenthesis_unit = equivalent_quantity_unit[0]
        
        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis quantity-unit as our quantity and unit
        if not quantity_unit_data.quantity and not quantity_unit_data.unit:

            quantity_unit_data.parenthesis_notes.append("used equivalence quantity unit as our quantity and unit")

            # set quantity/unit to the parenthesis values
            quantity_unit_data.quantity = parenthesis_quantity
            quantity_unit_data.unit = parenthesis_unit

            return quantity_unit_data
        
        # Case when: YES quantity, NO unit:
            # we can assume the equivelent quantity units 
            # in the parenthesis are actually a better fit for the quantities and units so 
            # we can use those are our quantities/units and then stash the original quantity in the "description" field 
            # with a "maybe quantity is " prefix in front of the original quantity for maybe use later on
        if quantity_unit_data.quantity and not quantity_unit_data.unit:

            # stash the old quantity with a trailing string before changing best_quantity
            quantity_unit_data.parenthesis_notes.append(f"maybe quantity is: {' '.join(quantity_unit_data.quantity)}")


            # make the secondary_quantity the starting quantity before converting the quantity to the value found in the parenthesis
            quantity_unit_data.secondary_quantity = quantity_unit_data.quantity

            # set the quantity/unit to the parenthesis values
            quantity_unit_data.quantity = parenthesis_quantity
            quantity_unit_data.unit = parenthesis_unit

            return quantity_unit_data

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are probably "better" so use the
            # parenthesis quantity/units and then stash the old unit in the description
        if not quantity_unit_data.quantity and quantity_unit_data.unit:

            # stash the old quantity with a trailing "maybe"
            quantity_unit_data.parenthesis_notes.append(f"maybe unit is: {quantity_unit_data.unit}")

            # make the secondary_unit the starting unit before converting the unit to the unit string found in the parenthesis
            quantity_unit_data.secondary_unit = quantity_unit_data.unit

            quantity_unit_data.quantity = parenthesis_quantity
            quantity_unit_data.unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return quantity_unit_data
        
        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely found an equivalent quantity/unit
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if quantity_unit_data.quantity and quantity_unit_data.unit:
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = quantity_unit_data.unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units:  (# TODO: Maybe we should use parenthesis quantity/unit instead...?)
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
                # return [quantity_unit_data.quantity, quantity_unit_data.unit, description]

                # set the secondary quantity/units to the values in the parenthesis
                quantity_unit_data.secondary_quantity = parenthesis_quantity
                quantity_unit_data.secondary_unit = parenthesis_unit

                return quantity_unit_data
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
                # return [quantity_unit_data.quantity, quantity_unit_data.unit, description]
                
                # set the secondary quantity/units to the values in the parenthesis
                quantity_unit_data.secondary_quantity = parenthesis_quantity
                quantity_unit_data.secondary_unit = parenthesis_unit

                return quantity_unit_data

            # Case when: YES basic parenthesis unit, NO basic original unit: 
            #   then use the parenthesis quantity/unit (stash the original in the description)
            if parenthesis_unit_is_basic:
                quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {quantity_unit_data.quantity}/{quantity_unit_data.unit}")
                
                # set the secondary quantity/units to the original quantity/units
                quantity_unit_data.secondary_quantity = quantity_unit_data.quantity
                quantity_unit_data.secondary_unit = quantity_unit_data.unit

                # update the primary quantities/units to the parenthesis values
                quantity_unit_data.quantity = parenthesis_quantity
                quantity_unit_data.unit = parenthesis_unit
                
                # return [parenthesis_quantity, parenthesis_unit, description]
                return quantity_unit_data

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then use the original quantity/unit (stash the parenthesis in the description)
            if unit_is_basic:
                quantity_unit_data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")

                # set the secondary quantity/units to the original quantity/units
                quantity_unit_data.secondary_quantity = parenthesis_quantity
                quantity_unit_data.secondary_unit = parenthesis_unit

                return quantity_unit_data


        quantity_unit_data.parenthesis_notes.append(f"used quantity/units from parenthesis with equivalent quantity/units")

        # set the secondary quantity/units to the original quantity/units
        quantity_unit_data.secondary_quantity = quantity_unit_data.quantity
        quantity_unit_data.secondary_unit = quantity_unit_data.unit

        quantity_unit_data.quantity = parenthesis_quantity
        quantity_unit_data.unit = parenthesis_unit

        return quantity_unit_data

    
    def _address_equivalence_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content contains any equivalence strings like "about" or "approximately", followed by a quantity and then a unit later in the sting.
        Attempts to update self._quantity, self._unit, self._secondary_quantity, and self._secondary_unit given 
        information from the parenthesis string and the current self._quantity and self._unit
        e.g. "(about 3 ounces)", "(about a 1/3 cup)", "(approximately 1 large tablespoon)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self._reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self._quantity}'\nUnit: '{self._unit}'""") if self.debug else None

        
        # Set a None Description
        description = None

        # check for the equivelency pattern (e.g. "<equivelent string> <quantity> <unit>" )
        equivalent_quantity_unit = _utils._extract_equivalent_quantity_units(parenthesis)
        # equivalent_quantity_unit = _regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall(parenthesis)
        # equivalent_quantity_unit = [item for i in [regex.EQUIV_QUANTITY_UNIT_GROUPS.findall(i) for i in parenthesis] for item in i]

        # remove parenthesis and then split on whitespace
        split_parenthesis = parenthesis.replace("(", "").replace(")", "").split()

        # Case when: NO equivelence quantity unit matches 
        #           OR parenthesis contains a quantity per unit like string in the parenthesis (i.e. "(about 2 ounces each)" contains "each")
        # Then return early with NO UPDATES and keep the current quantity/unit as is
        if not equivalent_quantity_unit or any([True if i in _constants.QUANTITY_PER_UNIT_STRINGS else False for i in split_parenthesis]):
            # print(f"\n > Return early from EQUIVALENCE parenthesis") if self.debug else None
            description = f"not a equivalence quantity unit parenthesis"
            self._parenthesis_notes.append(description)
            return
        
        # pull out the suffix word, parenthesis quantity and unit
        parenthesis_suffix, parenthesis_quantity, parenthesis_unit = equivalent_quantity_unit[0]
        
        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis quantity-unit as our quantity and unit
        if not self._quantity and not self._unit:

            description = f"used equivalence quantity unit as our quantity and unit"
            self._parenthesis_notes.append(description)

            # set quantity/unit to the parenthesis values
            self._quantity = parenthesis_quantity
            self._unit = parenthesis_unit

            return
        
        # Case when: YES quantity, NO unit:
            # we can assume the equivelent quantity units 
            # in the parenthesis are actually a better fit for the quantities and units so 
            # we can use those are our quantities/units and then stash the original quantity in the "description" field 
            # with a "maybe quantity is " prefix in front of the original quantity for maybe use later on
        if self._quantity and not self._unit:

            # stash the old quantity with a trailing string before changing best_quantity
            description = f"maybe quantity is: {' '.join(self._quantity)}"
            self._parenthesis_notes.append(description)

            # make the secondary_quantity the starting quantity before converting the quantity to the value found in the parenthesis
            self._secondary_quantity = self._quantity

            # set the quantity/unit to the parenthesis values
            self._quantity = parenthesis_quantity
            self._unit = parenthesis_unit

            return 

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are probably "better" so use the
            # parenthesis quantity/units and then stash the old unit in the description
        if not self._quantity and self._unit:

            # stash the old quantity with a trailing "maybe"
            description = f"maybe unit is: {self._unit}"
            self._parenthesis_notes.append(description)

            # make the secondary_unit the starting unit before converting the unit to the unit string found in the parenthesis
            self._secondary_unit = self._unit

            self._quantity = parenthesis_quantity
            self._unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return 
        
        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely found an equivalent quantity/unit
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if self._quantity and self._unit:
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = self._unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units:  (# TODO: Maybe we should use parenthesis quantity/unit instead...?)
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self._parenthesis_notes.append(description)
                # return [self._quantity, self._unit, description]

                # set the secondary quantity/units to the values in the parenthesis
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit

                return
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self._parenthesis_notes.append(description)
                # return [self._quantity, self._unit, description]
                
                # set the secondary quantity/units to the values in the parenthesis
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit

                return

            # Case when: YES basic parenthesis unit, NO basic original unit: 
            #   then use the parenthesis quantity/unit (stash the original in the description)
            if parenthesis_unit_is_basic:
                description = f"maybe quantity/unit is: {self._quantity}/{self._unit}"
                self._parenthesis_notes.append(description)
                
                # set the secondary quantity/units to the original quantity/units
                self._secondary_quantity = self._quantity
                self._secondary_unit = self._unit

                # update the primary quantities/units to the parenthesis values
                self._quantity = parenthesis_quantity
                self._unit = parenthesis_unit
                
                # return [parenthesis_quantity, parenthesis_unit, description]
                return

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then use the original quantity/unit (stash the parenthesis in the description)
            if unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit

                return

        description = f"used quantity/units from parenthesis with equivalent quantity/units"
        self._parenthesis_notes.append(description)

        # set the secondary quantity/units to the original quantity/units
        self._secondary_quantity = self._quantity
        self._secondary_unit = self._unit

        self._quantity = parenthesis_quantity
        self._unit = parenthesis_unit

        return
    
    def _address_quantity_unit_only_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content contains exactly a quantity and unit (NOT prefixed by any equivalence strings like "about" or "approximately").
        Attempts to update self._quantity, self._unit, self._secondary_quantity, and self._secondary_unit given 
        information from the parenthesis string and the current self._quantity and self._unit
        e.g. "(3 ounces)", "(3 ounces each)", "(a 4 cup scoop)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self._standardized_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self._quantity}'\nUnit: '{self._unit}'""") if self.debug else None

        # Set a None Description
        description = None

        # pull out quantity unit only pattern
        quantity_unit_only = _utils._extract_quantity_unit_pairs(parenthesis)

        # if no numbers only parenthesis, then just return the original ingredient
        if not quantity_unit_only:
            description = f"not a quantity unit only parenthesis"
            self._parenthesis_notes.append(description)
            return
        
        # pull out the parenthesis quantity and unit
        parenthesis_quantity, parenthesis_unit = quantity_unit_only[0]

        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis self._quantity-unit as our self._quantity and unit
        if not self._quantity and not self._unit:
            # updated_quantity, updated_unit = quantity_unit_only[0]
            # print(f"\n > Case when: NO quantity, NO unit") if self.debug else None

            description = f"used quantity/unit from parenthesis with no quantity/unit"
            self._parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self._secondary_quantity = self._quantity
            self._secondary_unit = self._unit

            self._quantity = parenthesis_quantity
            self._unit = parenthesis_unit

            return

        # Case when: YES quantity, NO unit:
            # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
            # then use the unit in the parenthesis
        if self._quantity and not self._unit:
            # print(f"\n > Case when: YES quantity, NO unit") if self.debug else None

            # quantity_unit_only[0][0]
            updated_quantity = str(float(self._quantity) * float(parenthesis_quantity))

            description = f"multiplied starting quantity with parenthesis quantity"
            self._parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self._secondary_quantity = self._quantity
            self._secondary_unit = self._unit

            self._quantity = _utils._make_int_or_float_str(updated_quantity)
            self._unit = parenthesis_unit

            return

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are either:
            # 1. A description/note (i.e. cut 0.5 inch slices)
            # 2. A quantity and unit (i.e. 2 ounces)
            # either case, just return the parenthesis units to use those
        if not self._quantity and self._unit:
            # print(f"\n > Case when: NO quantity, YES unit") if self.debug else None

            description = f"No quantity but has units, used parenthesis. maybe quantity/unit is: {self._quantity}/{self._unit}"
            self._parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self._secondary_quantity = self._quantity
            self._secondary_unit = self._unit

            self._quantity = parenthesis_quantity
            self._unit = parenthesis_unit

            return

        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely just found a description 
            # OR we may have found an equivalence quantity unit.
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if self._quantity and self._unit:
            # print(f"\n > Case when: YES quantity, YES unit") if self.debug else None

            # flags for if original unit/parenthesis unit are in the set of basic units (BASIC_UNITS_SET) or not
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = self._unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units: 
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, BASIC unit") if self.debug else None

                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit
                return
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values 
            #   (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, NOT BASIC unit") if self.debug else None
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit
                return

            # Case when: YES basic parenthesis unit, NO basic original unit (EXPLICIT):
            #  Try to merge (multiply) the current quantity and the parenthesis quantity
            #  AND set the secondary quantity/units to the ORIGINAL values
            if parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (EXPLICIT)") if self.debug else None
                updated_quantity = str(float(self._quantity) * float(parenthesis_quantity))

                description = f"multiplied starting quantity with parenthesis quantity"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self._secondary_quantity = self._quantity
                self._secondary_unit = self._unit

                # self._quantity = updated_quantity
                self._quantity = _utils._make_int_or_float_str(updated_quantity)
                self._unit = parenthesis_unit

                return

            # TODO: I think this condition can be dropped, gets covered by previous condition...
            # Case when: YES basic parenthesis unit, NO basic original unit (IMPLICITLY): 
            #   then use the parenthesis quantity/unit AND set the secondary quantity/units to the ORIGINAL values
            #   (stash the original in the description)
            if parenthesis_unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (IMPLICIT)") if self.debug else None
                description = f"maybe quantity/unit is: {self._quantity}/{self._unit}"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self._secondary_quantity = self._quantity
                self._secondary_unit = self._unit

                self._quantity = parenthesis_quantity
                self._unit = parenthesis_unit

                return

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then just keep the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values
            #   (stash the original in the description)
            if unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, BASIC unit (IMPLICIT)") if self.debug else None
                description = f"maybe quantity/unit is: {self._quantity}/{self._unit}"
                self._parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self._secondary_quantity = parenthesis_quantity
                self._secondary_unit = parenthesis_unit

                return
        
        # print(f"\n ----> Case when: ALL OTHER CASES FAILED") if self.debug else None

        # TODO: Don't think this should ever happen, need to rethink this part
        # Case when: All other conditions were NOT met:
            # just set the quantity/unit to the parenthesis values 
            # and then put the original quantity/units in the secondary quantity/units
        description = f"used quantity/units from parenthesis with quantity/units only"
        self._parenthesis_notes.append(description)

        # set the secondary quantity/units to the ORIGINAL quantity/units
        self._secondary_quantity = self._quantity 
        self._secondary_unit = self._unit

        # set the primary quantity/units to the parenthesis quantity/units
        self._quantity = parenthesis_quantity
        self._unit = parenthesis_unit

        return
    
    def _address_parenthesis(self, parenthesis_content : list) -> None:
        """
        Address any parenthesis that were in the ingredient.
        """
        # print(f"Addressing parenthesis: '{self._parenthesis_content}'") if self.debug else None

        # loop through each of the parenthesis in the parenthesis content and apply address_parenthesis functions 
        for parenthesis in parenthesis_content:

            # address the case where the parenthesis content only contains a quantity
            self._address_quantity_only_parenthesis(parenthesis)
            
            self._address_equivalence_parenthesis(parenthesis)

            self._address_quantity_unit_only_parenthesis(parenthesis)

        return 
    
    def _add_standard_units(self) -> None:
        """
        Add standard units to the parsed ingredient if they are present in the
        constants units to standard units map.
        If the "unit"/"secondary_unit" exists and it is present in the unit to standard unit map, 
        then get the standard unit name for the unit and set the "standardized_unit" and "standardized_secondary_unit" member variables.
        """

        if self._unit and self._unit in _constants.UNIT_TO_STANDARD_UNIT:
            self._standardized_unit = _constants.UNIT_TO_STANDARD_UNIT[self._unit]
        
        if self._secondary_unit and self._secondary_unit in _constants.UNIT_TO_STANDARD_UNIT:
            self._standardized_secondary_unit = _constants.UNIT_TO_STANDARD_UNIT[self._secondary_unit]

        return 

    def _prioritize_weight_units(self) -> None:
        """
        Prioritize weight units over volume units if both are present in the parsed ingredient.
        If the first unit is not a weight unit but the secondary_unit is a weight unit, then swap them so 
        the weight unit is always given as the primary unit.
        (i.e. unit = "cups", secondary_unit = "ounces" --> Swap them so that unit = "ounces" and secondary_unit = "cups")
        """

        # # if the first unit is already a weight, just return early
        if self._unit in _constants.WEIGHT_UNITS_SET:
            return 
        
        # TODO: first part of this if statement is probably redundent...
        # if the first unit is NOT a weight and the second unit IS a weight, then swap them
        if self._unit not in _constants.WEIGHT_UNITS_SET and self._secondary_unit in _constants.WEIGHT_UNITS_SET:

            # print(f"Swapping first quantity/units with second quantity/units") if self.debug else None
            # print(f"Swapping first quantity/units with second quantity/units") if self.debug else None

            # switch the units and quantities with the secondary units and quantities
            self._quantity, self._secondary_quantity = self._secondary_quantity, self._quantity
            self._unit, self._secondary_unit = self._secondary_unit,  self._unit
            self._standardized_unit, self._standardized_secondary_unit = self._standardized_secondary_unit, self._standardized_unit

        return 
    
    def _extract_foods(self, ingredient: str) -> str:
        """Does a best effort attempt to extract foods from the ingredient by 
        removing all extraneous details, words, characters and hope we get left with the food.
        """

        # print(f"Best effort extraction of food words from: {ingredient}") if self.debug else None

        # Apply _utils._remove_parenthesis_from_str() to remove parenthesis content
        ingredient = _utils._remove_parenthesis_from_str(ingredient)

        # check for obscure/tricky edge case foods and if found, return them as the food (i.e. half-and-half, etc.)
        edge_food = _utils._extract_edge_case_foods(ingredient)
        if edge_food:
            return edge_food

        # regular expressions to find and remove from the ingredient
        # NOTE: important to remove "parenthesis" first and "stop words" last to.
        # Parenthesis can contain other patterns and they need to be dealt with first (i.e. "(about 8 oz)" contains a number and a unit)
        patterns_map = {
            # "parenthesis" : _regex_patterns.SPLIT_BY_PARENTHESIS, # NOTE: testing this removal
            "units" : _regex_patterns.UNITS_PATTERN,
            "numbers" : _regex_patterns.ALL_NUMBERS,
            "prep words" : _regex_patterns.PREP_WORDS_PATTERN,
            "ly-words" : _regex_patterns.WORDS_ENDING_IN_LY,
            "unit modifiers" : _regex_patterns.UNIT_MODIFIERS_PATTERN,
            "dimension units" : _regex_patterns.DIMENSION_UNITS_PATTERN,
            "approximate strings" : _regex_patterns.APPROXIMATE_STRINGS_PATTERN,
            "size modifiers" : _regex_patterns.SIZE_MODIFIERS_PATTERN,
            "casual quantities" : _regex_patterns.CASUAL_QUANTITIES_PATTERN,
            "stop words" : _regex_patterns.STOP_WORDS_PATTERN
        }

        for key, pattern in patterns_map.items():
            ingredient = _utils._find_and_remove(ingredient, pattern)
        
        ingredient = re.sub(r'[^\w\s]', '', ingredient) # remove any special characters
        ingredient = re.sub(r'\s+', ' ', ingredient).strip() # remove any extra whitespace

        return ingredient
    
    def _extract_prep_words(self, ingredient: str) -> str:
        """Get prep words from the ingredient (including words ending in 'ly')"""

        ly_ending_words = set(_regex_patterns.WORDS_ENDING_IN_LY.findall(ingredient))
        ly_ending_words = list(ly_ending_words - _constants.APPROXIMATE_STRINGS) # remove any accidental match overlaps like "approximately"

        prep_words = _regex_patterns.PREP_WORDS_PATTERN.findall(ingredient)
        prep_words.extend(ly_ending_words) # combine the prep words with the 'ly' ending words
        prep_words = list(set(prep_words)) # unique 
        prep_words.sort()       

        return prep_words
    
    def _extract_size_modifiers(self, ingredient: str) -> str:
        """Extract size modifier words from the ingredient"""

        size_modifiers = _regex_patterns.SIZE_MODIFIERS_PATTERN.findall(ingredient)
        size_modifiers.sort()

        return size_modifiers

    def _add_food_density(self):
        """Add food densities to the units variables if they are the only possible units after the ingredient has been parsed."""
        # ingredient = "2 1/2 cups of sugar (about 1/2 inch squares of sugar)"
        
        if _utils._has_volume_unit(self._unit, self._standardized_unit, self._secondary_unit, self._standardized_secondary_unit):
            densities       = _utils._get_food_density(self._food, "dice")
            self._densities = densities

    def _add_gram_weights(self):
        """Add gram weights to the units variables if they are the only possible units after the ingredient has been parsed."""
        
        grams_map = _utils._get_gram_weight(self._food, self._quantity, self._unit, self._densities, "dice")

        if grams_map:
            self._gram_weight     = grams_map.get("gram_weight", None)
            self._min_gram_weight = grams_map.get("min_gram_weight", None)
            self._max_gram_weight = grams_map.get("max_gram_weight", None)

        return
    
    def _add_gram_weights_for_single_item_foods(self):

        if not self._gram_weight:
            # print(f'THIS IS A SINGLE ITEM FOOD: {self._food}') if self.debug else None
            # NOTE: this is an arbitrary fuzzy string matching ratio of 0.85 for now, probably want this to be pretty strict 
            # NOTE: so we don't get false positives (maybe even just make it 0.95 or 1 to just only match single character differences)
            gram_weight = _utils._get_single_item_gram_weight(self._food, self._quantity)

            self._gram_weight = gram_weight

        return 

    def _get_food_units(self):
        """If no units were found, check for possible 'food units', and use those if they are found"""

        if not self._unit and not self._standardized_unit:
            food_unit     = _utils._get_food_unit(self._standardized_ingredient)
            std_food_unit = _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(food_unit)

            self._unit              = food_unit
            self._standardized_unit = std_food_unit
        
        return 
    
    def _set_default_quantities(self):
        """Set a default quantity if no quantity was found"""
        
        is_weight_or_volume_unit = _utils._is_weight_unit(self._standardized_unit) or _utils._is_volumetric_unit(self._standardized_unit)
        missing_primary_quantity = self._quantity is None
        
        if is_weight_or_volume_unit and missing_primary_quantity:
            self._quantity = "1"

        return

    def _get_animal_protein_gram_weight(self):
        """If the food is an animal protein, then get the gram weight for that protein"""
        if not self._gram_weight:
            gram_weight = _utils._get_animal_protein_gram_weight(self._quantity, self._unit)
            if not gram_weight:
                gram_weight = _utils._get_animal_protein_gram_weight(self._secondary_quantity, self._secondary_unit)
            
            self._gram_weight = gram_weight

        return 
    
    def _address_parenthesis(self, parenthesis_content : list) -> None:
        """
        Address any parenthesis that were in the ingredient.
        """
        # print(f"Addressing parenthesis: '{self._parenthesis_content}'") if self.debug else None

        # loop through each of the parenthesis in the parenthesis content and apply address_parenthesis functions 
        for parenthesis in parenthesis_content:

            # address the case where the parenthesis content only contains a quantity
            self._address_quantity_only_parenthesis(parenthesis)
            
            self._address_equivalence_parenthesis(parenthesis)

            self._address_quantity_unit_only_parenthesis(parenthesis)

        return

    def _parse(self):
        # TODO: process parenthesis content

        print(f"Standardizing ingredient: \n > '{self.ingredient}'") if self.debug else None

        # ----------------------------------- STEP 1 ------------------------------------------
        # ---- Get the input ingredient string into a standardized form ----
        # -------------------------------------------------------------------------------------

        # # run the standardization method to cleanup raw ingredient and create the "standard_ingredient" and "_reduced_ingredient" member variables 
        # self._standardize()

        print(f"Standardized ingredient: \n > '{self._standardized_ingredient}'") if self.debug else None
        # ----------------------------------- STEP 2 ------------------------------------------
        # ---- Check if there is any indication of the ingredient being required/optional ----
        # -------------------------------------------------------------------------------------

        # run the is_required method to check if the ingredient is required or optional and set the "is_required" member variable to the result
        self._is_required = self._is_ingredient_required(self.ingredient_standardizer)

        print(f"Is the ingredient required? {self._is_required}") if self.debug else None
        # ----------------------------------- STEP 3 ------------------------------------------
        # ---- Extract first options of quantities and units from the "_reduced_ingredient" ----
        # -------------------------------------------------------------------------------------
        print(f"Attempting to extract quantity and unit") if self.debug else None
        # run the extract_first_quantity_unit method to extract the first unit and quantity from the ingredient string
        quantity_unit_data = self.extract_first_quantity_unit(self.ingredient_standardizer.get_standardized_ingredient())
        self._quantity = quantity_unit_data.quantity
        self._unit     = quantity_unit_data.unit

        # ----------------------------------- STEP 4 ------------------------------------------
        # ---- Address any parenthesis that were in the ingredient  ----
        # -------------------------------------------------------------------------------------
        # NOTE: Stash the best_quantity and best_units before preceeding (for debugging)

        print(f"""Addressing parenthesis: 
                > Standard ingredient: '{self._standardized_ingredient}'
                > Parenthesis content: '{self._parenthesis_content}'
            """) if self.debug else None

        self._address_parenthesis(self.ingredient_standardizer.get_parenthesis_content())

        # ----------------------------------- STEP 5 ------------------------------------------
        # ---- Get the standard names of the units and secondary units ----
        # -------------------------------------------------------------------------------------
        print(f"Adding standard unit names for {self._unit} and {self._secondary_unit}") if self.debug else None

        self._add_standard_units()

        # ----------------------------------- STEP 6 ------------------------------------------
        # ---- Prioritize weight units and always place the weight unit as the primary ingredient if it exists ----
        # -------------------------------------------------------------------------------------
        print(f"Prioritizing weight units") if self.debug else None

        self._prioritize_weight_units()

        # ----------------------------------- STEP 7 ------------------------------------------
        # ---- Extract foods the best we can by removing:
        # > parenthesis content
        # > stop words
        # > units
        # > quantities
        # > prep words
        # > "ly"-words
        # -------------------------------------------------------------------------------------
        print(f"Extracting food words") if self.debug else None
        
        self._food = self._extract_foods(self._standardized_ingredient)

        # ----------------------------------- STEP 8 ------------------------------------------
        # ---- Extract extra, descriptors (prep words, size modifiers, dimension units) ----
        # -------------------------------------------------------------------------------------
        print(f"Extracting prep words, size modifiers") if self.debug else None
        self._prep = self._extract_prep_words(self._staged_ingredient) 
        self._size_modifiers = self._extract_size_modifiers(self._staged_ingredient) 
        
        # ----------------------------------- STEP 9 ------------------------------------------
        # ---- Calculate food density if possible ----
        # -------------------------------------------------------------------------------------
        print(f"Calculating food density") if self.debug else None
        self._add_food_density() 

        # ----------------------------------- STEP 10 ------------------------------------------
        # ---- Calculate gram weights if possible ----
        # -------------------------------------------------------------------------------------
        print(f"Calculating gram weights") if self.debug else None
        self._add_gram_weights() 

        # ----------------------------------- STEP 11 ------------------------------------------
        # ---- Calculate gram weights if possible ----
        # -------------------------------------------------------------------------------------
        print(f"Estimating gram weights for unitless foods") if self.debug else None
        self._add_gram_weights_for_single_item_foods() 

        # ----------------------------------- STEP 12 ------------------------------------------
        # ---- If no units were found ---- 
        # ---- check for food units and set those as the unit / standardized_unit ----
        # -------------------------------------------------------------------------------------
        print(f"Checking for possible 'food units' (i.e. '2 corn tortillas' has a unit of 'tortillas')") if self.debug else None
        self._get_food_units() 
       
        # ----------------------------------- STEP 13 ------------------------------------------
        # ---- If not quantity is found, set quantity to a default of 1 ---- 
        # -------------------------------------------------------------------------------------
        print(f"Set quantity to 1 if not found") if self.debug else None
        self._set_default_quantities()
       
        # ----------------------------------- STEP 14 ------------------------------------------
        # ---- If no gram weight has been found ---- 
        # ---- check for any common 'animal protein units' (i.e. 'breasts', 'drumsticks', etc)
        # ---- and calculate a gram weight for any found units ----
        # -------------------------------------------------------------------------------------
        print(f"Checking for possible 'animal protein units' (i.e. '2 chicken breasts' has a unit of 'breast') and calculating a gram weight for any found units") if self.debug else None
        self._get_animal_protein_gram_weight() 