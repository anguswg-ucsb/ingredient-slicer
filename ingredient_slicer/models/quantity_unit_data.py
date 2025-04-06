from typing import Union
from dataclasses import dataclass, field

from ingredient_slicer import _constants
from ingredient_slicer import _utils

@dataclass
class QuantityUnitData:
    quantity: Union[str, None] = None 
    unit: Union[str, None] = None 
    standardized_unit : Union[str, None] = None
    secondary_quantity: Union[str, None] = None
    secondary_unit: Union[str, None] = None
    standardized_secondary_unit : Union[str, None] = None
    parenthesis_notes: list[str] = field(default_factory=list)

    def standardize_unit(self) -> None:
        self.standardized_unit = self._convert_to_standard_unit(self.unit)
        return 

    def standardize_secondary_unit(self) -> None:
        self.standardized_secondary_unit = self._convert_to_standard_unit(self.secondary_unit)
        return 

    def _convert_to_standard_unit(self, unit : str) -> str:
        """
        Add standard units to the parsed ingredient if they are present in the
        constants units to standard units map.
        If the "unit"/"secondary_unit" exists and it is present in the unit to standard unit map, 
        then get the standard unit name for the unit and set the "standardized_unit" and "standardized_secondary_unit" member variables.
        """

        if unit and unit in _constants.UNIT_TO_STANDARD_UNIT:
            return _constants.UNIT_TO_STANDARD_UNIT.get(unit)
        
        return 
    
    def swap_quantity_unit_ordering(self):
        self.swap_quantities()
        self.swap_units()
        self.swap_standardized_units()
        return 

    def swap_quantities(self):
        self.quantity, self.secondary_quantity = self.secondary_quantity, self.quantity
        return 
    
    def swap_units(self):
        self.unit, self.secondary_unit = self.secondary_unit, self.unit
        return 

    def swap_standardized_units(self):
        self.standardized_unit, self.standardized_secondary_unit = self.standardized_secondary_unit, self.standardized_unit
        return 

    def set_food_units(self, ingredient : str) -> None: 
        """If no units were found, check for possible 'food units', and update the QuantityUnitData if any food units are found/needed"""

        if not self.unit and not self.standardized_unit:
            food_unit     = _utils._get_food_unit(ingredient)
            std_food_unit = _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(food_unit)

            self.unit = food_unit
            self.standardized_unit = std_food_unit
        
        return 

    def set_default_quantity(self, default_quantity : str = "1") -> None:
        """Set a default quantity if no quantity was found"""
        
        is_weight_or_volume_unit = _utils._is_weight_unit(self.standardized_unit) or _utils._is_volumetric_unit(self.standardized_unit)
        missing_primary_quantity = self.quantity is None
        
        if is_weight_or_volume_unit and missing_primary_quantity:
            self.quantity = default_quantity

        return 


class IngredientParser: 

    def _address_quantity_only_parenthesis(self, parenthesis: str, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
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
    
    def _apply_parenthesis_content_to_quantity_unit_data(self, 
                                                         parenthesis_content : list, 
                                                         quantity_unit_data : QuantityUnitData
                                                         ) -> QuantityUnitData:
        """
        Address any parenthesis that were in the ingredient.
        """
        # print(f"Addressing parenthesis: '{self._parenthesis_content}'") if self.debug else None
        parenthesis_functions = [
            self._address_quantity_only_parenthesis,
            # TODO: there will be more methods here
            # self._address_equivalence_parenthesis,
            # self._address_quantity_unit_only_parenthesis
        ]

        # loop through each of the parenthesis in the parenthesis content and apply address_parenthesis functions 
        for parenthesis in parenthesis_content:

            # address the different cases when parenthesis will be used to modify quanity and/or units 
            for func in parenthesis_functions:
                quantity_unit_data = func(parenthesis, quantity_unit_data)

        return quantity_unit_data
    