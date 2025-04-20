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
