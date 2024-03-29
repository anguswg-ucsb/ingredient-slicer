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
# # from ._regex_patterns import IngredientTools


# # local dev import statements
# from ingredient_slicer import _utils
# from ingredient_slicer import _regex_patterns
# from ingredient_slicer import _constants
# # from ingredient_slicer import IngredientTools

class IngredientSlicer:
    """
    A class to parse recipe ingredients into a standard format.

    Args:
        ingredient (str): The ingredient to parse.
        debug (bool): Whether to print debug statements (default is False)
    """

    # regex = IngredientTools()

    def __init__(self, ingredient: str, debug = False):
        self.ingredient          = ingredient
        self.standardized_ingredient = ingredient
        
        self.food           = None 
        self.quantity       = None    # the best quantity found in the ingredient string
        self.unit           = None    # the best unit found in the ingredient string


        # make member variables for seconday quantities and units
        self.secondary_quantity = None
        self.secondary_unit     = None

        # "standard units" are the commonplace names for the found units (i.e. the standard unit of "oz" is "ounce")
        self.standardized_unit           = None 
        self.standardized_secondary_unit = None

        # "prep" are words that describe the state of the ingredient (i.e. "chopped", "diced", "minced")
        self.prep                  = []

        # "size modifiers" are words that describe the size of the ingredient (i.e. "large", "small", "medium")
        self.size_modifiers        = [] 

        # "dimension units" are units that describe the dimensions of the ingredient (i.e. "inch", "foot", "centimeter")
        self.dimension_units             = []

        # stash the best quantity and unit for testing/debugging
        self.stashed_quantity    = None 
        self.stashed_unit        = None

        self.required            = True    # default sets the ingredient as a required ingredient

        self.reduced_ingredient  = None    # parenthesis removed from the ingredient string

        self.parenthesis_content = None  # content of the parenthesis removed from the ingredient string
        self.parenthesis_notes   = []

        self.debug = debug
        # self.extract_version = extract_version

        self.parse()

        # self.found_units         = None    # where units will get stored after being parsed (temporarily)
        # self.parenthesis_obj = {
        #     "raw_ingredient": "",
        #     "standard_ingredient": "",
        #     "reduced_ingredient": self.reduced_ingredient,
        #     "parenthesis_content": ""
        #     }

    def _standardized_ingredient(self):
        
        return self.standardized_ingredient
    
    def _find_units(self, ingredient: str) -> List[str]:
        """
        Find units in the ingredient string.
        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            List[str]: A list of units found in the ingredient string.
        """

        # split the input string on whitespaces
        split_ingredient = ingredient.split()

        matched_units = [i for i in split_ingredient if i in _constants.UNITS]

        return matched_units
    
    # TODO: move to a utils file for generic functions ---> COMPLETED (Deprecated, this function, use the one in _utils.py)
    def _make_int_or_float_str(self, number_str: str) -> str:
        """ Convert a string representation of a number to its integer or float equivalent.
        If the number is a whole number, return the integer value as a string. If the number is a decimal, return the float value as a string.
        Args:
            number_str (str): The string representation of the number.
        Returns:
            str: The integer or float value of the number as a string.
        
        Examples:
        >>> make_int_or_float_str("1.0") 
        "1"
        >>> make_int_or_float_str("1")
        "1"
        >>> make_int_or_float_str("0.25")
        "0.25"
        """
        number = float(number_str.strip())  # Convert string to float
        if number == int(number):  # Check if float is equal to its integer value
            return str(int(number))  # Return integer value if it's a whole number
        else:
            return str(number)  # Return float if it's a decimal

    def _find_and_remove_percentages(self) -> None:
        """
        Find and remove percentages from the ingredient string.
        """
        # ingredient = "1 cup of 2% heavy cream"
        
        for key, pattern in _regex_patterns.PCT_REGEX_MAP.items():
            pattern_iter = pattern.finditer(self.standardized_ingredient)
            offset = 0
            for match in pattern_iter:
                match_string = match.group()
                start, end = match.start(), match.end()
                modified_start = start + offset
                modified_end = end + offset

                replacement_str = ""

                # Construct the modified string with the replacement applied
                self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(replacement_str) + self.standardized_ingredient[modified_end:]
                # ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]
                offset += len(str(replacement_str)) - (end - start)
        # pattern_iter = _regex_patterns.NUMBERS_FOLLOWED_BY_PERCENTAGE.finditer(self.standardized_ingredient)
                
        return
    
    def _replace_number_followed_by_inch_symbol(self) -> None:

        self.standardized_ingredient = _utils._replace_number_followed_by_inch_symbol(self.standardized_ingredient)

        return 
    
    def _find_and_replace_fraction_words(self) -> None:
        """ Find and replace fraction words with their corresponding numerical values in the parsed ingredient."""

        for key, pattern in _regex_patterns.NUMBER_WITH_FRACTION_WORD_MAP.items():
            
            pattern_iter = pattern.finditer(self.standardized_ingredient)
            offset = 0

            for match in pattern_iter:
                print(f"Got a fraction word match with key: {key}") if self.debug else None
                match_string = match.group(0)
                start, end = match.start(), match.end()
                modified_start = start + offset
                modified_end = end + offset

                match_string = match_string.replace("-", " ")
                print(f"Match: {match_string}") if self.debug else None
                # match_string = match_string.replace("-", " ")
                split_match = match_string.split(" ")

                split_match = [i.strip() for i in split_match]

                print(f"Split Match: {split_match}") if self.debug else None

                number_word = split_match[0]
                fraction_word = split_match[1]

                fraction_value, decimal = _constants.FRACTION_WORDS[fraction_word]

                updated_value = str(float(number_word) * float(decimal))
                self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(updated_value) + self.standardized_ingredient[modified_end:]
                # self.standardized_ingredient = self.standardized_ingredient[:match.start()] + str(updated_value) + self.standardized_ingredient[match.end():]
                # ingredient = ingredient[:modified_start] + str(updated_value) + ingredient[modified_end:]

                offset += len(str(updated_value)) - (end - start)

        # pattern_iter = _regex_patterns.NUMBER_WITH_FRACTION_WORD_GROUPS.finditer(self.standardized_ingredient)
        # offset = 0

        # for match in pattern_iter:
        #     start, end = match.start(), match.end()
        #     number_word   = match.group(1)
        #     fraction_word = match.group(2)
        #     fraction_value, decimal = _constants.FRACTION_WORDS[fraction_word]
        #     # multiply first number in match by the decimal value of the fraction word (i.e. "2 third" -> 2 * 1/3)
        #     updated_value = str(float(number_word) * float(decimal))
        #     self.standardized_ingredient = self.standardized_ingredient[:match.start()] + str(updated_value) + self.standardized_ingredient[match.end():]
        #     offset += len(updated_value) - (end - start)

        return 

    def _find_and_replace_numbers_separated_by_add_numbers(self) -> None:
        """Find numbers separated by "and", "&", "plus", or "+" and replace the matched strings with their sum of the 2 number values
        Examples:
        "1 and 0.5" -> "1.5"
        "1 & 0.5" -> "1.5"
        "2 plus 0.66" -> "2.66"
        "2 + 0.66" -> "2.66"
        """
        add_pattern_iter = _regex_patterns.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS.finditer(self.standardized_ingredient)

        offset = 0

        for match in add_pattern_iter:
            match_string = match.group(0)
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            first_number = float(match.group(1).strip())
            second_number = float(match.group(2).strip())

            print(f"MATCH: {match_string}") if self.debug else None
            print(f"First Number: {first_number}") if self.debug else None
            print(f"Second Number: {second_number}") if self.debug else None

            updated_value = f" {_utils._make_int_or_float_str(str(first_number + second_number))} "
            print(f"Updated Value: {updated_value}") if self.debug else None

            self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(updated_value) + self.standardized_ingredient[modified_end:]
            # self.standardized_ingredient = self.standardized_ingredient[:match.start()] + updated_value + self.standardized_ingredient[match.end():]
            offset += len(updated_value) - (end - start)
    
        return
    
    def _find_and_replace_casual_quantities(self):
        """
        Find and replace matches of CASUAL_QUANTITIES_PATTERN with the key from the CASUAL_QUANTITIES dictionary
        """

        offset = 0
        pattern_iter = _regex_patterns.CASUAL_QUANTITIES_PATTERN.finditer(self.standardized_ingredient)

        for match in pattern_iter:
            match_string    = match.group()

            # Get the start and end of the match and the modified start and end positions given the offset
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            replacement_str = _constants.CASUAL_QUANTITIES[match_string] 

            # Construct the modified string with the replacement applied
            self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(replacement_str) + self.standardized_ingredient[modified_end:]
            # input_ingredient = input_ingredient[:modified_start] + str(replacement_str) + input_ingredient[modified_end:]
            
            # Update the offset for subsequent removals 
            offset += len(str(replacement_str)) - (end - start)

    def _drop_special_dashes(self) -> None:
        # print("Dropping special dashes")
        self.standardized_ingredient = self.standardized_ingredient.replace("—", "-").replace("–", "-").replace("~", "-")
        return

    def _find_and_replace_prefixed_number_words(self) -> None:
        """ Replace prefixed number words with their corresponding numerical values in the parsed ingredient 
        Strings like "twenty five" are replaced with "25", or "thirty-two" is replaced with "32"

        """
        number_words_iter = _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.finditer(self.standardized_ingredient)

        offset = 0

        for match in number_words_iter:
            
            if match:
                start, end = match.start(), match.end()

                match_string = match.group()
                prefix_word = match.group(1)
                number_word = match.group(2)
                
                prefix_value = _constants.NUMBER_PREFIX_WORDS.get(prefix_word, 0)
                number_value = _constants.NUMBER_WORDS.get(number_word, 0)

                combined_value = prefix_value + number_value

                # Calculate the start and end positions in the modified string
                modified_start = start + offset
                modified_end = end + offset

                # Construct the modified string with the replacement applied
                self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(combined_value) + self.standardized_ingredient[modified_end:]
                # ingredient = ingredient[:modified_start] + str(combined_value) + ingredient[modified_end:]

                # Update the offset for subsequent replacements
                offset += len(str(combined_value)) - (end - start)

                # print(f"""
                # Match string: {match_string}
                # - Prefix word: {prefix_word}
                # - Number word: {number_word}
                # Prefix value ({prefix_value}) + Number value ({number_value}) = Combined value ({combined_value})
                # > {prefix_value} + {number_value} = {combined_value}
                # -> Match: {match_string} at positions {start}-{end}
                # ---> Modified ingredient: {self.standardized_ingredient}""") if self.debug else None

    def _find_and_replace_number_words(self) -> None:
        """
        Replace number words with their corresponding numerical values in the parsed ingredient.
        """

        # print("Parsing number words")
        for word, regex_data in _regex_patterns.NUMBER_WORDS_MAP.items():
            pattern = regex_data[1]
            # print statement if word is found in ingredient and replaced
            if pattern.search(self.standardized_ingredient):
                # print(f"- Found {word} in ingredient. Replacing with {regex_data[0]}") if self.debug else None
                self.standardized_ingredient = pattern.sub(regex_data[0], self.standardized_ingredient)

    def _clean_hyphen_padded_substrings(self) -> None:
        """Find and remove hyphens around "to", "or", and "and" substrings in the parsed ingredient.
        For example, "1-to-3 cups of soup" becomes "1 to 3 cups of soup" and "1-or-2 cups of soup" becomes "1 or 2 cups of soup"
        """

        substrings_to_fix = ["to", "or", "and", "&"]
        
        for substring in substrings_to_fix:
            self.standardized_ingredient = _utils._find_and_remove_hyphens_around_substring(self.standardized_ingredient, substring)

    
    def _clean_html_and_unicode(self) -> None:
        """Unescape fractions from HTML code coded fractions to unicode fractions."""

        # Unescape HTML
        self.standardized_ingredient = unescape(self.standardized_ingredient)

        # Replace unicode fractions with their decimal equivalents
        for unicode_fraction, decimal_fraction in _constants.UNICODE_FRACTIONS.items():
            self.standardized_ingredient = self.standardized_ingredient.replace(unicode_fraction, f" {decimal_fraction}")
            # self.standardized_ingredient = self.standardized_ingredient.replace(unicode_fraction, decimal_fraction)

    def _replace_unicode_fraction_slashes(self) -> None:
        """Replace unicode fraction slashes with standard slashes in the parsed ingredient."""

        # Replace unicode fraction slashes with standard slashes
        self.standardized_ingredient = self.standardized_ingredient.replace('\u2044', '/') # could use .replace('\u2044', '\u002F'), or just .replace("⁄", "/")

    def _add_whitespace(self):
        # regex pattern to match consecutive sequences of letters or digits
        pattern = _regex_patterns.CONSECUTIVE_LETTERS_DIGITS        
        # pattern = re.compile(r'([a-zA-Z]+)(\d+)|(\d+)([a-zA-Z]+)')

        # replace consecutive sequences of letters or digits with whitespace-separated sequences
        self.standardized_ingredient = re.sub(pattern, r'\1 \2\3 \4', self.standardized_ingredient)
    
    # # TODO: Deprecated, DELETE
    # def _fractions_to_decimals(self) -> None:
    #     """
    #     Replace fractions with their decimal equivalents in the parsed ingredient.
    #     """
    #     # print("Parsing fractions")
    #     fractions = re.findall(IngredientSlicer.regex.FRACTION_PATTERN, self.standardized_ingredient)

    #     split_frac = [i.replace(" ", "").split("/") for i in fractions]
    #     split_frac = [(int(f[0]), int(f[1])) for f in split_frac]
    #     fraction_decimal = [round(float(Fraction(f[0], f[1])), 3) for f in split_frac]

    #     # replace fractions in original string with decimal equivalents
    #     for i, f in enumerate(fractions):
    #         self.standardized_ingredient = self.standardized_ingredient.replace(f, str(fraction_decimal[i]))
    
    # # TODO: Get rid of this (Deprecated, use the one in _utils.py)
    # def _fraction_str_to_decimal(self, fraction_str: str) -> float:
    #     """
    #     Convert a string representation of a fraction to its decimal equivalent.
    #     """
    #     # Split the fraction string into its numerator and denominator
    #     split_fraction = [i.strip() for i in fraction_str.split("/")]
    #     # print(f"Split Fraction: {split_fraction}") if self.debug else None

    #     # If the fraction is a whole number, return the number
    #     if len(split_fraction) == 1:
    #         # print(f"---> Only one part: {split_fraction[0]}")

    #         converted_number = _utils._make_int_or_float_str(split_fraction[0])

    #         # print(f"---> OLD Output: {round(float(split_fraction[0]), 3)}")
    #         # print(f"---> NEW Output: {converted_number}")
    #         return converted_number

    #     numerator = int(split_fraction[0])
    #     denominator = int(split_fraction[1])

    #     # Convert the fraction to a decimal
    #     # return round(float(Fraction(numerator, denominator)), 3)
    #     return _utils._make_int_or_float_str(str(round(float(Fraction(numerator, denominator)), 3)))

    def _convert_fractions_to_decimals(self) -> None:
        """
        Convert fractions in the parsed ingredient to their decimal equivalents.
        """

        # fraction_str = "1 to 1/2 cups, 2 and 5 animals, 2 2 / 4 cats, 1 and 1/22 cups water melon"
        matches = _regex_patterns.FRACTION_PATTERN.findall(self.standardized_ingredient)
        # matches = regex.FRACTION_PATTERN.findall(fraction_str)

        # Replace fractions with their decimal equivalents
        for match in matches:
            # print(f"Match: {match}")

            fraction_decimal = _utils._fraction_str_to_decimal(match)
            # print(f"Fraction Decimal: {fraction_decimal}") if self.debug else None
            self.standardized_ingredient = self.standardized_ingredient.replace(match, str(fraction_decimal))

    def _force_ws(self):
        
        """Forces spaces between numbers and units and between units and numbers.
        End result is a string with a space between numbers and units and between units and numbers.
        Examples:
        "1cup" becomes "1 cup"
        "cup1" becomes "cup 1" 
        and ultimately "1cup" becomes "1 - cup" and "cup1" becomes "cup - 1"
        """

        NUMBERS_TO_LETTERS = re.compile(r"(\d)\-?([a-zA-Z])")  # 1cup
        LETTERS_TO_NUMBERS = re.compile(r"([a-zA-Z])(\d)")     # cup1
        LETTERS_DASH_NUMBERS = re.compile(r"([a-zA-Z])\-(\d)") # cup - 1

        self.standardized_ingredient = NUMBERS_TO_LETTERS.sub(r"\1 \2", self.standardized_ingredient)
        self.standardized_ingredient = LETTERS_TO_NUMBERS.sub(r"\1 \2", self.standardized_ingredient)
        self.standardized_ingredient = LETTERS_DASH_NUMBERS.sub(r"\1 - \2", self.standardized_ingredient)

    def _update_ranges(self, ingredient: str, pattern: re.Pattern, replacement_function=None) -> str:
        """Update the ranges in the ingredient string with the updated ranges
        Args:
            ingredient (str): The ingredient string to update
            pattern (re.Pattern): The pattern to use to find the ranges
            replacement_function (function, optional): A function to use to replace the matched ranges. Defaults to None.
        Returns:
            str: The updated ingredient string
        """
        
        # pattern = _regex_patterns.QUANTITY_DASH_QUANTITY
        
        matches = pattern.findall(ingredient)
        # matched_ranges = [match.split("-") for match in matches]

        if replacement_function:
            # print(f"Replacement Function given")
            matched_ranges = [replacement_function(match).split("-") for match in matches]
        else:
            # print(f"No Replacement Function given")
            matched_ranges = [match.split("-") for match in matches]

        # print(f"Matched Ranges: \n > {matched_ranges}") if self.debug else None

        updated_ranges = [" - ".join([str(_utils._fraction_str_to_decimal(i)) for i in match if i]) for match in matched_ranges]
        # updated_ranges = [" - ".join([str(int(i)) for i in match if i]) for match in matched_ranges]
        
        # Create a dictionary to map the matched ranges to the updated ranges
        ranges_map = dict(zip(matches, updated_ranges))

        # Replace the ranges in the original string with the updated ranges
        for original_range, updated_range in ranges_map.items():
            # print(f"Original Range: {original_range}")
            # print(f"Updated Range: {updated_range}")
            # if replacement_function:
            #     print(f"Replacement Function given")
            #     updated_range = replacement_function(updated_range)
            ingredient = ingredient.replace(original_range, updated_range)
            # print("\n") if self.debug else None

        return ingredient

    def _avg_ranges2(self) -> None:
        """
        Replace ranges of numbers with their average in the parsed ingredient.
        Examples:
        "1-2 oz" -> "1.5 oz"
        "1 - 2 ft" -> "1.5 ft"
        """
        # ingredient = "1 - 2 cups of sugar"
        search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(self.standardized_ingredient)
        # search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(ingredient)

        # OG = re.compile(r"\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?") # NOTE: this is the golden child, OG --> PREVIOUS VERSION THAT WORKS PERFECTLY (ALMOST)
        # search_ranges = OG.search(ingredient)

        print(f"Starting while loop searching for ranges in ingredient: {self.standardized_ingredient}") if self.debug else None
        while search_ranges:

            start, end = search_ranges.start(), search_ranges.end()
            match_string = search_ranges.group()
            
            left_range, right_range = match_string.split("-")
            
            left_range = left_range.strip()
            right_range = right_range.strip()

            print(f"Match: {match_string}") if self.debug else None
            print(f"left_range: {left_range}") if self.debug else None
            print(f"right_range: {right_range}") if self.debug else None
            print(f"Start: {start}") if self.debug else None
            print(f"End: {end}") if self.debug else None

            first_number  = float(_utils._fraction_str_to_decimal(left_range).strip())
            second_number = float(_utils._fraction_str_to_decimal(right_range).strip())
            
            range_average = f" {_utils._make_int_or_float_str(str((first_number + second_number) / 2))} "
            self.standardized_ingredient = self.standardized_ingredient[:start] + range_average + self.standardized_ingredient[end:]

            search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(self.standardized_ingredient)
            # search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY_GROUPS.search(ingredient)
        
        print(f"All ranges have been updated: {self.standardized_ingredient}") if self.debug else None

        self.standardized_ingredient = self.standardized_ingredient.strip()

        return
    
    def _avg_ranges(self) -> None:
        """
        Replace ranges of numbers with their average in the parsed ingredient.
        Examples:
        "1-2 oz" -> "1.5 oz"
        "1 - 2 ft" -> "1.5 ft"
        """
        
        all_ranges = re.finditer(_regex_patterns.QUANTITY_DASH_QUANTITY, self.standardized_ingredient)

        # initialize offset and replacement index values for updating the ingredient string, 
        # these will be used to keep track of the position of the match in the string
        offset = 0

        # Update the ingredient string with the merged values
        for match in all_ranges:
            print(f"Ingredient string: {self.standardized_ingredient}") if self.debug else None

            # Get the start and end positions of the match
            start, end = match.start(), match.end()

            print(f"Match: {match.group()} at positions {start}-{end}") if self.debug else None

            # Get the range values from the match
            range_values = re.findall(_regex_patterns.QUANTITY_DASH_QUANTITY, match.group())

            print(f"Range Values: {range_values}") if self.debug else None
            
            # split the range values into a list of lists
            split_range_values = [i.split("-") for i in range_values]
            
            print(f"  >>> Split Range Values: {split_range_values}") if self.debug else None
            # print() if self.debug else None

            # get the average of each of the range values
            range_avgs    = [sum([float(num_str) for num_str in i]) / 2 for i in split_range_values][0]
            range_average = _utils._make_int_or_float_str(str(range_avgs))

            print(f"Range Averages: {range_average}") if self.debug else None

            # Calculate the start and end positions in the modified string
            modified_start = start + offset
            modified_end = end + offset

            print(f"Replacing {match.group()} with '{range_average}'...") if self.debug else None
            
            # Construct the modified string with the replacement applied
            self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(range_average) + self.standardized_ingredient[modified_end:]
            # ingredient = ingredient[:modified_start] + str(range_average) + ingredient[modified_end:]

            # Update the offset for subsequent replacements
            offset += len(range_average) - (end - start)
    
        return 
    
    def _average_ranges(self) -> None:
        """ Average all hyphen separated ranges of numbers in the parsed ingredient. """
        self.standardized_ingredient = _utils.avg_ranges(self.standardized_ingredient)
        return
    
    # TODO: write tests for this
    def _merge_misleading_ranges(self) -> None:
        """ Merge misleading ranges in the parsed ingredient (i.e. "4-1/2" is not a valid range, it should be "4.5" instead)"""

        # Find all the ranges in the ingredient
        range_iter = _regex_patterns.QUANTITY_DASH_QUANTITY_GROUPS.finditer(self.standardized_ingredient)

        offset = 0

        for match in range_iter:
            match_string    = match.group()
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            left_range = match.group(1).strip()
            right_range = match.group(2).strip()

            first_number  = float(_utils._fraction_str_to_decimal(left_range).strip())
            second_number = float(_utils._fraction_str_to_decimal(right_range).strip())

            # If the second number is less than the first number, then the range is misleading
            #  and the numbers should be merged (added if second number is a fraction)
            if second_number < first_number:
                # print(f"Fixing misleading range: {match_string} with ")
                second_number_is_fraction = second_number < 1
                multiply_or_add_str = "add" if second_number_is_fraction else "multiply"

                print(f"Second number is a fraction: {second_number_is_fraction}\n > '{multiply_or_add_str}' {first_number} and {second_number}") if self.debug else None

                updated_value = f" {_utils._make_int_or_float_str(str(first_number + second_number))} " if second_number_is_fraction else f" {_utils._make_int_or_float_str(str(first_number * second_number))} "
                # updated_value = f" {_make_int_or_float_str(str(first_number + second_number))} "
                print(f"Fixing misleading range: {match_string} with {updated_value}") if self.debug else None
                
                self.standardized_ingredient = self.standardized_ingredient[:modified_start] + updated_value + self.standardized_ingredient[modified_end:]
                offset += len(updated_value) - (end - start)

                print(f"Ingredient after updating: {self.standardized_ingredient}") if self.debug else None

        self.standardized_ingredient = self.standardized_ingredient.strip()

        return

    def _fix_ranges(self):
        """
        Fix ranges in the parsed ingredient.
        Given a parsed ingredient, this method will fix ranges of numbers that are separated by one or more hyphens, ranges of numbers that are preceded by "between" and followed by "and" or "&", and ranges that are separated by "to" or "or".
        Examples:
        - "1-2 oz" -> "1 - 2 oz"
        - "between 1 and 5" -> "1 - 5"
        - "1 to 5" -> "1 - 5"

        """
        print("Fixing ranges") if self.debug else None
        # Define the regular expression pattern to match ranges

        print(f"Before initial range update:\n {self.standardized_ingredient}") if self.debug else None

        # # NOTE: NEW METHOD (in _utils.py)
        # Update ranges of numbers that are separated by one or more hyphens
        self.standardized_ingredient = _utils._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_DASH_QUANTITY)
        # self.standardized_ingredient = self._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_DASH_QUANTITY)

        print(f"After initial range update:\n {self.standardized_ingredient}") if self.debug else None

        # NOTE: NEW METHOD (in _utils.py)
        # # Update ranges of numbers that are preceded by "between" and followed by "and" or "&"
        self.standardized_ingredient = _utils._update_ranges(self.standardized_ingredient, _regex_patterns.BETWEEN_QUANTITY_AND_QUANTITY)
        # self.standardized_ingredient = self._update_ranges(self.standardized_ingredient, _regex_patterns.BETWEEN_QUANTITY_AND_QUANTITY, _utils._replace_and_with_hyphen)


        # NOTE: NEW METHOD (in _utils.py)
        # Update ranges that are separated by "to" 
        self.standardized_ingredient = _utils._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_TO_QUANTITY)
        # self.standardized_ingredient = self._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_TO_QUANTITY, _utils._replace_to_with_hyphen)
  
        print(f"After 'TO' update:\n {self.standardized_ingredient}") if self.debug else None

        # NOTE: NEW METHOD (in _utils.py)
        # Update ranges that are separated by "or"
        self.standardized_ingredient = _utils._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_OR_QUANTITY)
        # self.standardized_ingredient = self._update_ranges(self.standardized_ingredient, _regex_patterns.QUANTITY_OR_QUANTITY, _utils._replace_or_with_hyphen)
 
        print(f"After 'OR' update:\n {self.standardized_ingredient}") if self.debug else None

        # check and merge any misleading ranges
        self._merge_misleading_ranges()

        print(f"After misleading range update:\n {self.standardized_ingredient}") if self.debug else None

        return
    
    def _remove_repeat_units(self) -> None:
        """
        Remove repeat units from the ingredient string.
        Examples:
        "2 oz - 3 oz diced tomatoes" -> "2 - 3 oz diced tomatoes"
        "3cups-4 cups of cats" -> "3 - 4 cups of cats"
        """

        # get any strings that match the pattern 1<unitA> - 2<unitA> or 1<unitA> - 2<unitB>
        repeat_unit_matches = _regex_patterns.REPEAT_UNIT_RANGES.finditer(self.standardized_ingredient)
        # matches = pattern.finditer(self.standardized_ingredient)

        for match in repeat_unit_matches:

            # original string matched by the pattern (used for replacement)
            original_string = match.group(0)

            # quantities from first quantity/unit pair
            quantity1 = match.group(1)
            unit1     = match.group(2)

            # quantities from second quantity/unit pair
            quantity2 = match.group(3)
            unit2     = match.group(4)

            # if the units are the same, replace the original string with the quantities and units
            if unit1 == unit2:
                self.standardized_ingredient = self.standardized_ingredient.replace(original_string, f"{quantity1} - {quantity2} {unit1}")

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
        self.standardized_ingredient = _regex_patterns.X_AFTER_NUMBER.sub(replace_x, self.standardized_ingredient)

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
    
    def _merge_multi_nums(self) -> None:
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
        spaced_matches = re.finditer(_regex_patterns.SPACE_SEP_NUMBERS, self.standardized_ingredient)
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
            unit_after_match = re.search(_regex_patterns.UNITS_PATTERN,  self.standardized_ingredient[end:])
            # unit_after_match = re.search(regex_map.UNITS_PATTERN, ingredient[end:])
            
            if unit_after_match:
                # print(f"unit after match: > '{unit_after_match.group()}'")
                units.append(unit_after_match.group())

            # add the spaced number to the list
            spaced_nums.append(match.group())

            # print(f"Match: {match.group()} at positions {start}-{end}")
            merged_quantity = self._merge_spaced_numbers(match.group())
            merge_operation = self._which_merge_on_spaced_numbers(match.group())

            # print(f"merged_quantity: {merged_quantity}") if self.debug else None
            # print(f"merge_operation: {merge_operation}\n") if self.debug else None

            # Calculate the start and end positions in the modified string
            modified_start = start + offset
            modified_end = end + offset

            # print(f" -> Modified match positions: {modified_start}-{modified_end}")
            # print(f"Replacing {match.group()} with '{merged_quantity}'...") if self.debug else None
            
            # Construct the modified string with the replacement applied
            self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(merged_quantity) + self.standardized_ingredient[modified_end:]
            # ingredient = ingredient[:modified_start] + str(merged_quantity) + ingredient[modified_end:]

            # Update the offset for subsequent replacements
            offset += len(merged_quantity) - (end - start)
            replacement_index += 1

    def _replace_a_or_an_quantities(self) -> None:
        """
        Replace "a" or "an" with "1" in the parsed ingredient if no number is present in the ingredient string.
        """
        self.standardized_ingredient = _utils._replace_a_or_an_quantities(self.standardized_ingredient)
        return 
    
    def _drop_special_characters(self):

        # Drop unwanted periods and replace them with whitespace
        self.standardized_ingredient = self.standardized_ingredient.replace(".", " ")

    def _separate_parenthesis(self):
        
        """Get the content of any parenthesis and store it for analysis later on, also remove those parenthesis from the ingredient.
        Updates the parenthesis_content and reduced_ingredient variables
        """

        # # split the ingredient string by the open/close parenthesis sets
        # no_parenthesis1 = re.split(_regex_patterns.SPLIT_BY_PARENTHESIS, self.standardized_ingredient)
        # # remove any leading or trailing whitespace from the split strings and join them back together
        # no_parenthesis1 = " ".join([i.strip() for i in no_parenthesis1])
        # parenthesis1 = re.findall(_regex_patterns.SPLIT_BY_PARENTHESIS, self.standardized_ingredient)
        # # parenthesis = re.findall(_regex_patterns.SPLIT_BY_PARENTHESIS, ingredient)
        
        ingredient_without_parenthesis, parenthesis = _utils._split_by_parenthesis(self.standardized_ingredient)

        # # update the paranthensis object with the parsed values
        # self.parenthesis_obj["raw_ingredient"] = self.ingredient
        # self.parenthesis_obj["standard_ingredient"] = self.standardized_ingredient
        # self.parenthesis_obj["reduced_ingredient"] = no_parenthesis
        # self.parenthesis_obj["parenthesis_content"] = parenthesis
        
        # set "reduced_ingredient" to the parsed ingredient with parenthesis removed
        self.reduced_ingredient = ingredient_without_parenthesis
        # self.reduced_ingredient = no_parenthesis

        # set "parenthesis_content" to the parsed parenthesis strings
        self.parenthesis_content = parenthesis
        # self.parenthesis_content = parenthesis1
    
    # return parsed_parenthesis
        
    # TODO: delete this 
    # def _pull_units(self):
    #     """
    #     Pull out all of the units in the string
    #     Returns a dictionary containing all of the units found in the ingredient string (all units, basic units, nonbasic units, volumetric units, and a flag indicating if the ingredient has a unit).
    #     Args:
    #         ingredient (str): The ingredient string to parse.
    #     Returns:
    #         dict: A dictionary containing all of the units found in the ingredient string (all units, basic units, nonbasic units, volumetric units, and a flag indicating if the ingredient has a unit).
    #     Examples:
    #         >>> pull_units('0.25 teaspoon crushed red pepper (optional)')
    #         {'units': ['teaspoon'],
    #             'basic_units': ['teaspoon'],
    #             'nonbasic_units': [],
    #             'volumetric_units': ['teaspoon'],
    #             'has_unit': True}
    #         >>> pull_units('1 1/2 cups diced tomatoes, 2 tablespoons of sugar, 1 stick of butter')
    #         {'units': ['cups', 'tablespoons', 'stick'],
    #             'basic_units': ['cups', 'tablespoons', 'stick'],
    #             'nonbasic_units': ['stick'],
    #             'volumetric_units': ['cups', 'tablespoons'],
    #             'has_unit': True}
    #     """

    #     if not self.reduced_ingredient:
    #         return None
        
    #     # initliaze the has_unit flag to True, if no units are found, then the flag will be set to False
    #     has_unit = True

    #     # get all of the units in the ingredient string
    #     all_units = _regex_patterns.UNITS_PATTERN.findall(self.reduced_ingredient)

    #     # get the basic units in the ingredient string by checking if the units are in the basic units set
    #     basic_units = [unit for unit in all_units if unit in _constants.BASIC_UNITS_SET]
    #     # basic_units = regex.BASIC_UNITS_PATTERN.findall(ingredient) # Does the same thing but uses regex, probably better to NOT regex backtrack if we can avoid it..

    #     # get the nonbasic units in the ingredient string by checking if the units are not in the basic units set
    #     nonbasic_units = list(set(all_units) - set(basic_units))

    #     # get the volumetric units in the ingredient string by checking if the units are in the volumetric units set
    #     volumetric_units = [unit for unit in all_units if unit in _constants.VOLUME_UNITS_SET]
    #     # volumetric_units = regex.VOLUME_UNITS_PATTERN.findall(ingredient) 

    #     # if no units are found, then set the has_unit flag to False
    #     if not all_units and not basic_units and not nonbasic_units and not volumetric_units:
    #         has_unit = False

    #     self.found_units = {"units" : all_units,
    #                 "basic_units" : basic_units,
    #                 "nonbasic_units" : nonbasic_units,
    #                 "volumetric_units" : volumetric_units,
    #                 "has_unit" : has_unit}
    
    def _remove_extra_whitespaces(self, input_string: str) -> str:
        """Remove extra whitespaces from a string and return the string with only single whitespaces."""
        # ingredient = re.sub(r'\s+', ' ', ingredient).strip() # remove any extra whitespace
        return " ".join(input_string.split())
    
    def standardize(self):
        
        # define a list containing the class methods that should be called in order on the input ingredient string
        methods = [
            self._drop_special_dashes,
            self._find_and_remove_percentages,
            self._replace_number_followed_by_inch_symbol,
            self._find_and_replace_casual_quantities, # NOTE: testing this out
            self._find_and_replace_prefixed_number_words, # NOTE: testing this out
            self._find_and_replace_number_words,
            self._find_and_replace_fraction_words, # NOTE: testing this out
            self._clean_html_and_unicode,
            self._replace_unicode_fraction_slashes,
            self._convert_fractions_to_decimals,
            # self._fix_ranges, # TODO: ORIGINAL place for fix_ranges() ---> need to decide where this should go
            # self._remove_x_separators,
            self._force_ws,
            self._remove_repeat_units,
            self._remove_x_separators,
            self._clean_hyphen_padded_substrings, # Still needs tests written for this
            self._merge_multi_nums,
            self._fix_ranges,  # TODO: NEW place for fix_ranges() (THIS MIGHT BREAK THINGS) ---> need to decide where this should go
            self._find_and_replace_numbers_separated_by_add_numbers, # NOTE: testing this out (THIS MIGHT BREAK THINGS)
            # self._merge_multi_nums2,
            self._replace_a_or_an_quantities,
            self._average_ranges,
            # self._avg_ranges2,
            # self._avg_ranges,
            self._separate_parenthesis
            # self._pull_units
        ]

        # call each method in the list on the input ingredient string
        for method in methods:
            print(f"Calling method: {method.__name__}") if self.debug else None
            print(f"> Starting ingredient: '{self.standardized_ingredient}'") if self.debug else None

            method()

            print(f"> Ending ingredient: '{self.standardized_ingredient}'") if self.debug else None
        
        
        print(f"Removing extra whitespaces...") if self.debug else None

        self.standardized_ingredient = _utils._remove_extra_whitespaces(self.standardized_ingredient)
        # self.standardized_ingredient = self._remove_extra_whitespaces(self.standardized_ingredient)

        print(f"Done, returning standardized ingredient: \n > '{self.standardized_ingredient}'") if self.debug else None

        # return the parsed ingredient string
        # return self.standardized_ingredient
        return

    def extract_first_quantity_unit(self) -> None:

        """
        Extract the first unit and quantity from an ingredient string.
        Function will extract the first unit and quantity from the ingredient string and set the self.quantity and self.unit member variables.
        Quantities and ingredients are extracted in this order and if any of the previous steps are successful, the function will return early.
        1. Check for basic units (e.g. 1 cup, 2 tablespoons)
        2. Check for nonbasic units (e.g. 1 fillet, 2 carrot sticks)
        3. Check for quantity only, no units (e.g. 1, 2)

        If none of the above steps are successful, then the self.quantity and self.unit member variables will be set to None.

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
        basic_unit_matches = _regex_patterns.QUANTITY_BASIC_UNIT_GROUPS.findall(self.reduced_ingredient)
        # basic_unit_matches = regex.QUANTITY_BASIC_UNIT_GROUPS.findall(reduced_ingredient)

        # remove any empty matches
        valid_basic_units = [i for i in basic_unit_matches if len(i) > 0]

        # debugging message
        basic_units_message = f"Valid basic units: {valid_basic_units}" if valid_basic_units else f"No valid basic units found..."
        # print(basic_units_message) if self.debug else None

        # if we have valid single number quantities, then set the self.quantity and the self.unit member variables and exit the function
        if basic_unit_matches and valid_basic_units:
            self.quantity = valid_basic_units[0][0].strip()
            self.unit = valid_basic_units[0][1].strip()
            # return {"quantity": self.quantity, "unit": self.unit}
            return 

        # ---- STEP 2: CHECK FOR QUANTITY - NONBASIC UNITS (e.g. 1 fillet, 2 carrot sticks) ----
        # Example: "1 fillet of salmon" -> quantity: "1", unit: "fillet"

        # If no basic units are found, then check for anumber followed by a nonbasic units
        nonbasic_unit_matches = _regex_patterns.QUANTITY_NON_BASIC_UNIT_GROUPS.findall(self.reduced_ingredient)
        # nonbasic_unit_matches = regex.QUANTITY_NON_BASIC_UNIT_GROUPS.findall(reduced_ingredient)

        # remove any empty matches
        valid_nonbasic_units = [i for i in nonbasic_unit_matches if len(i) > 0]

        # debugging message
        nonbasic_units_message = f"Valid non basic units: {valid_nonbasic_units}" if valid_nonbasic_units else f"No valid non basic units found..."
        print(nonbasic_units_message) if self.debug else None

        # if we found a number followed by a non basic unit, then set the self.quantity and the self.unit member variables and exit the function
        if nonbasic_unit_matches and valid_nonbasic_units:
            self.quantity = valid_nonbasic_units[0][0].strip()
            self.unit = valid_nonbasic_units[0][1].strip()
            # return {"quantity": self.quantity, "unit": self.unit}
            return
        
        # ---- STEP 3: CHECK FOR ANY QUANTITIES or ANY UNITS in the string, and use the first instances (if they exist) ----
        # Example: "cups, 2 juice of lemon" -> quantity: "2", unit: "juice"

        # if neither basic nor nonbasic units are found, then get all of the numbers and all of the units
        quantity_matches = _regex_patterns.ALL_NUMBERS.findall(self.reduced_ingredient)
        unit_matches     = _regex_patterns.UNITS_PATTERN.findall(self.reduced_ingredient)

        # remove any empty matches
        valid_quantities = [i for i in quantity_matches if len(i) > 0]
        valid_units     = [i for i in unit_matches if len(i) > 0]

        # debugging messages
        all_quantities_message = f"Valid quantities: {valid_quantities}" if valid_quantities else f"No valid quantities found..."
        all_units_message = f"Valid units: {valid_units}" if valid_units else f"No valid units found..."

        # print(all_quantities_message) if self.debug else None
        # print(all_units_message) if self.debug else None

        # if either have valid quantities then set the best quantity and best unit to 
        # the first valid quantity and units found, otherwise set as None
        # TODO: Drop this "if valid_quantities or valid_units"...?
        if valid_quantities or valid_units:
            self.quantity = valid_quantities[0].strip() if valid_quantities else None
            self.unit = valid_units[0].strip() if valid_units else None
            # return {"quantity": self.quantity, "unit": self.unit}
            return

        # # ---- STEP 3: CHECK FOR QUANTITY - NO UNITS (e.g. 1, 2) ----

        # # if neither basic nor nonbasic units are found, then get the first number
        # quantity_matches = _regex_patterns.ALL_NUMBERS.findall(self.reduced_ingredient)
        # # quantity_matches = regex.ALL_NUMBERS.findall(reduced_ingredient)
        # # remove any empty matches
        # valid_quantities = [i for i in quantity_matches if len(i) > 0]
        # # debugging message
        # quantity_only_message = f"Valid quantities: {valid_quantities}" if valid_quantities else f"No valid quantities found..."
        # print(quantity_only_message)
        # # print(quantity_only_message) if self.debug else None
        # # if we have valid single number quantities, then return the first one
        # if quantity_matches and valid_quantities:
        #     self.quantity = valid_quantities[0].strip()
        #     # return {"quantity": self.quantity, "unit": self.unit}
        #     return
            
        # # ---- STEP 4: UNITS ONLY ----
        # regex.print_matches(reduced_ingredient)
        # unit_matches = regex.UNITS_PATTERN.findall(reduced_ingredient)

        # ---- STEP 4: NO MATCHES ----
        # just print a message if no valid quantities or units are found and return None
        # best_quantity and best_unit are set to None by default and will remain that way if no units or quantities were found.
        no_matches_message = f"No valid quantities or units found..."
        # print(no_matches_message) if self.debug else None

        return 
    
    def _check_if_required_parenthesis(self, parenthesis_list: list) -> bool:
        """
        Check if the parenthesis content contains the word "optional".
        Args:
            parenthesis_list (list): A list of strings containing the content of the parenthesis in the ingredient string.
        Returns:
            bool: A boolean indicating whether the word "optional" is found in the parenthesis content.
        """
        # parenthesis_list = parenthesis_list

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
    
    def _is_required(self) -> bool:
        """
        Check if the ingredient is required or optional
        Returns a boolean indicating whether the ingredient is required or optional.
        """

        # check if the ingredient string contains the word "optional" or "required"
        ingredient_is_required = self._check_if_required_string(self.reduced_ingredient)

        # check the parenthesis content for the word "optional" or "required"
        parenthesis_is_required = self._check_if_required_parenthesis(self.parenthesis_content)

        # if BOTH of the above conditions are True then return True otherwise return False
        return True if ingredient_is_required and parenthesis_is_required else False
    
    def _address_quantity_only_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content only contains a quantity.
        Attempts to update self.quantity, self.unit, self.secondary_quantity, and self.secondary_unit given 
        information from the parenthesis string and the current self.quantity and self.unit
        (e.g. "(3)", "(2.5)", "(1/2)")
        Args:
            parenthesis (str): The content of the parenthesis in the ingredient string.
        Returns:
            None
        """
        
        # print(f"""Ingredient: '{self.reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self.quantity}'\nUnit: '{self.unit}'""") if self.debug else None

        # Set a None Description
        description = None

        # pull out the parenthesis quantity values
        numbers_only = _utils._extract_quantities_only(parenthesis) # NOTE: testing this out
        # numbers_only = _regex_patterns.PARENTHESIS_WITH_NUMBERS_ONLY.findall(parenthesis)

        # if no numbers only parenthesis, then just return the original ingredient
        if not numbers_only:
            print(f"\n > Return early from QUANTITY parenthesis") if self.debug else None
            description = f"not a quantity only parenthesis"
            self.parenthesis_notes.append(description)
            return

        # pull out the self.quantity from the parenthesis
        parenthesis_quantity = numbers_only[0]

        # if there is not a unit or a quantity, then we can use the parenthesis number as the quantity and
        #  return the ingredient with the new quantity
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if not self.quantity and not self.unit:
            description = f"maybe unit is: the 'food' or a 'sometimes unit'"
            self.parenthesis_notes.append(description)

            self.quantity = parenthesis_quantity
            return
        
        # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
        # then the unit is also likely the food 
        # TODO: OR the unit MIGHT be the food OR might be a "SOMETIMES_UNIT", maybe do that check here, not sure yet...
        if self.quantity and not self.unit:
            updated_quantity = str(float(self.quantity) * float(parenthesis_quantity))
            
            description = f"maybe unit is: the 'food' or a 'sometimes unit'"
            self.parenthesis_notes.append(description)

            # set the secondary quantity to the ORIGINAL quantity/units
            self.secondary_quantity = self.quantity 

            # Update the quantity with the updated merged quantity
            self.quantity = _utils._make_int_or_float_str(updated_quantity)
            # self.quantity = updated_quantity

            # return [updated_quantity, self.unit, description]
            return
        
        # if there is a unit but no quantity, then we can use the parenthesis number as the quantity and 
        # return the ingredient with the new quantity
        if not self.quantity and self.unit:
            # updated_quantity = numbers_only[0]
            description = f"used quantity from parenthesis"
            self.parenthesis_notes.append(description)

            # set the secondary quantity to the ORIGINAL quantity/units
            self.secondary_quantity = self.quantity 

            # set the quantity to the parenthesis quantity
            self.quantity = parenthesis_quantity

            return

        # if there is a quantity and a unit, then we can try
        # to merge (multiply) the current quantity and the parenthesis quantity
        # then return the ingredient with the new quantity
        if self.quantity and self.unit:
            # if there is a quantity and a unit, then we can try to merge (multiply) the current quantity and the parenthesis quantity
            # then return the ingredient with the new quantity

            description = f"multiplied starting quantity with parenthesis quantity"
            self.parenthesis_notes.append(description)

            updated_quantity = str(float(self.quantity) * float(parenthesis_quantity))

            # set the secondary quantity to the ORIGINAL quantity/units
            self.secondary_quantity = self.quantity 

            # Update the quantity with the updated merged quantity (original quantity * parenthesis quantity)
            self.quantity = _utils._make_int_or_float_str(updated_quantity)
            # self.quantity = updated_quantity

            return

        description = f"used quantity from parenthesis with quantity only"
        self.parenthesis_notes.append(description)
        
        # set the secondary quantity to the ORIGINAL quantity/units
        self.secondary_quantity = self.quantity 

        # update the quantity with the parenthesis quantity value
        self.quantity = parenthesis_quantity

        return
    
    def _address_equivalence_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content contains any equivalence strings like "about" or "approximately", followed by a quantity and then a unit later in the sting.
        Attempts to update self.quantity, self.unit, self.secondary_quantity, and self.secondary_unit given 
        information from the parenthesis string and the current self.quantity and self.unit
        e.g. "(about 3 ounces)", "(about a 1/3 cup)", "(approximately 1 large tablespoon)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self.reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self.quantity}'\nUnit: '{self.unit}'""") if self.debug else None

        
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
            self.parenthesis_notes.append(description)
            return
        
        # pull out the suffix word, parenthesis quantity and unit
        parenthesis_suffix, parenthesis_quantity, parenthesis_unit = equivalent_quantity_unit[0]
        
        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis quantity-unit as our quantity and unit
        if not self.quantity and not self.unit:

            description = f"used equivalence quantity unit as our quantity and unit"
            self.parenthesis_notes.append(description)

            # set quantity/unit to the parenthesis values
            self.quantity = parenthesis_quantity
            self.unit = parenthesis_unit

            return
        
        # Case when: YES quantity, NO unit:
            # we can assume the equivelent quantity units 
            # in the parenthesis are actually a better fit for the quantities and units so 
            # we can use those are our quantities/units and then stash the original quantity in the "description" field 
            # with a "maybe quantity is " prefix in front of the original quantity for maybe use later on
        if self.quantity and not self.unit:

            # stash the old quantity with a trailing string before changing best_quantity
            description = f"maybe quantity is: {' '.join(self.quantity)}"
            self.parenthesis_notes.append(description)

            # make the secondary_quantity the starting quantity before converting the quantity to the value found in the parenthesis
            self.secondary_quantity = self.quantity

            # set the quantity/unit to the parenthesis values
            self.quantity = parenthesis_quantity
            self.unit = parenthesis_unit

            return 

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are probably "better" so use the
            # parenthesis quantity/units and then stash the old unit in the description
        if not self.quantity and self.unit:

            # stash the old quantity with a trailing "maybe"
            description = f"maybe unit is: {self.unit}"
            self.parenthesis_notes.append(description)

            # make the secondary_unit the starting unit before converting the unit to the unit string found in the parenthesis
            self.secondary_unit = self.unit

            self.quantity = parenthesis_quantity
            self.unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return 
        
        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely found an equivalent quantity/unit
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if self.quantity and self.unit:
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = self.unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units:  (# TODO: Maybe we should use parenthesis quantity/unit instead...?)
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self.parenthesis_notes.append(description)
                # return [self.quantity, self.unit, description]

                # set the secondary quantity/units to the values in the parenthesis
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit

                return
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self.parenthesis_notes.append(description)
                # return [self.quantity, self.unit, description]
                
                # set the secondary quantity/units to the values in the parenthesis
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit

                return

            # Case when: YES basic parenthesis unit, NO basic original unit: 
            #   then use the parenthesis quantity/unit (stash the original in the description)
            if parenthesis_unit_is_basic:
                description = f"maybe quantity/unit is: {self.quantity}/{self.unit}"
                self.parenthesis_notes.append(description)
                
                # set the secondary quantity/units to the original quantity/units
                self.secondary_quantity = self.quantity
                self.secondary_unit = self.unit

                # update the primary quantities/units to the parenthesis values
                self.quantity = parenthesis_quantity
                self.unit = parenthesis_unit
                
                # return [parenthesis_quantity, parenthesis_unit, description]
                return

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then use the original quantity/unit (stash the parenthesis in the description)
            if unit_is_basic:
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit

                return

        description = f"used quantity/units from parenthesis with equivalent quantity/units"
        self.parenthesis_notes.append(description)

        # set the secondary quantity/units to the original quantity/units
        self.secondary_quantity = self.quantity
        self.secondary_unit = self.unit

        self.quantity = parenthesis_quantity
        self.unit = parenthesis_unit

        return
    
    def _address_quantity_unit_only_parenthesis(self, parenthesis: str) -> None:
        """
        Address the case where the parenthesis content contains exactly a quantity and unit (NOT prefixed by any equivalence strings like "about" or "approximately").
        Attempts to update self.quantity, self.unit, self.secondary_quantity, and self.secondary_unit given 
        information from the parenthesis string and the current self.quantity and self.unit
        e.g. "(3 ounces)", "(3 ounces each)", "(a 4 cup scoop)"

        Args:
            parenthesis (str): A string containing parenthesis from the ingredients string
        Returns:
            None
        """

        # print(f"""Ingredient: '{self.reduced_ingredient}'\nParenthesis: '{parenthesis}'\nQuantity: '{self.quantity}'\nUnit: '{self.unit}'""") if self.debug else None

        # Set a None Description
        description = None

        # pull out quantity unit only pattern
        quantity_unit_only = _utils._extract_quantity_unit_pairs(parenthesis)
        # quantity_unit_only = _regex_patterns.QUANTITY_UNIT_GROUPS.findall(parenthesis)
        # quantity_unit_only = [item for i in [_regex_patterns.QUANTITY_UNIT_GROUPS.findall(i) for i in parenthesis] for item in i]

        # if no numbers only parenthesis, then just return the original ingredient
        if not quantity_unit_only:
            # print(f"\n > Return early from QUANTITY UNIT parenthesis") if self.debug else None
            description = f"not a quantity unit only parenthesis"
            self.parenthesis_notes.append(description)
            # return [self.quantity, unit, description]
            return
        
        # pull out the parenthesis quantity and unit
        parenthesis_quantity, parenthesis_unit = quantity_unit_only[0]

        # Case when: NO quantity, NO unit:
            # if no quantity AND no unit, then we can use the parenthesis self.quantity-unit as our self.quantity and unit
        if not self.quantity and not self.unit:
            # updated_quantity, updated_unit = quantity_unit_only[0]
            # print(f"\n > Case when: NO quantity, NO unit") if self.debug else None

            description = f"used quantity/unit from parenthesis with no quantity/unit"
            self.parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self.secondary_quantity = self.quantity
            self.secondary_unit = self.unit

            self.quantity = parenthesis_quantity
            self.unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return

        # Case when: YES quantity, NO unit:
            # if there is a quantity but no unit, we can try to merge (multiply) the current quantity and the parenthesis quantity 
            # then use the unit in the parenthesis
        if self.quantity and not self.unit:
            # print(f"\n > Case when: YES quantity, NO unit") if self.debug else None

            # quantity_unit_only[0][0]
            updated_quantity = str(float(self.quantity) * float(parenthesis_quantity))

            description = f"multiplied starting quantity with parenthesis quantity"
            self.parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self.secondary_quantity = self.quantity
            self.secondary_unit = self.unit

            # self.quantity = updated_quantity
            self.quantity = _utils._make_int_or_float_str(updated_quantity)
            self.unit = parenthesis_unit

            # return [updated_quantity, parenthesis_unit, description]
            return

        # Case when: NO quantity, YES unit:
            # if there is no quantity BUT there IS a unit, then the parenthesis units/quantities are either:
            # 1. A description/note (i.e. cut 0.5 inch slices)
            # 2. A quantity and unit (i.e. 2 ounces)
            # either case, just return the parenthesis units to use those
        if not self.quantity and self.unit:
            # print(f"\n > Case when: NO quantity, YES unit") if self.debug else None

            description = f"No quantity but has units, used parenthesis. maybe quantity/unit is: {self.quantity}/{self.unit}"
            self.parenthesis_notes.append(description)

            # set the secondary quantity/units to the original quantity/units
            self.secondary_quantity = self.quantity
            self.secondary_unit = self.unit

            self.quantity = parenthesis_quantity
            self.unit = parenthesis_unit

            # return [parenthesis_quantity, parenthesis_unit, description]
            return

        # Case when: YES quantity, YES unit:
            # if we already have a quantity AND a unit, then we likely just found a description 
            # OR we may have found an equivalence quantity unit.
            # we will choose to use the quantity/unit pairing that is has a unit in the BASIC_UNITS_SET
        if self.quantity and self.unit:
            # print(f"\n > Case when: YES quantity, YES unit") if self.debug else None

            # flags for if original unit/parenthesis unit are in the set of basic units (BASIC_UNITS_SET) or not
            parenthesis_unit_is_basic = parenthesis_unit in _constants.BASIC_UNITS_SET
            unit_is_basic = self.unit in _constants.BASIC_UNITS_SET

            # Case when BOTH are basic units: 
            #   use the original quantity/unit (stash the parenthesis in the description)
            if parenthesis_unit_is_basic and unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, BASIC unit") if self.debug else None

                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit
                return
            
            # Case when NEITHER are basic units:    # TODO: this can be put into the above condition but thought separated was more readible.
            #   use the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values 
            #   (stash the parenthesis in the description)
            if not parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, NOT BASIC unit") if self.debug else None
                description = f"maybe quantity/unit is: {parenthesis_quantity}/{parenthesis_unit}"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit
                return

            # Case when: YES basic parenthesis unit, NO basic original unit (EXPLICIT):
            #  Try to merge (multiply) the current quantity and the parenthesis quantity
            #  AND set the secondary quantity/units to the ORIGINAL values
            if parenthesis_unit_is_basic and not unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (EXPLICIT)") if self.debug else None
                updated_quantity = str(float(self.quantity) * float(parenthesis_quantity))

                description = f"multiplied starting quantity with parenthesis quantity"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self.secondary_quantity = self.quantity
                self.secondary_unit = self.unit

                # self.quantity = updated_quantity
                self.quantity = _utils._make_int_or_float_str(updated_quantity)
                self.unit = parenthesis_unit

                return

            # TODO: I think this condition can be dropped, gets covered by previous condition...
            # Case when: YES basic parenthesis unit, NO basic original unit (IMPLICITLY): 
            #   then use the parenthesis quantity/unit AND set the secondary quantity/units to the ORIGINAL values
            #   (stash the original in the description)
            if parenthesis_unit_is_basic:
                # print(f"\n >>> Case when: BASIC parenthesis unit, NOT BASIC unit (IMPLICIT)") if self.debug else None
                description = f"maybe quantity/unit is: {self.quantity}/{self.unit}"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the original quantity/units
                self.secondary_quantity = self.quantity
                self.secondary_unit = self.unit

                self.quantity = parenthesis_quantity
                self.unit = parenthesis_unit

                return

            # Case when: NO basic parenthesis unit, YES basic original unit: 
            #   then just keep the original quantity/unit AND set the secondary quantity/units to the PARENTHESIS values
            #   (stash the original in the description)
            if unit_is_basic:
                # print(f"\n >>> Case when: NOT BASIC parenthesis unit, BASIC unit (IMPLICIT)") if self.debug else None
                description = f"maybe quantity/unit is: {self.quantity}/{self.unit}"
                self.parenthesis_notes.append(description)

                # set the secondary quantity/units to the parenthesis quantity/units
                self.secondary_quantity = parenthesis_quantity
                self.secondary_unit = parenthesis_unit

                return
        
        print(f"\n ----> Case when: ALL OTHER CASES FAILED") if self.debug else None

        # TODO: Don't think this should ever happen, need to rethink this part
        # Case when: All other conditions were NOT met:
            # just set the quantity/unit to the parenthesis values 
            # and then put the original quantity/units in the secondary quantity/units
        description = f"used quantity/units from parenthesis with quantity/units only"
        self.parenthesis_notes.append(description)

        # set the secondary quantity/units to the ORIGINAL quantity/units
        self.secondary_quantity = self.quantity 
        self.secondary_unit = self.unit

        # set the primary quantity/units to the parenthesis quantity/units
        self.quantity = parenthesis_quantity
        self.unit = parenthesis_unit

        return
    
    def _add_standard_units(self) -> None:
        """
        Add standard units to the parsed ingredient if they are present in the
        constants units to standard units map.
        If the "unit"/"secondary_unit" exists and it is present in the unit to standard unit map, 
        then get the standard unit name for the unit and set the "standardized_unit" and "standardized_secondary_unit" member variables.
        """

        if self.unit and self.unit in _constants.UNIT_TO_STANDARD_UNIT:
            self.standardized_unit = _constants.UNIT_TO_STANDARD_UNIT[self.unit]
        
        if self.secondary_unit and self.secondary_unit in _constants.UNIT_TO_STANDARD_UNIT:
            self.standardized_secondary_unit = _constants.UNIT_TO_STANDARD_UNIT[self.secondary_unit]

        return 

    def _prioritize_weight_units(self) -> None:
        """
        Prioritize weight units over volume units if both are present in the parsed ingredient.
        If the first unit is not a weight unit but the secondary_unit is a weight unit, then swap them so 
        the weight unit is always given as the primary unit.
        (i.e. unit = "cups", secondary_unit = "ounces" --> Swap them so that unit = "ounces" and secondary_unit = "cups")
        """

        # # if the first unit is already a weight, just return early
        if self.unit in _constants.WEIGHT_UNITS_SET:
            return 
        
        # TODO: first part of this if statement is probably redundent...
        # if the first unit is NOT a weight and the second unit IS a weight, then swap them
        if self.unit not in _constants.WEIGHT_UNITS_SET and self.secondary_unit in _constants.WEIGHT_UNITS_SET:

            print(f"Swapping first quantity/units with second quantity/units") if self.debug else None
            # print(f"Swapping first quantity/units with second quantity/units") if self.debug else None

            # switch the units and quantities with the secondary units and quantities
            self.quantity, self.secondary_quantity = self.secondary_quantity, self.quantity
            self.unit, self.secondary_unit = self.secondary_unit,  self.unit
            self.standardized_unit, self.standardized_secondary_unit = self.standardized_secondary_unit, self.standardized_unit

        return 
    
    def _find_and_remove(self, string: str, pattern: re.Pattern) -> str:
        """Find and remove all matches of a pattern from a string.
        Args:
            string (str): The string to search for matches in
            pattern (re.Pattern): The pattern to search for in the string
        Returns:
            str: The modified string with all matches removed
        """

        pattern_iter = pattern.finditer(string)

        offset = 0

        for match in pattern_iter:
            match_string    = match.group()
            replacement_str = ""

            # Get the start and end of the match and the modified start and end positions given the offset
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            # Construct the modified string with the replacement applied
            string = string[:modified_start] + str(replacement_str) + string[modified_end:]
            # self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(replacement_str) + self.standardized_ingredient[modified_end:]

            # Update the offset for subsequent removals # TODO: this is always 0 because we're removing the match, probably just remove...
            offset += len(str(replacement_str)) - (end - start)
            # print(f"""
            # Match string: {match_string}
            # -> Match: {match_string} at positions {start}-{end}
            # --> Modified start/end match positions: {modified_start}-{modified_end}
            # ---> Modified string: {string}""")

        return string
    
    def _extract_foods(self, ingredient: str) -> str:
        """Does a best effort attempt to extract foods from the ingredient by 
        removing all extraneous details, words, characters and hope we get left with the food.
        """

        print(f"Best effort extraction of food words from: {ingredient}") if self.debug else None

        # Apply _utils._remove_parenthesis_from_str() to remove parenthesis content
        ingredient = _utils._remove_parenthesis_from_str(ingredient)

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
            print(f" > Removing '{key}' from the ingredient\n") if self.debug else None

            print(f"Starting ingredient:\n > '{ingredient}'") if self.debug else None
            # ingredient = self._find_and_remove(ingredient, pattern)
            ingredient = _utils._find_and_remove(ingredient, pattern)
            print(f"Ending ingredient:\n > '{ingredient}'") if self.debug else None

        print(f" > Removing any remaining special characters") if self.debug else None
        
        ingredient = re.sub(r'[^\w\s]', '', ingredient) # remove any special characters

        print(f" > Removing any extra whitespaces") if self.debug else None

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

    def _extract_dimension_units(self, ingredient: str) -> str:
        """Add sometimes units to the units variables if they are the only possible units after the ingredient has been parsed."""
        # ingredient = "2 1/2 cups of sugar (about 1/2 inch squares of sugar)"

        dimension_units = _regex_patterns.QUANTITY_DIMENSION_UNIT_GROUPS.findall(ingredient)
        dimension_units.sort()

        return dimension_units

    def _address_parenthesis(self) -> None:
        """
        Address any parenthesis that were in the ingredient.
        """

        # print(f"Addressing parenthesis: '{self.parenthesis_content}'") if self.debug else None

        # loop through each of the parenthesis in the parenthesis content and apply address_parenthesis functions 
        for parenthesis in self.parenthesis_content:
            print(f"Addressing parenthesis: '{parenthesis}'") if self.debug else None

            # address the case where the parenthesis content only contains a quantity
            print(f"> Apply QUANTITY Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
            self._address_quantity_only_parenthesis(parenthesis)
            
            print(f"> Apply EQUIVALENCE Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
            self._address_equivalence_parenthesis(parenthesis)

            print(f"> Apply QUANTITY UNIT Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
            self._address_quantity_unit_only_parenthesis(parenthesis)

        return

    def parse(self):
        # TODO: process parenthesis content

        print(f"Standardizing ingredient: \n > '{self.ingredient}'") if self.debug else None
        # print(f"Standardizing ingredient: \n > '{self.ingredient}'")

        # ----------------------------------- STEP 1 ------------------------------------------
        # ---- Get the input ingredient string into a standardized form ----
        # -------------------------------------------------------------------------------------

        # run the standardization method to cleanup raw ingredient and create the "standard_ingredient" and "reduced_ingredient" member variables 
        self.standardize()

        print(f"Standardized ingredient: \n > '{self.standardized_ingredient}'") if self.debug else None
        print(f"Reduced ingredient: \n > '{self.reduced_ingredient}'") if self.debug else None
        print(f"Extracting first quantity and unit from reduced ingredient: \n > '{self.reduced_ingredient}'") if self.debug else None
        # ----------------------------------- STEP 2 ------------------------------------------
        # ---- Check if there is any indication of the ingredient being required/optional ----
        # -------------------------------------------------------------------------------------

        # run the is_required method to check if the ingredient is required or optional and set the "is_required" member variable to the result
        self.is_required = self._is_required()

        print(f"Is the ingredient required? {self.is_required}") if self.debug else None

        # ----------------------------------- STEP 3 ------------------------------------------
        # ---- Extract first options of quantities and units from the "reduced_ingredient" ----
        # -------------------------------------------------------------------------------------

        #  reduced_ingredient ---> (i.e. standardized ingredient with parenthesis content removed)
        # run the extract_first_quantity_unit method to extract the first unit and quantity from the ingredient string
        self.extract_first_quantity_unit()

        # ----------------------------------- STEP 4 ------------------------------------------
        # ---- Address any parenthesis that were in the ingredient  ----
        # -------------------------------------------------------------------------------------
        # NOTE: Stash the best_quantity and best_units before preceeding (for debugging)

        # stash the best quantity and unit for testing/debugging
        self.stashed_quantity    = self.quantity 
        self.stashed_unit        = self.unit

        print(f"""Status of ingredients before parenthesis handling: {self.ingredient}
            Ingredient: > '{self.ingredient}'
                > Standard ingredient: '{self.standardized_ingredient}'
                > Stashed Quantity ingredient: '{self.stashed_quantity}'
                > Stashed unit ingredient: '{self.stashed_unit}'
                > Parenthesis content: '{self.parenthesis_content}'
            """) if self.debug else None
        
        # # loop through each of the parenthesis in the parenthesis content and apply address_parenthesis functions 
        # for parenthesis in self.parenthesis_content:
        #     print(f"Addressing parenthesis: '{parenthesis}'") if self.debug else None

        #     # address the case where the parenthesis content only contains a quantity
        #     print(f"> Apply QUANTITY Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
        #     self._address_quantity_only_parenthesis(parenthesis)
            
        #     print(f"> Apply EQUIVALENCE Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
        #     self._address_equivalence_parenthesis(parenthesis)

        #     print(f"> Apply QUANTITY UNIT Parenthesis to: '{self.quantity} {self.unit}'") if self.debug else None
        #     self._address_quantity_unit_only_parenthesis(parenthesis)

        self._address_parenthesis()

        # ----------------------------------- STEP 5 ------------------------------------------
        # ---- Get the standard names of the units and secondary units ----
        # -------------------------------------------------------------------------------------
        print(f"Adding standard unit names for {self.unit} and {self.secondary_unit}") if self.debug else None

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
        # print(f"Extracting food words (version {self.extract_version})") if self.debug else None
        
        self.food = self._extract_foods(self.standardized_ingredient)

        # ----------------------------------- STEP 8 ------------------------------------------
        # ---- Extract extra, descriptors (prep words, size modifiers, dimension units) ----
        # -------------------------------------------------------------------------------------
        print(f"Extracting prep words, size modifiers") if self.debug else None
        # print(f"Extracting food words (version {self.extract_version})") if self.debug else None
        
        self.prep = self._extract_prep_words(self.standardized_ingredient)
        self.size_modifiers = self._extract_size_modifiers(self.standardized_ingredient)

    def to_json(self) -> dict:
        """
        Convert the IngredientSlicer object to a dictionary.
        Returns:
            dict: A dictionary containing the IngredientSlicer object's member variables.
        """
        return {
            "ingredient": self.ingredient,                                # "2 1/2 large cups of sugar lightly packed (about 40 tbsp of sugar)"
            "standardized_ingredient": self.standardized_ingredient,          # "2.5 cups of sugar"
        
            "food" : self.food,                                           # "sugar"

            "quantity": self.quantity,                                    # "2.5"
            "unit": self.unit,                                            # "cups"
            "standardized_unit": self.standardized_unit,                      # "cup"

            "secondary_quantity": self.secondary_quantity,                # "40"
            "secondary_unit": self.secondary_unit,                        # "tbsp"
            "standardized_secondary_unit": self.standardized_secondary_unit,  # "tablespoon"

            "prep": self.prep,                                            # ["lightly", "packed"]
            "size_modifiers": self.size_modifiers,                        # ["large"]

            "is_required": self.is_required,                              # True

            # NOTE: drop these at some point
            "parenthesis_content": self.parenthesis_content               # ["(about 40 tbsp of sugar)"]
            # "parenthesis_notes": self.parenthesis_notes,
            # "stashed_quantity" : self.stashed_quantity,
            # "stashed_unit" : self.stashed_unit
            # "reduced_ingredient": self.reduced_ingredient, 
        }


# # ####### Deprecated ####### 
# def _merge_multi_nums2(self) -> None:
#     """
#     Replace unicode and standard fractions with their decimal equivalents in the parsed ingredient.
#     Assumes that numeric values in string have been padded with a space between numbers and non numeric characters and
#     that any fractions have been converted to their decimal equivalents.
#     Args:
#         ingredient (str): The ingredient string to parse.
#     Returns:
#         str: The parsed ingredient string with the numbers separated by a space merged into a single number (either added or multiplied).
    
#     >>> _merge_multi_nums('2 0.5 cups of sugar')
#     '2.5 cups of sugar'
#     >>> _merge_multi_nums('1 0.5 pounds skinless, boneless chicken breasts, cut into 0.5 inch pieces')
#     '1.5 pounds skinless, boneless chicken breasts, cut into 0.5 inch pieces'
#     """
    
#     # get the units from the ingredient string
#     # units = re.findall(regex_map.UNITS_PATTERN, ingredient)
#     units = re.findall(_regex_patterns.UNITS_PATTERN, self.standardized_ingredient)

#     # spaced_nums = re.findall(regex.SPACE_SEP_NUMBERS, '2 0.5 cups of sugar 3 0.5 lbs of carrots')
#     spaced_nums = re.findall(_regex_patterns.SPACE_SEP_NUMBERS, self.standardized_ingredient)

#     # Merge the numbers from the space seperated string of numbers
#     merged_values = [self._merge_spaced_numbers(num_pair) for num_pair in spaced_nums]

#     # Was the operation to merge the numbers an addition or a multiplication?
#     merge_type = [self._which_merge_on_spaced_numbers(num_pair) for num_pair in spaced_nums]

#     # ---- METHOD 1 ----
#     # METHOD 1: Create a list of dictionaries with the units and their converted quantities
#     merged_unit_quantities = [{"units":u, "quantities": q, "merge_operation": m} for u, q, m in zip(units, merged_values, merge_type)]
#     # merged_unit_quantities = [{"units":u, "quantities": q} for u, q in zip(units, merged_values)] # not including merge_type

#     # map the spaced numbers to the units and their converted quantities
#     # Key is the spaced numbers, value is a dictionary with the units, merged quantities, and the merge operation
#     conversions_map = dict(zip(spaced_nums, merged_unit_quantities))

#     # ---- METHOD 2 ----
#     # METHOD 2: Create a LIST of dictionaries with the original string, the units, their converted quantities, and the merge method (keep track of iteration index and index the matches by position)
#     conversions_list = [{"input_numbers": n, "units":u, "quantities": q, "merge_operation": m} for n, u, q, m in zip(spaced_nums, units, merged_values, merge_type)]

#     if len(spaced_nums) != len(conversions_map):
#         warnings.warn(f"Number of spaced numbers and number of converted matches (MAP) are not equal...")

#     if len(spaced_nums) != len(conversions_list):    
#         warnings.warn(f"Number of spaced numbers and number of converted matches (LIST) are not equal...")
    
#     # Create iterable of the matched spaced numbers to insert updated values into the original string
#     spaced_matches = re.finditer(_regex_patterns.SPACE_SEP_NUMBERS, self.standardized_ingredient)

#     # initialize offset and replacement index values for updating the ingredient string, 
#     # these will be used to keep track of the position of the match in the string
#     offset = 0
#     replacement_index = 0

#     # Update the ingredient string with the merged values
#     for match in spaced_matches:
#         # print(f"Ingredient string: {self.standardized_ingredient}")

#         # Get the start and end positions of the match
#         start, end = match.start(), match.end()

#         # print(f"Match: {match.group()} at positions {start}-{end}")

#         # Get key value pair in the conversions_map that corresponds to the current match and the new quantity values to sub in
#         conversions = conversions_map[match.group()]
#         # conversions = conversions_list[replacement_index]

#         # print(f"Conversions: {conversions}")

#         # starting_quantity = conversions["input_numbers"]
#         merged_quantity = conversions["quantities"]
#         merge_operation = conversions["merge_operation"] # add or multiply

#         # print(f"Starting quantity {starting_quantity}")
#         # print(f"Merged Quantity: {merged_quantity}") if self.debug else None

#         # Calculate the start and end positions in the modified string
#         modified_start = start + offset
#         modified_end = end + offset

#         # print(f" -> Modified match positions: {modified_start}-{modified_end}")
#         # print(f"Replacing {match.group()} with '{merged_quantity}'...")
        
#         # Construct the modified string with the replacement applied
#         self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(merged_quantity) + self.standardized_ingredient[modified_end:]
#         # ingredient = ingredient[:modified_start] + str(merged_quantity) + ingredient[modified_end:]

#         # Update the offset for subsequent replacements
#         offset += len(merged_quantity) - (end - start)
#         replacement_index += 1
#         # print(f" --> Output ingredient: \n > '{self.standardized_ingredient}'")

# ####### Deprecated ####### 
# def _parse_fractions(self):
#     """
#     Replace unicode and standard fractions with their decimal equivalents in the parsed ingredient.
#     """
#     # print("Parsing fractions")
#     # regex.MULTI_PART_FRACTIONS_PATTERN
#     # fractions = re.findall(regex.MULTI_PART_FRACTIONS_PATTERN, self.standardized_ingredient)
#     # fractions = re.findall(regex.MULTI_PART_FRACTIONS_PATTERN_AND, self.standardized_ingredient)

#     # finditer() method
#     fractions = re.finditer(_regex_patterns.MULTI_PART_FRACTIONS_PATTERN, self.standardized_ingredient)
#     # fractions = re.finditer(regex.MULTI_PART_FRACTIONS_PATTERN_AND, self.standardized_ingredient)

#     # Replace fractions in the original string with their sum based on match indices
#     # updated_ingredient = self.standardized_ingredient
#     offset = 0

#     for match in fractions:

#         # keep track of the offset to adjust the index of the match
#         start_index = match.start() + offset
#         end_index = match.end() + offset
#         matched_fraction = match.group()

#         print(f"Matched Fraction: {matched_fraction}")
#         # remove "and" and "&" from the matched fraction
#         matched_fraction = matched_fraction.replace("and", " ").replace("&", " ")

#         print(f"Matched Fraction after removing AND: {matched_fraction}")

#         # Parse the matched fraction, make sure it's in the correct format, to be able to be summed
#         parsed_fraction = self._parse_mixed_fraction(matched_fraction)

#         print(f"Parsed Fraction: {parsed_fraction}")

#         # Replace the matched fraction with the sum of the parse    d fraction
#         sum_fraction = self._sum_parsed_fractions(parsed_fraction)

#         print(f"Sum Fraction: {sum_fraction}")
#         # Insert the sum of the fraction into the updated ingredient string
#         # updated_ingredient = updated_ingredient[:start_index] + str(sum_fraction) + updated_ingredient[end_index:]
#         self.standardized_ingredient = self.standardized_ingredient[:start_index] + " " + str(sum_fraction) + self.standardized_ingredient[end_index:]

#         # Update the offset to account for the difference in length between the matched fraction and the sum of the fraction
#         offset += len(str(sum_fraction)) - len(matched_fraction)

# ####### Deprecated ####### 
# def _parse_mixed_fraction(self, fraction_str: str) -> list:
#     # Remove whitespace to the left and right of a slash
#     cleaned_fractions = re.sub(r'\s*/\s*', '/', fraction_str)

#     # print(f"Cleaned Fractions: {cleaned_fractions}")

#     # Define the regular expression pattern to match the mixed fraction
#     pattern = re.compile(r'\b(\d+)\s*(\d+/\d+)\b')
#     match = pattern.search(cleaned_fractions)
    
#     if match:
#         whole_number = match.group(1)
#         fraction = match.group(2)
#         return [whole_number, fraction]
#     else:
#         # If no match found, split the string based on space and return
#         return cleaned_fractions.split()
    
# ####### Deprecated ####### 
# def _sum_parsed_fractions(self, fraction_list: list, truncate = 3) -> float:
    
#     total = 0
#     for i in fraction_list:
#         total += Fraction(i)
    
#     return round(float(total), truncate)

# regex = IngredientTools()

# parenthesis = [ "(2 ounces)", 
#                 "(about 3 cups)",
#                 "(3)",
#                 "(3 ounces each)", 
#                 "(3 each)",
#                 "(about 4 cups each)", 
#                 "(about a couple of 3 tablespoons)", 
#                 "(3 ounces about)"
#                   ]
# regex.print_matches(parenthesis[3])