from ingredient_slicer import _constants 
from ingredient_slicer import _utils
from ingredient_slicer.parenthesis.parenthesis_handler import ParenthesisHandler
from ingredient_slicer.models.quantity_unit_data import QuantityUnitData

class QuantityUnitOnlyParenthesisHandler(ParenthesisHandler):
    def handle(self, parenthesis: str, data: QuantityUnitData) -> QuantityUnitData:
    
        """
        Address the case where the parenthesis content contains exactly a quantity and unit (NOT prefixed by any equivalence strings like "about" or "approximately").
        Attempts to update self._quantity, self._unit, self._secondary_quantity, and data.secondary_unit given 
        information from the parenthesis string and the current self._quantity and data.unit
        e.g. "(3 ounces)", "(3 ounces each)", "(a 4 cup scoop)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self._standardized_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self._quantity}'\nUnit: '{data.unit}'""") if self.debug else None

        # pull out quantity unit only pattern
        quantity_unit_only = _utils._extract_quantity_unit_pairs(parenthesis)

        # if no numbers only parenthesis, then just return the original ingredient
        if not quantity_unit_only:
            data.parenthesis_notes.append("not a quantity unit only parenthesis")

            return data 
        
        # pull out the parenthesis quantity and unit
        parenthesis_quantity, parenthesis_unit = quantity_unit_only[0]

        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis self._quantity-unit as our data.quantity and unit
        if not data.quantity and not data.unit:
            # updated_quantity, updated_unit = quantity_unit_only[0]
            # print(f"\n > Case when: NO quantity, NO unit") if self.debug else None

            data.parenthesis_notes.append(f"used quantity/unit from parenthesis with no quantity/unit")

            # set the secondary quantity/units to the original quantity/units
            data.secondary_quantity = data.quantity
            data.secondary_unit = data.unit

            data.quantity = parenthesis_quantity
            data.unit = parenthesis_unit

            return data

        # Case when: YES quantity, NO unit:
            # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
            # then use the unit in the parenthesis
        if data.quantity and not data.unit:
            # print(f"\n > Case when: YES quantity, NO unit") if self.debug else None

            # quantity_unit_only[0][0]
            updated_quantity = str(float(data.quantity) * float(parenthesis_quantity))

            data.parenthesis_notes.append(f"multiplied starting quantity with parenthesis quantity")

            # set the secondary quantity/units to the original quantity/units
            data.secondary_quantity = data.quantity
            data.secondary_unit = data.unit

            data.quantity = _utils._make_int_or_float_str(updated_quantity)
            data.unit = parenthesis_unit

            return data

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are either:
            # 1. A description/note (i.e. cut 0.5 inch slices)
            # 2. A quantity and unit (i.e. 2 ounces)
            # either case, just return the parenthesis units to use those
        if not data.quantity and data.unit:
            # print(f"\n > Case when: NO quantity, YES unit") if self.debug else None

            data.parenthesis_notes.append(f"No quantity but has units, used parenthesis. maybe quantity/unit is: {data.quantity}/{data.unit}")

            # set the secondary quantity/units to the original quantity/units
            data.secondary_quantity = data.quantity
            data.secondary_unit = data.unit

            data.quantity = parenthesis_quantity
            data.unit = parenthesis_unit

            return data

        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely just found a description 
            # OR we may have found an equivalence quantity unit.
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if data.quantity and data.unit:
            # print(f"\n > Case when: YES quantity, YES unit") if self.debug else None

            # flags for if original unit/parenthesis unit are in the set of basic units (BASIC_UNITS_SET) or not
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = data.unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units: 
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, BASIC unit") if self.debug else None

                data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")

    
                # set the secondary quantity/units to the parenthesis quantity/units
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data

            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values 
            #   (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, NOT BASIC unit") if self.debug else None
                data.parenthesis_notes.append(f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}")


                # set the secondary quantity/units to the parenthesis quantity/units
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data

            # Case when: YES basic parenthesis unit, NO basic original unit (EXPLICIT):
            #  Try to merge (multiply) the current quantity and the parenthesis quantity
            #  AND set the secondary quantity/units to the ORIGINAL values
            if parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (EXPLICIT)") if self.debug else None
                updated_quantity = str(float(data.quantity) * float(parenthesis_quantity))

                data.parenthesis_notes.append(f"multiplied starting quantity{data.quantity}/{parenthesis_quantity}")

                # set the secondary quantity/units to the original quantity/units
                data.secondary_quantity = data.quantity
                data.secondary_unit = data.unit

                # data.quantity = updated_quantity
                data.quantity = _utils._make_int_or_float_str(updated_quantity)
                data.unit = parenthesis_unit

                return data

            # TODO: I think this condition can be dropped, gets covered by previous condition...
            # Case when: YES basic parenthesis unit, NO basic original unit (IMPLICITLY): 
            #   then use the parenthesis quantity/unit AND set the secondary quantity/units to the ORIGINAL values
            #   (stash the original in the description)
            if parenthesis_unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (IMPLICIT)") if self.debug else None
                data.parenthesis_notes.append(f"maybe quantity/unit is: {data.quantity}/{data.unit}")

                # set the secondary quantity/units to the original quantity/units
                data.secondary_quantity = data.quantity
                data.secondary_unit = data.unit

                data.quantity = parenthesis_quantity
                data.unit = parenthesis_unit

                return data

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then just keep the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values
            #   (stash the original in the description)
            if unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, BASIC unit (IMPLICIT)") if self.debug else None
                data.parenthesis_notes.append(f"maybe quantity/unit is: {data.quantity}/{data.unit}")

                # set the secondary quantity/units to the parenthesis quantity/units
                data.secondary_quantity = parenthesis_quantity
                data.secondary_unit = parenthesis_unit

                return data

        # TODO: Don't think this should ever happen, need to rethink this part
        # Case when: All other conditions were NOT met:
            # just set the quantity/unit to the parenthesis values 
            # and then put the original quantity/units in the secondary quantity/units
        data.parenthesis_notes.append(f"used quantity/units from parenthesis with quantity/units only")

        # set the secondary quantity/units to the ORIGINAL quantity/units
        data.secondary_quantity = data.quantity 
        data.secondary_unit = data.unit

        # set the primary quantity/units to the parenthesis quantity/units
        data.quantity = parenthesis_quantity
        data.unit = parenthesis_unit

        return data