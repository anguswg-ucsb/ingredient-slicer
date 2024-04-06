# Description: This module contains all the regex patterns used in the recipe parser. 
# As well as a class to hold all regex patterns used in the recipe parser (version 2)

import re
from typing import Dict, List, Tuple, Union

# # import constants from _constants module
from . import _constants 

# # import for for local development
# from ingredient_slicer import _constants

# -----------------------------------------------------------------------------
# --------------------------- Conversion patterns -----------------------------
# Patterns for converting: 
# - Fraction phrases/words to fraction strings (e.g. "one half" to "1/2")
# - Number words to numerical values (e.g. "one" to "1")
# - Unicode fractions to decimals (e.g. "½" to "0.5")
# -----------------------------------------------------------------------------

NUMBER_WORDS_MAP = {}
for word, value in _constants.NUMBER_WORDS.items():
    NUMBER_WORDS_MAP[word] = [str(value), re.compile(r'\b' + word + r'\b', re.IGNORECASE)]

# Matches unicode fractions in the string
UNICODE_FRACTIONS_PATTERN = re.compile( r'\b(?:' + '|'.join(re.escape(word) for word in _constants.UNICODE_FRACTIONS.keys()) + r')\b', re.IGNORECASE)

# -----------------------------------------------------------------------------
# --------------------------- Alternation patterns -----------------------------
# ---> NOTE: the main Alternation patterns for various units are created here and these get used in many of the other regular expression
# -----------------------------------------------------------------------------
# ---- Set up Alternation patterns from list of possible units and their variants ----

# Generate the regular expression pattern for units in the string
ANY_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.UNITS.values() for unit in variants_list])
# ANY_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.UNITS.values())
# ANY_UNIT_ALT = '|'.join('|'.join(re.escape(variant) for variant in variants) for variants in _constants.UNITS.values())

# just the basic units 
BASIC_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.BASIC_UNITS.values() for unit in variants_list])
# BASIC_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.BASIC_UNITS.values())

# just the non-basic units
NON_BASIC_UNIT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.NON_BASIC_UNITS_SET)])
# NON_BASIC_UNIT_ALT = '|'.join(list(_constants.NON_BASIC_UNITS_SET))

# Generate the regular expression pattern for units in the string
VOLUME_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.VOLUME_UNITS.values() for unit in variants_list])
# VOLUME_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.VOLUME_UNITS.values())

# The "sometimes might be a unit" strings as a "or" pattern
SOMETIMES_UNIT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.SIZE_MODIFIERS_SET)])
# SOMETIMES_UNIT_ALT = '|'.join(list(_constants.SIZE_MODIFIERS_SET))

# get a pattern for the "approximate" strings (these are typically used to describe an equivelant amount of a unit)
EQUIVALENT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.APPROXIMATE_STRINGS)])
# EQUIVALENT_ALT = '|'.join(list(_constants.APPROXIMATE_STRINGS))

# prep word alternate
PREP_WORD_ALT = '|'.join([re.escape(prep_word) for prep_word in list(_constants.PREP_WORDS)])

# sort the stopwords by their length to make sure longer stopwords get matched before shorter ones
#  to make sure we don't match a shorter stopword that is part of a longer stopword
STOP_WORDS_ALT = '|'.join(sorted([re.escape(stop_word) for stop_word in _constants.STOP_WORDS], key=len, reverse=True))
# STOP_WORDS_ALT = '|'.join([re.escape(stop_word) for stop_word in list(_constants.STOP_WORDS)])


FRACTION_WORDS_ALT = '|'.join([re.escape(fraction_word) for fraction_word in _constants.FRACTION_WORDS])

# Alternations for creating patterns that match prefix number words followed by number words (e.g "twenty five", "thirty three")
NUMBER_WORDS_ALT = '|'.join([re.escape(word) for word in _constants.NUMBER_WORDS])
NUMBER_PREFIX_WORD_ALT = '|'.join([re.escape(word) for word in _constants.NUMBER_PREFIX_WORDS])

# Alternations for patterns like "a pinch of" or "a handful" or "a sprinkle"
CASUAL_UNITS_ALT        = '|'.join([re.escape(casual_unit) for casual_unit in _constants.CASUAL_UNITS_SET])
CASUAL_QUANTITIES_ALT   = '|'.join([re.escape(casual_quantity) for casual_quantity in _constants.CASUAL_QUANTITIES_SET])

# alternations for remvoing useless words from the string when trying to find the food item
DIMENSION_UNITS_ALT     = '|'.join([re.escape(unit) for unit in _constants.DIMENSION_UNITS_SET])
UNIT_MODIFIERS_ALT      = '|'.join([re.escape(unit_modifier) for unit_modifier in _constants.UNIT_MODIFIERS])
APPROXIMATE_STRINGS_ALT = '|'.join([re.escape(approximate_string) for approximate_string in _constants.APPROXIMATE_STRINGS])

# # sort the denominator words by their length to make sure longer words get matched before shorter ones
# #  to make sure we don't match a shorter word that is part of a longer word
# DENOMINATOR_WORDS_ALT = '|'.join(sorted([re.escape(word) for word in _constants.DENOMINATOR_WORDS], key=len, reverse=True))
# # DENOMINATOR_WORDS_ALT = '|'.join([re.escape(word) for word in _constants.DENOMINATOR_WORDS])


# -----------------------------------------------------------------------------
# --------------------------- Units patterns -----------------------------
# ---> NOTE: uses the above Alternation patterns to create the following basic regular expression patterns
# - units in a string
# - matching a number followed by a unit
# - matching a unit followed by a number
# -----------------------------------------------------------------------------
# ---- Use the unit varients to create the regular expression patterns ----

# create a regular expression pattern to match the units in a string
UNITS_PATTERN = re.compile(r'\b(?:' + ANY_UNIT_ALT + r')\b', re.IGNORECASE)
# UNITS_PATTERN = re.compile(r'\b(?:' + '|'.join('|'.join(variants) for variants in UNITS.values()) + r')\b', re.IGNORECASE)

# match just the basic units
BASIC_UNITS_PATTERN = re.compile(r'\b(?:' + BASIC_UNIT_ALT + r')\b', re.IGNORECASE)

# match just the non-basic units
NON_BASIC_UNITS_PATTERN = re.compile(r'\b(?:' + NON_BASIC_UNIT_ALT + r')\b', re.IGNORECASE)

# match the "sometimes might be a unit" strings
SIZE_MODIFIERS_PATTERN = re.compile(r'\b(?:' + SOMETIMES_UNIT_ALT + r')\b', re.IGNORECASE)
# SIZE_MODIFIERS_PATTERN = re.compile(r'\b(?:' + '|'.join(SIZE_MODIFIERS_SET) + r')\b', re.IGNORECASE)

# create a regular expression pattern to match specifically volume units in a string
VOLUME_UNITS_PATTERN = re.compile(r'\b(?:' + VOLUME_UNIT_ALT + r')\b', re.IGNORECASE)

# generic prep words pattern for matching prep words in a string
PREP_WORDS_PATTERN = re.compile(r'\b(?:' + PREP_WORD_ALT + r')\b', re.IGNORECASE)

# general stop words pattern for matching stop words in a string
STOP_WORDS_PATTERN = re.compile(r'\b(?:' + STOP_WORDS_ALT + r')\b', re.IGNORECASE)

# match word versions of fractions in a string (e.g. "half", "thirds")
FRACTION_WORDS_PATTERN = re.compile(r'\b(?:' + FRACTION_WORDS_ALT + r')\b', re.IGNORECASE)

# patterns for things like "a pinch of" or "a handful" or "a sprinkle"
CASUAL_UNITS_PATTERN       = re.compile(r'\b(?:' + CASUAL_UNITS_ALT + r')\b', re.IGNORECASE) # e.g. "bunch", "sprig", "stalk", "stick", "piece", "slice", "strip", "strip", "segment", "wedge", "chunk", "hunk", "slab", "sliver", "shred", "shard", "scrap", "scrape", "scraping", "scrapings
CASUAL_QUANTITIES_PATTERN   = re.compile(r'\b(?:' + CASUAL_QUANTITIES_ALT + r')\b', re.IGNORECASE) # e.g. "a few", "a couple", "a handful", "a pinch", "a sprinkle", "a dash", "a smidgen", "a touch", "a bit"

# Miscellaneous patterns used for trimmin the string down to get the food item 
DIMENSION_UNITS_PATTERN     = re.compile(r'\b(?:' + DIMENSION_UNITS_ALT + r')\b', re.IGNORECASE) # e.g. "inch", "inches", "cm", "mm", "millimeter", "millimeters", "centimeter", "centimeters"
UNIT_MODIFIERS_PATTERN      = re.compile(r'\b(?:' + UNIT_MODIFIERS_ALT + r')\b', re.IGNORECASE) # e.g. "large", "small", "medium
APPROXIMATE_STRINGS_PATTERN = re.compile(r'\b(?:' + APPROXIMATE_STRINGS_ALT + r')\b', re.IGNORECASE) # e.g. "about", "approximately", "around", "roughly", "nearly", "almost

# -----------------------------------------------------------------------------
# --------------------------- Prefix number words with number words patterns -----------------------------
# Patterns for matching:
# - prefix number words followed by number words (e.g "twenty five", "thirty three")
# -----------------------------------------------------------------------------

# regular expression pattern to match prefix number words followed by number words
PREFIXED_NUMBER_WORDS = re.compile(r'\b(?:' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*[-\s]*\s*)(?:' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)
# PREFIXED_NUMBER_WORDS = re.compile(r'\b(?:' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*|\s*-*\s*)(?:' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)

# PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*[-\s]*\s*)(' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE) # OG
PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')(?:[-\s]*)(' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE) # NEW
# PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')[-\s](' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)

PREFIXED_NUMBER_WORDS_MAP = {}
for prefix_word, prefix_number in _constants.NUMBER_PREFIX_WORDS.items():
    for number_word, number_value in _constants.NUMBER_WORDS.items():
        PREFIXED_NUMBER_WORDS_MAP[prefix_word + " " + number_word] = [str(prefix_number + number_value), re.compile(r'\b' + prefix_word + r'(?:[-\s]*)' + number_word + r'\b', re.IGNORECASE)]

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------- Unit/Number or Number/Unit patterns -----------------------------
# Patterns for matching:
# - a number followed by a unit
# - a unit followed by a number
# - a number followed by a unit followed by any text (full unit and abbreviation)
# - a unit followed by a number followed by any text (full unit and abbreviation)
# - a number/decimal/fraction followed by a space and then another number/decimal/fraction
# - a number/decimal/fraction followed by a space and then another number/decimal/fraction followed by a unit
# -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# same as above but with 2 capture groups (number and unit, either basic, non-basic, or any unit)
QUANTITY_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')
QUANTITY_BASIC_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + BASIC_UNIT_ALT + r')\b')
QUANTITY_NON_BASIC_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + NON_BASIC_UNIT_ALT + r')\b')
QUANTITY_SOMETIMES_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + SOMETIMES_UNIT_ALT + r')\b')
QUANTITY_DIMENSION_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + DIMENSION_UNITS_ALT + r')\b')
QUANTITY_ANYTHING_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')

# restrictive quantity unit group matcher, matches a quantity number followed by 0+ whitespaces/0+ hyphens and then a unit in ANY_UNIT_ALT
# (i.e. "1 cup", "1-1/2 cup", "12 -- cup")
QUANTITY_UNIT_ONLY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*[-\s]*\b(' + ANY_UNIT_ALT + r')\b')

# Pattern for finding quantity unit patterns that are preceeded by an "equivalent" string 
# (i.e. "about 1/2 cup", "about 3 tablespoons", "approximately 1/2 cup", "approximately 3 tablespoons")
EQUIV_QUANTITY_UNIT_GROUPS = re.compile(r'\b(' + EQUIVALENT_ALT + r')\b\s*.*?\s*\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')

QUANTITY_WITH_DIMENSION_UNITS_MAP = {}
for dimension_unit in _constants.DIMENSION_UNITS_SET:
    QUANTITY_WITH_DIMENSION_UNITS_MAP[dimension_unit] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)[-\s]*' + dimension_unit + r'\b', re.IGNORECASE)

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------- Generic number patterns and numbers w/ specific separators -----------------------------
# Patterns for matching:
# - a number/decimal/fraction followed by a space and then another number/decimal/fraction
# - a number/decimal/fraction followed by a space and then another number/decimal/fraction followed by a unit
# - a number/decimal/fraction followed by a space and then a denominator word
# - a number/decimal/fraction followed by a space and then a fraction word
# - a number/decimal/fraction followed by a space and then a fraction word (capture groups)
# - numbers separated by "and" or "&" (e.g. "1/2 and 3/4", "1/2 & 3/4")
# - numbers separated by "and", "&", "+", or "plus" (e.g. "1/2 and 3/4", "1/2 & 3/4") # NOTE: same as above with "+" and "plus" added
# - a number followed by 0+ whitespaces and then another number
# ----------------------------------------------------------------------------------------------------------------------

# Match ALL numbers in a string regardless of padding
ALL_NUMBERS = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)')

NUMBER_WITH_FRACTION_WORD = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*[-\s]*\s*)(?:' + FRACTION_WORDS_ALT + r')\b')

# # capture groups for above pattern
NUMBER_WITH_FRACTION_WORD_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*[-\s]*\s*)(' + FRACTION_WORDS_ALT + r')\b', re.IGNORECASE)

NUMBER_WITH_FRACTION_WORD_MAP = {}
for word, fraction in _constants.FRACTION_WORDS.items():
    NUMBER_WITH_FRACTION_WORD_MAP[word] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)[-\s]*' + word + r'\b', re.IGNORECASE)

NUMBERS_SEPARATED_BY_ADD_SYMBOLS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&|\+|plus)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')

# regex for matching numbers/fractions/decimals separated by "and", "&", "+", or "plus" (e.g. "1/2 and 3/4", "1/2 & 3/4") # NOTE: same as above with "+" and "plus" added
NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:and|&|\+|plus))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)

# Match any number/decimal/fraction followed by a space and then a number/decimal/fraction (Currently used version)
# (e.g "1 1/2", "3 1/4", "3 0.5", "2.5 3/4")
SPACE_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s+(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # NOTE: New version (good to go) (testing out, this ones safer, because the removal of the "+" after first group)
# SPACE_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)+\s+(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # NOTE: Original working version (risky regex though)
# # matches any number/decimals/fractions followed by 1+ spaces then a fraction word (e.g. "1 half", "1 quarter")
# NUMBER_WITH_FRACTION_WORD = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*[-\s]*\s*)(?:' + FRACTION_WORDS_ALT + r')\b')
# # NUMBER_WITH_FRACTION_WORD = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + FRACTION_WORDS_ALT + r')\b')

# # capture groups for above pattern
# NUMBER_WITH_FRACTION_WORD_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*[-\s]*\s*)(' + FRACTION_WORDS_ALT + r')\b', re.IGNORECASE)

# NUMBER_WITH_FRACTION_WORD_MAP = {}
# for word, fraction in _constants.FRACTION_WORDS.items():
#     NUMBER_WITH_FRACTION_WORD_MAP[word] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)[-\s]*' + word + r'\b', re.IGNORECASE)

# --------------------------------------------------------------------------------------------------
# --------------------------- RANGE PATTERNS ----------------------------------
# Patterns to match a number followed by a hyphen and then another number
# Handles cases with whole numbers, decimals, and fractions:
# - Whole number - Whole number
# - Whole number - Decimal
# - Whole number - Fraction
# - Decimal - Decimal
# - Decimal - Whole number
# - Decimal - Fraction
# - Fraction - Fraction
# - Fraction - Decimal
# - Fraction - Whole number
# Range patterns for some common language patterns:
# - "1/2 to 3/4"
# - "1/2 or 3/4"
# - "between 1/2 and 3/4"
# --------------------------------------------------------------------------------------------------

# matches ANY numbers/decimals/fractions followed by a hypen to ANY numbers/decimals/fractions 
# This pattern does a really good job of matching almost ANY hypen separated numbers in a string

# Best quantity pattern with word boundaries (version WITHOUT word boundaries was what was originally used but the word boundaries lower the risk of catastrophic backtracking)
QUANTITY_DASH_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?\b") # NOTE:Golden child with word boundaries for safety (GOOD TO GO)
# QUANTITY_DASH_QUANTITY = re.compile(r"\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?") # NOTE: this is the golden child, WITHOUT WORD BOUNDARDIES (GOOD TO GO)
# QUANTITY_DASH_QUANTITY = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*[-\s]+\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b')

# Capture groups version of the above pattern
QUANTITY_DASH_QUANTITY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?!\s*[a-zA-Z0-9])(?:[-\s]*)((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\b', re.IGNORECASE) # NOTE: safer new version (GOOD TO GO)
# QUANTITY_DASH_QUANTITY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?!\s*[a-zA-Z0-9])(?:\s*[-\s]*\s*)((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\b', re.IGNORECASE) # NOTE: Old dangerous version

# Matches ANY numbers/decimals/fractions followed by a hypen to ANY numbers/decimals/fractions followed by a unit (0+ whitespace between last number and unit)
QUANTITY_DASH_QUANTITY_UNIT = re.compile(r'\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?(?:\s*(?:' + ANY_UNIT_ALT + r'))?\b')
# QUANTITY_DASH_QUANTITY_UNIT_OG = re.compile(r'\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?\s*(?:' + ANY_UNIT_ALT + r')\b')

# These are sub patterns of the QUANTITY_DASH_QUANTITY that match specific types of numbers
# Likely these won't be used but they are here for reference, as a sanity check, 
# for testing, and to use as a starting point

# Starts with a whole number:
WHOLE_NUMBER_DASH_WHOLE_NUMBER = re.compile(r"\d+\s*-\s*\d+")
WHOLE_NUMBER_DASH_DECIMAL = re.compile(r"\d+\s*-\s*\d+\.\d+")
WHOLE_NUMBER_DASH_FRACTION = re.compile(r"\d+\s*-\s*\d+/\d+")

# Starts with a decimal:
DECIMAL_DASH_DECIMAL = re.compile(r"\d+\.\d+\s*-\s*\d+\.\d+")
DECIMAL_DASH_WHOLE_NUMBER = re.compile(r"\d+\.\d+\s*-\s*\d+")
DECIMAL_DASH_FRACTION = re.compile(r"\d+\.\d+\s*-\s*\d+/\d+")

# Starts with a fraction:
FRACTION_DASH_FRACTION = re.compile(r"\d+/\d+\s*-\s*\d+/\d+")
FRACTION_DASH_DECIMAL = re.compile(r"\d+/\d+\s*-\s*\d+\.\d+")
FRACTION_DASH_WHOLE_NUMBER = re.compile(r"\d+/\d+\s*-\s*\d+")

# Matches quantities (numbers) separated by "to" or "or" which indicates a range of ingredients typically (e.g. "1 to 4 cups", "2 or 3 cups")
QUANTITY_OR_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*or\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE)
QUANTITY_TO_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*to\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE)

# # match pattern for a range of number/decimal/fraction with "to" or "or" in between them (e.g. "1/2 to 3/4", "1/2 or 3/4", "1-to-2", "1-or-2", "1 to-2")
# QUANTITY_TO_OR_QUANTITY = re.compile(r'\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?:to|or|\s*-?\s*to\s*-?\s*|\s*-?\s*or\s*-?\s*)\s*(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))')
# # QUANTITY_TO_OR_QUANTITY = re.compile(r'\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?:to|or|-or-|-to-)\s*(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))')

# Regex pattern for matching "between" followed by a number/decimal/fraction, then "and" or "&", 
# and then another number/decimal/fraction (e.g. "between 1/2 and 3/4")
BETWEEN_QUANTITY_AND_QUANTITY = re.compile(r"\bbetween\b\s*\d+(?:/\d+|\.\d+)?\s*(?:and|&)\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE) # NOTE: NEW version (SAFE)
# BETWEEN_QUANTITY_AND_QUANTITY = re.compile(r'\bbetween\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s+(?:and|&)\s+(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))') # NOTE: OLD WORKING VERSION

# -----------------------------------------------------------------------------
# --------------------------- Fraction specific PATTERNS -----------------------
# Regular expressions for fraction specific pattern matching tasks
# Non standard forward slashes need to be replaced before matching them with the following patterns
# (i.e. replace U+2044 ( ⁄ ) with U+002f ( / ))
# Patterns to match:
# - General fraction match
# - match fraction parts in a string
# - match multi-part fractions in a string
# - match multi-part fractions with "and" or "&" in between the numbers
# - match whole numbers and fractions
# - match a number followed by a space and then a word and then a number or a fraction
# -----------------------------------------------------------------------------

# Regex pattern for fraction parts, finds all the fraction parts in a string (e.g. 1/2, 1/4, 3/4). 
# A number followed by 0+ white space characters followed by a number then a forward slash then another number.
# FRACTION_PATTERN = re.compile(r'\d*\s*/\s*\d+')

# NOTE: THIS is the working one
FRACTION_PATTERN = re.compile(r'\d+\s*/\s*\d+') # TODO: Current good to go basic fraction matter, below are some alternatives, not sure how safe they are though....
# FRACTION_PATTERN = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)?\s*/\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)?', re.IGNORECASE) # TODO: runner up, not sure if its completly safe though....
# FRACTION_PATTERN = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*/\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE) # TODO: Version 3 test

# Regex for capturing and splitting whitespace seperated numbers/decimals/fractions 
# (e.g. 1 1/2 -> ["1", "1/2"], "2 2.3 -> ["2", "2.3"])
SPLIT_SPACED_NUMS   = re.compile(r'^(\d+(?:/\d+|\.\d+)?)\s+(\d+(?:/\d+|\.\d+)?)$')
# NUMS_SPLIT_BY_SPACES = re.compile(r'^(\d+(?:/\d+|\.\d+)?)\s+(\d+(?:/\d+|\.\d+)?)$')


# the 9 types of fractions are:
# - Whole number / Whole number
# - Whole number / Decimal
# - Whole number / Fraction
# - Decimal / Decimal
# - Decimal / Whole number
# - Decimal / Fraction
# - Fraction / Fraction
# - Fraction / Decimal
# - Fraction / Whole number
FRACTION_TYPE_MAP = {
    # Put the decimal based patterns first (order matters)
    "DECIMAL_SLASH_DECIMAL": re.compile(r"\d+\.\d+\s*/\s*\d+\.\d+"),
    "DECIMAL_SLASH_NUMBER": re.compile(r"\d+\.\d+\s*/\s*\d+"),
    "DECIMAL_SLASH_FRACTION": re.compile(r"\d+\.\d+\s*/\s*\d+/\d+"),
    "FRACTION_SLASH_DECIMAL": re.compile(r"\d+/\d+\s*/\s*\d+\.\d+"),
    "NUMBER_SLASH_DECIMAL": re.compile(r"\d+\s*/\s*\d+\.\d+"),

    # the rest of the patterns without decimals
    "NUMBER_SLASH_NUMBER": re.compile(r"\d+\s*/\s*\d+"),
    "NUMBER_SLASH_FRACTION": re.compile(r"\d+\s*/\s*\d+/\d+"),
    "FRACTION_SLASH_FRACTION": re.compile(r"\d+/\d+\s*/\s*\d+/\d+"),
    "FRACTION_SLASH_NUMBER": re.compile(r"\d+/\d+\s*/\s*\d+")
}

# Any fractions with decimals, need to be handled first, hence the order definition here, if you want to find and 
# convert the fraction patterns in the FRACTION_TYPE_MAP, this is the recommended order to do so
FRACTION_TYPE_ORDER = ("DECIMAL_SLASH_DECIMAL", "DECIMAL_SLASH_NUMBER", "DECIMAL_SLASH_FRACTION", 
                           "FRACTION_SLASH_DECIMAL", "NUMBER_SLASH_DECIMAL", 
                           "NUMBER_SLASH_NUMBER", "NUMBER_SLASH_FRACTION", "FRACTION_SLASH_FRACTION", 
                           "FRACTION_SLASH_NUMBER")
# FRACTION_TYPE_MAP = {
#     # Starts with a decimal:
#     "DECIMAL_SLASH_DECIMAL": re.compile(r"\d+\.\d+\s*/\s*\d+\.\d+"),
#     "DECIMAL_SLASH_NUMBER": re.compile(r"\d+\.\d+\s*/\s*\d+"),
#     "DECIMAL_SLASH_FRACTION": re.compile(r"\d+\.\d+\s*/\s*\d+/\d+"),

#     # Starts with a whole number:
#     "NUMBER_SLASH_DECIMAL": re.compile(r"\d+\s*/\s*\d+\.\d+"),
#     "NUMBER_SLASH_NUMBER": re.compile(r"\d+\s*/\s*\d+"),
#     "NUMBER_SLASH_FRACTION": re.compile(r"\d+\s*/\s*\d+/\d+"),

#     # Starts with a fraction:
#     "FRACTION_SLASH_FRACTION": re.compile(r"\d+/\d+\s*/\s*\d+/\d+"),
#     "FRACTION_SLASH_DECIMAL": re.compile(r"\d+/\d+\s*/\s*\d+\.\d+"),
#     "FRACTION_SLASH_NUMBER": re.compile(r"\d+/\d+\s*/\s*\d+")
# }

# FRACTION_PATTERN = re.compile(r'\d+\s*/\s*\d+') # TODO: Testing new fraction pattern, old pattern would match even if there was NOT a number in front of the forward slash...
# FRACTION_PATTERN2 = re.compile(r'\b(\d*\.\d+|\d+)\s*/\s*(\d*\.\d+|\d+)\b')
# NUMBER_SLASH_NUMBER = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)?\s*/\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)?', re.IGNORECASE)
# NUMBER_SLASH_NUMBER = re.compile(r"\d+(?:/\d+|\.\d+)?\s*/\s*\d+(?:/\d+|\.\d+)?", re.IGNORECASE) # NOTE: NEW version (SAFE)


# -----------------------------------------------------------------------------
# --------------------------- Repeated strings PATTERNS -----------------------
# Patterns to match specific cases when a known unit string is repeated in a string
# This is typically seen in ranges where the unit appears after both quantities (e.g. 100 g - 200 g)
# These regular expressions are used for removing the unit from the string if its repeated
# -----------------------------------------------------------------------------

# TODO: this needs an overhaul to be safer (maybe use QUANTITY_UNIT_DASH_QUANTITY_UNIT or QUANTITY_UNIT_X_QUANTITY_UNIT)
# Regex pattern to match hypen seperated numbers/decimals/fractions followed by a unit
REPEAT_UNIT_RANGES = re.compile(r'(\d+(?:\.\d+|/\d+)?)\s*([a-zA-Z]+)\s*-\s*(\d+(?:\.\d+|/\d+)?)\s*([a-zA-Z]+)')
# REPEAT_UNIT_RANGES = re.compile(r'(\d+)\s*([a-zA-Z]+)\s*-\s*(\d+)\s*([a-zA-Z]+)')

# TODO: Use the same logic in QUANTITY_UNIT_DASH_QUANTITY_UNIT in REPEAT_UNIT_RANGES
# matches a number followed by a space and then a word and then an "-" followed by a another number or then a word
QUANTITY_UNIT_DASH_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))(?:\s*(?:-))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))\b', re.IGNORECASE)
# QUANTITY_UNIT_DASH_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))(?:\s*(?:-))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))\b', re.IGNORECASE)

# matches a number followed by a space and then a word and then an "x" or an "X" followed by a another number or then a word
QUANTITY_UNIT_X_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))(?:\s*(?:x|X))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))\b', re.IGNORECASE)
# QUANTITY_UNIT_X_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))(?:\s*(?:x|X))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))\b', re.IGNORECASE)

# matches a number followed by a space and then a word and then an "by followed by a another number or then a word
QUANTITY_UNIT_BY_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))(?:\s*(?:by))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))\b', re.IGNORECASE)
# QUANTITY_UNIT_BY_QUANTITY_UNIT = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))(?:\s*(?:by))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:[a-zA-Z]+))\b', re.IGNORECASE)

# TODO: This is "QUANTITY_UNIT_X_QUANTITY_UNIT" combined with "QUANTITY_UNIT_BY_QUANTITY_UNIT", probably can just use this versions instead
# Matches a number followed by a space and then a word and then an "x", "X", or "by" followed by a another number or then a word (i.e. "salmon steak, 1 inch by 2 inch")
DIMENSION_RANGES = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))(?:\s*(?:x|X|by))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))\b', re.IGNORECASE)

# matches a number followed by a space and then an "x", "X", or "by" followed by a another number or then a word 
SINGLE_DIMENSION_UNIT_RANGES = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*(?:\s*(?:x|X|by))\s*((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*((?:[a-zA-Z]+))\b', re.IGNORECASE)

# number separated by 0+ whitespace and then an "x" or "X" and then another number
NUMBER_X_NUMBER = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:x|X))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)

# number separated by 0+ whitespace and then "by" and then another number
NUMBER_BY_NUMBER = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:by))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)


# -----------------------------------------------------------------------------
# --------------------------- Parenthesis patterns -----------------------------
# Patterns for converting: 
# - Pattern for matching strings wrapped in parentheses
# - Pattern for matching parentheses containing only a whole number, decimal, or fraction
# - Pattern for matching parentheses containing a number followed by a unit
# -----------------------------------------------------------------------------

# Split string by instances of open and close parentheses (e.g. "1 cup of oats (2 ounces) in a big mixing bowl" -> ["1 cup of oats ", " in a big mixing bowl"]
# When used with re.split() the string will be split on the set of open/close parentheses and the parantheses and the text inside them will be removed from the list
SPLIT_BY_PARENTHESIS = re.compile(r'\(.*?\)')  # use with re.split()  # TODO: DELETE (DEPRECATED)

# Regular expression to match parentheses containing only a whole number, decimal, or fraction
PARENTHESIS_WITH_NUMBERS_ONLY = re.compile(r'\(\s*(\d*(?:\.\d+|\s*/\s*\d+|\d+))\s*\)') # TODO: Vulnerable regex (DEPRECATED)

# -----------------------------------------------------------------------------
# --------------------------- Misc. patterns -----------------------------
# Patterns for converting: 
# - Pattern for finding consecutive letters and digits in a string so whitespace can be added
# - pattern for matching "x" or "X" after numbers
# - pattern for matching "x" or "X" after numbers and not followed by another character
# - pattern for matching a quantity followed by "x" or "X" and then another quantity
# - pattern for matching optional strings (e.g. "option" or "optional")
# - pattern for matching required strings (e.g. "required" or "requirement")
# - pattern for matching words ending in "ly" (e.g. "firmly", "lightly", "rapidly")
# -----------------------------------------------------------------------------

# Regular expression to match consecutive letters and digits in a string
CONSECUTIVE_LETTERS_DIGITS = re.compile(r'([a-zA-Z]+)(\d+)|(\d+)([a-zA-Z]+)') # TODO: Delete, this doesn't get used anymore

# Match any number/decimal/fraction followed by 'x' or 'X' and 
# is NOT followed by another character after the x (removes possiblity of accidently matching a word that starts with X after a number)
# (e.g "1 x 5" matches "1 x", "1X1.5" matches "1X", "2.5x20" matches "2.5x", "1 xillion" mathces [])
X_AFTER_NUMBER = re.compile(r'(?:\d*\.\d+|\d+\s*\/\s*\d+|\d+)+\s*[xX](?![a-zA-Z])')

# Regular expression to match optional strings (e.g. "option" or "optional")
OPTIONAL_STRING = re.compile(r'\b(?:option|options|optional|opt.|opts.|opt|opts|unrequired)\b')

# Regular expression to match required strings (e.g. "required" or "requirement")
REQUIRED_STRING = re.compile(r'\b(?:required|requirement|req.|req)\b')

# matches any word ending in "ly" (e.g. "firmly", "lightly", "rapidly")
# we use this to remove adverbs from the ingredient names (e.g. "lightly beaten eggs" -> "beaten eggs")
WORDS_ENDING_IN_LY = re.compile(r'\b\w+ly\b')

# create a map containg regexs for matching a number followed by a "%", "percent", or "pct" string
PCT_REGEX_MAP = {}

for pct_string in ["%", "percent", "pct"]:
    PCT_REGEX_MAP[pct_string] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*' + pct_string + r'')

# create a map containg regexs for matching a number followed by a "%", "percent", or "pct" string
# NUMBER_WITH_DIMENSIONS_SYMBOLS_MAP = {}

# NUMBER_WITH_INCH_SYMBOL.findall("1 1/2\"")
# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\"')
# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\”')
# NUMBER_WITH_INCH_SYMBOL = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*\"')

NUMBER_WITH_INCH_SYMBOL_MAP = {}
for inch_symbol in ["\"", "”"]:
    NUMBER_WITH_INCH_SYMBOL_MAP[inch_symbol] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*' + inch_symbol + r'')

# # -----------------------------------------------------------------------------
# # ---------------------------- OLD IngredientTools class... ---------------------------------
# # -----------------------------------------------------------------------------
    
# # -----------------------------------------------------------------------------
# # --------------------------- Class to store all regex patterns -----------------------
# # A class to hold all regex patterns used in the recipe parser (version 2)
# # - Each pattern is stored as a class attribute and the class 
# # - IngredientTools class has a single method that applies ALL of the 
# #     regex patterns to a given string and return a dictionary of matches (for testing mainly)
# # -----------------------------------------------------------------------------
# # regex variables and maps to put in the class:
# class IngredientTools:
#     """
#     A class to hold all regex patterns used in recipe parsing.
#     """

#     def __init__(self) -> None:
#         # Constant data values and lookup tables
#         self.constants = {

#             # regex hashmaps
#             "NUMBER_WORDS": _constants.NUMBER_WORDS,
#             "NUMBER_PREFIX_WORDS": _constants.NUMBER_PREFIX_WORDS,
#             "MULTI_FRACTION_WORDS": _constants.MULTI_FRACTION_WORDS,
#             "FRACTION_WORDS": _constants.FRACTION_WORDS,
#             # "DENOMINATOR_WORDS": _constants.DENOMINATOR_WORDS,
#             "UNICODE_FRACTIONS": _constants.UNICODE_FRACTIONS,
            
#             # unit hashmaps
#             "UNITS": _constants.UNITS,
#             "BASIC_UNITS": _constants.BASIC_UNITS,
#             "VOLUME_UNITS": _constants.VOLUME_UNITS,
#             "WEIGHT_UNITS": _constants.WEIGHT_UNITS,
#             "DIMENSION_UNITS": _constants.DIMENSION_UNITS,
#             "CASUAL_UNITS": _constants.CASUAL_UNITS,

#             # unit hashsets
#             "UNITS_SET": _constants.UNITS_SET,
#             "BASIC_UNITS_SET": _constants.BASIC_UNITS_SET,
#             "NON_BASIC_UNITS_SET": _constants.NON_BASIC_UNITS_SET, 
#             "VOLUME_UNITS_SET": _constants.VOLUME_UNITS_SET,
#             "WEIGHT_UNITS_SET": _constants.WEIGHT_UNITS_SET,
#             "DIMENSION_UNITS_SET": _constants.DIMENSION_UNITS_SET,
#             "SIZE_MODIFIERS_SET": _constants.SIZE_MODIFIERS_SET,
#             "CASUAL_UNITS_SET": _constants.CASUAL_UNITS_SET,
#             "CASUAL_QUANTITIES_SET": _constants.CASUAL_QUANTITIES_SET,

#             "CASUAL_QUANTITIES": _constants.CASUAL_QUANTITIES,
#             "UNIT_MODIFIERS": _constants.UNIT_MODIFIERS,
#             "PREP_WORDS": _constants.PREP_WORDS,
#             "APPROXIMATE_STRINGS": _constants.APPROXIMATE_STRINGS,
#             "QUANTITY_PER_UNIT_STRINGS": _constants.QUANTITY_PER_UNIT_STRINGS,
#             "UNIT_TO_STANDARD_UNIT": _constants.UNIT_TO_STANDARD_UNIT,
#             "STOP_WORDS": _constants.STOP_WORDS,
#             "DASH_SYMBOLS": _constants.DASH_SYMBOLS,
#             'REMOVABLE_DASH_SYMBOLS': _constants.REMOVABLE_DASH_SYMBOLS
#         }

#         # Define regex patterns
#         # string numbers to number map
#         self.NUMBER_WORDS_MAP = NUMBER_WORDS_MAP
#         self.PREFIXED_NUMBER_WORDS = PREFIXED_NUMBER_WORDS
#         self.PREFIXED_NUMBER_WORDS_GROUPS = PREFIXED_NUMBER_WORDS_GROUPS

#         # unicode fractions
#         self.UNICODE_FRACTIONS_PATTERN = UNICODE_FRACTIONS_PATTERN
        
#         # unit matching patterns
#         self.UNITS_PATTERN = UNITS_PATTERN
#         self.BASIC_UNITS_PATTERN = BASIC_UNITS_PATTERN
#         self.NON_BASIC_UNITS_PATTERN = NON_BASIC_UNITS_PATTERN
#         self.VOLUME_UNITS_PATTERN = VOLUME_UNITS_PATTERN
#         self.SIZE_MODIFIERS_PATTERN = SIZE_MODIFIERS_PATTERN
#         self.PREP_WORDS_PATTERN = PREP_WORDS_PATTERN
#         self.STOP_WORDS_PATTERN = STOP_WORDS_PATTERN
#         self.CASUAL_QUANTITIES_PATTERN = CASUAL_QUANTITIES_PATTERN
#         self.CASUAL_UNITS_PATTERN = CASUAL_UNITS_PATTERN
#         self.DIMENSION_UNITS_PATTERN = DIMENSION_UNITS_PATTERN
#         self.UNIT_MODIFIERS_PATTERN = UNIT_MODIFIERS_PATTERN
#         self.APPROXIMATE_STRINGS_PATTERN = APPROXIMATE_STRINGS_PATTERN

#         # capture groups for getting anumber followed by the next closest units/basics units/non-basic units
#         self.QUANTITY_UNIT_GROUPS = QUANTITY_UNIT_GROUPS
#         self.QUANTITY_BASIC_UNIT_GROUPS = QUANTITY_BASIC_UNIT_GROUPS
#         self.QUANTITY_NON_BASIC_UNIT_GROUPS = QUANTITY_NON_BASIC_UNIT_GROUPS
#         self.QUANTITY_SOMETIMES_UNIT_GROUPS = QUANTITY_SOMETIMES_UNIT_GROUPS
#         self.QUANTITY_DIMENSION_UNIT_GROUPS = QUANTITY_DIMENSION_UNIT_GROUPS
#         self.QUANTITY_ANYTHING_UNIT_GROUPS = QUANTITY_ANYTHING_UNIT_GROUPS
#         self.QUANTITY_UNIT_ONLY_GROUPS = QUANTITY_UNIT_ONLY_GROUPS
#         self.EQUIV_QUANTITY_UNIT_GROUPS = EQUIV_QUANTITY_UNIT_GROUPS
        
#         # word fraction patterns
#         self.NUMBER_WITH_FRACTION_WORD = NUMBER_WITH_FRACTION_WORD
#         self.NUMBER_WITH_FRACTION_WORD_GROUPS = NUMBER_WITH_FRACTION_WORD_GROUPS
#         self.NUMBER_WITH_FRACTION_WORD_MAP = NUMBER_WITH_FRACTION_WORD_MAP

#         # generic number matchings and/or numbers with specific separators
#         self.ALL_NUMBERS = ALL_NUMBERS
#         self.SPACE_SEP_NUMBERS = SPACE_SEP_NUMBERS
#         self.NUMBERS_SEPARATED_BY_ADD_SYMBOLS = NUMBERS_SEPARATED_BY_ADD_SYMBOLS
#         self.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS = NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS

#         # range patterns
#         self.QUANTITY_DASH_QUANTITY = QUANTITY_DASH_QUANTITY
#         self.QUANTITY_DASH_QUANTITY_GROUPS = QUANTITY_DASH_QUANTITY_GROUPS
#         self.QUANTITY_DASH_QUANTITY_UNIT = QUANTITY_DASH_QUANTITY_UNIT
#         self.QUANTITY_OR_QUANTITY = QUANTITY_OR_QUANTITY
#         self.QUANTITY_TO_QUANTITY = QUANTITY_TO_QUANTITY
#         self.BETWEEN_QUANTITY_AND_QUANTITY = BETWEEN_QUANTITY_AND_QUANTITY

#         # fraction specific patterns
#         self.FRACTION_PATTERN = FRACTION_PATTERN
#         self.SPLIT_SPACED_NUMS = SPLIT_SPACED_NUMS
        
#         # repeated unit string patterns
#         self.REPEAT_UNIT_RANGES = REPEAT_UNIT_RANGES

#         # miscellaneous patterns
#         self.CONSECUTIVE_LETTERS_DIGITS = CONSECUTIVE_LETTERS_DIGITS

#         self.SPLIT_BY_PARENTHESIS = SPLIT_BY_PARENTHESIS

#         # "x" and "X" separators
#         self.X_AFTER_NUMBER = X_AFTER_NUMBER

#         # match specific strings 
#         self.OPTIONAL_STRING = OPTIONAL_STRING
#         self.REQUIRED_STRING = REQUIRED_STRING
#         self.WORDS_ENDING_IN_LY = WORDS_ENDING_IN_LY
#         self.PCT_REGEX_MAP = PCT_REGEX_MAP
#         self.NUMBER_WITH_INCH_SYMBOL_MAP = NUMBER_WITH_INCH_SYMBOL_MAP

#         # get a list of all the attributes of the class in sorted order by name
#         self.sorted_keys = sorted(self.__dict__.keys(), key=lambda x: x[0])

#         # # Sort attributes by name
#         # self.sorted_attrs = sorted(self.__dict__.items(), key=lambda x: x[0])

#     def find_matches(self, input_string: str) -> Dict[str, List[Union[str, Tuple[str]]]]:
#         """
#         Find all matches in the input string for each regex pattern.
#         Returns a dictionary with pattern names as keys and corresponding matches as values.
#         """

#         matches = {}
#         for name, pattern in self.__dict__.items():
#             if isinstance(pattern, re.Pattern):
#                 matches[name] = pattern.findall(input_string)
#         return matches
    
#     def print_matches(self, input_string: str) -> None:
#         """
#         Print out all matches in the input string for each regex pattern.
#         Returns None
#         """
#         matches = {}
        
#         for key in self.sorted_keys:
#             attribute = self.__dict__[key]
#             if isinstance(attribute, re.Pattern):
#                 matches[key] = attribute.findall(input_string)
#                 print(f"{key}: {matches[key]}")

#         # matches = {}
#         # for name, pattern in self.__dict__.items():
#         #     if isinstance(pattern, re.Pattern):
#         #         matches[name] = pattern.findall(input_string)
#         #         print(f"{name}: {matches[name]}")

        
#     def list_constants(self) -> None:
#         """
#         List all the attributes of the class.
#         """ 

#         # attrs = [name for name in self.__dict__]

#         for name, pattern in self.__dict__.items():
#             print(f"- {name} ({type(self.__dict__[name]).__name__})")
#             if isinstance(self.__dict__[name], dict):
#                 print(f"  > {len(self.__dict__[name])} items")
#                 # for key, value in self.__dict__[name].items():
#                 #     print(f"   - {key}")
#         # return [name for name in self.__dict__ if isinstance(self.__dict__[name], re.Pattern)]
    
#     def get_desc(self, pattern_name: str) -> str:
#         """
#         Get the description of a specific regex pattern.
#         Returns the description of the pattern if found, otherwise returns an empty string.
#         """
        
#         # Define descriptions for each pattern
#         descriptions = {
#             ### Constants and lookup tables
#             "NUMBER_WORDS": "Dictionary of number words to numerical values.",
#             "MULTI_FRACTION_WORDS": "Dictionary of fraction phrases (i.e. 'two thirds' or '1 half') to their fractional string value",
#             "FRACTION_WORDS": "Dictionary of single fraction words that represent a singular fraction (i.e. a quarter is equal to 1/4).",
#             "UNICODE_FRACTIONS": "Dictionary of unicode fractions to numerical values.",

#             # dictionaries of units
#             "UNITS": "Dictionary of units used in the recipe parser (All units, including basic, volume, and specific units).",
#             "BASIC_UNITS": "Dictionary of basic units used in the recipe parser (The most common units).",
#             "VOLUME_UNITS": "Dictionary of volume units used in the recipe parser (Units used for measuring volume).",
#             "WEIGHT_UNITS": "Dictionary of weight units used in the recipe parser (Units used for measuring weight).",
#             "DIMENSION_UNITS": "Dictionary of dimension units used in the recipe parser (Units used for measuring dimensions).",
#             "CASUAL_UNITS": "Dictionary of casual units used in the recipe parser (Units that are not standard units).",

#             # sets of all unit words
#             "UNITS_SET": "Set of units used in the recipe parser (All units, including basic, volume, and specific units).",
#             "BASIC_UNITS_SET": "Set of basic units used in the recipe parser (The most common units).",
#             "NON_BASIC_UNITS_SET": "Set of non-basic units used in the recipe parser (Units that are not in the BASIC_UNITS dictionary).",
#             "SIZE_MODIFIERS_SET": "Set of units that are sometimes used in the recipe parser (Set of words that MIGHT be units if no other units are around).",
#             "VOLUME_UNITS_SET": "Set of volume units used in the recipe parser (Units used for measuring volume).",
#             "WEIGHT_UNITS_SET": "Set of weight units used in the recipe parser (Units used for measuring weight).",
#             "DIMENSION_UNITS_SET": "Set of dimension units used in the recipe parser (Units used for measuring dimensions).",
#             "CASUAL_UNITS_SET": "Set of casual units used in the recipe parser (Units that are not standard units).",
#             "CASUAL_QUANTITIES_SET": "Set of casual quantities used in the recipe parser (Quantities that are not standard quantities).",

#             "CASUAL_QUANTITIES": "Dictionary of casual quantities used in the recipe parser.",
#             "UNIT_MODIFIERS": "Set of unit modifier words for lookups in recipe parser.",
#             "PREP_WORDS": "Set of preparation words for lookups in recipe parser.",
#             "APPROXIMATE_STRINGS": "Set of strings that indicate an approximate quantity in the recipe parser.",
#             "QUANTITY_PER_UNIT_STRINGS": "Set of strings that indicate a quantity per unit in the recipe parser.",
#             "NUMBER_WORDS_MAP": "Dictionary of regex patterns to match number words in a string (i.e. 'one' : '1', 'two' : '2').",
            
#             ### Regex patterns

#             # simple unit matching patterns
#             "UNITS_PATTERN": "Matches units in a string.",
#             "BASIC_UNITS_PATTERN": "Matches just the basic units from the BASIC_UNITS dictionary.",
#             "NON_BASIC_UNITS_PATTERN": "Matches non-basic units in a string.",
#             "VOLUME_UNITS_PATTERN": "Matches specifically volume units in a string.",
#             "SIZE_MODIFIERS_PATTERN": "Matches sometimes units in a string.",
#             "PREP_WORDS_PATTERN": "Matches preparation words in a string.",
#             "STOP_WORDS_PATTERN": "Matches stop words in a string.",
#             "CASUAL_QUANTITIES_PATTERN": "Matches casual quantities in a string (i.e. 'couple' = 2).",
#             "CASUAL_UNITS_PATTERN": "Matches casual units in a string (i.e. 'dash', 'pinch').",
#             "DIMENSION_UNITS_PATTERN": "Matches dimension units in a string (i.e. 'inches', 'cm').",
#             "UNIT_MODIFIERS_PATTERN": "Matches unit modifiers in a string (i.e. 'large', 'small').",
#             "APPROXIMATE_STRINGS_PATTERN": "Matches approximate strings in a string (i.e. 'about', 'approximately').",

#             "QUANTITY_UNIT_GROUPS": "Matches a number followed by a unit with capture groups.", 
#             "QUANTITY_BASIC_UNIT_GROUPS": "Matches a number followed by a basic unit with capture groups.",
#             "QUANTITY_NON_BASIC_UNIT_GROUPS": "Matches a number followed by a non-basic unit with capture groups.",
#             "QUANTITY_SOMETIMES_UNIT_GROUPS": "Matches a number followed by a 'sometimes unit' with capture groups (i.e. 'large' is sometimes a unit if no other units are around).",
#             "QUANTITY_ANYTHING_UNIT_GROUPS": "Matches a number followed by any text and then a unit with capture groups.",
#             "QUANTITY_DIMENSION_UNIT_GROUPS": "Matches a number followed by a dimension unit with capture groups.",
#             "QUANTITY_UNIT_ONLY_GROUPS": "Matches a quantity followed by  0+whitespaces/hypens and then a unit with capture groups.",
#             "EQUIV_QUANTITY_UNIT_GROUPS": "Matches an 'approximate/equivalent' string followed by a number followed by a unit with capture groups (helpful for finding equivalent quantity-unit patterns i.e. 'about 1/2 cup').",

#             # general umber matching patterns and number with specific separators
#             "ALL_NUMBERS": "Matches ALL number/decimal/fraction in a string regardless of padding.",
#             "SPACE_SEP_NUMBERS": "Matches any number/decimal/fraction followed by a space and then another number/decimal/fraction.",
#             "NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS": "Matches numbers/decimals/fractions separated by 'and', '&', 'plus', or '+' symbols with capture groups.",

#             "QUANTITY_DASH_QUANTITY": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions.",
#             "QUANTITY_DASH_QUANTITY_GROUPS": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions with capture groups.",
#             "QUANTITY_DASH_QUANTITY_UNIT": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions followed by a unit (0+ whitespace between last number and the unit).",
#             "QUANTITY_OR_QUANTITY": "Matches numbers/decimals/fractions separated by 'or'.",
#             "QUANTITY_TO_QUANTITY": "Matches numbers/decimals/fractions separated by 'to'.",
#             "BETWEEN_QUANTITY_AND_QUANTITY": "Matches numbers/decimals/fractions separated by 'between' and 'and'.",
            
#             # Unicode fractions
#             "UNICODE_FRACTIONS_PATTERN": "Matches unicode fractions in the string.",
            
#             # fraction word patterns
#             "NUMBER_WITH_FRACTION_WORD_GROUPS": "Matches a number followed by a fraction word with capture groups.",
#             "NUMBER_WITH_FRACTION_WORD_MAP": "Dictionary of regex patterns to match number followed by a fraction word in a string (i.e. '1 half' : '1 1/2').",

#             # fraction specific patterns
#             "FRACTION_PATTERN": "Matches fraction parts in a string.",
#             "SPLIT_SPACED_NUMS": "Splits numbers/decimals/fractions separated by 1+ whitespaces into a capture group (i.e '1.5 1/2' -> ['1.5', '1/2']).",
#             "REPEAT_UNIT_RANGES": "Matches repeated unit strings in a string.",

#             "SPLIT_BY_PARENTHESIS": "Matches parentheses in a string and splits the string by them if used with re.split().",

#             "CONSECUTIVE_LETTERS_DIGITS": "Matches consecutive letters and digits in a string.",
#             "X_AFTER_NUMBER": "Matches a number followed by an 'x'/'X' (can't be the start of a word starting with xX).",
#             "OPTIONAL_STRING": "Matches the word 'optional', 'option', 'opt', etc. in a string.",
#             "REQUIRED_STRING": "Matches the word 'required', 'requirement', 'req', etc. in a string.",
#             "WORDS_ENDING_IN_LY": "Matches any word ending in 'ly' (i.e. 'firmly', 'lightly', 'rapidly').",
#             "PCT_REGEX_MAP" : "Dictionary of regex patterns to match numbers followed by a percentage character '%', 'percentage', 'percent', or 'pct'."
#         }

#         # Retrieve description based on pattern name
#         return descriptions.get(pattern_name, "")
    
# ##################################################################################################################
# ##################################################################################################################
# ########################################## OLD SETUP CODE BELOW ##################################################
# ##################################################################################################################

# # Description: This module contains all the regex patterns used in the recipe parser. 
# # As well as a class to hold all regex patterns used in the recipe parser (version 2)

# import re
# from typing import Dict, List, Tuple, Union

# # # import constants from _constants module
# from . import _constants 

# # # import for for local development
# # from ingredient_slicer import _constants

# # -----------------------------------------------------------------------------
# # --------------------------- Conversion patterns -----------------------------
# # Patterns for converting: 
# # - Fraction phrases/words to fraction strings (e.g. "one half" to "1/2")
# # - Number words to numerical values (e.g. "one" to "1")
# # - Unicode fractions to decimals (e.g. "½" to "0.5")
# # -----------------------------------------------------------------------------

# MULTI_FRACTION_WORDS_MAP = {}
# for phrase, fraction in _constants.MULTI_FRACTION_WORDS.items():
#     MULTI_FRACTION_WORDS_MAP[phrase] = [fraction, re.compile(r'\b' + phrase + r'\b', re.IGNORECASE)]

# NUMBER_WORDS_MAP = {}
# for word, value in _constants.NUMBER_WORDS.items():
#     NUMBER_WORDS_MAP[word] = [str(value), re.compile(r'\b' + word + r'\b', re.IGNORECASE)]

# # Matches unicode fractions in the string
# UNICODE_FRACTIONS_PATTERN = re.compile( r'\b(?:' + '|'.join(re.escape(word) for word in _constants.UNICODE_FRACTIONS.keys()) + r')\b', re.IGNORECASE)

# # standard_ingredient = "two third of a cups of flour, 1 half n half pint"

# # # print("Parsing fraction words")
# # for word, regex_data in MULTI_FRACTION_WORDS_MAP.items():
# #     fraction_str, pattern = regex_data
# #     # print(f"Word: '{word}'\n > Fraction string: '{fraction_str}'\n > Pattern: {pattern}")
# #     if pattern.search(standard_ingredient):
# #         print(f"Word: '{word}'\n > Fraction string: '{fraction_str}'\n > Pattern: {pattern}")
# #         print(f"Found {word} in ingredient. Replacing with {fraction_str}")
# #     print(f"----" * 5)
# #     print()
# #     # pattern = regex_data[1]
# #     # print statement if word is found in ingredient and replaced
# #     if pattern.search(self.standard_ingredient):
# #         print(f"- Found {word} in ingredient. Replacing with {regex_data[0]}") if self.debug else None
# #     self.standard_ingredient = pattern.sub(regex_data[0], self.standard_ingredient)

# # -----------------------------------------------------------------------------
# # --------------------------- Alternation patterns -----------------------------
# # ---> NOTE: the main Alternation patterns for various units are created here and these get used in many of the other regular expression
# # -----------------------------------------------------------------------------
# # ---- Set up Alternation patterns from list of possible units and their variants ----

# # Generate the regular expression pattern for units in the string
# ANY_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.UNITS.values() for unit in variants_list])
# # ANY_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.UNITS.values())
# # ANY_UNIT_ALT = '|'.join('|'.join(re.escape(variant) for variant in variants) for variants in _constants.UNITS.values())

# # just the basic units 
# BASIC_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.BASIC_UNITS.values() for unit in variants_list])
# # BASIC_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.BASIC_UNITS.values())

# # just the non-basic units
# NON_BASIC_UNIT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.NON_BASIC_UNITS_SET)])
# # NON_BASIC_UNIT_ALT = '|'.join(list(_constants.NON_BASIC_UNITS_SET))

# # Generate the regular expression pattern for units in the string
# VOLUME_UNIT_ALT = '|'.join([re.escape(unit) for variants_list in _constants.VOLUME_UNITS.values() for unit in variants_list])
# # VOLUME_UNIT_ALT = '|'.join('|'.join(variants) for variants in _constants.VOLUME_UNITS.values())

# # The "sometimes might be a unit" strings as a "or" pattern
# SOMETIMES_UNIT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.SIZE_MODIFIERS_SET)])
# # SOMETIMES_UNIT_ALT = '|'.join(list(_constants.SIZE_MODIFIERS_SET))

# # get a pattern for the "approximate" strings (these are typically used to describe an equivelant amount of a unit)
# EQUIVALENT_ALT = '|'.join([re.escape(unit) for unit in list(_constants.APPROXIMATE_STRINGS)])
# # EQUIVALENT_ALT = '|'.join(list(_constants.APPROXIMATE_STRINGS))

# # prep word alternate
# PREP_WORD_ALT = '|'.join([re.escape(prep_word) for prep_word in list(_constants.PREP_WORDS)])

# # sort the stopwords by their length to make sure longer stopwords get matched before shorter ones
# #  to make sure we don't match a shorter stopword that is part of a longer stopword
# STOP_WORDS_ALT = '|'.join(sorted([re.escape(stop_word) for stop_word in _constants.STOP_WORDS], key=len, reverse=True))
# # STOP_WORDS_ALT = '|'.join([re.escape(stop_word) for stop_word in list(_constants.STOP_WORDS)])


# FRACTION_WORDS_ALT = '|'.join([re.escape(fraction_word) for fraction_word in _constants.FRACTION_WORDS])

# # sort the denominator words by their length to make sure longer words get matched before shorter ones
# #  to make sure we don't match a shorter word that is part of a longer word
# DENOMINATOR_WORDS_ALT = '|'.join(sorted([re.escape(word) for word in _constants.DENOMINATOR_WORDS], key=len, reverse=True))
# # DENOMINATOR_WORDS_ALT = '|'.join([re.escape(word) for word in _constants.DENOMINATOR_WORDS])

# # Alternations for creating patterns that match prefix number words followed by number words (e.g "twenty five", "thirty three")
# NUMBER_WORDS_ALT = '|'.join([re.escape(word) for word in _constants.NUMBER_WORDS])
# NUMBER_PREFIX_WORD_ALT = '|'.join([re.escape(word) for word in _constants.NUMBER_PREFIX_WORDS])

# # Alternations for patterns like "a pinch of" or "a handful" or "a sprinkle"
# CASUAL_UNITS_ALT        = '|'.join([re.escape(casual_unit) for casual_unit in _constants.CASUAL_UNITS_SET])
# CASUAL_QUANTITIES_ALT   = '|'.join([re.escape(casual_quantity) for casual_quantity in _constants.CASUAL_QUANTITIES_SET])

# # alternations for remvoing useless words from the string when trying to find the food item
# DIMENSION_UNITS_ALT     = '|'.join([re.escape(unit) for unit in _constants.DIMENSION_UNITS_SET])
# UNIT_MODIFIERS_ALT      = '|'.join([re.escape(unit_modifier) for unit_modifier in _constants.UNIT_MODIFIERS])
# APPROXIMATE_STRINGS_ALT = '|'.join([re.escape(approximate_string) for approximate_string in _constants.APPROXIMATE_STRINGS])


# # -----------------------------------------------------------------------------
# # --------------------------- Units patterns -----------------------------
# # ---> NOTE: uses the above Alternation patterns to create the following basic regular expression patterns
# # - units in a string
# # - matching a number followed by a unit
# # - matching a unit followed by a number
# # -----------------------------------------------------------------------------
# # ---- Use the unit varients to create the regular expression patterns ----

# # create a regular expression pattern to match the units in a string
# UNITS_PATTERN = re.compile(r'\b(?:' + ANY_UNIT_ALT + r')\b', re.IGNORECASE)
# # UNITS_PATTERN = re.compile(r'\b(?:' + '|'.join('|'.join(variants) for variants in UNITS.values()) + r')\b', re.IGNORECASE)

# # match just the basic units
# BASIC_UNITS_PATTERN = re.compile(r'\b(?:' + BASIC_UNIT_ALT + r')\b', re.IGNORECASE)

# # match just the non-basic units
# NON_BASIC_UNITS_PATTERN = re.compile(r'\b(?:' + NON_BASIC_UNIT_ALT + r')\b', re.IGNORECASE)

# # match the "sometimes might be a unit" strings
# SIZE_MODIFIERS_PATTERN = re.compile(r'\b(?:' + SOMETIMES_UNIT_ALT + r')\b', re.IGNORECASE)
# # SIZE_MODIFIERS_PATTERN = re.compile(r'\b(?:' + '|'.join(SIZE_MODIFIERS_SET) + r')\b', re.IGNORECASE)

# # create a regular expression pattern to match specifically volume units in a string
# VOLUME_UNITS_PATTERN = re.compile(r'\b(?:' + VOLUME_UNIT_ALT + r')\b', re.IGNORECASE)

# # generic prep words pattern for matching prep words in a string
# PREP_WORDS_PATTERN = re.compile(r'\b(?:' + PREP_WORD_ALT + r')\b', re.IGNORECASE)

# # general stop words pattern for matching stop words in a string
# STOP_WORDS_PATTERN = re.compile(r'\b(?:' + STOP_WORDS_ALT + r')\b', re.IGNORECASE)

# # match word versions of fractions in a string (e.g. "half", "thirds")
# FRACTION_WORDS_PATTERN = re.compile(r'\b(?:' + FRACTION_WORDS_ALT + r')\b', re.IGNORECASE)

# # patterns for things like "a pinch of" or "a handful" or "a sprinkle"
# CASUAL_UNITS_PATTERN       = re.compile(r'\b(?:' + CASUAL_UNITS_ALT + r')\b', re.IGNORECASE) # e.g. "bunch", "sprig", "stalk", "stick", "piece", "slice", "strip", "strip", "segment", "wedge", "chunk", "hunk", "slab", "sliver", "shred", "shard", "scrap", "scrape", "scraping", "scrapings
# CASUAL_QUANTITIES_PATTERN   = re.compile(r'\b(?:' + CASUAL_QUANTITIES_ALT + r')\b', re.IGNORECASE) # e.g. "a few", "a couple", "a handful", "a pinch", "a sprinkle", "a dash", "a smidgen", "a touch", "a bit"

# # Miscellaneous patterns used for trimmin the string down to get the food item 
# DIMENSION_UNITS_PATTERN     = re.compile(r'\b(?:' + DIMENSION_UNITS_ALT + r')\b', re.IGNORECASE) # e.g. "inch", "inches", "cm", "mm", "millimeter", "millimeters", "centimeter", "centimeters"
# UNIT_MODIFIERS_PATTERN      = re.compile(r'\b(?:' + UNIT_MODIFIERS_ALT + r')\b', re.IGNORECASE) # e.g. "large", "small", "medium
# APPROXIMATE_STRINGS_PATTERN = re.compile(r'\b(?:' + APPROXIMATE_STRINGS_ALT + r')\b', re.IGNORECASE) # e.g. "about", "approximately", "around", "roughly", "nearly", "almost


# # -----------------------------------------------------------------------------
# # --------------------------- Prefix number words with number words patterns -----------------------------
# # Patterns for matching:
# # - prefix number words followed by number words (e.g "twenty five", "thirty three")
# # -----------------------------------------------------------------------------

# # regular expression pattern to match prefix number words followed by number words
# PREFIXED_NUMBER_WORDS = re.compile(r'\b(?:' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*[-\s]*\s*)(?:' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)
# # PREFIXED_NUMBER_WORDS = re.compile(r'\b(?:' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*|\s*-*\s*)(?:' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)

# # PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')(?:\s*[-\s]*\s*)(' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE) # OG
# PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')(?:[-\s]*)(' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE) # NEW
# # PREFIXED_NUMBER_WORDS_GROUPS = re.compile(r'\b(' + NUMBER_PREFIX_WORD_ALT + r')[-\s](' + NUMBER_WORDS_ALT + r')\b', re.IGNORECASE)

# PREFIXED_NUMBER_WORDS_MAP = {}
# for prefix_word, prefix_number in _constants.NUMBER_PREFIX_WORDS.items():
#     for number_word, number_value in _constants.NUMBER_WORDS.items():
#         PREFIXED_NUMBER_WORDS_MAP[prefix_word + " " + number_word] = [str(prefix_number + number_value), re.compile(r'\b' + prefix_word + r'(?:[-\s]*)' + number_word + r'\b', re.IGNORECASE)]

# # ----------------------------------------------------------------------------------------------------------------------
# # --------------------------- Unit/Number or Number/Unit patterns -----------------------------
# # Patterns for matching:
# # - a number followed by a unit
# # - a unit followed by a number
# # - a number followed by a unit followed by any text (full unit and abbreviation)
# # - a unit followed by a number followed by any text (full unit and abbreviation)
# # - a number/decimal/fraction followed by a space and then another number/decimal/fraction
# # - a number/decimal/fraction followed by a space and then another number/decimal/fraction followed by a unit
# # -----------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------

# # Construct the regular expression pattern that matches the number (including fractions and decimals)
# # followed by 0+ spaces and then a unit in UNITS dictionary
# ANY_NUMBER_THEN_UNIT = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + ANY_UNIT_ALT + r')\b')
# # ANY_NUMBER_THEN_UNIT = r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + ANY_UNIT_ALT + r')\b'

# # Construct the regular expression pattern that matches the number (including fractions and decimals)
# # followed by any text and then a unit in UNITS dictionary
# ANY_NUMBER_THEN_ANYTHING_THEN_UNIT = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*.*?\s*(?:' + ANY_UNIT_ALT + r')\b')

# # same as above but with 2 capture groups (number and unit)
# ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS  = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s+(\S*\b(?:' + ANY_UNIT_ALT + r'))\b')
# # ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS2 = re.compile(r'\b(\d+)\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')

# r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(can|cup|cups|cabin)\b'
# # same as above but with 2 capture groups (number and unit, either basic, non-basic, or any unit)
# QUANTITY_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')
# QUANTITY_BASIC_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + BASIC_UNIT_ALT + r')\b')
# QUANTITY_NON_BASIC_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + NON_BASIC_UNIT_ALT + r')\b')
# QUANTITY_SOMETIMES_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + SOMETIMES_UNIT_ALT + r')\b')
# QUANTITY_DIMENSION_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + DIMENSION_UNITS_ALT + r')\b')

# QUANTITY_ANYTHING_UNIT_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')

# # restrictive quantity unit group matcher, matches a quantity number followed by 0+ whitespaces/0+ hyphens and then a unit in ANY_UNIT_ALT
# # (i.e. "1 cup", "1-1/2 cup", "12 -- cup")
# QUANTITY_UNIT_ONLY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*[-\s]*\b(' + ANY_UNIT_ALT + r')\b')

# # Pattern for finding quantity unit patterns that are preceeded by an "equivalent" string 
# # (i.e. "about 1/2 cup", "about 3 tablespoons", "approximately 1/2 cup", "approximately 3 tablespoons")
# EQUIV_QUANTITY_UNIT_GROUPS = re.compile(r'\b(' + EQUIVALENT_ALT + r')\b\s*.*?\s*\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')
# # EQUIV_QUANTITY_UNIT_GROUPS = re.compile(r'\b(' + EQUIVALENT_ALT + r')\s+((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')
# # EQUIVALENT_QUANTITY_UNIT_GROUPS = re.compile(r'\b(' + EQUIVALENT_ALT + r')\s+((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\s*.*?\s*\b(' + ANY_UNIT_ALT + r')\b')

# # a number/decimal/fraction followed by 1+ spaces to another number/decimal/fraction followed by a 0+ spaces then a VOLUME unit
# # (e.g. 1/2 cup, 1 1/2 cups, 1 1/2 tablespoon)
# SPACED_NUMS_THEN_VOLUME_UNITS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)+\s*(?:\d+/\d+|\d+\.\d+)\s*(?:' + VOLUME_UNIT_ALT + r')\b')

# # Construct the regular expression pattern that matches the number (including fractions and decimals)
# # followed by 0+ spaces and then a unit in UNITS dictionary (EXPIREMENTAL, probably throw away)
# ANY_NUMBER_THEN_UNIT_CAPTURE = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(.*?)*(?:' + ANY_UNIT_ALT + r')\b')

# # Construct the regular expression pattern that matches the unit followed by 0+ spaces
# # and then a number (including fractions and decimals)
# UNIT_THEN_ANY_NUMBER = re.compile(r'\b(?:' + ANY_UNIT_ALT + r')\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b')
# # UNIT_THEN_ANY_NUMBER = r'\b(?:' + ANY_UNIT_ALT + r')\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b'

# # Regex to match number (QUANTITY) then unit abbreviation (single string as unit)
# NUMBER_THEN_UNIT_ABBR = re.compile(r"(\d)\-?([a-zA-Z])") # 3g = 3 g

# # Regex to match number (QUANTITY) then unit word (full word string as unit)
# NUMBER_THEN_UNIT_WORD = re.compile(r"(\d+)\-?([a-zA-Z]+)") #  "3tbsp vegetable oil" = 3 tbsp

# # ----------------------------------------------------------------------------------------------------------------------
# # --------------------------- Generic number patterns and numbers w/ specific separators -----------------------------
# # Patterns for matching:
# # - a number/decimal/fraction followed by a space and then another number/decimal/fraction
# # - a number/decimal/fraction followed by a space and then another number/decimal/fraction followed by a unit
# # - a number/decimal/fraction followed by a space and then a denominator word
# # - a number/decimal/fraction followed by a space and then a fraction word
# # - a number/decimal/fraction followed by a space and then a fraction word (capture groups)
# # - numbers separated by "and" or "&" (e.g. "1/2 and 3/4", "1/2 & 3/4")
# # - numbers separated by "and", "&", "+", or "plus" (e.g. "1/2 and 3/4", "1/2 & 3/4") # NOTE: same as above with "+" and "plus" added
# # - a number followed by 0+ whitespaces and then another number
# # ----------------------------------------------------------------------------------------------------------------------

# # Match ALL numbers in a string regardless of padding
# ALL_NUMBERS = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)')

# # # Regular expression pattern to match any number/decimals/fraction in a string padded by atleast 1+ whitespaces
# # ANY_NUMBER = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # TODO: (DEPRECATED)

# # # matches any number/decimals/fractions followed by 1+ spaces then a denominator word
# # NUMBER_WITH_DENOMINATOR = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*[-\s]*\s*)(?:' + DENOMINATOR_WORDS_ALT + r')\b') # TODO: (DEPRECATED)
# # # NUMBER_WITH_DENOMINATOR = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + DENOMINATOR_WORDS_ALT + r')\b')

# # matches any number/decimals/fractions followed by 1+ spaces then a fraction word (e.g. "1 half", "1 quarter")
# NUMBER_WITH_FRACTION_WORD = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*[-\s]*\s*)(?:' + FRACTION_WORDS_ALT + r')\b')
# # NUMBER_WITH_FRACTION_WORD = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + FRACTION_WORDS_ALT + r')\b')

# # capture groups for above pattern
# NUMBER_WITH_FRACTION_WORD_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*[-\s]*\s*)(' + FRACTION_WORDS_ALT + r')\b', re.IGNORECASE)

# NUMBER_WITH_FRACTION_WORD_MAP = {}
# for word, fraction in _constants.FRACTION_WORDS.items():
#     NUMBER_WITH_FRACTION_WORD_MAP[word] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)[-\s]*' + word + r'\b', re.IGNORECASE)

# # for key, value in NUMBER_WITH_FRACTION_WORD_MAP.items():
# #     print(f"key: {key}")
# #     print(f"{key}: {value.findall('1--quarter cup of milk')}")
# #     print()
# # NUMBER_WITH_FRACTION_WORD_MAP['half']
# # _constants.FRACTION_WORDS

# # '(?:\\d*\\.\\d+|\\d+\\s*/\\s*\\d+|\\d+)\\s*pct' # NOTE: SAFE
# # for pct_string in pct_strings:
# #     PCT_REGEX_MAP[pct_string] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*' + pct_string + r'')
# ### (DEPRACTED version of SPACE_SEP_NUMBERS)
# # # Match any number/decimal/fraction followed by a space and then another number/decimal/fraction
# # # (e.g "1 1/2", "3 1/4", "3 0.5", "2.5 3/4")
# # SPACE_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)+\s*(?:\d+/\d+|\d+\.\d+)\b')

# # regex for matching numbers/fractions/decimals separated by "and" or "&" (e.g. "1/2 and 3/4", "1/2 & 3/4")
# AND_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')

# # regex for matching numbers/fractions/decimals separated by "and", "&", "+", or "plus" (e.g. "1/2 and 3/4", "1/2 & 3/4") # NOTE: same as above with "+" and "plus" added
# NUMBERS_SEPARATED_BY_ADD_SYMBOLS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*(?:and|&|\+|plus)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')
# # NUMBERS_SEPARATED_BY_ADD_SYMBOLS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:and|&|\+|plus)\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+))+\b')

# NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:and|&|\+|plus))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)

# # Match any number/decimal/fraction followed by a space and then a number/decimal/fraction (Currently used version)
# # (e.g "1 1/2", "3 1/4", "3 0.5", "2.5 3/4")
# SPACE_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s+(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # NOTE: New version (good to go) (testing out, this ones safer, because the removal of the "+" after first group)
# # SPACE_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)+\s+(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # NOTE: Original working version (risky regex though)

# # --------------------------------------------------------------------------------------------------
# # --------------------------- RANGE PATTERNS ----------------------------------
# # Patterns to match a number followed by a hyphen and then another number
# # Handles cases with whole numbers, decimals, and fractions:
# # - Whole number - Whole number
# # - Whole number - Decimal
# # - Whole number - Fraction
# # - Decimal - Decimal
# # - Decimal - Whole number
# # - Decimal - Fraction
# # - Fraction - Fraction
# # - Fraction - Decimal
# # - Fraction - Whole number
# # Range patterns for some common language patterns:
# # - "1/2 to 3/4"
# # - "1/2 or 3/4"
# # - "between 1/2 and 3/4"
# # --------------------------------------------------------------------------------------------------

# # matches ANY numbers/decimals/fractions followed by a hypen to ANY numbers/decimals/fractions 
# # This pattern does a really good job of matching almost ANY hypen separated numbers in a string

# # Best quantity pattern with word boundaries (version WITHOUT word boundaries was what was originally used but the word boundaries lower the risk of catastrophic backtracking)
# QUANTITY_DASH_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?\b") # NOTE:Golden child with word boundaries for safety (GOOD TO GO)
# # QUANTITY_DASH_QUANTITY = re.compile(r"\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?") # NOTE: this is the golden child, WITHOUT WORD BOUNDARDIES (GOOD TO GO)
# # QUANTITY_DASH_QUANTITY = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*[-\s]+\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b')

# # #  other variation of the above 2 patterns
# # QUANTITY_DASH_QUANTITY = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?!\s*[a-zA-Z0-9])(?:[-\s]*)(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE) # NOTE: RUNNER UP

# # Capture groups version of the above pattern
# QUANTITY_DASH_QUANTITY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?!\s*[a-zA-Z0-9])(?:[-\s]*)((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\b', re.IGNORECASE) # NOTE: safer new version (GOOD TO GO)
# # QUANTITY_DASH_QUANTITY_GROUPS = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?!\s*[a-zA-Z0-9])(?:\s*[-\s]*\s*)((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))\b', re.IGNORECASE) # NOTE: Old dangerous version

# # ANY_QUANTITY_RANGE = re.compile(r"\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?")

# # Matches ANY numbers/decimals/fractions followed by a hypen to ANY numbers/decimals/fractions followed by a unit (0+ whitespace between last number and unit)
# QUANTITY_DASH_QUANTITY_UNIT = re.compile(r'\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?(?:\s*(?:' + ANY_UNIT_ALT + r'))?\b')
# # QUANTITY_DASH_QUANTITY_UNIT_OG = re.compile(r'\b\d+(?:/\d+|\.\d+)?\s*-\s*\d+(?:/\d+|\.\d+)?\s*(?:' + ANY_UNIT_ALT + r')\b')

# # These are sub patterns of the QUANTITY_DASH_QUANTITY that match specific types of numbers
# # Likely these won't be used but they are here for reference, as a sanity check, 
# # for testing, and to use as a starting point

# # Starts with a whole number:
# WHOLE_NUMBER_DASH_WHOLE_NUMBER = re.compile(r"\d+\s*-\s*\d+")
# WHOLE_NUMBER_DASH_DECIMAL = re.compile(r"\d+\s*-\s*\d+\.\d+")
# WHOLE_NUMBER_DASH_FRACTION = re.compile(r"\d+\s*-\s*\d+/\d+")

# # Starts with a decimal:
# DECIMAL_DASH_DECIMAL = re.compile(r"\d+\.\d+\s*-\s*\d+\.\d+")
# DECIMAL_DASH_WHOLE_NUMBER = re.compile(r"\d+\.\d+\s*-\s*\d+")
# DECIMAL_DASH_FRACTION = re.compile(r"\d+\.\d+\s*-\s*\d+/\d+")

# # Starts with a fraction:
# FRACTION_DASH_FRACTION = re.compile(r"\d+/\d+\s*-\s*\d+/\d+")
# FRACTION_DASH_DECIMAL = re.compile(r"\d+/\d+\s*-\s*\d+\.\d+")
# FRACTION_DASH_WHOLE_NUMBER = re.compile(r"\d+/\d+\s*-\s*\d+")

# # match pattern for a range of number/decimal/fraction with "to" or "or" in between them (e.g. "1/2 to 3/4", "1/2 or 3/4", "1-to-2", "1-or-2", "1 to-2")
# QUANTITY_TO_OR_QUANTITY = re.compile(r'\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?:to|or|\s*-?\s*to\s*-?\s*|\s*-?\s*or\s*-?\s*)\s*(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))')
# # QUANTITY_TO_OR_QUANTITY = re.compile(r'\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?:to|or|-or-|-to-)\s*(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))')

# QUANTITY_OR_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*or\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE)
# QUANTITY_TO_QUANTITY = re.compile(r"\b\d+(?:/\d+|\.\d+)?\s*to\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE)

# # Regex pattern for matching "between" followed by a number/decimal/fraction, then "and" or "&", 
# # and then another number/decimal/fraction (e.g. "between 1/2 and 3/4")
# BETWEEN_QUANTITY_AND_QUANTITY = re.compile(r"\bbetween\b\s*\d+(?:/\d+|\.\d+)?\s*(?:and|&)\s*\d+(?:/\d+|\.\d+)?\b", re.IGNORECASE) # NOTE: NEW version (SAFE)
# # BETWEEN_QUANTITY_AND_QUANTITY = re.compile(r'\bbetween\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s+(?:and|&)\s+(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))') # NOTE: OLD WORKING VERSION
# # BETWEEN_NUM_AND_NUM = re.compile(r'\bbetween\b\s*((?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?)\s+(?:and|&)\s+(?:\d+(?:\.\d+)?\s*(?:/)?\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?))')

# ####### (OLD VERSION of the QUANTITY_DASH_QUANTITY) ########
# # TODO: can probably drop this pattern...
# QUANTITY_RANGE = re.compile(r"\d+(?:\.\d+)?\s*(?:\s*-\s*)+\d+(?:\.\d+)?") #  matches numbers AND decimals with a hyphen in between them
# # QUANTITY_RANGE = re.compile(r"\d+\s*(?:\s*-\s*)+\d+") #  matches numbers with a hyphen in between them (only whole numbers seperated by hypens)

# # -----------------------------------------------------------------------------
# # --------------------------- Fraction specific PATTERNS -----------------------
# # Regular expressions for fraction specific pattern matching tasks
# # Non standard forward slashes need to be replaced before matching them with the following patterns
# # (i.e. replace U+2044 ( ⁄ ) with U+002f ( / ))
# # Patterns to match:
# # - General fraction match
# # - match fraction parts in a string
# # - match multi-part fractions in a string
# # - match multi-part fractions with "and" or "&" in between the numbers
# # - match whole numbers and fractions
# # - match a number followed by a space and then a word and then a number or a fraction
# # -----------------------------------------------------------------------------

# # Regex pattern for fraction parts, finds all the fraction parts in a string (e.g. 1/2, 1/4, 3/4). 
# # A number followed by 0+ white space characters followed by a number then a forward slash then another number.
# FRACTION_PATTERN = re.compile(r'\d*\s*/\s*\d+')

# # Regex for capturing and splitting whitespace seperated numbers/decimals/fractions 
# # (e.g. 1 1/2 -> ["1", "1/2"], "2 2.3 -> ["2", "2.3"])
# SPLIT_SPACED_NUMS   = re.compile(r'^(\d+(?:/\d+|\.\d+)?)\s+(\d+(?:/\d+|\.\d+)?)$')
# # NUMS_SPLIT_BY_SPACES = re.compile(r'^(\d+(?:/\d+|\.\d+)?)\s+(\d+(?:/\d+|\.\d+)?)$')

# # # Regex for splititng whole numbers and fractions e.g. 1 1/2 -> ["1", "1/2"]
# # # TODO: extend this to include decimals as well (DEPRECATED)
# # SPLIT_INTS_AND_FRACTIONS = re.compile(r'^(\d+(?:/\d+|\.\d+)?)\s+(\d+(?:/\d+|\.\d+)?)$')
# # # SPLIT_INTS_AND_FRACTIONS = re.compile(r'^(\d+)\s+((?:\d+\s*/\s*\d+)?)$')

# # -----------------------------------------------------------------------------
# # --------------------------- (DEPRECATED) fraction specific patterns ---------
# # -----------------------------------------------------------------------------
# # Regex pattern for fraction parts.
# # Matches 0+ numbers followed by 0+ white space characters followed by a number then
# # a forward slash then another number.
# MULTI_PART_FRACTIONS_PATTERN = re.compile(r"(\d*\s*(?:and|&)?\s*\d/\d+)") # TODO: (Deprecated, replaced by AND_SEP_NUMBERS)
# # MULTI_PART_FRACTIONS_PATTERN = re.compile(r"(\d*\s*\d/\d+)")

# # Updated regex pattern for multi-part fractions that includes "and" or "&" in between the numbers
# MULTI_PART_FRACTIONS_PATTERN_AND = re.compile(r"(\d*\s*(?:and|&)?\s*\d/\d+)") # TODO: (DEPRECATED)

# # -----------------------------------------------------------------------------
# # --------------------------- Repeated strings PATTERNS -----------------------
# # Patterns to match specific cases when a known unit string is repeated in a string
# # This is typically seen in ranges where the unit appears after both quantities (e.g. 100 g - 200 g)
# # These regular expressions are used for removing the unit from the string if its repeated
# # -----------------------------------------------------------------------------

# # Regex pattern to match hypen seperated numbers/decimals/fractions followed by a unit
# REPEAT_UNIT_RANGES = re.compile(r'(\d+(?:\.\d+|/\d+)?)\s*([a-zA-Z]+)\s*-\s*(\d+(?:\.\d+|/\d+)?)\s*([a-zA-Z]+)')
# # REPEAT_UNIT_RANGES = re.compile(r'(\d+)\s*([a-zA-Z]+)\s*-\s*(\d+)\s*([a-zA-Z]+)')

# # -----------------------------------------------------------------------------
# # --------------------------- Parenthesis patterns -----------------------------
# # Patterns for converting: 
# # - Pattern for matching strings wrapped in parentheses
# # - Pattern for matching parentheses containing only a whole number, decimal, or fraction
# # - Pattern for matching parentheses containing a number followed by a unit
# # -----------------------------------------------------------------------------

# # Regular expression to match strings wrapped in parentheses, including the parentheses
# PARENTHESIS_VALUES = re.compile(r'\((.*?)\)')

# # Split string by instances of open and close parentheses (e.g. "1 cup of oats (2 ounces) in a big mixing bowl" -> ["1 cup of oats ", " in a big mixing bowl"]
# # When used with re.split() the string will be split on the set of open/close parentheses and the parantheses and the text inside them will be removed from the list
# SPLIT_BY_PARENTHESIS = re.compile(r'\(.*?\)') # use with re.split() 

# # re.findall("[^()]+", "I love looking for (multiple) parenthesis in a (string of 100s) woohoo!")
# # re.split(SPLIT_BY_PARENTHESIS, "I love looking for (multiple) parenthesis in a (string of 100s) woohoo!")
# # re.findall(SPLIT_BY_PARENTHESIS, "I love looking for (multiple) parenthesis in a (string (of) 100s) woohoo!")

# # Regular expression to match parentheses containing only a whole number, decimal, or fraction
# PARENTHESIS_WITH_NUMBERS_ONLY = re.compile(r'\(\s*(\d*(?:\.\d+|\s*/\s*\d+|\d+))\s*\)')

# # Regular expression to match parentheses containing a number followed by a unit
# PARENTHESIS_WITH_UNITS = re.compile(r'\((\d*(?:\.\d+|\s*/\s*\d+|\d+)\s*[-\s]*' + ANY_UNIT_ALT + r')\)')

# # Captures parenthesis with just a number and a unit in parenthesis
# PARENTHESIS_WITH_NUMBER_UNIT = re.compile(r'\(\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + ANY_UNIT_ALT + r')\s*\)')
# # PARENTHESIS_WITH_NUMBER_UNIT = re.compile(r'\((?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:' + ANY_UNIT_ALT + r')\)')

# # captures text in parenthesis where the number then unit pattern 
# # is met and any number of whitespaces can pad the left and right of the string within the parenthesis
# PARENTHESIS_WITH_NUMBER_ANYTHING_UNIT = re.compile(r'\(\s*(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*.*?\s*(?:' + ANY_UNIT_ALT + r')\s*\)') # this is best now

# # -----------------------------------------------------------------------------
# # --------------------------- Misc. patterns -----------------------------
# # Patterns for converting: 
# # - Pattern for finding consecutive letters and digits in a string so whitespace can be added
# # - pattern for matching "x" or "X" after numbers
# # - pattern for matching "x" or "X" after numbers and not followed by another character
# # - pattern for matching a quantity followed by "x" or "X" and then another quantity
# # - pattern for matching optional strings (e.g. "option" or "optional")
# # - pattern for matching required strings (e.g. "required" or "requirement")
# # - pattern for matching words ending in "ly" (e.g. "firmly", "lightly", "rapidly")
# # -----------------------------------------------------------------------------

# # Regular expression to match consecutive letters and digits in a string
# CONSECUTIVE_LETTERS_DIGITS = re.compile(r'([a-zA-Z]+)(\d+)|(\d+)([a-zA-Z]+)')

# # Match any number/decimal/fraction followed by 'x' or 'X' and 
# # is NOT followed by another character after the x (removes possiblity of accidently matching a word that starts with X after a number)
# # (e.g "1 x 5" matches "1 x", "1X1.5" matches "1X", "2.5x20" matches "2.5x", "1 xillion" mathces [])
# X_AFTER_NUMBER = re.compile(r'(?:\d*\.\d+|\d+\s*\/\s*\d+|\d+)+\s*[xX](?![a-zA-Z])')

# # Regular expression to match optional strings (e.g. "option" or "optional")
# OPTIONAL_STRING = re.compile(r'\b(?:option|options|optional|opt.|opts.|opt|opts|unrequired)\b')

# # Regular expression to match required strings (e.g. "required" or "requirement")
# REQUIRED_STRING = re.compile(r'\b(?:required|requirement|req.|req)\b')

# # matches any word ending in "ly" (e.g. "firmly", "lightly", "rapidly")
# # we use this to remove adverbs from the ingredient names (e.g. "lightly beaten eggs" -> "beaten eggs")
# WORDS_ENDING_IN_LY = re.compile(r'\b\w+ly\b')

# PCT_REGEX_MAP = {}

# for pct_string in ["%", "percentage", "percent", "pct"]:
#     PCT_REGEX_MAP[pct_string] = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*' + pct_string + r'')

# # # Match ALL numbers followed by 0+ whitespaces and then a percentage character "%", "percentage", or "pct" 
# # NUMBERS_FOLLOWED_BY_PERCENTAGE = re.compile(r'(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\s*(?:%|percent|percentage|pct)') # TODO: (DEPRECATED)
    
# # # Matches any nubmer/decimal/fraction, followed by 0+ spaces, then an "x" or "X", then 0+ spaces, then another number/decimal/fraction
# # # (e.g. "1 x 5", "1X1.5", "2.5x20")
# # QUANTITY_X_QUANTITY = re.compile(r'(?:\d*\.\d+|\d+\s*\/\s*\d+|\d+)+\s*[xX](?![a-zA-Z])\s*(?:\d*\.\d+|\d+\s*\/\s*\d+|\d+)') # TODO: (DEPRECATED)

# # # 'x' or 'X' after numbers pattern
# # # Match any number/decimal/fraction followed by 'x' or 'X' and then another number/decimal/fraction. An "x" or "X" is used to indicate multiplication (how many of a unit to use)
# # # (e.g "1 x 5", "1X1.5", "2.5x20")
# # # TODO: Deprecated, probably delete this pattern
# # X_SEP_NUMBERS = re.compile(r'\b(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)(?:\s*[xX]\s*)(?:\d*\.\d+|\d+\s*/\s*\d+|\d+)\b') # TODO: (DEPRECATED)


# # -----------------------------------------------------------------------------
# # --------------------------- Class to store all regex patterns -----------------------
# # A class to hold all regex patterns used in the recipe parser (version 2)
# # - Each pattern is stored as a class attribute and the class 
# # - IngredientTools class has a single method that applies ALL of the 
# #     regex patterns to a given string and return a dictionary of matches (for testing mainly)
# # -----------------------------------------------------------------------------
# # regex variables and maps to put in the class:
# class IngredientTools:
#     """
#     A class to hold all regex patterns used in recipe parsing.
#     """

#     def __init__(self) -> None:
#         # Constant data values and lookup tables
#         self.constants = {

#             # regex hashmaps
#             "NUMBER_WORDS": _constants.NUMBER_WORDS,
#             "NUMBER_PREFIX_WORDS": _constants.NUMBER_PREFIX_WORDS,
#             "MULTI_FRACTION_WORDS": _constants.MULTI_FRACTION_WORDS,
#             "FRACTION_WORDS": _constants.FRACTION_WORDS,
#             "DENOMINATOR_WORDS": _constants.DENOMINATOR_WORDS,
#             "UNICODE_FRACTIONS": _constants.UNICODE_FRACTIONS,
            
#             # unit hashmaps
#             "UNITS": _constants.UNITS,
#             "BASIC_UNITS": _constants.BASIC_UNITS,
#             "VOLUME_UNITS": _constants.VOLUME_UNITS,
#             "WEIGHT_UNITS": _constants.WEIGHT_UNITS,
#             "DIMENSION_UNITS": _constants.DIMENSION_UNITS,
#             "CASUAL_UNITS": _constants.CASUAL_UNITS,

#             # unit hashsets
#             "UNITS_SET": _constants.UNITS_SET,
#             "BASIC_UNITS_SET": _constants.BASIC_UNITS_SET,
#             "NON_BASIC_UNITS_SET": _constants.NON_BASIC_UNITS_SET, 
#             "VOLUME_UNITS_SET": _constants.VOLUME_UNITS_SET,
#             "WEIGHT_UNITS_SET": _constants.WEIGHT_UNITS_SET,
#             "DIMENSION_UNITS_SET": _constants.DIMENSION_UNITS_SET,
#             "SIZE_MODIFIERS_SET": _constants.SIZE_MODIFIERS_SET,
#             "CASUAL_UNITS_SET": _constants.CASUAL_UNITS_SET,
#             "CASUAL_QUANTITIES_SET": _constants.CASUAL_QUANTITIES_SET,

#             "CASUAL_QUANTITIES": _constants.CASUAL_QUANTITIES,
#             "UNIT_MODIFIERS": _constants.UNIT_MODIFIERS,
#             "PREP_WORDS": _constants.PREP_WORDS,
#             "APPROXIMATE_STRINGS": _constants.APPROXIMATE_STRINGS,
#             "QUANTITY_PER_UNIT_STRINGS": _constants.QUANTITY_PER_UNIT_STRINGS,
#             "UNIT_TO_STANDARD_UNIT": _constants.UNIT_TO_STANDARD_UNIT,
#             "STOP_WORDS": _constants.STOP_WORDS,
#             "DASH_SYMBOLS": _constants.DASH_SYMBOLS,
#             'REMOVABLE_DASH_SYMBOLS': _constants.REMOVABLE_DASH_SYMBOLS
#         }

#         # Define regex patterns
#         # string numbers to number map
#         self.NUMBER_WORDS_MAP = NUMBER_WORDS_MAP
#         self.PREFIXED_NUMBER_WORDS = PREFIXED_NUMBER_WORDS
#         self.PREFIXED_NUMBER_WORDS_GROUPS = PREFIXED_NUMBER_WORDS_GROUPS
#         self.MULTI_FRACTION_WORDS_MAP = MULTI_FRACTION_WORDS_MAP

#         # unicode fractions
#         self.UNICODE_FRACTIONS_PATTERN = UNICODE_FRACTIONS_PATTERN
        
#         # unit matching patterns
#         self.UNITS_PATTERN = UNITS_PATTERN
#         self.BASIC_UNITS_PATTERN = BASIC_UNITS_PATTERN
#         self.NON_BASIC_UNITS_PATTERN = NON_BASIC_UNITS_PATTERN
#         self.VOLUME_UNITS_PATTERN = VOLUME_UNITS_PATTERN
#         self.SIZE_MODIFIERS_PATTERN = SIZE_MODIFIERS_PATTERN
#         self.PREP_WORDS_PATTERN = PREP_WORDS_PATTERN
#         self.STOP_WORDS_PATTERN = STOP_WORDS_PATTERN
#         self.CASUAL_QUANTITIES_PATTERN = CASUAL_QUANTITIES_PATTERN
#         self.CASUAL_UNITS_PATTERN = CASUAL_UNITS_PATTERN
#         self.DIMENSION_UNITS_PATTERN = DIMENSION_UNITS_PATTERN
#         self.UNIT_MODIFIERS_PATTERN = UNIT_MODIFIERS_PATTERN
#         self.APPROXIMATE_STRINGS_PATTERN = APPROXIMATE_STRINGS_PATTERN


#         # unit/number or number/unit matching patterns
#         self.ANY_NUMBER_THEN_UNIT = ANY_NUMBER_THEN_UNIT
#         self.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT = ANY_NUMBER_THEN_ANYTHING_THEN_UNIT
#         self.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS = ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS
#         # self.ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS2 = ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS2
#         self.SPACED_NUMS_THEN_VOLUME_UNITS = SPACED_NUMS_THEN_VOLUME_UNITS
#         self.ANY_NUMBER_THEN_UNIT_CAPTURE = ANY_NUMBER_THEN_UNIT_CAPTURE

#         # capture groups for getting anumber followed by the next closest units/basics units/non-basic units
#         self.QUANTITY_UNIT_GROUPS = QUANTITY_UNIT_GROUPS
#         self.QUANTITY_BASIC_UNIT_GROUPS = QUANTITY_BASIC_UNIT_GROUPS
#         self.QUANTITY_NON_BASIC_UNIT_GROUPS = QUANTITY_NON_BASIC_UNIT_GROUPS
#         self.QUANTITY_SOMETIMES_UNIT_GROUPS = QUANTITY_SOMETIMES_UNIT_GROUPS
#         self.QUANTITY_DIMENSION_UNIT_GROUPS = QUANTITY_DIMENSION_UNIT_GROUPS
#         self.QUANTITY_ANYTHING_UNIT_GROUPS = QUANTITY_ANYTHING_UNIT_GROUPS
#         self.QUANTITY_UNIT_ONLY_GROUPS = QUANTITY_UNIT_ONLY_GROUPS
#         self.EQUIV_QUANTITY_UNIT_GROUPS = EQUIV_QUANTITY_UNIT_GROUPS
        
#         # word fraction patterns
#         self.NUMBER_WITH_FRACTION_WORD = NUMBER_WITH_FRACTION_WORD
#         self.NUMBER_WITH_DENOMINATOR = NUMBER_WITH_DENOMINATOR
#         self.NUMBER_WITH_FRACTION_WORD_GROUPS = NUMBER_WITH_FRACTION_WORD_GROUPS
#         self.NUMBER_WITH_FRACTION_WORD_MAP = NUMBER_WITH_FRACTION_WORD_MAP

#         # generic number matchings and/or numbers with specific separators
#         self.ALL_NUMBERS = ALL_NUMBERS
#         self.SPACE_SEP_NUMBERS = SPACE_SEP_NUMBERS
#         self.NUMBERS_SEPARATED_BY_ADD_SYMBOLS = NUMBERS_SEPARATED_BY_ADD_SYMBOLS
#         self.NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS = NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS

#         # range patterns
#         self.QUANTITY_DASH_QUANTITY = QUANTITY_DASH_QUANTITY
#         self.QUANTITY_DASH_QUANTITY_GROUPS = QUANTITY_DASH_QUANTITY_GROUPS
#         self.QUANTITY_DASH_QUANTITY_UNIT = QUANTITY_DASH_QUANTITY_UNIT
#         self.QUANTITY_OR_QUANTITY = QUANTITY_OR_QUANTITY
#         self.QUANTITY_TO_QUANTITY = QUANTITY_TO_QUANTITY
#         self.BETWEEN_QUANTITY_AND_QUANTITY = BETWEEN_QUANTITY_AND_QUANTITY

#         # fraction specific patterns
#         self.FRACTION_PATTERN = FRACTION_PATTERN
#         self.SPLIT_SPACED_NUMS = SPLIT_SPACED_NUMS
#         self.SPLIT_INTS_AND_FRACTIONS = SPLIT_INTS_AND_FRACTIONS
        
#         # repeated unit string patterns
#         self.REPEAT_UNIT_RANGES = REPEAT_UNIT_RANGES

#         # miscellaneous patterns
#         self.CONSECUTIVE_LETTERS_DIGITS = CONSECUTIVE_LETTERS_DIGITS
#         self.PARENTHESIS_VALUES = PARENTHESIS_VALUES
#         self.SPLIT_BY_PARENTHESIS = SPLIT_BY_PARENTHESIS
#         self.PARENTHESIS_WITH_NUMBERS_ONLY = PARENTHESIS_WITH_NUMBERS_ONLY
#         self.PARENTHESIS_WITH_UNITS = PARENTHESIS_WITH_UNITS
#         self.PARENTHESIS_WITH_NUMBER_UNIT = PARENTHESIS_WITH_NUMBER_UNIT
#         self.PARENTHESIS_WITH_NUMBER_ANYTHING_UNIT = PARENTHESIS_WITH_NUMBER_ANYTHING_UNIT

#         # "x" and "X" separators
#         self.X_AFTER_NUMBER = X_AFTER_NUMBER

#         # match specific strings 
#         self.OPTIONAL_STRING = OPTIONAL_STRING
#         self.REQUIRED_STRING = REQUIRED_STRING
#         self.WORDS_ENDING_IN_LY = WORDS_ENDING_IN_LY
#         self.NUMBERS_FOLLOWED_BY_PERCENTAGE = NUMBERS_FOLLOWED_BY_PERCENTAGE
#         self.PCT_REGEX_MAP = PCT_REGEX_MAP

#         # get a list of all the attributes of the class in sorted order by name
#         self.sorted_keys = sorted(self.__dict__.keys(), key=lambda x: x[0])

#         # # Sort attributes by name
#         # self.sorted_attrs = sorted(self.__dict__.items(), key=lambda x: x[0])

#     def find_matches(self, input_string: str) -> Dict[str, List[Union[str, Tuple[str]]]]:
#         """
#         Find all matches in the input string for each regex pattern.
#         Returns a dictionary with pattern names as keys and corresponding matches as values.
#         """

#         matches = {}
#         for name, pattern in self.__dict__.items():
#             if isinstance(pattern, re.Pattern):
#                 matches[name] = pattern.findall(input_string)
#         return matches
    
#     def print_matches(self, input_string: str) -> None:
#         """
#         Print out all matches in the input string for each regex pattern.
#         Returns None
#         """
#         matches = {}
        
#         for key in self.sorted_keys:
#             attribute = self.__dict__[key]
#             if isinstance(attribute, re.Pattern):
#                 matches[key] = attribute.findall(input_string)
#                 print(f"{key}: {matches[key]}")

#         # matches = {}
#         # for name, pattern in self.__dict__.items():
#         #     if isinstance(pattern, re.Pattern):
#         #         matches[name] = pattern.findall(input_string)
#         #         print(f"{name}: {matches[name]}")

        
#     def list_constants(self) -> None:
#         """
#         List all the attributes of the class.
#         """ 

#         # attrs = [name for name in self.__dict__]

#         for name, pattern in self.__dict__.items():
#             print(f"- {name} ({type(self.__dict__[name]).__name__})")
#             if isinstance(self.__dict__[name], dict):
#                 print(f"  > {len(self.__dict__[name])} items")
#                 # for key, value in self.__dict__[name].items():
#                 #     print(f"   - {key}")
#         # return [name for name in self.__dict__ if isinstance(self.__dict__[name], re.Pattern)]
    
#     def get_desc(self, pattern_name: str) -> str:
#         """
#         Get the description of a specific regex pattern.
#         Returns the description of the pattern if found, otherwise returns an empty string.
#         """
        
#         # Define descriptions for each pattern
#         descriptions = {
#             ### Constants and lookup tables
#             "NUMBER_WORDS": "Dictionary of number words to numerical values.",
#             "MULTI_FRACTION_WORDS": "Dictionary of fraction phrases (i.e. 'two thirds' or '1 half') to their fractional string value",
#             "FRACTION_WORDS": "Dictionary of single fraction words that represent a singular fraction (i.e. a quarter is equal to 1/4).",
#             "UNICODE_FRACTIONS": "Dictionary of unicode fractions to numerical values.",

#             # dictionaries of units
#             "UNITS": "Dictionary of units used in the recipe parser (All units, including basic, volume, and specific units).",
#             "BASIC_UNITS": "Dictionary of basic units used in the recipe parser (The most common units).",
#             "VOLUME_UNITS": "Dictionary of volume units used in the recipe parser (Units used for measuring volume).",
#             "WEIGHT_UNITS": "Dictionary of weight units used in the recipe parser (Units used for measuring weight).",
#             "DIMENSION_UNITS": "Dictionary of dimension units used in the recipe parser (Units used for measuring dimensions).",
#             "CASUAL_UNITS": "Dictionary of casual units used in the recipe parser (Units that are not standard units).",

#             # sets of all unit words
#             "UNITS_SET": "Set of units used in the recipe parser (All units, including basic, volume, and specific units).",
#             "BASIC_UNITS_SET": "Set of basic units used in the recipe parser (The most common units).",
#             "NON_BASIC_UNITS_SET": "Set of non-basic units used in the recipe parser (Units that are not in the BASIC_UNITS dictionary).",
#             "SIZE_MODIFIERS_SET": "Set of units that are sometimes used in the recipe parser (Set of words that MIGHT be units if no other units are around).",
#             "VOLUME_UNITS_SET": "Set of volume units used in the recipe parser (Units used for measuring volume).",
#             "WEIGHT_UNITS_SET": "Set of weight units used in the recipe parser (Units used for measuring weight).",
#             "DIMENSION_UNITS_SET": "Set of dimension units used in the recipe parser (Units used for measuring dimensions).",
#             "CASUAL_UNITS_SET": "Set of casual units used in the recipe parser (Units that are not standard units).",
#             "CASUAL_QUANTITIES_SET": "Set of casual quantities used in the recipe parser (Quantities that are not standard quantities).",

#             "CASUAL_QUANTITIES": "Dictionary of casual quantities used in the recipe parser.",
#             "UNIT_MODIFIERS": "Set of unit modifier words for lookups in recipe parser.",
#             "PREP_WORDS": "Set of preparation words for lookups in recipe parser.",
#             "APPROXIMATE_STRINGS": "Set of strings that indicate an approximate quantity in the recipe parser.",
#             "QUANTITY_PER_UNIT_STRINGS": "Set of strings that indicate a quantity per unit in the recipe parser.",
#             "NUMBER_WORDS_MAP": "Dictionary of regex patterns to match number words in a string (i.e. 'one' : '1', 'two' : '2').",
            
#             ### Regex patterns
#             # Unicode fractions
#             "UNICODE_FRACTIONS_PATTERN": "Matches unicode fractions in the string.",
            
#             # simple unit matching patterns
#             "UNITS_PATTERN": "Matches units in a string.",
#             "BASIC_UNITS_PATTERN": "Matches just the basic units from the BASIC_UNITS dictionary.",
#             "NON_BASIC_UNITS_PATTERN": "Matches non-basic units in a string.",
#             "VOLUME_UNITS_PATTERN": "Matches specifically volume units in a string.",
#             "SIZE_MODIFIERS_PATTERN": "Matches sometimes units in a string.",
#             "PREP_WORDS_PATTERN": "Matches preparation words in a string.",
#             "STOP_WORDS_PATTERN": "Matches stop words in a string.",
#             "CASUAL_QUANTITIES_PATTERN": "Matches casual quantities in a string (i.e. 'couple' = 2).",
#             "CASUAL_UNITS_PATTERN": "Matches casual units in a string (i.e. 'dash', 'pinch').",
#             "DIMENSION_UNITS_PATTERN": "Matches dimension units in a string (i.e. 'inches', 'cm').",
#             "UNIT_MODIFIERS_PATTERN": "Matches unit modifiers in a string (i.e. 'large', 'small').",
#             "APPROXIMATE_STRINGS_PATTERN": "Matches approximate strings in a string (i.e. 'about', 'approximately').",

#             # Quantities followed by units
#             "ANY_NUMBER_THEN_UNIT": "Matches a number followed by a unit.",
#             "ANY_NUMBER_THEN_ANYTHING_THEN_UNIT": "Matches a number followed by any text and then a unit.",

#             "ANY_NUMBER_THEN_ANYTHING_THEN_UNIT_GROUPS": "Matches a number followed by any text and then a unit with capture groups.",
#             "SPACED_NUMS_THEN_VOLUME_UNITS": "Matches a number/decimal/fraction followed by 1+ spaces to another number/decimal/fraction followed by a 0+ spaces then a VOLUME unit.",
#             "ANY_NUMBER_THEN_UNIT_CAPTURE": "Matches a number followed by any text and then a unit.",
#             "NUMBER_THEN_UNIT_ABBR": "Matches a number followed by a unit abbreviation.",
#             "NUMBER_THEN_UNIT_WORD": "Matches a number followed by a unit word (full word string as unit).",

#             "QUANTITY_UNIT_GROUPS": "Matches a number followed by a unit with capture groups.", 
#             "QUANTITY_BASIC_UNIT_GROUPS": "Matches a number followed by a basic unit with capture groups.",
#             "QUANTITY_NON_BASIC_UNIT_GROUPS": "Matches a number followed by a non-basic unit with capture groups.",
#             "QUANTITY_SOMETIMES_UNIT_GROUPS": "Matches a number followed by a 'sometimes unit' with capture groups (i.e. 'large' is sometimes a unit if no other units are around).",
#             "QUANTITY_ANYTHING_UNIT_GROUPS": "Matches a number followed by any text and then a unit with capture groups.",
#             "QUANTITY_DIMENSION_UNIT_GROUPS": "Matches a number followed by a dimension unit with capture groups.",
#             "QUANTITY_UNIT_ONLY_GROUPS": "Matches a quantity followed by  0+whitespaces/hypens and then a unit with capture groups.",
#             "EQUIV_QUANTITY_UNIT_GROUPS": "Matches an 'approximate/equivalent' string followed by a number followed by a unit with capture groups (helpful for finding equivalent quantity-unit patterns i.e. 'about 1/2 cup').",

#             # general umber matching patterns and number with specific separators
#             "ALL_NUMBERS": "Matches ALL number/decimal/fraction in a string regardless of padding.",
#             "SPACE_SEP_NUMBERS": "Matches any number/decimal/fraction followed by a space and then another number/decimal/fraction.",
#             "NUMBERS_SEPARATED_BY_ADD_SYMBOLS": "Matches numbers/decimals/fractions separated by 'and', '&', 'plus', or '+' symbols.",
#             "NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS": "Matches numbers/decimals/fractions separated by 'and', '&', 'plus', or '+' symbols with capture groups.",

#             "QUANTITY_DASH_QUANTITY": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions.",
#             "QUANTITY_DASH_QUANTITY_GROUPS": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions with capture groups.",
#             "QUANTITY_DASH_QUANTITY_UNIT": "Matches numbers/decimals/fractions followed by a hyphen to numbers/decimals/fractions followed by a unit (0+ whitespace between last number and the unit).",
#             "QUANTITY_RANGE": "Matches numbers/decimals/fractions with a hyphen in between them.",
#             "QUANTITY_TO_OR_QUANTITY": "Matches numbers/decimals/fractions separated by 'to' or 'or'.",
#             "QUANTITY_OR_QUANTITY": "Matches numbers/decimals/fractions separated by 'or'.",
#             "QUANTITY_TO_QUANTITY": "Matches numbers/decimals/fractions separated by 'to'.",
#             "BETWEEN_QUANTITY_AND_QUANTITY": "Matches numbers/decimals/fractions separated by 'between' and 'and'.",

#             # fraction word patterns
#             "NUMBER_WITH_FRACTION_WORD": "Matches a number followed by a fraction word (i.e. '1 half').",
#             "NUMBER_WITH_FRACTION_WORD_GROUPS": "Matches a number followed by a fraction word with capture groups.",
#             "NUMBER_WITH_FRACTION_WORD_MAP": "Dictionary of regex patterns to match number followed by a fraction word in a string (i.e. '1 half' : '1 1/2').",

#             # fraction specific patterns
#             "FRACTION_PATTERN": "Matches fraction parts in a string.",
#             "SPLIT_SPACED_NUMS": "Splits numbers/decimals/fractions separated by 1+ whitespaces into a capture group (i.e '1.5 1/2' -> ['1.5', '1/2']).",
#             "REPEAT_UNIT_RANGES": "Matches repeated unit strings in a string.",

#             "CONSECUTIVE_LETTERS_DIGITS": "Matches consecutive letters and digits in a string.",
#             "PARENTHESIS_VALUES": "Matches strings wrapped in parentheses, including the parentheses.",
#             "SPLIT_BY_PARENTHESIS": "Matches parentheses in a string and splits the string by them if used with re.split().",
#             "PARENTHESIS_WITH_NUMBERS_ONLY": "Matches parentheses containing only a whole number, decimal, or fraction.",
#             "PARENTHESIS_WITH_UNITS": "Matches parentheses containing a number followed by a unit.",
#             "X_AFTER_NUMBER": "Matches a number followed by an 'x'/'X' (can't be the start of a word starting with xX).",
#             "OPTIONAL_STRING": "Matches the word 'optional', 'option', 'opt', etc. in a string.",
#             "REQUIRED_STRING": "Matches the word 'required', 'requirement', 'req', etc. in a string.",
#             "WORDS_ENDING_IN_LY": "Matches any word ending in 'ly' (i.e. 'firmly', 'lightly', 'rapidly').",
#             "PCT_REGEX_MAP" : "Dictionary of regex patterns to match numbers followed by a percentage character '%', 'percentage', 'percent', or 'pct'."
#         }

#         # Retrieve description based on pattern name
#         return descriptions.get(pattern_name, "")
    
# -----------------------------------------
# ---- List of used constants/regexes -----
# -----------------------------------------

# UNITS
# CASUAL_QUANTITIES
# UNIT_TO_STANDARD_UNIT
# NUMBER_PREFIX_WORDS
# NUMBER_WORDS
# FRACTION_WORDS
# UNICODE_FRACTIONS
# BASIC_UNITS_SET
# WEIGHT_UNITS_SET

# PCT_REGEX_MAP
# NUMBER_WITH_FRACTION_WORD_MAP
# NUMBER_WORDS_MAP

# NUMBERS_SEPARATED_BY_ADD_SYMBOLS_GROUPS
# CASUAL_QUANTITIES_PATTERN
# PREFIXED_NUMBER_WORDS_GROUPS
# CONSECUTIVE_LETTERS_DIGITS
# FRACTION_PATTERN

# QUANTITY_DASH_QUANTITY
# QUANTITY_DASH_QUANTITY_GROUPS
# BETWEEN_QUANTITY_AND_QUANTITY
# QUANTITY_TO_QUANTITY
# QUANTITY_OR_QUANTITY

# REPEAT_UNIT_RANGES
# X_AFTER_NUMBER
# SPLIT_SPACED_NUMS
# SPACE_SEP_NUMBERS
# UNITS_PATTERN
# ALL_NUMBERS
# SPLIT_BY_PARENTHESIS # NOTE: old
# QUANTITY_BASIC_UNIT_GROUPS
# QUANTITY_NON_BASIC_UNIT_GROUPS
# OPTIONAL_STRING
# REQUIRED_STRING
# PREP_WORDS_PATTERN
# WORDS_ENDING_IN_LY
# UNIT_MODIFIERS_PATTERN
# DIMENSION_UNITS_PATTERN
# APPROXIMATE_STRINGS_PATTERN
# SIZE_MODIFIERS_PATTERN
# STOP_WORDS_PATTERN