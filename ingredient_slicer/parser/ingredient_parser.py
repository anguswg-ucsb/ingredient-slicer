import re
from typing import List, Dict, Any, Union, Tuple
from fractions import Fraction
from html import unescape
import warnings

# package imports
from ingredient_slicer import _utils
from ingredient_slicer import _regex_patterns
from ingredient_slicer import _constants

from ingredient_slicer.standardizer._ingredient_standardizer import IngredientStandardizer 

from ingredient_slicer.parenthesis.parenthesis_handler import ParenthesisHandler
from ingredient_slicer.parenthesis.quantity_only_parenthesis_strategy import QuantityOnlyParenthesisHandler 
from ingredient_slicer.parenthesis.equivalence_parenthesis_strategy import EquivalenceParenthesisHandler 
from ingredient_slicer.parenthesis.quantity_unit_only_parenthesis_strategy import QuantityUnitOnlyParenthesisHandler

from ingredient_slicer.models.quantity_unit_data import QuantityUnitData
from ingredient_slicer.models.parsed_ingredient_data import ParsedIngredientData

class IngredientParser:
    """
    A class to parse recipe ingredients into a standard format.

    Args:
        ingredient (str): The ingredient to parse.
        debug (bool): Whether to print debug statements (default is False)
    """

    def __init__(self, ingredient: str, debug = False):
        self.ingredient          = ingredient
        self.debug               = debug
        
        # Ordered strategies to apply to parenthesis content (order matters)
        self.parenthesis_handlers: list[ParenthesisHandler] = [
            QuantityOnlyParenthesisHandler(),
            EquivalenceParenthesisHandler(),
            QuantityUnitOnlyParenthesisHandler()
        ]

        self.ingredient_standardizer = None 
        self.ingredient_standardizer = self._get_ingredient_standardizer(self.ingredient)

        self.parsed_data = self._parse()
    
    def to_json(self) -> Dict[str, Any]:
        return self.parsed_data.to_json()
    
    def get_parsed_data(self) -> ParsedIngredientData: 
        return self.parsed_data

    def _get_ingredient_standardizer(self, ingredient : str) -> IngredientStandardizer:
        if self.ingredient_standardizer:
            return self.ingredient_standardizer 

        # Create an IngredientStandardizer
        ingredient_standardizer = IngredientStandardizer(ingredient)    
        return ingredient_standardizer

    def _is_ingredient_required(self, standardizer : IngredientStandardizer) -> bool:
        """
        Check if the ingredient is required or optional
        Returns a boolean indicating whether the ingredient is required or optional.
        """

        # check if the ingredient string contains the word "optional" or "required"
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
    
    def _apply_parenthesis_content_to_quantity_unit_data(
        self, 
        parenthesis_content: list[str], 
        data: QuantityUnitData
    ) -> QuantityUnitData:
        """
        Address any parenthesis that were in the ingredient.
        """
        for parenthesis in parenthesis_content:
            for handler in self.parenthesis_handlers:
                data = handler.handle(parenthesis, data)
        return data
   
    def _get_standard_unit(self, unit : str) -> str:
        """
        Add standard units to the parsed ingredient if they are present in the
        constants units to standard units map.
        If the "unit"/"secondary_unit" exists and it is present in the unit to standard unit map, 
        then get the standard unit name for the unit and set the "standardized_unit" and "standardized_secondary_unit" member variables.
        """

        if unit and unit in _constants.UNIT_TO_STANDARD_UNIT:
            return _constants.UNIT_TO_STANDARD_UNIT.get(unit)
        
        return 

    def _prioritize_weight_units(self, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
        """
        Prioritize weight units over volume units if both are present in the parsed ingredient.
        If the first unit is not a weight unit but the secondary_unit is a weight unit, then swap them so 
        the weight unit is always given as the primary unit.
        (i.e. unit = "cups", secondary_unit = "ounces" --> Swap them so that unit = "ounces" and secondary_unit = "cups")
        """

        # # if the first unit is already a weight, just return early
        if quantity_unit_data.unit in _constants.WEIGHT_UNITS_SET:
            return quantity_unit_data

        # TODO: first part of this if statement is probably redundent...
        # if the first unit is NOT a weight and the second unit IS a weight, then swap them
        if quantity_unit_data.unit not in _constants.WEIGHT_UNITS_SET and quantity_unit_data.secondary_unit in _constants.WEIGHT_UNITS_SET:

            # print(f"Swapping first quantity/units with second quantity/units") if self.debug else None

            # switch the units and quantities with the secondary units and quantities
            quantity_unit_data.swap_quantity_unit_ordering()

        return quantity_unit_data
    
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

    def _get_food_density(self, food : str, quantity_unit_data : QuantityUnitData):
        """Add food densities to the units variables if they are the only possible units after the ingredient has been parsed."""
        # ingredient = "2 1/2 cups of sugar (about 1/2 inch squares of sugar)"
        densities = {} 

        if _utils._has_volume_unit(quantity_unit_data.unit, quantity_unit_data.standardized_unit, quantity_unit_data.secondary_unit, quantity_unit_data.standardized_secondary_unit):
            densities       = _utils._get_food_density(food, "dice")

        return densities

    def _add_gram_weights(self):
        """Add gram weights to the units variables if they are the only possible units after the ingredient has been parsed."""
        
        grams_map = _utils._get_gram_weight(self._food, self._quantity, self._unit, self._densities, "dice")

        if grams_map:
            self._gram_weight     = grams_map.get("gram_weight", None)
            self._min_gram_weight = grams_map.get("min_gram_weight", None)
            self._max_gram_weight = grams_map.get("max_gram_weight", None)

        return
    
    def _get_gram_weights(self, food : str, quantity_unit_data : QuantityUnitData, densities : dict) -> dict:
        """Add gram weights to the units variables if they are the only possible units after the ingredient has been parsed."""
        
        gram_weights_map = _utils._get_gram_weight(food, quantity_unit_data.quantity, quantity_unit_data.unit, densities, "dice")

        return gram_weights_map
    
    def _get_gram_weights_for_single_item_foods(self, 
                                                food : str, 
                                                gram_weight : Union[str, int, float, None], 
                                                quantity : Union[str, None]
                                                ):

        if not gram_weight:
            # print(f'THIS IS A SINGLE ITEM FOOD: {self._food}') if self.debug else None
            # NOTE: this is an arbitrary fuzzy string matching ratio of 0.85 for now, probably want this to be pretty strict 
            # NOTE: so we don't get false positives (maybe even just make it 0.95 or 1 to just only match single character differences)
            gram_weight = _utils._get_single_item_gram_weight(food, quantity)

        return gram_weight

    def _add_food_units(self, 
                        ingredient : str, 
                        quantity_unit_data : QuantityUnitData
                        ) -> QuantityUnitData:
        """If no units were found, check for possible 'food units', and update the QuantityUnitData if any food units are found/needed"""

        if not quantity_unit_data.unit and not quantity_unit_data.standardized_unit:
            food_unit     = _utils._get_food_unit(ingredient)
            std_food_unit = _constants.FOOD_UNIT_TO_STANDARD_FOOD_UNIT.get(food_unit)

            quantity_unit_data.unit = food_unit
            quantity_unit_data.standardized_unit = std_food_unit
        
        return quantity_unit_data
    
    # def _set_default_quantities(self, quantity_unit_data : QuantityUnitData) -> QuantityUnitData:
    #     """Set a default quantity if no quantity was found"""
        
    #     is_weight_or_volume_unit = _utils._is_weight_unit(quantity_unit_data.standardized_unit) or _utils._is_volumetric_unit(quantity_unit_data.standardized_unit)
    #     missing_primary_quantity = quantity_unit_data.quantity is None
        
    #     if is_weight_or_volume_unit and missing_primary_quantity:
    #         quantity_unit_data.quantity = "1"

    #     return quantity_unit_data

    def _get_animal_protein_gram_weight(self,   
                                         gram_weight : Union[str, int, float, None], 
                                         quantity_unit_data : QuantityUnitData
                                         ) -> Union[str, int, float, None]:
        """If the food is an animal protein, then get the gram weight for that protein"""
        if not gram_weight:
            gram_weight = _utils._get_animal_protein_gram_weight(quantity_unit_data.quantity, quantity_unit_data.unit)
            if not gram_weight:
                gram_weight = _utils._get_animal_protein_gram_weight(quantity_unit_data.secondary_quantity, quantity_unit_data.secondary_unit)
            
        return gram_weight
    
    def _parse(self) -> ParsedIngredientData:
        # TODO: process parenthesis content

        print(f"Standardizing ingredient: \n > '{self.ingredient}'") if self.debug else None
        # ingredient = "1 cup of chicken (2 ounces)"
        # std_ingredient = "1 cup of chicken"

        parsed_data = ParsedIngredientData(ingredient=self.ingredient, 
                                           standardized_ingredient=self.ingredient_standardizer.get_standardized_ingredient(),
                                           dimensions=self.ingredient_standardizer.get_dimensions(),
                                           parenthesis_content=self.ingredient_standardizer.get_parenthesis_content()
                                           )
        # parsed_data = ParsedIngredientData(ingredient=ingredient, standardized_ingredient=std_ingredient)
        # parsed_data
        # ParsedIngredientData(ingredient=ingredient)
        # IngredientStandardizer(ingredient=ingredient).get_standardized_ingredient_data()

        # ----------------------------------- STEP 1 ------------------------------------------
        # ---- Get the input ingredient string into a standardized form ----
        # -------------------------------------------------------------------------------------

        # # run the standardization method to cleanup raw ingredient and create the "standard_ingredient" and "_reduced_ingredient" member variables 
        # self._standardize()

        print(f"Standardized ingredient: \n > '{parsed_data.standardized_ingredient}'") if self.debug else None
        # ----------------------------------- STEP 2 ------------------------------------------
        # ---- Check if there is any indication of the ingredient being required/optional ----
        # -------------------------------------------------------------------------------------

        # run the is_required method to check if the ingredient is required or optional and set the "is_required" member variable to the result
        parsed_data.is_required = self._is_ingredient_required(self.ingredient_standardizer) 
        # self._is_required = self._is_ingredient_required(self.ingredient_standardizer)

        print(f"Is the ingredient required? {parsed_data.is_required}") if self.debug else None
        # ----------------------------------- STEP 3 ------------------------------------------
        # ---- Extract first options of quantities and units from the "_reduced_ingredient" ----
        # -------------------------------------------------------------------------------------
        print(f"Attempting to extract quantity and unit") if self.debug else None
        # run the extract_first_quantity_unit method to extract the first unit and quantity from the ingredient string
        quantity_unit_data = self.extract_first_quantity_unit(self.ingredient_standardizer.get_standardized_ingredient())

        # ----------------------------------- STEP 4 ------------------------------------------
        # ---- Address any parenthesis that were in the ingredient  ----
        # -------------------------------------------------------------------------------------
        # NOTE: Stash the best_quantity and best_units before preceeding (for debugging)

        print(f"""Addressing parenthesis: 
                > Standard ingredient: '{parsed_data.standardized_ingredient}'
                > Parenthesis content: '{parsed_data.parenthesis_content}'
            """) if self.debug else None

        # self._address_parenthesis(self.ingredient_standardizer.get_parenthesis_content())
        quantity_unit_data = self._apply_parenthesis_content_to_quantity_unit_data(
                                            # parenthesis_content=self.ingredient_standardizer.get_parenthesis_content(), 
                                            parenthesis_content=parsed_data.parenthesis_content, 
                                            data=quantity_unit_data
                                            )

        # ----------------------------------- STEP 5 ------------------------------------------
        # ---- Get the standard names of the units and secondary units ----
        # -------------------------------------------------------------------------------------
        print(f"Adding standard unit names for {quantity_unit_data.unit} and {quantity_unit_data.secondary_unit}") if self.debug else None

        quantity_unit_data.standardize_unit()
        quantity_unit_data.standardize_secondary_unit()
        # quantity_unit_data.standardized_unit           = self._get_standard_unit(quantity_unit_data.unit)
        # quantity_unit_data.standardized_secondary_unit = self._get_standard_unit(quantity_unit_data.secondary_unit)

        # ----------------------------------- STEP 6 ------------------------------------------
        # ---- Prioritize weight units and always place the weight unit as the primary ingredient if it exists ----
        # -------------------------------------------------------------------------------------
        print(f"Prioritizing weight units") if self.debug else None
        quantity_unit_data = self._prioritize_weight_units(quantity_unit_data=quantity_unit_data)

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
        parsed_data.food = self._extract_foods(self.ingredient_standardizer.get_standardized_ingredient())
        # self._food = self._extract_foods(self.ingredient_standardizer.get_standardized_ingredient())

        # ----------------------------------- STEP 8 ------------------------------------------
        # ---- Extract extra, descriptors (prep words, size modifiers, dimension units) ----
        # -------------------------------------------------------------------------------------
        print(f"Extracting prep words, size modifiers") if self.debug else None
        parsed_data.prep           = self._extract_prep_words(self.ingredient_standardizer.get_staged_ingredient()) 
        parsed_data.size_modifiers = self._extract_size_modifiers(self.ingredient_standardizer.get_staged_ingredient()) 

        # self._prep           = self._extract_prep_words(self.ingredient_standardizer.get_staged_ingredient()) 
        # self._size_modifiers = self._extract_size_modifiers(self.ingredient_standardizer.get_staged_ingredient()) 
        
        # ----------------------------------- STEP 9 ------------------------------------------
        # ---- Calculate food density if possible ----
        # -------------------------------------------------------------------------------------
        print(f"Calculating food density") if self.debug else None
        # self._add_food_density() 
        # self._densities = self._get_food_density(self._food, quantity_unit_data)
        parsed_data.densities = self._get_food_density(parsed_data.food, quantity_unit_data) 

        # ----------------------------------- STEP 10 ------------------------------------------
        # ---- Calculate gram weights if possible ----
        # -------------------------------------------------------------------------------------
        
        print(f"Calculating gram weights") if self.debug else None
        # self._add_gram_weights() 
        gram_weights_map = self._get_gram_weights(food=parsed_data.food, 
                                                  quantity_unit_data=quantity_unit_data, 
                                                  densities=parsed_data.densities)

        # parsed_data.__dict__.update({
        #     k: v for k, v in gram_weights_map.items()
        #     if k in {'gram_weight', 'max_gram_weight', 'min_gram_weight'}
        # })
        parsed_data.gram_weight     = gram_weights_map.get("gram_weight") 
        parsed_data.max_gram_weight = gram_weights_map.get("max_gram_weight") 
        parsed_data.min_gram_weight = gram_weights_map.get("min_gram_weight") 

        # ----------------------------------- STEP 11 ------------------------------------------
        # ---- Calculate gram weights if possible ----
        # -------------------------------------------------------------------------------------
        print(f"Estimating gram weights for unitless foods") if self.debug else None
        # self._gram_weight = self._get_gram_weights_for_single_item_foods(food=self._food, 
        #                                                            gram_weight=self._gram_weight, 
        #                                                            quantity=quantity_unit_data.quantity)
        parsed_data.gram_weight = self._get_gram_weights_for_single_item_foods(food=parsed_data.food, 
                                                                   gram_weight=parsed_data.gram_weight, 
                                                                   quantity=quantity_unit_data.quantity
                                                                   ) 

        # ----------------------------------- STEP 12 ------------------------------------------
        # ---- If no units were found ---- 
        # ---- check for food units and set those as the unit / standardized_unit ----
        # -------------------------------------------------------------------------------------
        print(f"Checking for possible 'food units' (i.e. '2 corn tortillas' has a unit of 'tortillas')") if self.debug else None
        quantity_unit_data.set_food_units(ingredient=self.ingredient_standardizer.get_standardized_ingredient())
        # quantity_unit_data = self._add_food_units(
        #                     ingredient=self.ingredient_standardizer.get_standardized_ingredient(), 
        #                     quantity_unit_data=quantity_unit_data
        #                     )
       
        # ----------------------------------- STEP 13 ------------------------------------------
        # ---- If not quantity is found, set quantity to a default of 1 ---- 
        # -------------------------------------------------------------------------------------
        print(f"Set quantity to 1 if not found") if self.debug else None
        # self._set_default_quantities()
        quantity_unit_data.set_default_quantity("1")
        # quantity_unit_data = self._set_default_quantities2(quantity_unit_data)
       
        # ----------------------------------- STEP 14 ------------------------------------------
        # ---- If no gram weight has been found ---- 
        # ---- check for any common 'animal protein units' (i.e. 'breasts', 'drumsticks', etc)
        # ---- and calculate a gram weight for any found units ----
        # -------------------------------------------------------------------------------------
        print(f"Checking for possible 'animal protein units' (i.e. '2 chicken breasts' has a unit of 'breast') and calculating a gram weight for any found units") if self.debug else None
        parsed_data.gram_weight = self._get_animal_protein_gram_weight(gram_weight=parsed_data.gram_weight, quantity_unit_data=quantity_unit_data) 

        # ----------------------------------- STEP 15 ------------------------------------------
        # ------ Merge values from QuantityUnitData class into ParsedIngredientData class ------
        # --------------------------------------------------------------------------------------
        parsed_data.merge_quantity_unit_data(data=quantity_unit_data)

        return parsed_data
