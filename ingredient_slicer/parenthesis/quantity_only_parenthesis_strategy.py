# from . import _utils
# from .parser._parenthesis_handler import ParenthesisHandler
# from .models.quantity_unit_data import QuantityUnitData

from ingredient_slicer import _utils
from ingredient_slicer.parenthesis.parenthesis_handler import ParenthesisHandler
from ingredient_slicer.models.quantity_unit_data import QuantityUnitData

class QuantityOnlyParenthesisHandler(ParenthesisHandler):
    def handle(self, parenthesis: str, data: QuantityUnitData) -> QuantityUnitData:
    
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
            data.parenthesis_notes.append("not a quantity only parenthesis")
            return data
        
        is_approximate_quantity = _utils._is_approximate_quantity_only_parenthesis(parenthesis)

        # if the quantity is approximate, then add a note to the parenthesis notes and return early
        if is_approximate_quantity:
            data.parenthesis_notes.append("approximate quantity only")
            return data 

        # pull out the data.quantity from the parenthesis
        parenthesis_quantity = numbers_only[0]

        # if there is not a unit or a quantity, then we can use the parenthesis number as the quantity and
        #  return the ingredient with the new quantity
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if not data.quantity and not data.unit:
            data.parenthesis_notes.append("maybe unit is: the 'food' or a 'sometimes unit'")
            data.quantity = parenthesis_quantity
            return data
        
        # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
        # then the unit is also likely the food 
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if data.quantity and not data.unit:
            updated_quantity = str(float(data.quantity) * float(parenthesis_quantity))

            # update parenthesis notes 
            data.parenthesis_notes.append("maybe unit is: the 'food' or a 'sometimes unit'")

            # set the secondary quantity to the ORIGINAL quantity/units
            data.secondary_quantity = data.quantity 

            # Update the quantity with the updated merged quantity
            data.quantity = _utils._make_int_or_float_str(updated_quantity)

            return data
        
        # if there is a unit but no quantity, then we can use the parenthesis number as the quantity and 
        # return the ingredient with the new quantity
        if not data.quantity and data.unit:
            # updated_quantity = numbers_only[0]
            data.parenthesis_notes.append("used quantity from parenthesis")

            # set the secondary quantity to the ORIGINAL quantity/units
            data.secondary_quantity = data.quantity 

            # set the quantity to the parenthesis quantity
            data.quantity = parenthesis_quantity

            return data

        # if there is a quantity and a unit, then we can try
        # to merge (multiply) the current quantity and the parenthesis quantity
        # then return the ingredient with the new quantity
        if data.quantity and data.unit:
            # if there is a quantity and a unit, then we can try to merge (multiply) the current quantity and the parenthesis quantity
            # then return the ingredient with the new quantity

            data.parenthesis_notes.append("multiplied starting quantity with parenthesis quantity")

            updated_quantity = str(float(data.quantity) * float(parenthesis_quantity))

            # set the secondary quantity to the ORIGINAL quantity/units
            data.secondary_quantity = data.quantity 

            # Update the quantity with the updated merged quantity (original quantity * parenthesis quantity)
            data.quantity = _utils._make_int_or_float_str(updated_quantity)

            return data
    
        # update parenthesis notes
        data.parenthesis_notes.append("used quantity from parenthesis with quantity only")
        
        # set the secondary quantity to the ORIGINAL quantity/units
        data.secondary_quantity = data.quantity 

        # update the quantity with the parenthesis quantity value
        data.quantity = parenthesis_quantity

        return data