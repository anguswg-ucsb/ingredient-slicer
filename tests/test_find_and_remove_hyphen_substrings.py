# pytest library
import pytest

import re

from ingredient_slicer import _utils

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ---- Duplicate unit ranges tests ----
# -------------------------------------------------------------------------------

test_cases = {
    "test_case_1": ["I love cats -to- dogs to ", "to", "i love cats to dogs to"],
    "test_case_2": ["g -to- -to- -to-", "to", "g to to to"],
    "test_case_3": ["-to- -to- -to-", "to", "to to to"],
    "test_case_4": ["1-to-three cups of tomato-juice", "to", "1 to three cups of tomato-juice"],
    # "test_case_2": ["-to- -to- -to-", "to", "-to- to -to-"],
    # "test_case_3": ["I love cats -to- - dogs to ", "cat", "i love cats -to- - dogs to "],
    # "test_case_4": ["I love cats -to- - dogs to ", "love", "i love cats -to- - dogs to "],
    # "test_case_5": ["I love cats -to- - dogs to ", "dogs", "i love cats -to- - dogs to "],
    # "test_case_6": ["I love cats -to- - dogs to ", " ", "i love cats -to- - dogs to "],
    # "test_case_7": ["I love cats -to- - dogs to ", "-", "i love cats -to- - dogs to "],
    # "test_case_8": ["I love cats -to- - dogs to ", "dogs to", "i love cats -to- - dogs to "],
    # "test_case_9": ["I love cats -to- - dogs to ", "-to-", "i love cats -to- - dogs to "],
    # "test_case_10": ["I love cats -to- - dogs to ", "lo", "i ve cats -to- - dogs to "],
    # "test_case_11": ["I love cats -to- - dogs to ", "-to- -", "i love cats -to- - dogs to "],
    # "test_case_12": ["I love cats -to- - dogs to ", "c -to- - dogs", "i love cats -to- - dogs to "],
    # "test_case_13": ["I love cats -to- - dogs to ", " ", "i love cats -to- - dogs to "],
    # "test_case_14": ["I love cats -to- - dogs to ", "to", "i love cats to dogs to "],
    # "test_case_15": ["I love cats -to- - dogs to ", "to", "i love cats to dogs to "],
    # "test_case_16": ["-to- -to- -to-", "to", "-to- to -to-"],
    # "test_case_17": ["I love cats -to- - dogs to ", "cat", "i love cats -to- - dogs to "]
    # Add more test cases as needed
}

for test_name, (text, substring, expected_result) in test_cases.items():
    # _utils._find_and_remove_hyphens_around_substring("I love cats -to- dogs to ", "to", debug=True)
    # _utils._find_and_remove_hyphens_around_substring("g -to- -to- -to-", "to", debug=True)
    assert _utils._find_and_remove_hyphens_around_substring(text, substring) == expected_result, f"Failed test: {test_name}"
