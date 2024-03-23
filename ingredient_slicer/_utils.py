
from fractions import Fraction
import re

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

        number_str = number_str.replace(" ", "")

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
            return str(int(number))  # Return integer value if it's a whole number
        else:
            return str(number)  # Return float if it's a decimal

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
        has_only_valid_chars = all([i.isdigit() or i in {"-", "/", " "} for i in fraction_str])

        if not has_only_valid_chars:
            raise ValueError("Invalid input. Fraction string must contain only digits, hyphens, and a forward slash (possible invalid characters and/or periods?)")

        numerator = int(split_fraction[0])
        denominator = int(split_fraction[1])

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

# regex_patterns = _regex_patterns.IngredientRegexPatterns()

# ingredient = "1-2 apples and 1- 45 orange slices (2)"
# pattern = regex_patterns.QUANTITY_DASH_QUANTITY
# replacement_function=None


# BETWEEN_QUANTITY_AND_QUANTITY 
# _replace_and_with_hyphen
def _update_ranges(ingredient: str, pattern: re.Pattern, replacement_function=None) -> str:
        """Update the ranges in the ingredient string with the updated ranges
        Args:
            ingredient (str): The ingredient string to update
            pattern (re.Pattern): The pattern to use to find the ranges
            replacement_function (function, optional): A function to use to replace the matched ranges. Defaults to None.
        Returns:
            str: The updated ingredient string
        """
        
        # pattern = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY
        
        matches = pattern.findall(ingredient)

        # matched_ranges = [match.split("-") for match in matches]

        if replacement_function:
            # print(f"Replacement Function given")
            matched_ranges = [replacement_function(match).split("-") for match in matches]
        else:
            # print(f"No Replacement Function given")
            matched_ranges = [match.split("-") for match in matches]

        # print(f"Matched Ranges: \n > {matched_ranges}") if self.debug else None

        updated_ranges = [" - ".join([str(_fraction_str_to_decimal(i)) for i in match if i]) for match in matched_ranges]
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

# BETWEEN_QUANTITY_AND_QUANTITY 
# _replace_and_with_hyphen

def _update_ranges2(ingredient: str, pattern: re.Pattern) -> str:
        """Update the number ranges in the ingredient string to always have two numbers separated by a whitespace, then a hyphen, then another whitespace.
        Notes: Currently supports the following patterns in the IngredientRegexPatterns class:
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
        
        # # pattern = IngredientSlicer.regex.QUANTITY_DASH_QUANTITY
        # ingredient = "1-2 apples and 1- 45 orange slices between 4 and 5 lemons or 1 or 2 oranges and use 1 to 2 lemons"
        # pattern = regex_patterns.QUANTITY_DASH_QUANTITY
        
        # ingredient = '1 - 2 apples and 1 - 45 orange slices between 4 and 5 lemons or 1 or 2 oranges and use 1 to 2 lemons'
        # pattern = regex_patterns.BETWEEN_QUANTITY_AND_QUANTITY

        # ingredient = '1 - 2 apples and 1 - 45 orange slices 4 - 5 lemons or 1 or 2 oranges and use 1 to 2 lemons'
        # pattern = regex_patterns.QUANTITY_TO_QUANTITY

        # ingredient = '1 - 2 apples and 1 - 45 orange slices 4 - 5 lemons or 1 or 2 oranges and use 1 - 2 lemons'
        # pattern = regex_patterns.QUANTITY_OR_QUANTITY
        
        matched_ranges_iter = pattern.finditer(ingredient)
        offset = 0

        for match in matched_ranges_iter:
            start, end = match.start(), match.end()
            modified_start = start + offset  # new start position
            modified_end = end + offset      # new end position
            match_string = match.group()

            # print(f"Match String: '{match_string}'")
            # print(f"Start: {start} | End: {end}")
            # print(f"Modified Start: {modified_start} | Modified End: {modified_end}")
            # print(f"Offset: {offset}")

            # In the match string, replace all instances of "and", "&", "to", and "or" with hyphens
            match_string = match_string.replace("and", "-") \
                .replace("&", "-") \
                .replace("to", "-") \
                .replace("or", "-") \
                .replace("between", "").strip()
                
            # print(f"Match AFTER replacement: '{match_string}'\n")
            # print()
            updated_range = " - ".join([str(_fraction_str_to_decimal(i)) for i in match_string.split("-")])

            ingredient = ingredient[:modified_start] + updated_range + ingredient[modified_end:]

            # # Update the offset for subsequent replacements
            offset += len(str(updated_range)) - (end - start)
            
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

def _find_and_remove_hyphens_around_substring(text: str, substring: str, debug=False) -> str:

    """Find instances of a substring surrounded by some number of hyphens on the left or right of the substring and remove these hyphens
    Case insensitive, and will return the updated string with the hyphens removed from around the substring and in lower case
    Args:
        text (str): The text to search for the substring
        substring (str): The substring to search for in the text
        debug (bool, optional): Print debug information. Defaults to False.
    Returns:
        str: The updated text with the hyphens removed from around the substring
    """

    # substrings_to_fix = ["to", "or", "and"]
    # substring = "to"
    # text = '1 to- 4.5 cups of sugar'
    # text = '1 -to 4.5 cups of sugar'
    # text = "1-to-three cups of tomato-juice"
    # debug = True

    text = text.lower()
    substring = substring.lower().replace("-", "")

    substring_length = len(substring)

    L = 0
    substring_indices = []
    hypen_substrings = []

    for R in range(0, len(text)):

        print(f"L: {L}") if debug else None
        print(f"R: {R}") if debug else None
        print(f"text[L:R]: {text[L:R]}") if debug else None
        if R - L == substring_length:
            print(f"Found window the size of substring!") if debug else None
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
                    print(f"Substring is part of a larger word") if debug else None
                    print(f" - char_to_left: '{char_to_left}'") if debug else None
                    print(f" - char_to_right: '{char_to_right}'") if debug else None
                    print(f"Still increment L from {L} to {L + 1}") if debug else None
                    print() if debug else None
                    L += 1
                    continue

                # look LEFT of the matched substring
                GO_LEFT_INDEX = L - 1

                print(f"Try to go LEFT of '{substring}' substring") if debug else None
                while GO_LEFT_INDEX >= 0 and (text[GO_LEFT_INDEX] == " " or text[GO_LEFT_INDEX] == "-"):
                    print(f"GO_LEFT_INDEX: '{GO_LEFT_INDEX}'") if debug else None
                    print(f" - text[GO_LEFT_INDEX]: '{text[GO_LEFT_INDEX]}'") if debug else None
                    if text[GO_LEFT_INDEX] == "-":
                        has_left_hyphen = True
                    GO_LEFT_INDEX -= 1
                    print(f" --> Ending text[GO_LEFT_INDEX]: '{text[GO_LEFT_INDEX]}'") if debug else None
                
                print() if debug else None

                # look RIGHT of the matched substring
                print(f"Try to go RIGHT of '{substring}' substring") if debug else None

                GO_RIGHT_INDEX = R
                # GO_RIGHT_INDEX = R + 1 # NOTE: Bug fix, Setting the GO_RIGHT_INDEX to R + 1 will skip the first character after the substring

                while GO_RIGHT_INDEX < len(text) and (text[GO_RIGHT_INDEX] == " " or text[GO_RIGHT_INDEX] == "-"):
                    print(f"GO_RIGHT_INDEX: '{GO_RIGHT_INDEX}'") if debug else None
                    print(f" - text[GO_RIGHT_INDEX]: '{text[GO_RIGHT_INDEX]}'") if debug else None
                    if text[GO_RIGHT_INDEX] == "-":
                        has_right_hyphen = True
                    GO_RIGHT_INDEX += 1
                    print(f" --> Ending text[GO_RIGHT_INDEX]: '{text[GO_RIGHT_INDEX]}'") if debug else None

                look_around_string = text[GO_LEFT_INDEX+1:GO_RIGHT_INDEX]

                if has_left_hyphen or has_right_hyphen:
                    hypen_substrings.append(look_around_string)
                    print(f"Added '{look_around_string}' to hypen_substrings:\n > '{hypen_substrings}'") if debug else None

                print(f"FINAL --> GO_LEFT_INDEX: {GO_LEFT_INDEX} --> has LEFT hypen: {has_left_hyphen}") if debug else None
                print(f"FINAL --> GO_RIGHT_INDEX: {GO_RIGHT_INDEX} --> has RIGHT hypen: {has_right_hyphen}") if debug else None
                print(f"Final substring: '{look_around_string}'") if debug else None

            print(f"Incrementing L from {L} to {L + 1}") if debug else None
            L += 1
        print(f"----" * 5) if debug else None
        print() if debug else None
    
    print(f"hypen_substrings: {hypen_substrings}") if debug else None
    
    for hyphen_substring in hypen_substrings:
        replacement_string = f" {hyphen_substring.replace('-', '').replace(' ', '')} " 
        text = text.replace(hyphen_substring, replacement_string) 
        print(f"Replacing '{hyphen_substring}' in 'text' with '{replacement_string}'\n") if debug else None

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
# -----------------------------------------------------------------------------------------------
# ---- Functions for parsing parenthesis content / quantity unit regex functions ----
# -----------------------------------------------------------------------------------------------

# def test_parenthesis_with_equiv_quantity_unit_1():
#     parse = IngredientSlicer("1 cup of chopped chicken breast (about 12 ounces)", debug = True)
#     parse.parse()
#     parsed = parse.to_json()

#     assert parsed['quantity'] == "12"
#     assert parsed['unit'] == "ounces"
#     assert parsed["standardized_unit"] == "ounce"

#     assert parsed['secondary_quantity'] == None  # TODO: maybe this case should get a quantity of 1, but for now it's None
#     assert parsed['secondary_unit'] == "breast"
#     assert parsed['standardized_secondary_unit'] == "breast"

#     assert parsed['is_required'] == True


# ingredient = '1 cup of chopped chicken breast (about 12 ounces)'
# EQUIV_QUANTITY_UNIT_GROUPS
# QUANTITY_UNIT_GROUPS
# regex_patterns = _regex_patterns.IngredientRegexPatterns()

# # ingredient = "1 cup of chopped chicken breast (about 12 ounces)"
# ingredient = '1 cup of chopped chicken breast (about 12 tender and juicy ounces)'
# parenthesis_content = ['(about 12 tender and juicy ounces)']
# # parenthesis_content = ['(about tender and juicy ounces)']
# parenthesis = parenthesis_content[0]

# regex_patterns.EQUIV_QUANTITY_UNIT_GROUPS.findall(parenthesis)

# regex_patterns = _regex_patterns.IngredientRegexPatterns()
def _extract_quantities_only(input_string: str) -> list:

    """From a string get all quantities if they exist WITHOUT units
    Useful for just getting quantities if there are no units associated with them (e.g. "chicken breast (5)")
    Args:
        input_string (str): The string to parse
    Returns:
        list: A list of quantities
    """

    # input_string = parenthesis
    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(about 12 tender and juicy ounces)'
    # input_string = '(14 cups)'
    # input_string = '(juicy about 14 ,  and 456)'

    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    regex_patterns = _regex_patterns.IngredientRegexPatterns()


    # first check for units
    unit_matches = regex_patterns.UNITS_PATTERN.findall(input_string)

    # if we have units we just return because we only are looking for instances where quantities exist WITHOUT units
    if unit_matches:
        return []

    # regex_patterns.QUANTITY_UNIT_GROUPS.findall(input_string)
    quantity_matches = regex_patterns.ALL_NUMBERS.finditer(input_string)
    quantities = regex_patterns.ALL_NUMBERS.findall(input_string)

    # quantity_matches = regex_patterns.ALL_NUMBERS.finditer(input_string)
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

    # input_string = parenthesis
    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(about 12 tender and juicy ounces)'
    # input_string = '(juicy about or 14)'

    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    regex_patterns = _regex_patterns.IngredientRegexPatterns()

    # regex_patterns.QUANTITY_UNIT_GROUPS.findall(input_string)
    quantity_matches = regex_patterns.ALL_NUMBERS.finditer(input_string)

    quantity_unit_pairs = []

    for match in quantity_matches:
        match_string = match.group()
        start, end = match.start(), match.end()

        current_result = []
        current_result.append(match_string)

        str_after_number_match = input_string[end:]
        # print(f"String after number match: '{str_after_number_match}'")

        # regex_patterns.ALL_NUMBERS.findall(after_approx_match)
        nearest_unit_search = regex_patterns.UNITS_PATTERN.search(str_after_number_match)

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

    # input_string = parenthesis
    # input_string = '(about 12 tender and juicy ounces or about 14 grams)'
    # input_string = '(juicy about or 14)'
    # input_string = '(12 tender and juicy ounces or 14 grams about)'

    if not isinstance(input_string, str):
        raise ValueError("Invalid input. Input must be a string.")

    regex_patterns = _regex_patterns.IngredientRegexPatterns()

    approximate_string_matches = regex_patterns.APPROXIMATE_STRINGS_PATTERN.finditer(input_string)

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

        # regex_patterns.ALL_NUMBERS.findall(after_approx_match)
        nearest_number_search = regex_patterns.ALL_NUMBERS.search(str_after_approx_match) # search for the nearest number after the approximate string

        if not nearest_number_search:
            # print(f"No number found after approximate match")
            # print()
            continue

        closest_number = nearest_number_search.group() # the actual matching number string
        # print(f"Closest Number: '{closest_number}'")
        current_result.append(closest_number) # add the number to the result
        
        # string after the number 
        str_after_number_match = str_after_approx_match[nearest_number_search.end():] # string after the number match

        nearest_unit_search = regex_patterns.UNITS_PATTERN.search(str_after_number_match) # search for the nearest unit after the number

        if not nearest_unit_search: # if we don't find a unit after the number, we skip this triplet
            print(f"No unit found after approximate match")
            print()
            continue

        closest_unit = nearest_unit_search.group() # the actual matching unit string
        # print(f"Closest Unit: '{closest_unit}'")

        current_result.append(closest_unit) # add the unit to the result
        # approximate_triplets.append(current_result) # add the triplet to the list of approximate triplets
        approximate_triplets.append(tuple(current_result)) # add the triplet to the list of approximate triplets
        # print()
    

    # look for trailing approximate strings
    trailing_approx_strings = regex_patterns.APPROXIMATE_STRINGS_PATTERN.findall(input_string)

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

    return approximate_triplets
    # return [tuple(i) for i in approximate_triplets]

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