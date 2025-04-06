# from . import _constants
# from . import _utils
# from .parser._parenthesis_handler import ParenthesisHandler
# from .models.quantity_unit_data import QuantityUnitData

from ingredient_slicer import _constants
from ingredient_slicer import _utils
from ingredient_slicer.parenthesis.parenthesis_handler import ParenthesisHandler
from ingredient_slicer.models.quantity_unit_data import QuantityUnitData

class EquivalenceParenthesisHandler(ParenthesisHandler):
    def handle(self, parenthesis: str, data: QuantityUnitData) -> QuantityUnitData:
    
        """
        Address the case where the parenthesis content contains any equivalence strings like "about" or "approximately", followed by a quantity and then a unit later in the sting.
        Attempts to update data.quantity, data.unit, data.secondary_quantity, and data.secondary_unit given 
        information from the parenthesis string and the current data.quantity and data.unit
        e.g. "(about 3 ounces)", "(about a 1/3 cup)", "(approximately 1 large tablespoon)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self._reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{data.quantity}'\nUnit: '{data.unit}'""") if self.debug else None

        # check for the equivelency pattern (e.g. "<equivelent string> <quantity> <unit>" )
        equivalent_quantity_unit = _utils._extract_equivalent_quantity_units(parenthesis)

        # remove parenthesis and then split on whitespace
        split_parenthesis = parenthesis.replace("(", "").replace(")", "").split()

        # Case when: NO equivelence quantity unit matches 
        #           OR parenthesis contains a quantity per unit like string in the parenthesis (i.e. "(about 2 ounces each)" contains "each")
        # Then return early with NO UPDATES and keep the current quantity/unit as is
        if not equivalent_quantity_unit or any([True if i in _constants.QUANTITY_PER_UNIT_STRINGS else False for i in split_parenthesis]):
            # print(f"\n > Return early from EQUIVALENCE parenthesis") if self.debug else None
            data.parenthesis_notes.append("not a equivalence quantity unit parenthesis")
            return data
        
        # pull out the suffix word, parenthesis quantity and unit
        parenthesis_suffix, parenthesis_quantity, parenthesis_unit = equivalent_quantity_unit[0]
        
        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis quantity-unit as our quantity and unit
        if not data.quantity and not data.unit:

            data.parenthesis_notes.append("used equivalence quantity unit as our quantity and unit")

            # set quantity/unit to the parenthesis values
            data.quantity = parenthesis_quantity
            data.unit = parenthesis_unit

            return data
        
        # Case when: YES quantity, NO unit:
            # we can assume the equivelent quantity units 
            # in the parenthesis are actually a better fit for the quantities and units so 
            # we can use those are our quantities/units and then stash the original quantity in the "description" field 
            # with a "maybe quantity is " prefix in front of the original quantity for maybe use later on
        if data.quantity and not data.unit:

            # stash the old quantity with a trailing string before changing best_quantity
            data.parenthesis_notes.append(f"maybe quantity is: {' '.join(data.quantity)}")


            # make the secondary_quantity the starting quantity before converting the quantity to the value found in the parenthesis
            data.secondary_quantity = data.quantity

            # set the quantity/unit to the parenthesis values
            data.quantity = parenthesis_quantity
            data.unit = parenthesis_unit

            return data

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are probably "better" so use the
            # parenthesis quantity/units and then stash the old unit in the description
        if not data.quantity and data.unit:

            # stash the old quantity with a trailing "maybe"
            data.parenthesis_notes.append(f"maybe unit is: {data.unit}")

            # make the secondary_unit the starting unit before converting the unit to the unit string found in the parenthesis
            data.secondary_unit = data.unit

            data.quantity = parenthesis_quantity
            data.unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return data
        
        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely found an equivalent quantity/unit
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if data.quantity and data.unit:
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = data.unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units:  (# TODO: Maybe we should use parenthesis quantity/unit instead...?)
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
                # return [data.quantity, data.unit, description]

                # set the secondary quantity/units to the values in the parenthesis
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")
                # return [data.quantity, data.unit, description]
                
                # set the secondary quantity/units to the values in the parenthesis
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data

            # Case when: YES basic parenthesis unit, NO basic original unit: 
            #   then use the parenthesis quantity/unit (stash the original in the description)
            if parenthesis_unit_is_basic:
                data.parenthesis_notes.append(f"maybe quantity/unit is: {data.quantity}/{data.unit}")
                
                # set the secondary quantity/units to the original quantity/units
                data.secondary_quantity = data.quantity
                data.secondary_unit = data.unit

                # update the primary quantities/units to the parenthesis values
                data.quantity = parenthesis_quantity
                data.unit = parenthesis_unit
                
                # return [parenthesis_quantity, parenthesis_unit, description]
                return data

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then use the original quantity/unit (stash the parenthesis in the description)
            if unit_is_basic:
                data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")

                # set the secondary quantity/units to the original quantity/units
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data


        data.parenthesis_notes.append(f"used quantity/units from parenthesis with equivalent quantity/units")

        # set the secondary quantity/units to the original quantity/units
        data.secondary_quantity = data.quantity
        data.secondary_unit = data.unit

        data.quantity = parenthesis_quantity
        data.unit = parenthesis_unit

        return data