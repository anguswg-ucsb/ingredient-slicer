

from fractions import Fraction
from html import unescape
import re
import warnings
from typing import List, Dict, Any, Union, Tuple, Callable

from ingredient_slicer import _constants, _regex_patterns

# -----------------------------------------------------------------------------------------------
# ---- Utility functions for handling numbers, decimals, and fractions in strings ----
# -----------------------------------------------------------------------------------------------

def _make_int_or_float_str(number_str: str) -> str:
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

        # convert integer/float to string if it's not already a string
        if isinstance(number_str, (int, float)):
            number_str = str(number_str)

        number_str = number_str.replace(" ", "")

        # # NOTE: remove negative sign if it exists and replace whitespace
        # is_negative = False
        # if number_str[0] == "-":
        #     is_negative = True
        #     number_str = number_str[1:]
        #     number_str = number_str.replace(" ", "")

        period_count = 0

        for i in number_str:
            if i == ".":
                period_count += 1
            if not i.isdigit() and i != ".":
                raise ValueError("Invalid character in number. Only digits and periods are allowed.")
            
        if period_count > 1:
            raise ValueError("Invalid number format. Only one period is allowed in a number.")
        
        number = float(number_str.strip())  # Convert string to float

        if number == int(number):  # Check if float is equal to its integer value

            # f"-{str(int(number))}" if is_negative else str(int(number))

            return str(int(number))  # Return integer value if it's a whole number
        else:
            # f"-{str(number)}" if is_negative else str(number)

            return str(number)  # Return float if it's a decimal

# -----------------------------------------------------------------------------------------------
# ---- Convert a string fraction to a decimal (i.e. "1/2" -> "0.5") ----
# -----------------------------------------------------------------------------------------------

def _fraction_str_to_decimal(fraction_str: str) -> str:
        """
        Convert a string representation of a fraction to its decimal equivalent.
        Args:
            fraction_str (str): The string representation of the fraction. Must only contain digits, a forward slash, and possible whitespace. 
                                    Numbers must be separated by a forward slash. If a whole number string or a decimal string is passed, it will be returned as a string, 
                                    and converted to a whole number if values after the decimal point are only zeros (i.e. 1.0 -> 1, 2.0 -> 2, 3.00 -> 3).
        Returns:
            str: The decimal value of the fraction as a string. 
        """
        # FRACTION_PATTERN2 = re.compile(r'\d+(?:\.\d+|/\d+)')

        # fraction_str = "4/0.48"
        # fraction_str = "4/0.48"
        # FRACTION_PATTERN2.findall(fraction_str)
        # 4/0.48

        if not isinstance(fraction_str, str):
            raise ValueError("Invalid input. Fraction string must be a string.")

        # Split the fraction string into its numerator and denominator
        split_fraction = [i.strip() for i in fraction_str.split("/")]
        # print(f"Split Fraction: {split_fraction}") if self.debug else None

        # If the fraction is a whole number, return the number
        if len(split_fraction) == 1:
            # print(f"---> Only one part: {split_fraction[0]}")

            converted_number = _make_int_or_float_str(split_fraction[0])

            # print(f"---> OLD Output: {round(float(split_fraction[0]), 3)}")
            # print(f"---> NEW Output: {converted_number}")
            return converted_number
        
        # after returning cases of just a whole number or decimal number and returning that, 
        # we make sure all of our characters are valid 
        has_only_valid_chars = all([i.isdigit() or i in {"-", "/", " ", "."} for i in fraction_str])
        # has_only_valid_chars = all([i.isdigit() or i in {"-", "/", " "} for i in fraction_str])

        if not has_only_valid_chars:
            raise ValueError("Invalid input. Fraction string must contain only digits, hyphens, and a forward slash (possible invalid characters and/or periods?)")

        # # numerator = int(split_fraction[0])
        # # denominator = int(split_fraction[1])
        # numerator = int(float(split_fraction[0])) # TODO: This is being tested out
        # denominator = int(float(split_fraction[1]))
        # is_negative = True if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0) else False

        # Convert the fraction to a decimal
        # return round(float(Fraction(numerator, denominator)), 3)

        # decimal_value = round(float(Fraction(numerator, denominator)), 3)
        
        # converts the split up fraction list to a float
        decimal_value = round(_split_fraction_to_float(split_fraction), 3)

        is_negative   = True if decimal_value < 0 else False

        if is_negative:
            decimal_value = decimal_value * -1
            # decimal_value = decimal_value.replace("-", "")
        
        decimal_str = f"-{_make_int_or_float_str(str(decimal_value))}" if is_negative else _make_int_or_float_str(str(decimal_value))

        # return _make_int_or_float_str(str(round(float(Fraction(numerator, denominator)), 3)))
        return decimal_str

def _split_fraction_to_float(split_fraction: list) -> float:
    """
    Convert a split fraction to a float.
    Args:
        split_fraction (list): A list containing the numerator and denominator of a fraction.
    Returns:
        float: The float value of the fraction.
    """

    numerator_fraction =  Fraction(split_fraction[0])
    denominator_fraction = Fraction(split_fraction[1])

    return float(Fraction(numerator_fraction, denominator_fraction))

# TODO: Delete/Deprecated, this is the old version of the _fraction_str_to_decimal function above
def _fraction_str_to_decimal2(fraction_str: str) -> str:
        """
        Convert a string representation of a fraction to its decimal equivalent.
        Args:
            fraction_str (str): The string representation of the fraction. Must only contain digits, a forward slash, and possible whitespace. 
                                    Numbers must be separated by a forward slash. If a whole number string or a decimal string is passed, it will be returned as a string, 
                                    and converted to a whole number if values after the decimal point are only zeros (i.e. 1.0 -> 1, 2.0 -> 2, 3.00 -> 3).
        Returns:
            str: The decimal value of the fraction as a string. 
        """
        
        if not isinstance(fraction_str, str):
            raise ValueError("Invalid input. Fraction string must be a string.")

        # Split the fraction string into its numerator and denominator
        split_fraction = [i.strip() for i in fraction_str.split("/")]
        # print(f"Split Fraction: {split_fraction}") if self.debug else None

        # If the fraction is a whole number, return the number
        if len(split_fraction) == 1:
            converted_number = _make_int_or_float_str(split_fraction[0])
            return converted_number
        
        # remove trailing period if it exists
        if split_fraction[1][-1] == ".":
            split_fraction[1] = split_fraction[1][:-1]

        # after returning cases of just a whole number or decimal number and returning that, 
        # we make sure all of our characters are valid 
        has_only_valid_chars = all([i.isdigit() or i in {"-", "/", " ", "."} for i in fraction_str])
        # has_only_valid_chars = all([i.isdigit() or i in {"-", "/", " "} for i in fraction_str])

        if not has_only_valid_chars:
            raise ValueError("Invalid input. Fraction string must contain only digits, hyphens, and a forward slash (possible invalid characters and/or periods?)")

        numerator = int(split_fraction[0])
        denominator = int(split_fraction[1])
        # numerator = int(float(split_fraction[0])) # TODO: This is being tested out
        # denominator = int(float(split_fraction[1]))

        is_negative = True if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0) else False

        # Convert the fraction to a decimal
        # return round(float(Fraction(numerator, denominator)), 3)
        decimal_value = round(float(Fraction(numerator, denominator)), 3)

        if is_negative:
            decimal_value = decimal_value * -1
            # decimal_value = decimal_value.replace("-", "")
        
        decimal_str = f"-{_make_int_or_float_str(str(decimal_value))}" if is_negative else _make_int_or_float_str(str(decimal_value))

        # return _make_int_or_float_str(str(round(float(Fraction(numerator, denominator)), 3)))
        return decimal_str

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
# ---- Convert ALL fractions in a string to their decimal equivalent ----
# -----------------------------------------------------------------------------------------------

# TODO: Replace the _convert_fractions_to_decimals function defined in the IngredientSlicer class with this version
# NOTE: This is the NEW implementation of _convert_fractions_to_decimals and specifically deals with each fraction type
# NOTE: in a specific order and with a specific regex pattern to ensure the most accurate conversion
def _convert_fractions_to_decimals(ingredient: str) -> list:
        """
        Find all fractions in the parsed ingredient string.
        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            list: A list of all fractions found in the ingredient string.
        """

        if not isinstance(ingredient, str):
            raise ValueError("Invalid input. Ingredient must be a string.")

        # use the predefined order of FRACTION_TYPE_ORDER to iterate through the patterns in 
        # an order that will allow for the most accurate conversion (deals with decimal fractions first if they exist)
        for pattern_key in _regex_patterns.FRACTION_TYPE_ORDER:
        # for key, pattern in _regex_patterns.FRACTION_TYPE_MAP.items():
        # # for key, pattern in list(_regex_patterns.FRACTION_TYPE_MAP.items())[::-1]:
            pattern = _regex_patterns.FRACTION_TYPE_MAP[pattern_key]

            # match_fraction = pattern.findall(ingredient)
            match_fraction_iter = pattern.finditer(ingredient)

            offset = 0

            for match in match_fraction_iter:
                match_string    = match.group()
                start, end = match.start(), match.end()
                modified_start = start + offset
                modified_end = end + offset

                fraction_decimal = _fraction_str_to_decimal(match_string)

                ingredient = ingredient[:modified_start] + str(fraction_decimal) + ingredient[modified_end:]
                offset += len(str(fraction_decimal)) - (end - start)

        # # NOTE: trying the second loop implementation below will show why the order matters 
        # for key, pattern in _regex_patterns.FRACTION_TYPE_MAP.items():
        # # for key, pattern in list(_regex_patterns.FRACTION_TYPE_MAP.items())[::-1]: # NOTE: SHOWS WHY ORDER MATTERS

        return ingredient

# # NOTE: Old implementation of _convert_fractions_to_decimals 
# # NOTE: (this is roughly what was used in the IngredientSlicer class, relies mainly on correct matching from the FRACTION_PATTERN)
# def _convert_fractions_to_decimals2(ingredient: str) -> str:
#     """
#     Convert fractions in the parsed ingredient to their decimal equivalents.
#     """

#     # fraction_str = "1 to 1/2 cups, 2 and 5 animals, 2 2 / 4 cats, 1 and 1/22 cups water melon"
#     matches = _regex_patterns.FRACTION_PATTERN.findall(ingredient)
#     # matches = regex.FRACTION_PATTERN.findall(fraction_str)

#     # Replace fractions with their decimal equivalents
#     for match in matches:
#         # print(f"Match: {match}")

#         fraction_decimal = _fraction_str_to_decimal(match)
#         # print(f"Fraction Decimal: {fraction_decimal}") if self.debug else None
#         ingredient = ingredient.replace(match, str(fraction_decimal))

#     return ingredient

# -----------------------------------------------------------------------------------------------------------------------
# ---- Force whitespaces between an number followed by a character or vice versa (i.e. "1cup" -> "1 cup") ----
# -----------------------------------------------------------------------------------------------------------------------

def _force_ws_between_numbers_and_chars(ingredient: str) -> str:
    
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

    ingredient = NUMBERS_TO_LETTERS.sub(r"\1 \2", ingredient)
    ingredient = LETTERS_TO_NUMBERS.sub(r"\1 \2", ingredient)
    ingredient = LETTERS_DASH_NUMBERS.sub(r"\1 - \2", ingredient)

    return ingredient

# -----------------------------------------------------------------------------------------------
# ---- Standardize ranges (numbers separated by "-") so they all are the same form ----
# -----------------------------------------------------------------------------------------------

def _update_ranges(ingredient: str, pattern: re.Pattern) -> str:
        """Update the number ranges in the ingredient string to always have two numbers separated by a whitespace, then a hyphen, then another whitespace.
        Notes: Currently supports the following patterns in the IngredientTools class:
            - QUANTITY_DASH_QUANTITY
            - BETWEEN_QUANTITY_AND_QUANTITY
            - QUANTITY_TO_QUANTITY
            - QUANTITY_OR_QUANTITY
        Args:
            ingredient (str): The ingredient string to update
            pattern (re.Pattern): The pattern to use to find the ranges
        Returns:
            str: The updated ingredient string with all possible ranges updated to always 
                have 2 numbers separated by a whitespace, then a hyphen, then another whitespace.
        """

        matched_ranges_iter = pattern.finditer(ingredient)
        offset = 0

        for match in matched_ranges_iter:
            start, end = match.start(), match.end()
            modified_start = start + offset  # new start position
            modified_end = end + offset      # new end position
            match_string = match.group()

            # In the match string, replace all instances of "and", "&", "to", and "or" with hyphens
            match_string = match_string.replace("and", "-") \
                .replace("&", "-") \
                .replace("to", "-") \
                .replace("or", "-") \
                .replace("between", "").strip()
            
            updated_range = " - ".join([str(_fraction_str_to_decimal(i)) for i in match_string.split("-")])

            ingredient = ingredient[:modified_start] + updated_range + ingredient[modified_end:]

            # # Update the offset for subsequent replacements
            offset += len(str(updated_range)) - (end - start)
            
        return ingredient

# -----------------------------------------------------------------------------------------------
# ---- Merge/Fix any ranges that are not really ranges (i.e. "4-1/2" -> "4.5")
# -----------------------------------------------------------------------------------------------

def _merge_misleading_ranges(ingredient:str) -> str:
    """ Merge misleading ranges in the parsed ingredient (i.e. "4-1/2" is not a valid range, it should be "4.5" instead)"""

    # Find all the ranges in the ingredient
    range_iter = _regex_patterns.QUANTITY_DASH_QUANTITY_GROUPS.finditer(ingredient)

    offset = 0

    for match in range_iter:
        match_string    = match.group()
        start, end = match.start(), match.end()
        modified_start = start + offset
        modified_end = end + offset

        left_range = match.group(1).strip()
        right_range = match.group(2).strip()

        first_number  = float(_fraction_str_to_decimal(left_range).strip())
        second_number = float(_fraction_str_to_decimal(right_range).strip())

        # If the second number is less than the first number, then the range is misleading
        #  and the numbers should be merged (added if second number is a fraction)
        if second_number < first_number:
            # print(f"Fixing misleading range: {match_string} with ")
            second_number_is_fraction = second_number < 1
            multiply_or_add_str = "add" if second_number_is_fraction else "multiply"

            # print(f"Second number is a fraction: {second_number_is_fraction}\n > '{multiply_or_add_str}' {first_number} and {second_number}") if self.debug else None

            updated_value = f" {_make_int_or_float_str(str(first_number + second_number))} " if second_number_is_fraction else f" {_make_int_or_float_str(str(first_number * second_number))} "
            # updated_value = f" {_make_int_or_float_str(str(first_number + second_number))} "
            # print(f"Fixing misleading range: {match_string} with {updated_value}") if self.debug else None
            
            ingredient = ingredient[:modified_start] + updated_value + ingredient[modified_end:]
            offset += len(updated_value) - (end - start)

            # print(f"Ingredient after updating: {ingredient}") if self.debug else None

    ingredient = ingredient.strip()

    return ingredient

# -----------------------------------------------------------------------------------------------
# ---- Collapse ranges of numbers by averaging the values in the range ----
# -----------------------------------------------------------------------------------------------

def avg_ranges(ingredient: str) -> str:
    """
    Replace ranges of numbers with their average in the parsed ingredient.
    Examples:
    "1-2 oz" -> "1.5 oz"
    "1 - 2 ft" -> "1.5 ft"
    """

    if not isinstance(ingredient, str):
        raise ValueError("Invalid input. Ingredient must be a string.")

    # regex_patterns = _regex_patterns.IngredientTools()

    search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(ingredient)
    
    while search_ranges:
        start, end = search_ranges.start(), search_ranges.end()
        match_string = search_ranges.group()
        match_string = search_ranges.group()
            
        left_range, right_range = match_string.split("-")

        left_range = left_range.strip()
        right_range = right_range.strip()
        # left_range, right_range = map(str.strip, match_string.split("-"))

        first_number = float(_fraction_str_to_decimal(left_range))
        second_number = float(_fraction_str_to_decimal(right_range))
        
        range_average = _make_int_or_float_str(str((first_number + second_number) / 2))
        
        ingredient = ingredient[:start] + range_average + ingredient[end:]
        
        search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(ingredient)
    
    ingredient = ingredient.strip()
    
    return ingredient

# -----------------------------------------------------------------------------------------------
# ---- Replace leading "a" and "an" words if no quantities given ----
# -----------------------------------------------------------------------------------------------

def _replace_a_or_an_quantities(ingredient: str) -> str:
        """
        Replace "a" or "an" with "1" in the parsed ingredient if no number is present in the ingredient string.
        Args:
            ingredient (str): The ingredient string to parse.
        Returns:
            str: The updated ingredient string with "a" or "an" replaced with "1" if no other quantites are found.
        """

        if not isinstance(ingredient, str):
            raise ValueError("Invalid input. Ingredient must be a string.")

        # lowercase and split the ingredient string
        ingredient       = ingredient.lower()
        split_ingredient = ingredient.split()

        quantity_matches = re.findall(_regex_patterns.ALL_NUMBERS, ingredient)

        # if no quantities are found in the ingredient string, 
        # look for and replace the first "a" or "an" with "1"
        if not quantity_matches:
            
            # go and replace the first "a" or "an" with "1"
            for index, word in enumerate(split_ingredient):
                if set(word) == {"a"} or word == "an":
                    split_ingredient[index] = "1"
                    ingredient = " ".join(split_ingredient)
                    break

        # if (set(split_ingredient[0]) == {"a"} or split_ingredient[0] == "an") and not quantity_matches:
        #     split_ingredient[0] = "1"
        #     # ingredient = " ".join(split_ingredient)
        #     ingredient = " ".join(split_ingredient)

        return ingredient

# -----------------------------------------------------------------------------------------------
# ---- Substring finder and substring hyphen finder functions ----
# -----------------------------------------------------------------------------------------------

def _find_substring_indices(text: str, substring: str) -> list:

    """Find the start and end indices of a substring in a string
    Case insensitive, and will return all instances of the substring in the text string
    Args:
        text (str): The text to search for the substring
        substring (str): The substring to search for in the text
    Returns:
        list: A list of lists containing the start and end indices of the substring
    """

    text = text.lower()
    substring = substring.lower()

    substring_length = len(substring)

    L = 0
    substring_indices = []

    for R in range(0, len(text)):
        if R - L == substring_length:
            if text[L:R] == substring:
                substring_indices.append([L, R])
            L += 1
            
    return substring_indices

def _find_and_remove_hyphens_around_substring(text: str, substring: str) -> str:

    """Find instances of a substring surrounded by some number of hyphens on the left or right of the substring and remove these hyphens
    Case insensitive, and will return the updated string with the hyphens removed from around the substring and in lower case
    Args:
        text (str): The text to search for the substring
        substring (str): The substring to search for in the text
    Returns:
        str: The updated text with the hyphens removed from around the substring
    """

    # substrings_to_fix = ["to", "or", "and"]
    # substring = "to"
    # text = '1 to- 4.5 cups of sugar'

    text = text.lower()
    substring = substring.lower().replace("-", "")

    substring_length = len(substring)

    L = 0
    substring_indices = []
    hypen_substrings = []

    for R in range(0, len(text)):

        if R - L == substring_length:
            # print(f"Found window the size of substring!") if debug else None
            if text[L:R] == substring:
                substring_indices.append([L, R])
                
                has_left_hyphen = False
                has_right_hyphen = False

                char_to_left = text[L - 1] if L - 1 >= 0 else None
                char_to_right = text[R] if R < len(text) else None
                
                # character to the left or right of the substring is 
                # a digit, hyphen, or whitespace or is at the beginning/end of the string
                valid_left_char  = char_to_left is None or char_to_left.isdigit() or char_to_left == "-" or char_to_left == " "
                valid_right_char = char_to_right is None or char_to_right.isdigit() or char_to_right == "-" or char_to_right == " "

                # character to the left or right of the substring is NOT a digit, hyphen, or whitespace 
                # (i.e. the matched substring is part of a larger word)
                if not valid_left_char or not valid_right_char:
                    L += 1
                    continue

                # look LEFT of the matched substring
                GO_LEFT_INDEX = L - 1

                # print(f"Try to go LEFT of '{substring}' substring") if debug else None
                while GO_LEFT_INDEX >= 0 and (text[GO_LEFT_INDEX] == " " or text[GO_LEFT_INDEX] == "-"):
                    if text[GO_LEFT_INDEX] == "-":
                        has_left_hyphen = True
                    GO_LEFT_INDEX -= 1
                
                # look RIGHT of the matched substring

                GO_RIGHT_INDEX = R

                while GO_RIGHT_INDEX < len(text) and (text[GO_RIGHT_INDEX] == " " or text[GO_RIGHT_INDEX] == "-"):

                    if text[GO_RIGHT_INDEX] == "-":
                        has_right_hyphen = True
                    GO_RIGHT_INDEX += 1

                look_around_string = text[GO_LEFT_INDEX+1:GO_RIGHT_INDEX]

                if has_left_hyphen or has_right_hyphen:
                    hypen_substrings.append(look_around_string)
            L += 1

    for hyphen_substring in hypen_substrings:
        replacement_string = f" {hyphen_substring.replace('-', '').replace(' ', '')} " 
        text = text.replace(hyphen_substring, replacement_string) 

    text = text.strip()

    return text

# -----------------------------------------------------------------------------------------------
# ---- Set of simple replacement functions for replacing words in strings ----
# -----------------------------------------------------------------------------------------------

def _replace_and_with_hyphen(match):
    # Replace "and" and "&" with hyphens
    return match.replace("and", "-").replace("&", "-")
    
def _replace_to_or_with_hyphen(match):
    # Replace "and" and "&" with hyphens
    return match.replace("to", "-").replace("or", "-")

def _replace_to_with_hyphen(match):
    # Replace "to" with hyphen
    return match.replace("to", "-")

def _replace_or_with_hyphen(match):
    # Replace "or" with hyphen
    return match.replace("or", "-")

# replace all instances of multiple hypens (which can be separated by whitespaces) in a string with a single hypen
def replace_multiple_hyphens(string: str) -> str:
    return re.sub(r'[-\s]+', '-', string)

# -----------------------------------------------------------------------------------------------
# ---- Removes any extrawhitespaces from a string makes the string single spaced ----
# -----------------------------------------------------------------------------------------------

def _remove_extra_whitespaces(input_string: str) -> str:
    """Remove extra whitespaces from a string and return the string with only single whitespaces."""
    # ingredient = re.sub(r'\s+', ' ', ingredient).strip() # remove any extra whitespace
    return " ".join(input_string.split())

# -----------------------------------------------------------------------------------------------
# ---- Functions for parsing parenthesis content / quantity unit regex functions ----
# -----------------------------------------------------------------------------------------------
def _extract_quantities_only(input_string: str) -> list:

    """From a string get all quantities if they exist WITHOUT units
    Useful for just getting quantities if there are no units associated with them (e.g. "chicken breast (5)")
    Args:
        input_string (str): The string to parse
    Returns:
        list: A list of quantities
    """
    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    # regex_patterns = _regex_patterns.IngredientTools()

    # first check for units
    unit_matches = _regex_patterns.UNITS_PATTERN.findall(input_string)

    # if we have units we just return because we only are looking for instances where quantities exist WITHOUT units
    if unit_matches:
        return []

    # regex_patterns.QUANTITY_UNIT_GROUPS.findall(input_string)
    quantity_matches = _regex_patterns.ALL_NUMBERS.finditer(input_string)
    quantities = _regex_patterns.ALL_NUMBERS.findall(input_string)

    # quantity_matches = _regex_patterns.ALL_NUMBERS.finditer(input_string)
    # quantities = []
    # for match in quantity_matches:
    #     match_string = match.group()
    #     start, end = match.start(), match.end()
    #     quantities.append(match_string)

    return quantities

def _extract_quantity_unit_pairs(input_string: str) -> list[tuple]:

    """From a string get all sets of quantity/units
    Useful for getting quantity/units pairings from a string (e.g. "1 cup of chopped chicken breast")
    Args:
        input_string (str): The string to parse
    Returns:
        list: A list of tuples containing the quantity and unit
    """
    
    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    # regex_patterns = _regex_patterns.IngredientTools()

    # regex_patterns.QUANTITY_UNIT_GROUPS.findall(input_string)
    quantity_matches = _regex_patterns.ALL_NUMBERS.finditer(input_string)

    quantity_unit_pairs = []

    for match in quantity_matches:
        match_string = match.group()
        start, end = match.start(), match.end()

        current_result = []
        current_result.append(match_string)

        str_after_number_match = input_string[end:]
        # print(f"String after number match: '{str_after_number_match}'")

        # _regex_patterns.ALL_NUMBERS.findall(after_approx_match)
        nearest_unit_search = _regex_patterns.UNITS_PATTERN.search(str_after_number_match)

        if not nearest_unit_search:
            continue

        closest_unit = nearest_unit_search.group()

        current_result.append(closest_unit)
        quantity_unit_pairs.append(tuple(current_result))
    
    return quantity_unit_pairs
    # return [tuple(i) for i in quantity_unit_pairs]

def _extract_equivalent_quantity_units(input_string: str) -> list[tuple]:

    """From a string get all sets of quantity/units preceeded by "approximate" strings, (e.g. "about", "approximately", "around", etc.)
    
    Useful for getting instances where there is a quantity and unit in parenthesis that is 
    an approximation of the quantity and unit in the main ingredient string (e.g. "1 cup of chopped chicken breast (about 12 ounces)")

    Args:
        input_string (str): The string to parse
    Returns:
        list: A list of tuples containing the (approximate string, quantity, and unit)
    """

    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(12 tender and juicy ounces or 14 grams about)'

    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    # regex_patterns = _regex_patterns.IngredientTools()

    approximate_string_matches = _regex_patterns.APPROXIMATE_STRINGS_PATTERN.finditer(input_string)

    approximate_triplets = []

    for match in approximate_string_matches:
        match_string = match.group()
        start, end = match.start(), match.end()

        # print(f"Match String: '{match_string}'")
        # print(f"Start: {start} | End: {end}")
        # print(f"Input String: '{input_string}'")
        current_result = []
        
        current_result.append(match_string) # add the approximate string to the result

        str_after_approx_match = input_string[end:] # string after the approximate match

        # _regex_patterns.ALL_NUMBERS.findall(after_approx_match)
        nearest_number_search = _regex_patterns.ALL_NUMBERS.search(str_after_approx_match) # search for the nearest number after the approximate string

        if not nearest_number_search:
            # print(f"No number found after approximate match")
            continue

        closest_number = nearest_number_search.group() # the actual matching number string
        # print(f"Closest Number: '{closest_number}'")
        current_result.append(closest_number) # add the number to the result
        
        # string after the number 
        str_after_number_match = str_after_approx_match[nearest_number_search.end():] # string after the number match

        nearest_unit_search = _regex_patterns.UNITS_PATTERN.search(str_after_number_match) # search for the nearest unit after the number

        if not nearest_unit_search: # if we don't find a unit after the number, we skip this triplet
            # print(f"No unit found after approximate match")
            continue

        closest_unit = nearest_unit_search.group() # the actual matching unit string
        # print(f"Closest Unit: '{closest_unit}'")

        current_result.append(closest_unit) # add the unit to the result
        # approximate_triplets.append(current_result) # add the triplet to the list of approximate triplets
        approximate_triplets.append(tuple(current_result)) # add the triplet to the list of approximate triplets
    

    # look for trailing approximate strings
    trailing_approx_strings = _regex_patterns.APPROXIMATE_STRINGS_PATTERN.findall(input_string)

    # if we didn't get any [approximate, quantity, unit] triplets, but we did get a trailing approximate strings
    # check the string again for quantity unit pairs and 
    # add the trailing approximate string to the beginning of each pair
    # This will help handle the following case:
    #       "(12 ounces approximately)"
    if not approximate_triplets and trailing_approx_strings:
        # print(f"Trailing Approximate Strings: {trailing_approx_strings}")
        trailing_approx_string = trailing_approx_strings[0]
        
        quantity_unit_pairs = _extract_quantity_unit_pairs(input_string)

        for pair in quantity_unit_pairs:
            new_triplet = (trailing_approx_string, pair[0], pair[1])
            approximate_triplets.append(new_triplet)
            # pair.append(trailing_approx_string)
        # [i.append(trailing_approx_string) for i in quantity_unit_pairs]
        # print()
    
    # return [tuple(i) for i in approximate_triplets]
    return approximate_triplets

def _is_approximate_quantity_only_parenthesis(input_string: str) -> bool:
    """Check if a string is an approximate quantity only parenthesis (e.g. "(about 12)")"""

    # input_string = "(about 4)"
    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(juicy about or 14)'
    # input_string = '(12 tender and juicy ounces or 14 grams about)'

    if not isinstance(input_string, str):
        return False

    approximate_string_matches = _regex_patterns.APPROXIMATE_STRINGS_PATTERN.findall(input_string)
    quantity_matches           = _regex_patterns.ALL_NUMBERS.findall(input_string)
    unit_matches               = _regex_patterns.UNITS_PATTERN.findall(input_string)

    has_approximate_string = True if approximate_string_matches else False
    has_quantity           = True if quantity_matches else False
    has_unit               = True if unit_matches else False

    if has_unit:
        return False
    
    approximate_and_quantity_only = has_approximate_string and has_quantity

    return approximate_and_quantity_only

def _extract_equivalent_quantity_only(input_string: str) -> list[tuple]:

    """From a string get all sets of quantity/units preceeded by "approximate" strings, (e.g. "about", "approximately", "around", etc.)
    
    Useful for getting instances where there is a quantity and unit in parenthesis that is 
    an approximation of the quantity and unit in the main ingredient string (e.g. "1 cup of chopped chicken breast (about 12 ounces)")

    Args:
        input_string (str): The string to parse
    Returns:
        list: A list of tuples containing the (approximate string, quantity, and unit)
    """

    # input_string = parenthesis
    # input_string = "(about 4)"
    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(juicy about or 14)'
    # input_string = '(12 tender and juicy ounces or 14 grams about)'

    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    # regex_patterns = _regex_patterns.IngredientTools()

    approximate_string_matches = _regex_patterns.APPROXIMATE_STRINGS_PATTERN.finditer(input_string)
    
    unit_matches = _regex_patterns.UNITS_PATTERN.findall(input_string)
    has_units = True if unit_matches else False

    if has_units:
        return []

    approximate_triplets = []

    for match in approximate_string_matches:
        match_string = match.group()
        start, end = match.start(), match.end()

        # print(f"Match String: '{match_string}'")
        # print(f"Start: {start} | End: {end}")
        # print(f"Input String: '{input_string}'")
        current_result = []
        
        current_result.append(match_string) # add the approximate string to the result

        str_after_approx_match = input_string[end:] # string after the approximate match

        # _regex_patterns.ALL_NUMBERS.findall(after_approx_match)
        nearest_number_search = _regex_patterns.ALL_NUMBERS.search(str_after_approx_match) # search for the nearest number after the approximate string

        if not nearest_number_search:
            # print(f"No number found after approximate match")
            continue

        closest_number = nearest_number_search.group() # the actual matching number string
        # print(f"Closest Number: '{closest_number}'")
        current_result.append(closest_number) # add the number to the result
        
        # string after the number 
        str_after_number_match = str_after_approx_match[nearest_number_search.end():] # string after the number match

        nearest_unit_search = _regex_patterns.UNITS_PATTERN.search(str_after_number_match) # search for the nearest unit after the number

        if not nearest_unit_search: # if we don't find a unit after the number, we skip this triplet
            # print(f"No unit found after approximate match")
            continue

        closest_unit = nearest_unit_search.group() # the actual matching unit string
        # print(f"Closest Unit: '{closest_unit}'")

        current_result.append(closest_unit) # add the unit to the result
        # approximate_triplets.append(current_result) # add the triplet to the list of approximate triplets
        approximate_triplets.append(tuple(current_result)) # add the triplet to the list of approximate triplets
    

    # look for trailing approximate strings
    trailing_approx_strings = _regex_patterns.APPROXIMATE_STRINGS_PATTERN.findall(input_string)

    # if we didn't get any [approximate, quantity, unit] triplets, but we did get a trailing approximate strings
    # check the string again for quantity unit pairs and 
    # add the trailing approximate string to the beginning of each pair
    # This will help handle the following case:
    #       "(12 ounces approximately)"
    if not approximate_triplets and trailing_approx_strings:
        # print(f"Trailing Approximate Strings: {trailing_approx_strings}")
        trailing_approx_string = trailing_approx_strings[0]
        
        quantity_unit_pairs = _extract_quantity_unit_pairs(input_string)

        for pair in quantity_unit_pairs:
            new_triplet = (trailing_approx_string, pair[0], pair[1])
            approximate_triplets.append(new_triplet)
            # pair.append(trailing_approx_string)
        # [i.append(trailing_approx_string) for i in quantity_unit_pairs]
        # print()
    
    # return [tuple(i) for i in approximate_triplets]
    return approximate_triplets


# pattern = regex_patterns.QUANTITY_DASH_QUANTITY
# replacement_function=None

# TODO: Deprecated --> DELETE
def _fractions_to_decimals(input_string) -> str:
    """
    Replace fractions with their decimal equivalents in a string.
    Args:
        input_string (str): The string to replace fractions in.
    Returns:
        str: The updated string with fractions replaced by their decimal equivalents.
    """
    fraction_pattern = re.compile(r'\d*\s*/\s*\d+')  # regex pattern for fractions
    # print("Parsing fractions")
    fractions = re.findall(fraction_pattern, input_string)

    split_frac = [i.replace(" ", "").split("/") for i in fractions]
    split_frac = [(int(f[0]), int(f[1])) for f in split_frac]
    fraction_decimal = [round(float(Fraction(f[0], f[1])), 3) for f in split_frac]

    # replace fractions in original string with decimal equivalents
    for i, f in enumerate(fractions):
        input_string = input_string.replace(f, str(fraction_decimal[i]))

    return input_string

def _extract_parenthesis(ingredient: str) -> str:

    """Extract the content of the parenthesis in an ingredient string.
    Stack based approach to extract the content of the parenthesis in an ingredient string, probably deprecated...
    """
    if not _is_valid_parenthesis(ingredient):
        # print(f"Invalid parenthesis: {ingredient}")
        # cleaned_ingredient = ingredient.replace("(", "").replace(")", "")
        # cleaned_ingredient = cleaned_ingredient.strip()
        # cleaned_ingredient = _remove_extra_whitespaces(cleaned_ingredient)
        return ingredient, []
    
    stack = []
    parenthesis_list = []

    for i, char in enumerate(ingredient):

        if stack and stack[-1] == ")":

            stack.pop()
            parenthesis = []

            while stack and stack[-1] != "(":
                popped_char = stack.pop()
                parenthesis.append(popped_char)
            parenthesis = "".join(parenthesis[::-1])
            parenthesis_list.append(parenthesis)
            stack.pop()

        stack.append(char)
    
    return ["".join(stack), parenthesis_list]

# ingredient = "1 rice with (2 cups of (444) water) and (another) (())love"
# _extract_parenthesis(ingredient) # output: ['1 rice with  and  love', ['444', '2 cups of  water', 'another', '', '']]

def _split_by_parenthesis(ingredient: str) -> list:
    """ Split an ingredient string by parenthesis and return the cleaned ingredient and the content of the parenthesis.
    If the parenthesis is invalid, return the original ingredient string. and an empty list.
    If there are valid parenthesis, the function pulls out the parenthesis and unnests any nested parenthesis within 
    those parenthesis, it will the return the ingredient with the parenthesis extracted and 
    a list of the unnested parenthesis content.
    Args:
        ingredient (str): The ingredient string to split by parenthesis.
    Returns:
        list: A list containing the cleaned ingredient and a list of the content of the parenthesis.
    """

    if not isinstance(ingredient, str):
        raise ValueError("Invalid input. Ingredient must be a string.")

    if not _is_valid_parenthesis(ingredient):
        # print(f"Invalid parenthesis: {ingredient}")
        cleaned_ingredient = ingredient.replace("(", "").replace(")", "")
        cleaned_ingredient = cleaned_ingredient.strip()
        cleaned_ingredient = _remove_extra_whitespaces(cleaned_ingredient)
        return [cleaned_ingredient, []]

    stack = []
    parenthesis_list = []

    nested_level = 0
    cleaned_ingredient = []

    for char in ingredient:
        if char == '(':
            nested_level += 1
            if nested_level > 1:
                cleaned_ingredient.append(char)
        elif char == ')':
            if nested_level > 1:
                cleaned_ingredient.append(char)
            nested_level -= 1
            if nested_level == 0:
                parenthesis = []
                while stack:
                    parenthesis.append(stack.pop())
                parenthesis_list.append(''.join(parenthesis[::-1]))
        elif nested_level == 0:
            cleaned_ingredient.append(char)
        elif nested_level > 0:
            stack.append(char)

    cleaned_ingredient = ''.join(cleaned_ingredient)

    cleaned_ingredient = cleaned_ingredient.replace("(", "").replace(")", "")
    cleaned_ingredient = cleaned_ingredient.strip()
    cleaned_ingredient = _remove_extra_whitespaces(cleaned_ingredient)

    parenthesis_list = [_remove_extra_whitespaces(p.replace("(", "").replace(")", "").strip()) for p in parenthesis_list]
    # parenthesis_list = [p for p in parenthesis_list if p]

    return [cleaned_ingredient, parenthesis_list]

def _is_valid_parenthesis(string: str) -> bool:
    if not isinstance(string, str):
        raise ValueError("Invalid input. Ingredient must be a string.")
    
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0

def _remove_parenthesis_from_str(ingredient: str) -> str:
    """Remove parenthesis and their content from an ingredient string.
    Args:
        ingredient (str): The ingredient string to remove parenthesis from.
    Returns:
        str: The ingredient string with the parenthesis removed.
    """

    if not isinstance(ingredient, str):
        raise ValueError("Invalid input. Ingredient must be a string.")

    MATCH_PARENTHESIS = re.compile(r'\([^()]*\)|\[[^][]*]|[{}]')
    while MATCH_PARENTHESIS.search(ingredient):  # While regex matches the string
        ingredient = MATCH_PARENTHESIS.sub('', ingredient)  # Remove the matches

    ingredient = ingredient.replace("(", "").replace(")", "").strip()
    ingredient = _remove_extra_whitespaces(ingredient)
    return ingredient.strip()


def _find_and_remove(string: str, pattern: re.Pattern) -> str:
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
        
        string = string.strip()

        return string

def _find_and_replace_casual_quantities(ingredient: str) -> str:
    """
    Find and replace matches of CASUAL_QUANTITIES_PATTERN with the key from the CASUAL_QUANTITIES dictionary
    """

    offset = 0
    pattern_iter = _regex_patterns.CASUAL_QUANTITIES_PATTERN.finditer(ingredient)

    for match in pattern_iter:
        match_string    = match.group()

        # Get the start and end of the match and the modified start and end positions given the offset
        start, end = match.start(), match.end()
        modified_start = start + offset
        modified_end = end + offset

        replacement_str = _constants.CASUAL_QUANTITIES[match_string] 

        # Construct the modified string with the replacement applied
        ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]

        # Update the offset for subsequent removals 
        offset += len(str(replacement_str)) - (end - start)

    return ingredient

def _find_and_replace_prefixed_number_words(ingredient: str) -> str:
    """ Replace prefixed number words with their corresponding numerical values in the parsed ingredient 
    Strings like "twenty five" are replaced with "25", or "thirty-two" is replaced with "32"

    """
    number_words_iter = _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.finditer(ingredient)

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
            ingredient = ingredient[:modified_start] + str(combined_value) + ingredient[modified_end:]
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

    return ingredient

def _find_and_replace_number_words(ingredient:str) -> str:
    """
    Replace number words with their corresponding numerical values in the parsed ingredient.
    """

    # print("Parsing number words")
    for word, regex_data in _regex_patterns.NUMBER_WORDS_MAP.items():
        pattern = regex_data[1]
        # print statement if word is found in ingredient and replaced
        if pattern.search(ingredient):
            ingredient = pattern.sub(regex_data[0], ingredient)
    
    return ingredient

def _clean_html_and_unicode(ingredient: str) -> str:
    """Unescape fractions from HTML code coded fractions to unicode fractions."""

    # Unescape HTML
    ingredient = unescape(ingredient)

    # Replace unicode fractions with their decimal equivalents
    for unicode_fraction, decimal_fraction in _constants.UNICODE_FRACTIONS.items():
        ingredient = ingredient.replace(unicode_fraction, f" {decimal_fraction}")

    return ingredient

# def replace_number_followed_by_inch_symbol(ingredient: str) -> str:
#     """Replace numbers followed by the inch symbol with the word 'inch' in the ingredient string.
#     Args:
#         ingredient (str): The ingredient string to parse.
#     Returns:
#         str: The updated ingredient string with numbers followed by the inch symbol replaced with the word 'inch'.
#     """
#     if not isinstance(ingredient, str):
#         raise ValueError("Invalid input. Ingredient must be a string.")

#     # regex_patterns = _regex_patterns.IngredientTools()
#     # NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\"')

#     # Find all numbers followed by the inch symbol in the ingredient string
#     matches = _regex_patterns.NUMBER_WITH_INCH_SYMBOL.finditer(ingredient)
#     matches = NUMBER_WITH_INCH_SYMBOL.finditer(ingredient)

#     # Replace all numbers followed by the inch symbol with the word 'inch'
#     for match in matches:
#         match_string = match.group()
#         ingredient = ingredient.replace(match_string, "inch")

#     return ingredient

def _replace_number_followed_by_inch_symbol(ingredient: str ) -> str:
    """
    Find inch symbols (i.e. " or ”) in the ingredient string and replace them with the word "inch".
    """

    # ingredient = "fruit (4-2/3” long x 2-3/4” dia)"
    # ingredient = 'waffle round (4 " dia)'

    for key, pattern in _regex_patterns.NUMBER_WITH_INCH_SYMBOL_MAP.items():
        pattern_iter = pattern.finditer(ingredient)
        
        offset = 0
        for match in pattern_iter:
            match_string = match.group()
            start, end = match.start(), match.end()
            modified_start = start + offset
            modified_end = end + offset

            replacement_str = match_string.replace(key, "inch")

            ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]

            offset += len(str(replacement_str)) - (end - start)

    return ingredient

def _extract_dimensions(ingredient: str) -> list[str, list[str]]:
    """Extract dimension units from an ingredient string.
    Args:
        ingredient (str): The ingredient string to parse.
    Returns:
        list: A list containing the updated ingredient string with the dimension units removed and a list of the dimension units strings.
    """
    # ingredient = 'fruit (4.67inch long x 2.75inch dia)'
    dimension_units = []
    for dimension_unit, pattern in _regex_patterns.QUANTITY_WITH_DIMENSION_UNITS_MAP.items():
        # print(f"Dimension Unit: {dimension_unit}")

        # match_iter = pattern.finditer(ingredient)
        matches = pattern.findall(ingredient)
        # print(f"Matches: {matches}")

        if matches:
            # print(f"Finding and removing {matches} from ingredient")
            ingredient = _find_and_remove(ingredient, pattern)
            dimension_units.extend(matches)
        
        # print(f"Ingredient: {ingredient}\nDimension Units: {dimension_units}\n")

    return [ingredient, dimension_units]

# def _extract_dimensions(ingredient: str) -> list[str, list[str]]:
#     """Extract dimension units from an ingredient string.
#     Args:
#         ingredient (str): The ingredient string to parse.
#     Returns:
#         list: A list containing the updated ingredient string with the dimension units removed and a list of the dimension units strings.
#     """
#     # ingredient = 'fruit (4.67inch long x 2.75inch dia)'
#     dimension_units = []
#     for dimension_unit, pattern in _regex_patterns.QUANTITY_WITH_DIMENSION_UNITS_MAP.items():
#         # print(f"Dimension Unit: {dimension_unit}")

#         # match_iter = pattern.finditer(ingredient)
#         matches = pattern.findall(ingredient)
#         # print(f"Matches: {matches}")

#         if matches:
#             # print(f"Finding and removing {matches} from ingredient")
#             ingredient = _find_and_remove(ingredient, pattern)
#             dimension_units.extend(matches)
        
#         # print(f"Ingredient: {ingredient}\nDimension Units: {dimension_units}\n")

#     return [ingredient, dimension_units]

def _split_dimension_ranges(ingredient: str) -> list[str, list[str]]:
    """Split an ingredient string by any quantity dimension unit separated by an 'by' character.
    (i.e. "2 steaks, 3 inches by 4 inches thick" -> ("2 steaks, thick", "3 inches by 4 inches")
    
    Args:
        ingredient (str): The ingredient string to parse.
    Returns:
        list[str]: A list containing the updated ingredient string with the range removed and a list of the dimension units strings.
    """

    quantity_unit_by_range_iter = _regex_patterns.DIMENSION_RANGES.finditer(ingredient)

    dimension_units = []

    for match in quantity_unit_by_range_iter:
        # original string matched by the pattern (used for replacement)
        original_string = match.group(0)

        # quantities from first quantity/unit pair
        quantity1 = match.group(1)
        unit1     = match.group(2)

        # quantities from second quantity/unit pair
        quantity2 = match.group(3)
        unit2     = match.group(4)

        unit1_is_dimension = unit1 in _constants.DIMENSION_UNITS_SET
        unit2_is_dimension = unit2 in _constants.DIMENSION_UNITS_SET

        if unit1_is_dimension and unit2_is_dimension:
            # print(f"Both units are dimensions")
            # ingredient = _find_and_remove(ingredient, pattern)
            dimension_units.append(original_string)
            ingredient = ingredient.replace(original_string, "")

    return [ingredient, dimension_units]

def _split_single_unit_dimension_ranges(ingredient: str) -> list[str]:
    """Split an ingredient string by any quantity dimension unit separated by an 'by' character.
    (i.e. "2 steaks, 3 inches by 4 inches thick" -> ("2 steaks, thick", "3 inches by 4 inches")
    
    Args:
        ingredient (str): The ingredient string to parse.
    Returns:
        list[str]: A list containing the updated ingredient string with the range removed and a list of the dimension units strings.
    """

    # ingredient = "2 steaks, 3 x 4 inches thick"
    single_dimension_unit_iter = _regex_patterns.SINGLE_DIMENSION_UNIT_RANGES.finditer(ingredient)

    dimension_units = []

    for match in single_dimension_unit_iter:
        # original string matched by the pattern (used for replacement)
        original_string = match.group(0)

        # quantities from first quantity/unit pair
        quantity1 = match.group(1)
        # unit1     = match.group(2)

        # quantities from second quantity/unit pair
        quantity2 = match.group(2)
        unit2     = match.group(3)

        # unit1_is_dimension = unit1 in _constants.DIMENSION_UNITS_SET
        unit2_is_dimension = unit2 in _constants.DIMENSION_UNITS_SET

        if unit2_is_dimension:
            # print(f"---> Second unit is dimension!!!")
            # ingredient = _find_and_remove(ingredient, pattern)
            dimension_units.append(original_string)
            ingredient = ingredient.replace(original_string, "")

        # print()

    return [ingredient, dimension_units]

def _separate_dimensions(ingredient: str) -> str:
    """
    Split dimension unit ranges in the ingredient string.
    Examples:
    "2 steaks, 3 inches x 4 inches thick" -> ["2 steaks, thick", ["3 inches x 4 inches"]]
    """

    ingredient, dimension_ranges1 = _split_dimension_ranges(ingredient)
    ingredient, dimension_ranges2 = _split_single_unit_dimension_ranges(ingredient)
    ingredient, dimensions_with_number = _extract_dimensions(ingredient)

    dimensions = dimension_ranges1 + dimension_ranges2 + dimensions_with_number

    ingredient = _remove_extra_whitespaces(ingredient)

    return [ingredient, dimensions]

def _remove_x_separators(ingredient: str) -> str:
    """
    Remove "x" separators from the ingredient string and replace with whitespace
    Examples:
        >>> _removed_x_separators("1x2 cups")
        '1 2 cups'
        >>> _remove_x_separators("5 x cartons of eggs")
        "5   cartons of eggs"
    """
    # ingredient = "5 x cartons of eggs (3 x 4 inches)"

    def replace_x(match):
        return match.group().replace('x', ' ').replace('X', ' ')

    # Replace "x"/"X" separators with whitespace
    ingredient = _regex_patterns.X_AFTER_NUMBER.sub(replace_x, ingredient)

    return ingredient

def _remove_repeat_units_in_ranges(ingredient) -> str:
    """
    Remove repeat units in a range of quantities from an ingredient string.
    Examples:
    "2 oz - 3 oz diced tomatoes" -> "2 - 3 oz diced tomatoes"
    "3cups-4 cups of cat food" -> "3 - 4 cups of cat food"
    """
    
    ingredient = ingredient.lower()

    # get any strings that match the pattern 1<unitA> - 2<unitA> or 1<unitA> - 2<unitB>
    repeat_unit_matches = _regex_patterns.QUANTITY_UNIT_DASH_QUANTITY_UNIT.finditer(ingredient)
    # repeat_unit_matches = _regex_patterns.REPEAT_UNIT_RANGES.finditer(ingredient) # NOTE: old regex pattern (riskier)

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
            ingredient = ingredient.replace(original_string, f"{quantity1} - {quantity2} {unit1}")

    return ingredient 


def _get_gram_weight(food:str, quantity:str, unit:str, method:str = "dice") -> dict:

    """ Get the gram weight of a given quantity of food item.
    Args:
        food (str): The food item to convert.
        quantity (Union[str, int, float]): The quantity of the food item.
        unit (str): The unit of measurement for the quantity.
    Returns:
        dict: A dictionary containing the gram weight, maximum gram weight, and minimum gram weight.
    """

    if not unit:
        return {
            "gram_weight" : None,
            "min_gram_weight" : None,
            "max_gram_weight" : None
        }

    if quantity is None:
        quantity = "1"

    # ValueError checks
    if not isinstance(food, str):
        raise ValueError("'food' must be a string")

    if not isinstance(method, str):
        raise ValueError("'method' must be a string")

    method = method.lower()

    if method not in ["levenshtein", "jaccard", "dice"]:
        raise ValueError("Invalid 'method'. Options are 'levenshtein', 'jaccard', or 'dice'.")
    
    if not isinstance(quantity, (str, int, float)):
        raise ValueError("'quantity' must be a string, integer, or float")
    
    # if unit is not None and not isinstance(unit, str):
    if not isinstance(unit, str):
        raise ValueError("'unit' must be a string")

    quantity = float(quantity)
    
    gram_weight     = None
    min_gram_weight = None
    max_gram_weight = None
    
    # if unit:
    unit = unit.lower()
    
    unit_is_weight = unit in _constants.WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT
    unit_is_volume = unit in _constants.VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT

    # weight check
    if unit_is_weight:
        gram_weight = _convert_weights_to_grams(quantity, unit)

        return {
            "gram_weight" : str(round(gram_weight, 2)) if gram_weight else None,
            "min_gram_weight" : str(round(min_gram_weight, 2)) if min_gram_weight else None,
            "max_gram_weight" : str(round(max_gram_weight, 2)) if max_gram_weight else None
            }
    
    # volume check
    if unit_is_volume:
        gram_values_map = _convert_volume_to_grams(food, quantity, unit, method)  

        return {
            "gram_weight" : str(round(gram_values_map["gram_weight"], 2)) if gram_values_map["gram_weight"] else None,
            "min_gram_weight" : str(round(gram_values_map["min_gram_weight"], 2)) if gram_values_map["min_gram_weight"] else None,
            "max_gram_weight" : str(round(gram_values_map["max_gram_weight"], 2)) if gram_values_map["max_gram_weight"] else None
            }

    # if not unit or unit is None or (not unit_is_weight and not unit_is_volume):
    #     print(f"Attempting to get gram weights for single item...\n > food: '{food}'\n > quantity: '{quantity}'\n > unit: '{unit}'\n > gram_weight: '{gram_weight}'")
    #     gram_weight = _get_single_item_gram_weight(food, quantity, unit, gram_weight)

    #     return {
    #         "gram_weight" : str(round(gram_weight, 2)) if gram_weight else None,
    #         "min_gram_weight" : str(round(min_gram_weight, 2)) if min_gram_weight else None,
    #         "max_gram_weight" : str(round(max_gram_weight, 2)) if max_gram_weight else None
    #         }

    # if the given unit was not a weight or volume unit, return None for all of the gram weights
    return {
        "gram_weight" : str(round(gram_weight, 2)) if gram_weight else None,
        "min_gram_weight" : str(round(min_gram_weight, 2)) if min_gram_weight else None,
        "max_gram_weight" : str(round(max_gram_weight, 2)) if max_gram_weight else None
        }
    

def _convert_weights_to_grams(quantity: Union[str, int, float], unit:str) -> str:
    """
    Get the weight of a given quantity of units in grams
    If the given unit is not in the set of standard weight units (e.g. "pounds", "ounces", "grams", "kilograms", "milligrams", "micrograms") or an abbreviated form,
    the function returns None.
    Args:
        quantity (Union[str, int, float]): The quantity of the food item.
        unit (str): The unit of measurement for the quantity.
    Returns:
        str: The weight of the quantity in grams.
    """

    if not isinstance(quantity, (str, int, float)):
        raise ValueError("'quantity' must be a string, integer, or float")
    
    if not isinstance(unit, str):
        raise ValueError("'unit' must be a string")
    
    if isinstance(quantity, str):
        quantity = float(quantity)

    if unit in _constants.WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT:
        
        standard_unit     = _constants.WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT[unit]
        conversion_factor = _constants.GRAM_CONVERSION_FACTORS[standard_unit]

        gram_weight = quantity * conversion_factor

        return gram_weight
    
    return None


def _convert_volumes_to_milliliters(quantity: Union[str, int, float], unit:str) -> str:
    """
    Get the volume of a given quantity of units in milliliters
    If the given unit is not in the set of standard volume units (e.g. "teaspoons", "tablespoons", 
    "fluid ounces", "cups", "pints", "quarts", "gallons", "milliliters", "liters") or an abbreviated form, 
    then the function returns None.
    Args:
        quantity (Union[str, int, float]): The quantity of the food item. Can be a string, float, or integer (e.g. "1.0", 1, 1.0)
        unit (str): The unit of measurement for the quantity. (e.g. "cups", "teaspoons", "tablespoons", "fluid ounces", "milliliters", "liters")
    Returns:
        str: The volume of the quantity in milliliters.

    """

    if not isinstance(quantity, (str, int, float)):
        raise ValueError("'quantity' must be a string, integer, or float")
    
    if not isinstance(unit, str):
        raise ValueError("'unit' must be a string")
    
    if isinstance(quantity, str):
        quantity = float(quantity)

    if unit in _constants.VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT:
        
        standard_unit     = _constants.VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT[unit]
        conversion_factor = _constants.MILLILITER_CONVERSION_FACTORS[standard_unit]

        milliliter_volume = quantity * conversion_factor

        return milliliter_volume
    
    return None

def _convert_volume_to_grams(food: str, quantity: Union[str, int, float], unit: str, method:str = "levenshtein") -> dict:

    """
    Convert a volume measurement to a weight measurement in grams.
    Args:
        food (str): The food item to convert.
        quantity (Union[str, int, float]): The quantity of the food item.
        unit (str): The unit of measurement for the quantity.
        method (str): The method to use for fuzzy string matching. Options are "levenshtein", "jaccard", or "dice". Defaults to "levenshtein".
    Returns:
        dict: A dictionary containing the gram weight, maximum gram weight, and minimum gram weight.
    """

    # ############################################################
    # ingredient = "1 1/2 cups of all purpose almond flour, grounded"
    # method = "jaccard"
    # method = "levenshtein"
    # ############################################################

    if not isinstance(method, str):
        raise ValueError("'method' must be a string")
    
    method = method.lower()

    if method not in ["levenshtein", "jaccard", "dice"]:
        raise ValueError("Invalid 'method'. Options are 'levenshtein', 'jaccard', or 'dice'.")

    fuzzy_matcher =  _get_fuzzy_matcher(method)

    milliliter_quantity = _convert_volumes_to_milliliters(quantity, unit)

    # print(f"Looking for categories and densities for:\n > '{food}'")
    # no_match_string = "no match found in FOOD_CATALOG"
    
    # try to get the food groups for the given food...
    food_groups = _constants.FOOD_CATALOG.get(food, None)
    # food_groups = _constants.FOOD_CATALOG.get(food, no_match_string)

    # print(f"Categories for '{food}':\n--> '{food_groups}'")

    if not food_groups:
        # print(f"Going for the layup classification for '{food}'...")
        food_group = _check_food_for_easy_categorization(food)
        # print(f"Easily classified as '{food_group}'")
        if food_group:
            # print(f"Setting previously None 'food_groups' to '{[food_group, food_group]}'")
            food_groups = [food_group, food_group]

    # print(f"Categories for '{food}':\n--> '{food_groups}'")
            
    # Case when we get a real match in the FOOD_CATALOG, 
    # then we can just use the corresponding densities for the matched food
    if food_groups:
    # if food_groups != no_match_string:
        # print(f"Found exact category match:\n '{food}' >>> '{food_groups}'")
        primary_category, secondary_category = food_groups

        # try to get the density values for the given primary category food group, 
        # if that fails try to get the density values for the secondary category food group
        # and all else fails, use the default density map
        if primary_category in _constants.FOOD_DENSITY_BY_GROUP:
            density_map = _constants.FOOD_DENSITY_BY_GROUP.get(primary_category, _constants.DEFAULT_DENSITY_MAP)
        elif secondary_category in _constants.FOOD_DENSITY_BY_GROUP:
            density_map = _constants.FOOD_DENSITY_BY_GROUP.get(secondary_category, _constants.DEFAULT_DENSITY_MAP)
        else:
            density_map = _constants.DEFAULT_DENSITY_MAP
            
        # try to get the density values for the given primary category food group, 

        # print(f"Using density values for category:\n > '{density_map['category']}'")

        density     = density_map.get("density_g_per_ml", 1)
        min_density = density_map.get("min_density_g_per_ml", 0.9)
        max_density = density_map.get("max_density_g_per_ml", 1.1)

        # if primary_density and secondary_density:
            # print(" > Both densities are available")
        # print(f"Primary density: {primary_density}\nSecondary density: {secondary_density}")

        gram_weight     = milliliter_quantity * density
        min_gram_weight = milliliter_quantity * min_density
        max_gram_weight = milliliter_quantity * max_density
        
        return {
            "gram_weight" : gram_weight, 
            "min_gram_weight" : min_gram_weight,
            "max_gram_weight" : max_gram_weight
            }

    # However, if we do NOT get a match in the FOOD_CATALOG, we will have to do a fuzzy match between our given food
    # and all of the foods and determine the closet match and use the density of that food group (FOOD_DENSITY_BY_GROUP)

    similarity_scores = {}
    top_scoring_foods = {}

    for category in _constants.FOOD_DENSITY_BY_GROUP:
        food_set = _constants.FOODS_BY_CATEGORY[category]
        # print(f"Category: {category}\nFood set: {food_set}")

        # find the closeness from the given food to each food in the current category
        # and extract that food and its value, to stash the top matched food and its score for each category
        scores =  {i: round(fuzzy_matcher(food, i), 2) for i in food_set}
        top_score_key = max(scores, key=scores.get) 
        top_score_value = scores[top_score_key] if top_score_key else 0
        
        # NOTE: keep track of the food with the highest similarity score for each category
        top_scoring_foods[category] = [top_score_key, top_score_value]
        # print(f" - Top score key/value:\n ----> '{top_score_key} ({scores[top_score_key]})'\n")

        max_similarity = max([round(fuzzy_matcher(food, i), 2) for i in food_set])
        # max_similarity = max([round(_utils.score_sentence_similarity(food, i), 2) for i in food_set])

        similarity_scores[category] = max_similarity
        
    # get the key that has the highest similarity score in the dictionary of similarity scores
    best_category_match = max(similarity_scores, key=similarity_scores.get)

    # print(f"Key with max similarity score:\n > '{best_category_match}'")
    # print(f"Top score: {similarity_scores[best_category_match]}")
    # print(f"Top scoring food:\n > {top_scoring_foods[best_category_match]}")

    density = 1
    min_density = 0.9
    max_density = 1.1

    try: 
        # print(f"Successful best effort category match: \n '{food}' >>> '{best_category_match}'")
        gram_map    = _constants.FOOD_DENSITY_BY_GROUP[best_category_match]
        density     = gram_map["density_g_per_ml"]
        max_density = gram_map["max_density_g_per_ml"]
        min_density = gram_map["min_density_g_per_ml"]
        # print(f"Using density value of:\n > '{density} g/ml'")
    except:
        warnings.warn(f"No good food denstity match was found, defaulting to the density of water (1 g/ml)")

    # # NOTE: old way of catching if no good match was made or the matched category does not exist / density is <= 0
    # if ((best_category_match not in _constants.FOOD_DENSITY_BY_GROUP) or \
    #     (best_category_match in _constants.FOOD_DENSITY_BY_GROUP and _constants.FOOD_DENSITY_BY_GROUP[best_category_match]['density_g_per_ml'] <= 0)
    #     ):
    #     density = 1
    # else:
    #     density = _constants.FOOD_DENSITY_BY_GROUP[best_category_match]["density_g_per_ml"]
        
    gram_weight     = density * milliliter_quantity
    max_gram_weight = max_density * milliliter_quantity
    min_gram_weight = min_density * milliliter_quantity

    return {
        "gram_weight" : gram_weight, 
        "min_gram_weight" : min_gram_weight,
        "max_gram_weight" : max_gram_weight, 
        }

# # ingredient = "1 1/2 cups of all purpose almond flour, grounded"
# ingredient = "1 1/2 cups of chick nuggets, grounded"

# # ingredient = "1 1/2 cups of chicken nuggets, grounded"
# # ingredient = "1 1/2 cups of White whole wheat flour, grounded"

# slicer = IngredientSlicer(ingredient)
# food = slicer.food
# # food = "112"
# unit = slicer.standardized_unit if slicer.standardized_unit else slicer.unit
# quantity = slicer.quantity

def _check_food_for_easy_categorization(food:str) -> str:

    """Check if the food can be easily categorized based on the food name.
    If it can, return the category. Otherwise, return just return None.
    Args:
        food: str: The name of the food to categorize.
    Returns:
        str: The category of the food if it can be easily categorized. Otherwise, None.
    """

    # food = "whole  wheat  oaty flour  oil"
    # food = "toats vdf asvfgf df"

    # clean up tasks
    food = food.lower().strip()
    food = _remove_extra_whitespaces(food)
    food = food.split()

    matched_categories = []
    for word in food:
        match = _constants.INDICATOR_STRINGS_MAP.get(word, None)
        if match:
            matched_categories.append(match)

    # if we have multiple matches, return the last one because I think its more likely that the last match indicates the category
    # TODO: this might be stupid but made sense to me ("olive oil", "brown sugar", "white sugar", the indicator word seems to come last-ish)
    # TODO: Regardless, its pretty unlikely youll get multiple matches anyway
    category = matched_categories[-1] if matched_categories else None

    return category

def _get_fuzzy_matcher(method: str) -> Callable:
    """
    Get the fuzzy string matching function based on the given method.
    Internal conveniance function
    Args:
        method (str): The method to use for fuzzy string matching. Options are "levenshtein", "jaccard", or "dice".
    Returns:
        Callable: The fuzzy string matching function.
    """

    method = method.lower()

    if method not in ["levenshtein", "jaccard", "dice"]:
        raise ValueError("Invalid 'method'. Options are 'levenshtein', 'jaccard', or 'dice'.")

    fuzzy_matchers = {
        "levenshtein" : _levenshtein_similarity,
        "jaccard" : _jaccard_similarity,
        "dice" : _dice_coeff_similarity
        }

    return fuzzy_matchers[method]

def _levenshtein_dist(str1: str, str2: str) -> int:
    matrix = [[float("inf")] * (len(str2) + 1) for i in range(len(str1) + 1)]

    for j in range(len(str2) + 1):
        matrix[len(str1)][j] = len(str2) - j

    for i in range(len(str1) + 1):
        matrix[i][len(str2)] = len(str1) - i

    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1, -1):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix[i + 1][j + 1]
            else:
                matrix[i][j] = 1 + min(
                                    matrix[i + 1][j],    # delete
                                    matrix[i][j + 1],     # isert 
                                    matrix[i + 1][j + 1] # substitute
                                    )
    # levenstein distance == bottom right corner of matrix
    return matrix[0][0]

def _levenshtein_similarity(str1, str2):
    distance = _levenshtein_dist(str1, str2)
    max_len = max(len(str1), len(str2))
    return 1 - (distance / max_len)

def _jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

# Credit: to recipe_scrapers (hhruvs) GitHub repository for the following code
def _dice_coeff_similarity(first: str, second: str) -> float:
    """Calculate Dice coefficient for two strings.

    The dice coefficient is a measure of similarity determined by calculating
    the proportion of shared bigrams.

    Parameters
    ----------
    first : str
        First string
    second : str
        Second string

    Returns
    -------
    float
        Similarity score between 0 and 1.
        0 means the two strings do not share any bigrams.
        1 means the two strings are identical.
    """

    if first == second:
        # Indentical sentences have maximum score of 1
        return 1

    if len(first) < 2 or len(second) < 2:
        # If either sentence has 0 or 1 character we can't generate bigrams,
        # so the score is 0
        return 0

    first_bigrams = {first[i : i + 2] for i in range(len(first) - 1)}
    second_bigrams = {second[i : i + 2] for i in range(len(second) - 1)}

    intersection = first_bigrams & second_bigrams

    return 2.0 * len(intersection) / (len(first_bigrams) + len(second_bigrams))

def _fuzzy_match_key(fuzzy_key:str = None, 
                    map_to_check:dict = _constants.FOOD_CATEGORIES, 
                    method:str = "dice",
                    threshold: Union[float, None] = None,
                    ) -> str:
    """
    Get the key from the map that most closely matches the fuzzy key
    Args:
    fuzzy_key: key to match
    map_to_check: dictionary to check for matches
    method: method to use for fuzzy matching. Options are "dice", "jaccard", or "levenshtein"
    threshold: minimum similarity score to return a match (between 0 and 1, default is None)
    """

    if threshold is not None and not isinstance(threshold, float):
        raise ValueError("Threshold must be a float")

    method = method.lower()

    if method not in ["dice", "jaccard", "levenshtein"]:
        raise ValueError("Invalid method. Options are 'dice', 'jaccard', or 'levenshtein'")

    # fuzzy_key = primary_categories[0]
    # map_to_check = ingredient_slicer.FOOD_CATEGORIES

    fuzzy_matcher = _get_fuzzy_matcher(method)
    # map_keys = list(map_to_check.keys())

    best_match = None
    max_similarity = 0
    
    for key in map_to_check.keys():
        similarity = round(fuzzy_matcher(fuzzy_key, key), 3)

        if similarity >= max_similarity:
            max_similarity = similarity
            best_match = key
    
    if threshold and max_similarity < threshold:
        return None
    
    return best_match

def _fuzzy_match_str_parts_to_key(fuzzy_key:str = None, 
                    map_to_check:dict = _constants.FOOD_CATEGORIES, 
                    method:str = "dice",
                    threshold: Union[float, None] = None,
                    ) -> str:
    """
    Get the key from the map that most closely matches the fuzzy key
    Args:
    fuzzy_key: key to match, the key is split into parts and each part is matched to the map keys
    map_to_check: dictionary to check for matches
    method: method to use for fuzzy matching. Options are "dice", "jaccard", or "levenshtein"
    threshold: minimum similarity score to return a match (between 0 and 1, default is None)
    Returns:
        str: The key that most closely matches the fuzzy key
    """
    # fuzzy_key = 'farmraised fresh eggs'
    # fuzzy_key = "fresh broccoli heads, light"
    # map_to_check = _constants.SINGLE_ITEM_FOOD_WEIGHTS
    # method = "dice"
    # threshold = None

    if threshold is not None and not isinstance(threshold, float):
        raise ValueError("Threshold must be a float")

    method = method.lower()

    if method not in ["dice", "jaccard", "levenshtein"]:
        raise ValueError("Invalid method. Options are 'dice', 'jaccard', or 'levenshtein'")

    # fuzzy_key = primary_categories[0]
    # map_to_check = ingredient_slicer.FOOD_CATEGORIES

    fuzzy_matcher = _get_fuzzy_matcher(method)
    # map_keys = list(map_to_check.keys())

    best_match = None
    max_similarity = 0

    split_fuzzy_key = fuzzy_key.split()
    
    for key in map_to_check.keys():
        split_max_score = 0
        for split_fuzzy in split_fuzzy_key:
            # print(f"Split Fuzzy: {split_fuzzy}")
            if split_fuzzy == key:
                max_similarity = 1
                best_match = key
                continue

            similarity = round(fuzzy_matcher(split_fuzzy, key), 3)
            # print(f"Split Fuzzy: {split_fuzzy} > '{similarity}")

            split_max_score = max(similarity, split_max_score)
            # split_scores.append(similarity)
            # split_max_score = max(split_scores)
        
        if split_max_score >= max_similarity:
            # print(f"New best match: {key}")
            max_similarity = split_max_score
            best_match = key

        # print(f"best_match: {best_match}")
        # print(f"max_similarity: {max_similarity}")
        # print()

    if threshold and max_similarity < threshold:
        # print(f"Best match WAS '{best_match}' but the similarity score was too low ({max_similarity} < {threshold})")
        return None
    
    # print(f"Best match is '{best_match}' with a similarity score of {max_similarity}")
    return best_match

def _estimate_single_item_gram_weights(food:str, threshold:Union[float, None]) -> Union[str, None]:

    """ Estimate the weight of a single food item in grams
    Args:
        food: str, food item
        threshold: float, minimum similarity score to return a match
    Returns:
        estimated weight of the food in grams as a string or None
    """

    # food = "egg whites"
    # gram_weight = None

    # if gram_weight or gram_weight is not None:
    #     return gram_weight
    
    if food in _constants.SINGLE_ITEM_FOOD_WEIGHTS:
        return _constants.SINGLE_ITEM_FOOD_WEIGHTS[food]
    
    # closest_key = _fuzzy_match_key(food, _constants.SINGLE_ITEM_FOOD_WEIGHTS, "dice", 0.5)
    closest_key = _fuzzy_match_str_parts_to_key(food, _constants.SINGLE_ITEM_FOOD_WEIGHTS, "dice", threshold)

    # if closest_key:
        # return _constants.SINGLE_ITEM_FOOD_WEIGHTS[closest_key]
    
    return _constants.SINGLE_ITEM_FOOD_WEIGHTS.get(closest_key, None)

def _get_single_item_gram_weight2(food:str, quantity:str, unit:str, gram_weight:str) -> Union[str, None]:

    """ Get the weight of a single food item in grams
    Args:
        food: str, food item
        quantity: str, quantity of the food item
        unit: str, unit of measurement for the quantity
        gram_weight: str, weight of the food in grams

    Returns:
        estimated weight of the food in grams as a string or None
    """

    # food = "eggs"
    # unit = "cup"
    # unit = None
    # quantity = 1
    # gram_weight = None
    
    # set quantity to 1 if its None
    quantity = 1 if not quantity else float(quantity)

    # gram_weight already exists or the unit is a weight unit or volume unit just return the gram weight
    # if gram_weight or unit in _constants.BASIC_UNITS_SET or unit in _constants.VOLUME_UNITS_SET:
    if gram_weight or unit in _constants.WEIGHT_UNIT_TO_STANDARD_WEIGHT_UNIT or unit in _constants.VOLUME_UNIT_TO_STANDARD_VOLUME_UNIT:
        return gram_weight
    
    est_weight = _estimate_single_item_gram_weights(food)
    
    return float(est_weight) * quantity if est_weight else None

def _get_single_item_gram_weight(food:str, quantity:str, threshold:Union[float, None] = None) -> Union[str, None]:

    """ Get the weight of a single food item in grams
    Args:
        food: str, food item
        quantity: str, quantity of the food item

    Returns:
        estimated weight of the food in grams as a string or None
    """

    if not isinstance(food, str):
        raise TypeError("'food' must be a string")
    
    if quantity is not None and not isinstance(quantity, (str, int, float)):
        raise TypeError("'quantity' must be a string, integer, or float")

    # food = "eggs"
    # unit = "cup"
    # unit = None
    # quantity = 1
    # gram_weight = None
    
    # set quantity to 1 if its None
    quantity = 1 if not quantity else float(quantity)
    
    est_weight = _estimate_single_item_gram_weights(food,  threshold)
    
    return str(float(est_weight) * quantity) if est_weight else None


# def _split_dimension_unit_x_ranges(ingredient: str) -> tuple[str]:
#     """Split an ingredient string by any quantity dimension unit separated by an 'x' character.
#     (i.e. "2 steaks, 3 inches x 4 inches thick" -> ("2 steaks, thick", "3 inches x 4 inches")

#     Args:
#         ingredient (str): The ingredient string to parse.
#     Returns:
#         tuple[str]: A tuple containing the updated ingredient string with the range removed and a list of the dimension units strings.
#     """

#     # ingredient = "2 steaks, 3 inches x 4 inches thick"
#     # ingredient = "2 steaks, 3 cm x 4 inches thick"
#     # ingredient = "2 steaks, 3 cm x 4 inches thick"
#     # ingredient = "2 steaks, (3 cm x 4 inches) thick"

#     quantity_unit_x_range_iter = _regex_patterns.QUANTITY_UNIT_X_QUANTITY_UNIT.finditer(ingredient)

#     dimension_units = []

#     for match in quantity_unit_x_range_iter:
#         # original string matched by the pattern (used for replacement)
#         original_string = match.group(0)

#         # quantities from first quantity/unit pair
#         quantity1 = match.group(1)
#         unit1     = match.group(2)

#         # quantities from second quantity/unit pair
#         quantity2 = match.group(3)
#         unit2     = match.group(4)

#         unit1_is_dimension = unit1 in _constants.DIMENSION_UNITS_SET
#         unit2_is_dimension = unit2 in _constants.DIMENSION_UNITS_SET

#         print(f"Original String: {original_string}")
#         print("First Quantity/Unit Pair")
#         print(f"- Quantity 1: {quantity1}")
#         print(f"- Unit 1: {unit1}")
#         print(f" >> '{unit1}' is dimension? {unit1_is_dimension}")
#         print("Second Quantity/Unit Pair")
#         print(f"- Quantity 2: {quantity2}")
#         print(f"- Unit 2: {unit2}")
#         print(f" >> '{unit2}' is dimension? {unit2_is_dimension}")

#         if unit1_is_dimension and unit2_is_dimension:
#             print(f"Both units are dimensions")
#             # ingredient = _find_and_remove(ingredient, pattern)
#             dimension_units.append(original_string)
#             ingredient = ingredient.replace(original_string, "")

#         print()

#     return ingredient, dimension_units

# def _split_dimension_unit_by_ranges(ingredient: str) -> tuple[str]:
#     """Split an ingredient string by any quantity dimension unit separated by an 'by' character.
#     (i.e. "2 steaks, 3 inches by 4 inches thick" -> ("2 steaks, thick", "3 inches by 4 inches")
    
#     Args:
#         ingredient (str): The ingredient string to parse.
#     Returns:
#         tuple[str]: A tuple containing the updated ingredient string with the range removed and a list of the dimension units strings.
#     """

#     quantity_unit_by_range_iter = _regex_patterns.QUANTITY_UNIT_BY_QUANTITY_UNIT.finditer(ingredient)

#     dimension_units = []

#     for match in quantity_unit_by_range_iter:
#         # original string matched by the pattern (used for replacement)
#         original_string = match.group(0)

#         # quantities from first quantity/unit pair
#         quantity1 = match.group(1)
#         unit1     = match.group(2)

#         # quantities from second quantity/unit pair
#         quantity2 = match.group(3)
#         unit2     = match.group(4)

#         unit1_is_dimension = unit1 in _constants.DIMENSION_UNITS_SET
#         unit2_is_dimension = unit2 in _constants.DIMENSION_UNITS_SET

#         print(f"Original String: {original_string}")
#         print("First Quantity/Unit Pair")
#         print(f"- Quantity 1: {quantity1}")
#         print(f"- Unit 1: {unit1}")
#         print(f" >> '{unit1}' is dimension? {unit1_is_dimension}")
#         print("Second Quantity/Unit Pair")
#         print(f"- Quantity 2: {quantity2}")
#         print(f"- Unit 2: {unit2}")
#         print(f" >> '{unit2}' is dimension? {unit2_is_dimension}")

#         if unit1_is_dimension and unit2_is_dimension:
#             print(f"Both units are dimensions")
#             # ingredient = _find_and_remove(ingredient, pattern)
#             dimension_units.append(original_string)
#             ingredient = ingredient.replace(original_string, "")

#         print()

#     return ingredient, dimension_units

###################################################################
#### OLD AVERAGE RANGES functions from IngredientSlicer class ####
#### TODO: Delete these old versions... ###########################
###################################################################
# def _avg_ranges2(self) -> None:
#     """
#     Replace ranges of numbers with their average in the parsed ingredient.
#     Examples:
#     "1-2 oz" -> "1.5 oz"
#     "1 - 2 ft" -> "1.5 ft"
#     """
#     # ingredient = "1 - 2 cups of sugar"
#     search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(self.standardized_ingredient)
#     # search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(ingredient)

#     # OG = re.compile(r"\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?") # NOTE: this is the golden child, OG --> PREVIOUS VERSION THAT WORKS PERFECTLY (ALMOST)
#     # search_ranges = OG.search(ingredient)

#     print(f"Starting while loop searching for ranges in ingredient: {self.standardized_ingredient}") if self.debug else None
#     while search_ranges:

#         start, end = search_ranges.start(), search_ranges.end()
#         match_string = search_ranges.group()
        
#         left_range, right_range = match_string.split("-")
        
#         left_range = left_range.strip()
#         right_range = right_range.strip()

#         print(f"Match: {match_string}") if self.debug else None
#         print(f"left_range: {left_range}") if self.debug else None
#         print(f"right_range: {right_range}") if self.debug else None
#         print(f"Start: {start}") if self.debug else None
#         print(f"End: {end}") if self.debug else None

#         first_number  = float(_utils._fraction_str_to_decimal(left_range).strip())
#         second_number = float(_utils._fraction_str_to_decimal(right_range).strip())
        
#         range_average = f" {_utils._make_int_or_float_str(str((first_number + second_number) / 2))} "
#         self.standardized_ingredient = self.standardized_ingredient[:start] + range_average + self.standardized_ingredient[end:]

#         search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY.search(self.standardized_ingredient)
#         # search_ranges = _regex_patterns.QUANTITY_DASH_QUANTITY_GROUPS.search(ingredient)
    
#     print(f"All ranges have been updated: {self.standardized_ingredient}") if self.debug else None

#     self.standardized_ingredient = self.standardized_ingredient.strip()

#     return
    
# def _avg_ranges(self) -> None:
#     """
#     Replace ranges of numbers with their average in the parsed ingredient.
#     Examples:
#     "1-2 oz" -> "1.5 oz"
#     "1 - 2 ft" -> "1.5 ft"
#     """
    
#     all_ranges = re.finditer(_regex_patterns.QUANTITY_DASH_QUANTITY, self.standardized_ingredient)

#     # initialize offset and replacement index values for updating the ingredient string, 
#     # these will be used to keep track of the position of the match in the string
#     offset = 0

#     # Update the ingredient string with the merged values
#     for match in all_ranges:
#         print(f"Ingredient string: {self.standardized_ingredient}") if self.debug else None

#         # Get the start and end positions of the match
#         start, end = match.start(), match.end()

#         print(f"Match: {match.group()} at positions {start}-{end}") if self.debug else None

#         # Get the range values from the match
#         range_values = re.findall(_regex_patterns.QUANTITY_DASH_QUANTITY, match.group())

#         print(f"Range Values: {range_values}") if self.debug else None
        
#         # split the range values into a list of lists
#         split_range_values = [i.split("-") for i in range_values]
        
#         print(f"  >>> Split Range Values: {split_range_values}") if self.debug else None
#         # print() if self.debug else None

#         # get the average of each of the range values
#         range_avgs    = [sum([float(num_str) for num_str in i]) / 2 for i in split_range_values][0]
#         range_average = _utils._make_int_or_float_str(str(range_avgs))

#         print(f"Range Averages: {range_average}") if self.debug else None

#         # Calculate the start and end positions in the modified string
#         modified_start = start + offset
#         modified_end = end + offset

#         print(f"Replacing {match.group()} with '{range_average}'...") if self.debug else None
        
#         # Construct the modified string with the replacement applied
#         self.standardized_ingredient = self.standardized_ingredient[:modified_start] + str(range_average) + self.standardized_ingredient[modified_end:]
#         # ingredient = ingredient[:modified_start] + str(range_average) + ingredient[modified_end:]

#         # Update the offset for subsequent replacements
#         offset += len(range_average) - (end - start)

#     return 

# # import re
# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\"')
# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\”')
# NUMBER_WITH_FOOT_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\'')


# test_strings = [
#     f""" 1" """,
#     f""" 1 1/2" """,
#     f""" 1 1/2 inch """,
#     f""" 1 1/2 inches """,
#     f""" 1 1/2 inch(es)" """,
#     f""" 1 1/2" incch """,
#     f""" 1 0.5" inch """,
#     f""" 1 0.5 " inches """
# ]

# for test_string in test_strings:
#     print(NUMBER_WITH_INCH_SYMBOL.findall(test_string))

# NUMBER_WITH_INCH_SYMBOL.findall("1 1/2\"")

# # ingredient = "fruit (4-2/3” long x 2-3/4” dia)"
# # ingredient = 'waffle round (4" dia)'

# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\"')
# # NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\”')

# NUMBER_WITH_INCH_SYMBOL_MAP = {}
# for inch_symbol in ["\"", "”"]:
#     NUMBER_WITH_INCH_SYMBOL_MAP[inch_symbol] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*' + inch_symbol + r'')

# def _replace_number_followed_by_inch_symbol(ingredient: str ) -> str:
#     """
#     Find and remove percentages from the ingredient string.
#     """
#     # ingredient = "1 cup of 2% heavy cream"
#     # ingredient = "fruit (4-2/3” long x 2-3/4” dia)"
#     # ingredient = 'waffle round (4 " dia)'

#     for key, pattern in _regex_patterns.NUMBER_WITH_INCH_SYMBOL_MAP.items():
#         # print(f"Key: {key}")
#         # print(f"Pattern: {pattern}")
#         pattern_iter = pattern.finditer(ingredient)
#         # print(f"Pattern Iter: {pattern_iter}")
#         # all_matches = pattern.findall(ingredient)
#         # print(f"All Matches: {all_matches}")
        
#         offset = 0
#         for match in pattern_iter:
#             match_string = match.group()
#             start, end = match.start(), match.end()
#             modified_start = start + offset
#             modified_end = end + offset

#             # replacement_str = ""
#             # print(f"Match String: {match_string}")
#             # print(f"Start: {start} | End: {end}")
#             replacement_str = match_string.replace(key, "inch")

#             # Construct the modified string with the replacement applied
#             ingredient = ingredient[:modified_start] + str(replacement_str) + ingredient[modified_end:]

#             offset += len(str(replacement_str)) - (end - start)
#     return


# def _update_ranges(ingredient: str, pattern: re.Pattern, replacement_function=None) -> str:
#         """Update the ranges in the ingredient string with the updated ranges
#         Args:
#             ingredient (str): The ingredient string to update
#             pattern (re.Pattern): The pattern to use to find the ranges
#             replacement_function (function, optional): A function to use to replace the matched ranges. Defaults to None.
#         Returns:
#             str: The updated ingredient string
#         """
        
#         # pattern = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY
        
#         matches = pattern.findall(ingredient)

#         # matched_ranges = [match.split("-") for match in matches]

#         if replacement_function:
#             # print(f"Replacement Function given")
#             matched_ranges = [replacement_function(match).split("-") for match in matches]
#         else:
#             # print(f"No Replacement Function given")
#             matched_ranges = [match.split("-") for match in matches]

#         # print(f"Matched Ranges: \n > {matched_ranges}") if self.debug else None

#         updated_ranges = [" - ".join([str(_fraction_str_to_decimal(i)) for i in match if i]) for match in matched_ranges]
#         # updated_ranges = [" - ".join([str(int(i)) for i in match if i]) for match in matched_ranges]
        
#         # Create a dictionary to map the matched ranges to the updated ranges
#         ranges_map = dict(zip(matches, updated_ranges))

#         # Replace the ranges in the original string with the updated ranges
#         for original_range, updated_range in ranges_map.items():
#             # print(f"Original Range: {original_range}")
#             # print(f"Updated Range: {updated_range}")
#             # if replacement_function:
#             #     print(f"Replacement Function given")
#             #     updated_range = replacement_function(updated_range)
#             ingredient = ingredient.replace(original_range, updated_range)
#             # print("\n") if self.debug else None

#         return ingredient
