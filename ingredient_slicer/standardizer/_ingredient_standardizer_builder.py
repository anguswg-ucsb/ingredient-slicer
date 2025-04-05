    
# Authors: Angus Watters, Melissa Terry 

import re
from typing import List, Dict, Any, Union, Tuple
from fractions import Fraction
from html import unescape
import warnings

# package imports
from .. import _utils
from .. import _regex_patterns
from .. import _constants

class IngredientStandardizerBuilder:
    def __init__(self, ingredient: str):
        self._ingredient = ingredient
        self._standardized_ingredient = ingredient

        self._additional_keys = {
            "_dimensions": [],
            "_parenthesis_content": None,
            "_parenthesis_notes": [],
            "_staged_ingredient": None
        }

    def _drop_special_dashes(self):
        self._standardized_ingredient = self._standardized_ingredient.replace("—", "-").replace("–", "-").replace("~", "-")
        return self

    def _find_and_remove_percentages(self):
        """
        Find and remove percentages from the ingredient string.
        """
        
        for key, pattern in _regex_patterns.PCT_REGEX_MAP.items():
            pattern_iter = pattern.finditer(self._standardized_ingredient)
            offset = 0
            for match in pattern_iter:
                match_string = match.group()
                start, end = match.start(), match.end()
                modified_start = start + offset
                modified_end = end + offset

                replacement_str = ""

                # Construct the modified string with the replacement applied
                self._standardized_ingredient = self._standardized_ingredient[:modified_start] + str(replacement_str) + self._standardized_ingredient[modified_end:]
                offset += len(str(replacement_str)) - (end - start)
                
        return self

    def _replace_number_followed_by_inch_symbol(self):

        self._standardized_ingredient = _utils._replace_number_followed_by_inch_symbol(self._standardized_ingredient)

        return self
    

    def _find_and_replace_casual_quantities(self):

        self._standardized_ingredient = _utils._find_and_replace_casual_quantities(self._standardized_ingredient)

        return self    
    
    def _find_and_replace_prefixed_number_words(self):
        """ Replace prefixed number words with their corresponding numerical values in the parsed ingredient 
        Strings like "twenty five" are replaced with "25", or "thirty-two" is replaced with "32"
        """

        self._standardized_ingredient = _utils._find_and_replace_prefixed_number_words(self._standardized_ingredient)
        
        return self
    
    def _find_and_replace_number_words(self):
        """
        Replace number words with their corresponding numerical values in the parsed ingredient.
        """
        self._standardized_ingredient = _utils._find_and_replace_number_words(self._standardized_ingredient)
        
        return self
    
    def _find_and_replace_fraction_words(self):
        """ Find and replace fraction words with their corresponding numerical values in the parsed ingredient."""

        for key, pattern in _regex_patterns.NUMBER_WITH_FRACTION_WORD_MAP.items():
            
            pattern_iter = pattern.finditer(self._standardized_ingredient)
            offset = 0

            for match in pattern_iter:
                match_string = match.group(0)
                start, end = match.start(), match.end()
                modified_start = start + offset
                modified_end = end + offset

                match_string = match_string.replace("-", " ")
                split_match = match_string.split(" ")

                split_match = [i.strip() for i in split_match]

                number_word = split_match[0]
                fraction_word = split_match[1]

                fraction_value, decimal = _constants.FRACTION_WORDS[fraction_word.lower()]

                updated_value = str(float(number_word) * float(decimal))
                self._standardized_ingredient = self._standardized_ingredient[:modified_start] + str(updated_value) + self._standardized_ingredient[modified_end:]

                offset += len(str(updated_value)) - (end - start)

        return self 
    
    def _clean_html_and_unicode(self):
        """Unescape fractions from HTML code coded fractions to unicode fractions."""
        self._standardized_ingredient = _utils._clean_html_and_unicode(self._standardized_ingredient)

        return self
    
    def _replace_unicode_fraction_slashes(self):
        """Replace unicode fraction slashes with standard slashes in the parsed ingredient."""

        # Replace unicode fraction slashes with standard slashes
        self._standardized_ingredient = self._standardized_ingredient.replace('\u2044', '/') # could use .replace('\u2044', '\u002F'), or just .replace("⁄", "/")
        
        return self

    
    def _replace_emojis(self):
        """Remove emojis from the ingredient string."""
        
        self._standardized_ingredient = _utils._remove_emojis(self._standardized_ingredient)

        return self

    def _convert_fractions_to_decimals(self):
        """
        Convert fractions in the parsed ingredient to their decimal equivalents.
        """
        self._standardized_ingredient = _utils._convert_fractions_to_decimals(self._standardized_ingredient)
        
        return self

    def _force_ws_between_numbers_and_chars(self):
        
        """Forces spaces between numbers and units and between units and numbers.
        End result is a string with a space between numbers and units and between units and numbers.
        Examples:
        "1cup" becomes "1 cup"
        "cup1" becomes "cup 1" 
        and ultimately "1cup" becomes "1 - cup" and "cup1" becomes "cup - 1"
        """

        self._standardized_ingredient = _utils._force_ws_between_numbers_and_chars(self._standardized_ingredient)

        return self

    def _remove_repeat_units_in_ranges(self):
        
        self._standardized_ingredient = _utils._remove_repeat_units_in_ranges(self._standardized_ingredient)
        
        return self
    
    def _separate_dimensions(self):
        """
        Split the dimensions from the parsed ingredient.
        """
        # Split the dimensions from the ingredient
        self._standardized_ingredient, self._additional_keys["_dimensions"] = _utils._separate_dimensions(self._standardized_ingredient)

        return self
    

    def _remove_x_separators(self):
        """
        Remove "x" separators from the ingredient string and replace with whitespace
        Examples:
            >>> _removed_x_separators("1x2 cups")
            '1 2 cups'
            >>> _remove_x_separators("5 x cartons of eggs")
            "5   cartons of eggs"
        """

        def replace_x(match):
            return match.group().replace('x', ' ').replace('X', ' ')

        # Replace "x"/"X" separators with whitespace
        self._standardized_ingredient = _regex_patterns.X_AFTER_NUMBER.sub(replace_x, self._standardized_ingredient)
        
        return self
    
    def _clean_hyphen_padded_substrings(self):
        """Find and remove hyphens around "to", "or", and "and" substrings in the parsed ingredient.
        For example, "1-to-3 cups of soup" becomes "1 to 3 cups of soup" and "1-or-2 cups of soup" becomes "1 or 2 cups of soup"
        """

        substrings_to_fix = ["to", "or", "and", "&"]
        
        for substring in substrings_to_fix:
            self._standardized_ingredient = _utils._find_and_remove_hyphens_around_substring(self._standardized_ingredient, substring)

        return self

    def _merge_multi_nums(self):
        """
        Replace unicode and standard fractions with their decimal equivalents in the parsed ingredient (v2).
        Assumes that numeric values in string have been padded with a space between numbers and non numeric characters and
        that any fractions have been converted to their decimal equivalents.
        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            str: The parsed ingredient string with the numbers separated by a space merged into a single number (either added or multiplied).
        
        >>> _merge_multi_nums('2 0.5 cups of sugar')
        '2.5 cups of sugar'
        >>> _merge_multi_nums('1 0.5 pounds skinless, boneless chicken breasts, cut into 0.5 inch pieces')
        '1.5 pounds skinless, boneless chicken breasts, cut into 0.5 inch pieces'
        """

        # go the spaced numbers matches and get each spaced seperated numbers match AND 
        # try and get the units that follow them so we can correctly match each spaced number with its corresponding unit
        spaced_nums = []
        units = []

        # Create iterable of the matched spaced numbers to insert updated values into the original string
        spaced_matches = re.finditer(_regex_patterns.SPACE_SEP_NUMBERS, self._standardized_ingredient)
        # spaced_matches = re.finditer(regex_map.SPACE_SEP_NUMBERS, ingredient)

        # initialize offset and replacement index values for updating the ingredient string, 
        # these will be used to keep track of the position of the match in the string
        offset = 0
        replacement_index = 0

        # Update the ingredient string with the merged values
        for match in spaced_matches:
            # print(f"Ingredient string: {ingredient}")

            # Get the start and end positions of the match
            start, end = match.start(), match.end()

            # search for the first unit that comes after the spaced numbers
            unit_after_match = re.search(_regex_patterns.UNITS_PATTERN,  self._standardized_ingredient[end:])
            
            if unit_after_match:
                units.append(unit_after_match.group())

            # add the spaced number to the list
            spaced_nums.append(match.group())

            merged_quantity = self._merge_spaced_numbers(match.group())
            merge_operation = self._which_merge_on_spaced_numbers(match.group())

            modified_start = start + offset
            modified_end = end + offset

            self._standardized_ingredient = self._standardized_ingredient[:modified_start] + str(merged_quantity) + self._standardized_ingredient[modified_end:]

            # Update the offset for subsequent replacements
            offset += len(merged_quantity) - (end - start)
            replacement_index += 1

        return self
    
    def _merge_spaced_numbers(self, spaced_numbers: str) -> str:
        """ Add or multiply the numbers in a string separated by a space.
        If the second number is less than 1, then add the two numbers together, otherwise multiply them together.
        This was the most generic form of dealing with numbers seperated by spaces that i could come up with
        (i.e. 2 1/2 cups means 2.5 cups but in other contexts a number followed by a non fraction means to multiply the numbers 2 8 oz means 16 oz)
        Args:
            spaced_numbers (str): A string of numbers separated by a space.
        Returns:
            str: string containing the sum OR the product of the numbers in the string. 
        Examples:
            >>> _merge_spaced_numbers('2 0.5')
            '2.5'
            >>> _merge_spaced_numbers('2 8')
            '16'
        """

        # Get the numbers from the spaced seperated string
        split_numbers = re.findall(_regex_patterns.SPLIT_SPACED_NUMS, spaced_numbers)

        # If the second number is less than 1, then add the two numbers together, otherwise multiply them together
        # This was the most generic form of dealing with numbers seperated by spaces 
        # (i.e. 2 1/2 cups means 2.5 cups but in other contexts a number followed by a non fraction means to multiply the numbers 2 8 oz means 16 oz)
        try:
            merged_totals = [_utils._make_int_or_float_str(str(float(first) + float(second)) if float(second) < 1 else str(float(first) * float(second))) for first, second in split_numbers]
        except:
            warnings.warn(f"error while merging {split_numbers}...")
            merged_totals = [""]
        # # READABLE VERSION of above list comprehension: 
        # This is the above list comprehensions split out into 2 list comprehensions for readability
        # merged_totals = [float(first) + float(second) if float(second) < 1 else float(first) * float(second) for first, second in split_numbers]

        # return merged_totals
        return merged_totals[0] if merged_totals else ""

    def _which_merge_on_spaced_numbers(self, spaced_numbers: str) -> str:
        """ Inform whether to add or multiply the numbers in a string separated by a space.
        Args:
            spaced_numbers (str): A string of numbers separated by a space.
        Returns:
            str: string indicating whether to add or multiply the numbers in the string.
        """

        split_numbers = re.findall(_regex_patterns.SPLIT_SPACED_NUMS, spaced_numbers)
        # split_numbers = [("2", "1")]

        # If the second number is less than 1, then note the numbers should be "added", otherwise they should be "multiplied"
        # This was the most generic form of dealing with numbers seperated by spaces 
        # (i.e. 2 1/2 cups means 2.5 cups but in other contexts a number followed by a non fraction means
        #  to multiply the numbers 2 8 oz means 16 oz)
        try:
            add_or_multiply = ["add" if float(second) < 1 else "multiply" for first, second in split_numbers]
        except:
            warnings.warn(f"error while deciding whether to note '{split_numbers}' as numbers to 'add' or 'multiply'...")
            add_or_multiply = [""]

        return add_or_multiply[0] if add_or_multiply else ""
    
    
    def _fix_ranges(self):
        """
        Fix ranges in the parsed ingredient.
        Given a parsed ingredient, this method will fix ranges of numbers that are separated by one or more hyphens, ranges of numbers that are preceded by "between" and followed by "and" or "&", and ranges that are separated by "to" or "or".
        Examples:
        - "1-2 oz" -> "1 - 2 oz"
        - "between 1 and 5" -> "1 - 5"
        - "1 to 5" -> "1 - 5"
        """

        # Update ranges of numbers that are separated by one or more hyphens
        self._standardized_ingredient = _utils._update_ranges(self._standardized_ingredient, _regex_patterns.QUANTITY_DASH_QUANTITY)

        # Update ranges of numbers that are preceded by "between" and followed by "and" or "&"
        self._standardized_ingredient = _utils._update_ranges(self._standardized_ingredient, _regex_patterns.BETWEEN_QUANTITY_AND_QUANTITY)

        # Update ranges that are separated by "to" 
        self._standardized_ingredient = _utils._update_ranges(self._standardized_ingredient, _regex_patterns.QUANTITY_TO_QUANTITY)
  
        # Update ranges that are separated by "or"
        self._standardized_ingredient = _utils._update_ranges(self._standardized_ingredient, _regex_patterns.QUANTITY_OR_QUANTITY)
 
        # check and merge any misleading ranges
        self._standardized_ingredient = _utils._merge_misleading_ranges(self._standardized_ingredient)

        return self

    def _find_and_replace_numbers_separated_by_add_numbers(self):
        """Find numbers separated by "and", "&", "plus", or "+" and replace the matched strings with their sum of the 2 number values
        Examples:
        "1 and 0.5" -> "1.5"
        "1 & 0.5" -> "1.5"
        "2 plus 0.66" -> "2.66"
        "2 + 0.66" -> "2.66"
        """
        add_pattern_iter = _regex_patterns.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.finditer(self._standardized_ingredient)

        offset = 0

        for match in add_pattern_iter:
            match_string = match.group(0)
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            first_number = float(match.group(1).strip())
            second_number = float(match.group(2).strip())

            updated_value = f" {_utils._make_int_or_float_str(str(first_number + second_number))} "

            self._standardized_ingredient = self._standardized_ingredient[:modified_start] + str(updated_value) + self._standardized_ingredient[modified_end:]

            offset += len(updated_value) - (end - start)
    
        return self
    
    def _replace_a_or_an_quantities(self):
        """
        Replace "a" or "an" with "1" in the parsed ingredient if no number is present in the ingredient string.
        """
        self._standardized_ingredient = _utils._replace_a_or_an_quantities(self._standardized_ingredient)
        return self

    def _average_ranges(self):
        """ Average all hyphen separated ranges of numbers in the parsed ingredient. """
        self._standardized_ingredient = _utils.avg_ranges(self._standardized_ingredient)
        return self
    
    def _separate_parenthesis(self):
        
        """Get the content of any parenthesis and store it for analysis later on, also remove those parenthesis from the ingredient.
        Updates the parenthesis_content and _reduced_ingredient variables
        """

        ingredient_without_parenthesis, parenthesis = _utils._split_by_parenthesis(self._standardized_ingredient)

        self._additional_keys["_staged_ingredient"]       = self._standardized_ingredient
        self._standardized_ingredient                    = ingredient_without_parenthesis # TODO: TESTING THIS OUT
        self._additional_keys["_parenthesis_content"]     = parenthesis

        return self

    def get_standardized_ingredient_data(self):
        """Return the standardized ingredient and additional keys."""
        return {
            '_standardized_ingredient': self._standardized_ingredient,
            **self._additional_keys
        }
