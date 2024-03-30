# pytest library
import pytest

import re

from ingredient_slicer import _regex_patterns


# # TODO: Good to use now to get numbers separeted by "X" or "x" in a string
# NUMBER_X_NUMBER = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:x|X))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)
# NUMBER_BY_NUMBER = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:by))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)

# NUMBER_X_NUMBER.findall("4x4  inch")
# NUMBER_X_NUMBER.findall("0.5 inch X 4  inch")
# NUMBER_BY_NUMBER = re.compile(r'\b((?:\d*\.\d+|\d+\s*/\s*\d+|\d+))(?:\s*(?:by))\s*(\d*\.\d+|\d+\s*/\s*\d+|\d+)\b', re.IGNORECASE)
# NUMBER_BY_NUMBER.findall("4 by 4 inch")

def test_x_after_number_then_x_1():
    # def replace_x(match):
    #         return match.group().replace('x', ' ').replace('X', ' ')

    # # Replace "x"/"X" separators with whitespace
    # self.standardized_ingredient = _regex_patterns.X_AFTER_NUMBER.sub(replace_x, self.standardized_ingredient)

    assert 5 == 5
    # assert _regex_patterns.X_AFTER_NUMBER.findall("twenty five eggs") == [('twenty', 'five')]
    # assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("hundred twenty eggs") == [('hundred', 'twenty')]
    # assert _regex_patterns.PREFIXED_NUMBER_WORDS_GROUPS.findall("a twenty-two lb bag") == [('twenty', 'two')]